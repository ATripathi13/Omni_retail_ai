const chatForm = document.getElementById('chat-form');
const userInput = document.getElementById('user-input');
const chatHistory = document.getElementById('chat-history');

// Templates
const userTemplate = document.getElementById('user-msg-template');
const aiTemplate = document.getElementById('ai-msg-template');

chatForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const query = userInput.value.trim();
    if (!query) return;

    // 1. Render User Message
    appendUserMessage(query);
    userInput.value = '';

    // 2. Call API
    try {
        const loadingMsg = appendLoadingMessage();

        const response = await fetch('/api/v1/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ query: query })
        });

        const data = await response.json();

        // Remove loading
        loadingMsg.remove();

        if (response.ok) {
            appendAIMessage(data);
        } else {
            appendErrorMessage(data.detail || "Unknown error occurred.");
        }
    } catch (error) {
        appendErrorMessage("Network error: Could not reach the Orchestrator.");
    }
});

function appendUserMessage(text) {
    const clone = userTemplate.content.cloneNode(true);
    clone.querySelector('.message-content').textContent = text;
    chatHistory.appendChild(clone);
    scrollToBottom();
}

function appendAIMessage(data) {
    const clone = aiTemplate.content.cloneNode(true);
    const container = clone.querySelector('.message-content');

    // Render Natural Language Summary
    if (data.summary) {
        const summaryDiv = document.createElement('div');
        summaryDiv.className = 'ai-summary';
        summaryDiv.style.marginBottom = '16px';
        summaryDiv.style.fontSize = '1.05rem';
        summaryDiv.innerHTML = `<p>${data.summary.replace(/\n/g, '<br>')}</p>`;
        // Insert at the top
        container.insertBefore(summaryDiv, container.firstChild);
    }

    // Render Plan
    const stepsList = container.querySelector('.steps-list');
    if (data.plan && data.plan.length > 0) {
        data.plan.forEach(step => {
            const li = document.createElement('li');
            li.innerHTML = `<strong>${step.agent}</strong>: ${step.goal}`;
            stepsList.appendChild(li);
        });
    } else {
        container.querySelector('.plan-section').style.display = 'none';
    }

    // Render Results (Summary)
    const jsonOutput = container.querySelector('.json-output');
    // Format the results nicely. Maybe just key info or the full JSON
    // We'll strip out some verbosity for display
    const cleanResults = data.results.map(r => ({
        step: r.step,
        agent: r.agent,
        data: r.result.data ? `${r.result.data.length} records found` : r.result
    }));

    jsonOutput.textContent = JSON.stringify(cleanResults, null, 2);

    chatHistory.appendChild(clone);
    scrollToBottom();
}

function appendLoadingMessage() {
    const div = document.createElement('div');
    div.className = 'ai-message fade-in';
    div.innerHTML = `
        <div class="message-content glass-panel" style="color: var(--text-secondary)">
            <i class="fa-solid fa-circle-notch fa-spin"></i> Thinking...
        </div>
    `;
    chatHistory.appendChild(div);
    scrollToBottom();
    return div;
}

function appendErrorMessage(msg) {
    const div = document.createElement('div');
    div.className = 'ai-message fade-in';
    div.innerHTML = `
        <div class="message-content glass-panel" style="border-color: #ef4444; color: #fca5a5;">
            <i class="fa-solid fa-triangle-exclamation"></i> Error: ${msg}
        </div>
    `;
    chatHistory.appendChild(div);
    scrollToBottom();
}

function scrollToBottom() {
    chatHistory.scrollTop = chatHistory.scrollHeight;
}
