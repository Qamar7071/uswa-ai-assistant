"""
============================================================
USWA AI ASSISTANT - FLASK BACKEND (GROQ POWERED)
============================================================
Yeh main application file hai. Ab yeh Groq AI use karti hai:
1. Groq (Llama 3.3) - bohot tez aur 14,400 free requests/day
2. RAG system (sirf USWA data se jawab)
3. Har chat database mein save karti hai
4. Online deployment ke liye ready
============================================================
"""

# Zaroori libraries import karo
from flask import Flask, render_template, request, jsonify
from groq import Groq
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta, timezone

# Hamara school ka data import karo
from school_data import SCHOOL_KNOWLEDGE, get_answer

# Database functions import karo
from database import init_database, save_chat, get_all_chats, get_chat_count

# ============================================================
# ENVIRONMENT VARIABLES LOAD KARO (.env file se)
# ============================================================
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# ============================================================
# GROQ AI SETUP
# ============================================================
# Groq client banao API key ke saath
client = Groq(api_key=GROQ_API_KEY)

# Model select karo (Llama 3.3 - smart aur tez)
AI_MODEL = "llama-3.3-70b-versatile"


# ============================================================
# FLASK APP BANAO
# ============================================================
app = Flask(__name__)

# Database ready karo
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
# AAJ KI DATE AUR DIN (Pakistan Time)
# ============================================================
def get_today_info():
    """Aaj ki date aur din nikalta hai (Pakistan timezone PKT = UTC+5)."""
    # Pakistan timezone (UTC + 5 hours)
    pakistan_time = datetime.now(timezone.utc) + timedelta(hours=5)
    day_name = pakistan_time.strftime("%A")       # Monday, Tuesday...
    date_str = pakistan_time.strftime("%d %B %Y")  # 27 May 2026
    is_sunday = (day_name == "Sunday")
    return day_name, date_str, is_sunday


# ============================================================
# SYSTEM PROMPT - AI KO INSTRUCTIONS DENA
# ============================================================
def create_system_prompt():
    """AI ka system prompt banata hai (rules + school data + aaj ki date)."""
    school_data = get_full_school_data()

    # Aaj ki date aur din nikalo
    day_name, date_str, is_sunday = get_today_info()
    sunday_note = "Today is Sunday, so the school is CLOSED (weekly off)." if is_sunday \
        else f"Today is {day_name}, a regular school day (school is open, timing 8:00 AM to 2:15 PM)."

    today_info = (
        f"\n=================================================\n"
        f"TODAY'S DATE INFORMATION (use this for 'is school open today' type questions):\n"
        f"- Today's date: {date_str}\n"
        f"- Today's day: {day_name}\n"
        f"- {sunday_note}\n"
        f"- IMPORTANT: For religious holidays (Eid, etc.), the dates change every year based "
        f"on the moon. If today might be near a religious holiday, tell the user to confirm "
        f"with the school office, since you cannot be 100% sure of exact religious holiday dates.\n"
        f"=================================================\n"
    )

    system_prompt = f"""You are the official AI Assistant for USWA Education System 
(Uswa Boys Public School and College, Yultar, Skardu).

YOUR ROLE:
You are a warm, caring, and professional school representative - just like a friendly and 
experienced school receptionist who genuinely wants to help. You speak naturally and politely, 
making parents and students feel comfortable and welcomed, while always staying professional.

YOUR PERSONALITY & TONE:
- Be warm and human, not robotic. Talk like a real, caring person - not like a machine.
- Greet people warmly. For example, respond to greetings with warmth before answering.
- Show empathy and understanding. If a parent seems worried (e.g. about admission), 
  acknowledge their concern kindly before giving information.
- Use natural, conversational language. Avoid sounding stiff, mechanical, or list-like 
  unless you are actually listing items (like fees or documents).
- Be encouraging and positive about the school, but always honest and accurate.
- Do NOT use emojis. Keep it clean and professional with words only.
- Address people respectfully (you can use phrases like "Ji", "Ji bilkul", "zaroor" in 
  Roman Urdu, or polite English equivalents).
- End helpfully - gently invite them to ask more if they need anything else.

IMPORTANT RULES:
1. Answer ONLY using the school information provided below. Do NOT make up any information.
2. If the answer is not in the data below, politely say you don't have that specific 
   information and suggest contacting the school office.
3. Always be warm, friendly, caring, and professional - like a helpful, kind school 
   receptionist who treats every person with respect and patience.
4. Reply in the SAME language the user uses (English, Roman Urdu, or Urdu).
5. Keep answers clear and well-organized. Use bullet points when listing things.
6. Only answer questions related to USWA Education System. If asked about unrelated 
   topics, politely redirect to school-related questions.
7. Do not use markdown symbols like ** or ## in your response. Write in clean plain text.
8. DEVELOPER INFORMATION: If anyone asks about who developed/made/created this software, 
   the developer, technical issues, bugs, software problems, or how the system was built, 
   respond with this information:
   "This USWA AI Assistant was developed by Qamar.
   For any technical issues, software updates, or development queries, please contact the developer:
   Email: qamarjamal7071@gmail.com
   Phone/WhatsApp: 0340-8280700
   For school-related questions, I'm always here to help!"
9. SCHOOL OPEN/CLOSED: When someone asks if school is open or closed today, use the 
   "Today's Date Information" section below. Check the day and the holiday schedule. 
   For religious holidays whose exact dates you are unsure of, advise confirming with the office.
{today_info}
=================================================
USWA EDUCATION SYSTEM - OFFICIAL INFORMATION:
=================================================
{school_data}
=================================================
"""
    return system_prompt


# ============================================================
# AI SE JAWAB LENA (GROQ)
# ============================================================
def get_ai_answer(user_message):
    """Groq AI se professional jawab leta hai."""
    try:
        # System prompt (rules + data) banao
        system_prompt = create_system_prompt()

        # Groq ko message bhejo
        # System message = rules + data
        # User message = sawal
        response = client.chat.completions.create(
            model=AI_MODEL,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ],
            temperature=0.7,  # Thora creative lekin focused
            max_tokens=1024   # Jawab ki max length
        )

        # Jawab nikalo aur return karo
        return response.choices[0].message.content.strip()

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

    # AI se jawab lo
    bot_reply = get_ai_answer(user_message)

    # Database mein save karo
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
    """Saari chat history dikhata hai."""
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
if __name__ == '__main__':
    print("=" * 50)
    print("USWA AI Assistant (Groq Powered) chal raha hai!")
    print("=" * 50)

    if not GROQ_API_KEY:
        print("\nWARNING: GROQ_API_KEY nahi mili! .env check karein.\n")

    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)