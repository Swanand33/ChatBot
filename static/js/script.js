document.getElementById('send-button').addEventListener('click', async function () {
    const userInput = document.getElementById('user-input').value;
    const chatbox = document.getElementById('chatbox');

    if (userInput.trim() === '') return;

    // Append user message to chatbox
    chatbox.innerHTML += `<div class="user-message">You: ${userInput}</div>`;
    document.getElementById('user-input').value = '';

    try {
        const response = await fetch('/ask', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message: userInput })
        });

        const data = await response.json();
        if (response.ok) {
            chatbox.innerHTML += `<div class="bot-message">Bot: ${data.response}</div>`;
        } else {
            chatbox.innerHTML += `<div class="bot-message">Bot: ${data.error}</div>`;
        }
    } catch (error) {
        chatbox.innerHTML += `<div class="bot-message">Bot: Error connecting to the server.</div>`;
    }
});