"""
============================================================
USWA AI ASSISTANT - FLASK BACKEND (PRODUCTION READY)
============================================================
Yeh main application file hai. Yeh:
1. Google Gemini AI use karti hai (smart jawab)
2. RAG system (sirf USWA data se jawab)
3. Har chat database mein save karti hai
4. Online deployment ke liye ready hai (Render)
============================================================
"""

# Zaroori libraries import karo
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Hamara school ka data import karo
from school_data import SCHOOL_KNOWLEDGE, get_answer

# Database functions import karo
from database import init_database, save_chat, get_all_chats, get_chat_count

# ============================================================
# ENVIRONMENT VARIABLES LOAD KARO (.env file se)
# ============================================================
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# ============================================================
# GEMINI AI SETUP
# ============================================================
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")


# ============================================================
# FLASK APP BANAO
# ============================================================
app = Flask(__name__)

# ============================================================
# DATABASE READY KARO (app start hote hi)
# ============================================================
init_database()


# ============================================================
# SCHOOL DATA KO TEXT MEIN CONVERT KARO (AI ke liye)
# ============================================================
def get_full_school_data():
    """Saara school data aik text string mein convert karta hai."""
    data_text = ""
    for topic in SCHOOL_KNOWLEDGE:
        topic_name = topic.replace("_", " ").title()
        answer = get_answer(topic)
        data_text += f"\n--- {topic_name} ---\n{answer}\n"
    return data_text


# ============================================================
# SYSTEM PROMPT - AI KO INSTRUCTIONS DENA
# ============================================================
def create_system_prompt(user_message):
    """User ke sawal ke saath complete prompt banata hai."""
    school_data = get_full_school_data()

    prompt = f"""You are the official AI Assistant for USWA Education System 
(Uswa Boys Public School and College, Yultar, Skardu).

YOUR ROLE:
You help students and parents with information about the school.

IMPORTANT RULES:
1. Answer ONLY using the school information provided below. Do NOT make up any information.
2. If the answer is not in the data below, politely say you don't have that specific 
   information and suggest contacting the school office.
3. Be warm, friendly, and professional - like a helpful school receptionist.
4. Reply in the SAME language the user uses (English, Roman Urdu, or Urdu).
5. Keep answers clear and well-organized. Use bullet points when listing things.
6. Only answer questions related to USWA Education System. If asked about unrelated 
   topics, politely redirect to school-related questions.
7. Do not use markdown symbols like ** or ## in your response. Write in clean plain text.

=================================================
USWA EDUCATION SYSTEM - OFFICIAL INFORMATION:
=================================================
{school_data}
=================================================

USER'S QUESTION: {user_message}

Your helpful response:"""

    return prompt


# ============================================================
# AI SE JAWAB LENA
# ============================================================
def get_ai_answer(user_message):
    """Gemini AI se professional jawab leta hai."""
    try:
        prompt = create_system_prompt(user_message)
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print(f"AI Error: {e}")
        return (
            "I'm having a little trouble connecting right now. "
            "Please try again in a moment, or contact the school office "
            "at 05815-555202 for immediate assistance."
        )


# ============================================================
# ROUTE 1: HOME PAGE
# ============================================================
@app.route('/')
def home():
    """Main chat page dikhata hai."""
    return render_template('index.html')


# ============================================================
# ROUTE 2: CHAT API (AI + DATABASE)
# ============================================================
@app.route('/chat', methods=['POST'])
def chat():
    """User ka message receive karke AI se jawab deta hai aur save karta hai."""
    data = request.get_json()
    user_message = data.get('message', '')

    if not user_message.strip():
        return jsonify({'reply': 'Please type a question so I can help you!'})

    bot_reply = get_ai_answer(user_message)

    # Chat ko database mein save karo
    try:
        save_chat(user_message, bot_reply)
    except Exception as e:
        print(f"Database Save Error: {e}")

    return jsonify({'reply': bot_reply})


# ============================================================
# ROUTE 3: ADMIN - SAARI CHATS DEKHO
# ============================================================
@app.route('/admin/chats')
def admin_chats():
    """Saari chat history dikhata hai (simple text format)."""
    chats = get_all_chats()
    total = get_chat_count()

    html = f"""
    <html>
    <head>
        <title>USWA Chat History</title>
        <style>
            body {{ font-family: Arial; padding: 20px; background: #f5f5f5; }}
            h1 {{ color: #1BA5E0; }}
            .stats {{ background: #1BA5E0; color: white; padding: 15px; 
                     border-radius: 10px; margin-bottom: 20px; }}
            .chat {{ background: white; padding: 15px; margin-bottom: 12px; 
                    border-radius: 10px; border-left: 4px solid #1BA5E0; }}
            .user {{ color: #0a2540; font-weight: bold; }}
            .bot {{ color: #444; margin-top: 8px; }}
            .time {{ color: #999; font-size: 12px; margin-top: 8px; }}
        </style>
    </head>
    <body>
        <h1>USWA AI Assistant - Chat History</h1>
        <div class="stats">Total Conversations: {total}</div>
    """

    for chat in chats:
        chat_id, user_msg, bot_msg, timestamp = chat
        html += f"""
        <div class="chat">
            <div class="user">Q: {user_msg}</div>
            <div class="bot">A: {bot_msg}</div>
            <div class="time">ID: {chat_id} | {timestamp}</div>
        </div>
        """

    html += "</body></html>"
    return html


# ============================================================
# APP CHALAO
# ============================================================
# IMPORTANT: Online deployment ke liye PORT environment se aata hai
# Local pe 5000 use hota hai, online pe Render apna PORT deta hai
# ============================================================
if __name__ == '__main__':
    print("=" * 50)
    print("USWA AI Assistant chal raha hai!")
    print("=" * 50)

    if not GEMINI_API_KEY:
        print("\nWARNING: GEMINI_API_KEY nahi mili! .env check karein.\n")

    # PORT environment se lo (online ke liye), warna 5000 (local ke liye)
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)