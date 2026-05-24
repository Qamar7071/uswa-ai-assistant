/* ============================================================
   USWA AI ASSISTANT - FRONTEND JAVASCRIPT
   ============================================================
   Yeh file chatbot ko interactive banati hai:
   - User ka message backend bhejti hai
   - Jawab le kar screen pe dikhati hai
   ============================================================ */

// ============================================================
// HTML ELEMENTS PAKAR KE RAKHO
// ============================================================
const userInput = document.getElementById('userInput');
const sendBtn = document.getElementById('sendBtn');
const messagesContainer = document.getElementById('messagesContainer');
const welcomeScreen = document.getElementById('welcomeScreen');
const typingIndicator = document.getElementById('typingIndicator');
const chatArea = document.getElementById('chatArea');

// Logo ka path (HTML se nikalo taake Flask path sahi rahe)
const logoPath = document.querySelector('.sidebar-logo-img').getAttribute('src');


// ============================================================
// FUNCTION: Screen pe message add karo
// sender = "user" ya "bot"
// text = message ka content
// ============================================================
function addMessage(sender, text) {
    // Welcome screen chupa do (pehle message ke baad)
    if (welcomeScreen) {
        welcomeScreen.style.display = 'none';
    }

    // Naya message ka container banao
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${sender}-message`;

    // Avatar (user ke liye "You", bot ke liye logo)
    let avatarHTML = '';
    if (sender === 'bot') {
        avatarHTML = `<div class="message-avatar"><img src="${logoPath}" alt="USWA"></div>`;
    } else {
        avatarHTML = `<div class="message-avatar">You</div>`;
    }

    // Author ka naam
    const authorName = sender === 'bot' ? 'USWA AI Assistant' : 'You';

    // Message ka pura HTML banao
    messageDiv.innerHTML = `
        ${avatarHTML}
        <div class="message-body">
            <div class="message-author">${authorName}</div>
            <div class="message-text">${text.replace(/\n/g, '<br>')}</div>
        </div>
    `;

    // Message ko screen pe add karo
    messagesContainer.appendChild(messageDiv);

    // Neeche scroll karo (taake naya message dikhe)
    chatArea.scrollTop = chatArea.scrollHeight;
}


// ============================================================
// FUNCTION: Message backend ko bhejo
// ============================================================
async function sendMessage() {
    // User ka message lo
    const message = userInput.value.trim();

    // Agar message khaali hai, kuch mat karo
    if (message === '') return;

    // User ka message screen pe dikhao
    addMessage('user', message);

    // Input box khaali karo
    userInput.value = '';
    userInput.style.height = 'auto';

    // Typing indicator dikhao (3 dots)
    typingIndicator.classList.add('active');
    chatArea.scrollTop = chatArea.scrollHeight;

    try {
        // Backend ko message bhejo (POST request)
        const response = await fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message: message })
        });

        // Backend ka jawab lo
        const data = await response.json();

        // Typing indicator chupao
        typingIndicator.classList.remove('active');

        // Thora ruko (taake natural lage), phir bot ka jawab dikhao
        setTimeout(() => {
            addMessage('bot', data.reply);
        }, 300);

    } catch (error) {
        // Agar koi error aaye
        typingIndicator.classList.remove('active');
        addMessage('bot', 'Sorry, something went wrong. Please try again.');
        console.error('Error:', error);
    }
}


// ============================================================
// EVENT LISTENERS - Button aur keyboard
// ============================================================

// Send button click karne par
sendBtn.addEventListener('click', sendMessage);

// Enter key dabane par (Shift+Enter = nayi line)
userInput.addEventListener('keydown', function(e) {
    if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        sendMessage();
    }
});

// Textarea ko auto-resize karo (jaise user type karta hai)
userInput.addEventListener('input', function() {
    this.style.height = 'auto';
    this.style.height = (this.scrollHeight) + 'px';
});


// ============================================================
// QUICK SUGGESTIONS - Pills par click karne par
// ============================================================
const suggestionPills = document.querySelectorAll('.suggestion-pill');
suggestionPills.forEach(pill => {
    pill.addEventListener('click', function() {
        // Pill ka text input mein daalo (emoji hata ke)
        const text = this.textContent.trim().replace(/^[^\w]+/, '').trim();
        userInput.value = text;
        sendMessage();
    });
});


// ============================================================
// ACTION CARDS - Welcome screen ke cards par click
// ============================================================
const actionCards = document.querySelectorAll('.action-card');
actionCards.forEach(card => {
    card.addEventListener('click', function() {
        // Card ka data-question attribute lo
        const question = this.getAttribute('data-question');
        userInput.value = question;
        sendMessage();
    });
});


// ============================================================
// THEME TOGGLE - Dark/Light mode
// ============================================================
const themeToggle = document.getElementById('themeToggle');
if (themeToggle) {
    themeToggle.addEventListener('click', function() {
        const html = document.documentElement;
        const currentTheme = html.getAttribute('data-theme');
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
        html.setAttribute('data-theme', newTheme);
    });
}


// ============================================================
// CLEAR CHAT - Saari chat saaf karo
// ============================================================
const clearBtn = document.getElementById('clearBtn');
if (clearBtn) {
    clearBtn.addEventListener('click', function() {
        messagesContainer.innerHTML = '';
        if (welcomeScreen) {
            welcomeScreen.style.display = 'block';
        }
    });
}


// ============================================================
// NEW CHAT BUTTON
// ============================================================
const newChatBtn = document.getElementById('newChatBtn');
if (newChatBtn) {
    newChatBtn.addEventListener('click', function() {
        messagesContainer.innerHTML = '';
        if (welcomeScreen) {
            welcomeScreen.style.display = 'block';
        }
    });
}


// ============================================================
// MOBILE MENU TOGGLE - Sidebar kholna/band karna
// ============================================================
const menuToggle = document.getElementById('menuToggle');
const sidebar = document.getElementById('sidebar');
const sidebarOverlay = document.getElementById('sidebarOverlay');

if (menuToggle) {
    menuToggle.addEventListener('click', function() {
        sidebar.classList.add('active');
        sidebarOverlay.classList.add('active');
    });
}

if (sidebarOverlay) {
    sidebarOverlay.addEventListener('click', function() {
        sidebar.classList.remove('active');
        sidebarOverlay.classList.remove('active');
    });
}