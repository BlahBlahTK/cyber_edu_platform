document.addEventListener('DOMContentLoaded', () => {
    const chatHistory = document.getElementById('chat-history');
    const userInput = document.getElementById('user-input');
    const sendBtn = document.getElementById('send-btn');

    function appendMessage(text, isUser) {
        const div = document.createElement('div');
        div.classList.add('message');
        div.classList.add(isUser ? 'user-message' : 'bot-message');
        div.textContent = text;
        chatHistory.appendChild(div);
        chatHistory.scrollTop = chatHistory.scrollHeight;
    }

    async function sendMessage() {
        const text = userInput.value.trim();
        if (!text) return;

        // Add user message to UI
        appendMessage(text, true);
        userInput.value = '';

        // Show loading state (optional polish: could add a loader bubble)
        const loadingDiv = document.createElement('div');
        loadingDiv.classList.add('message', 'bot-message');
        loadingDiv.textContent = 'Thinking...';
        chatHistory.appendChild(loadingDiv);
        chatHistory.scrollTop = chatHistory.scrollHeight;

        try {
            const response = await fetch('/api/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ message: text })
            });

            const data = await response.json();
            
            // Remove loading message
            chatHistory.removeChild(loadingDiv);

            if (data.error) {
                appendMessage("Error: " + data.error, false);
            } else {
                appendMessage(data.reply, false);
            }
        } catch (error) {
            chatHistory.removeChild(loadingDiv);
            appendMessage("Network Error: Could not reach the server.", false);
            console.error(error);
        }
    }

    sendBtn.addEventListener('click', sendMessage);

    userInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            sendMessage();
        }
    });
});
