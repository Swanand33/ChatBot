import openai
from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Set the OpenAI API key
openai.api_key = OPENAI_API_KEY

class ContextualChatbot:
    def __init__(self):
        self.conversation_history = []
        self.max_history_length = 10  # Adjust as needed

    def update_conversation_history(self, role, content):
        self.conversation_history.append({"role": role, "content": content})
        # Trim history if it exceeds the maximum length
        if len(self.conversation_history) > self.max_history_length:
            self.conversation_history = self.conversation_history[-self.max_history_length:]

    def generate_response(self, user_input):
        self.update_conversation_history("user", user_input)
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    *self.conversation_history
                ]
            )
            assistant_response = response['choices'][0]['message']['content'].strip()
            self.update_conversation_history("assistant", assistant_response)
            return assistant_response
        except Exception as e:
            print(f"An error occurred: {e}")
            return "I'm sorry, but I encountered an error. Please try again."

    def run(self):
        print("Chatbot: Hello! How can I assist you today?")
        while True:
            user_input = input("You: ")
            if user_input.lower() in ['exit', 'quit', 'bye']:
                print("Chatbot: Goodbye! Have a great day!")
                break
            response = self.generate_response(user_input)
            print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot = ContextualChatbot()
    chatbot.run()