"""
============================================================
USWA AI ASSISTANT - DATABASE MODULE
============================================================
Yeh file database ka saara kaam karti hai:
1. Database aur table banati hai
2. Chat history save karti hai
3. Saari chats wapas laati hai (admin ke liye)

Hum SQLite use kar rahe hain - Python mein built-in hai.
Saara data 'database/school.db' file mein save hota hai.
============================================================
"""

import sqlite3
from datetime import datetime
import os
from datetime import datetime

def get_today_info():
    today = datetime.now()
    day_name = today.strftime("%A")  # Monday, Tuesday...
    date = today.strftime("%d %B %Y")  # 27 May 2026
    is_sunday = (day_name == "Sunday")
    return day_name, date, is_sunday
# ============================================================
# DATABASE FILE KA PATH
# ============================================================
# 'database' folder ke andar 'school.db' file
DATABASE_FOLDER = "database"
DATABASE_PATH = os.path.join(DATABASE_FOLDER, "school.db")


# ============================================================
# FUNCTION 1: DATABASE AUR TABLE BANAO
# ============================================================
# Yeh function aik dafa chalta hai - database aur table set karta hai
# ============================================================
def init_database():
    """Database aur chat_history table banata hai (agar nahi hai)."""

    # Pehle 'database' folder banao (agar nahi hai)
    if not os.path.exists(DATABASE_FOLDER):
        os.makedirs(DATABASE_FOLDER)

    # Database se connect karo (file na ho to ban jayegi)
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    # Table banao (agar pehle se nahi hai)
    # Yeh table chat history save karega
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS chat_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_message TEXT NOT NULL,
            bot_reply TEXT NOT NULL,
            timestamp TEXT NOT NULL
        )
    """)

    # Changes save karo aur connection band karo
    conn.commit()
    conn.close()

    print("Database ready hai! (database/school.db)")


# ============================================================
# FUNCTION 2: CHAT SAVE KARO
# ============================================================
# Har baar jab user sawal poochta hai aur bot jawab deta hai,
# yeh function us conversation ko database mein save karta hai
# ============================================================
def save_chat(user_message, bot_reply):
    """Aik conversation (sawal + jawab) database mein save karta hai."""

    # Database se connect karo
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    # Abhi ka time nikalo (date + time)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Data table mein daalo (INSERT)
    # ? marks security ke liye hain (SQL injection se bachne ke liye)
    cursor.execute("""
        INSERT INTO chat_history (user_message, bot_reply, timestamp)
        VALUES (?, ?, ?)
    """, (user_message, bot_reply, timestamp))

    # Save aur band
    conn.commit()
    conn.close()


# ============================================================
# FUNCTION 3: SAARI CHATS WAPAS LAAO
# ============================================================
# Yeh function database se saari conversations laata hai
# (Admin panel ke liye - Phase 6 mein use hoga)
# ============================================================
def get_all_chats():
    """Database se saari chats laata hai (newest first)."""

    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    # Saari rows nikalo, newest pehle
    cursor.execute("""
        SELECT id, user_message, bot_reply, timestamp
        FROM chat_history
        ORDER BY id DESC
    """)

    # Saari rows lo
    chats = cursor.fetchall()
    conn.close()

    return chats


# ============================================================
# FUNCTION 4: KITNI CHATS HUI (COUNT)
# ============================================================
def get_chat_count():
    """Total kitni chats save hui hain, wo number deta hai."""

    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM chat_history")
    count = cursor.fetchone()[0]
    conn.close()

    return count


# ============================================================
# TEST: Agar yeh file directly chalao
# ============================================================
if __name__ == "__main__":
    print("=" * 50)
    print("DATABASE TEST")
    print("=" * 50)

    # Database banao
    init_database()

    # Aik test chat save karo
    save_chat("Test sawal: fees kitni hai?", "Test jawab: Rs 2800 se 4000")
    print("Test chat save ho gayi!")

    # Count dekho
    print(f"Total chats: {get_chat_count()}")

    # Saari chats dikhao
    print("\nSaari chats:")
    for chat in get_all_chats():
        print(f"  ID {chat[0]} | {chat[1][:30]}... | {chat[3]}")