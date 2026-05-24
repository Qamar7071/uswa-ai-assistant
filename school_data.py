"""
============================================================
USWA EDUCATION SYSTEM - SCHOOL DATA & CHATBOT KNOWLEDGE BASE
============================================================
Yeh file USWA school ka saara data rakhti hai AUR ek simple
chatbot engine bhi deti hai jo user ke sawal samajh kar sahi
jawab deta hai.

Istemaal (Usage):
    from school_data import get_response, get_answer

    # Chatbot style (user ka sawal):
    print(get_response("fees kitni hai?"))
    print(get_response("school timing batao"))

    # Direct topic ka jawab:
    print(get_answer("fees"))

Ya direct chalao (test chatbot):
    python school_data.py

Source: Official USWA Information Form
        + Official Website (https://boysyultar.uswaeducation.com/)
School: Uswa Boys Public School And College, Yultar, Skardu

NOTE: Kuch values website aur purani form mein alag thi (jaise
total students, teachers, contact details). Website wali updated
values use ki gayi hain; purani values reference ke liye
"_old_form" key mein rakhi gayi hain.
============================================================
"""

# ============================================================
# SCHOOL KNOWLEDGE BASE
# Har topic mein:
#   - 'keywords'            : chatbot matching ke liye
#   - 'data'                : structured detail (database / app ke liye)
#   - 'professional_answer' : jo chatbot bolega
# ============================================================

SCHOOL_KNOWLEDGE = {

    # --------------------------------------------------------
    # 1. SCHOOL BASIC INFORMATION
    # --------------------------------------------------------
    "school_info": {
        "keywords": [
            "about", "college", "uswa", "information", "info", "intro",
            "introduction", "established", "founded", "students",
            "kitne students", "total students", "kab bana", "bare mein",
            "barey mein", "tareekh", "history", "welcome", "school ke bare"
        ],
        "data": {
            "full_name": "Uswa Boys Public School and College, Yultar, Skardu",
            "short_name": "USWA Education System",
            "established": "1994",
            "total_students": "1,843",            # Updated from website (form had 1,823)
            "total_classes": "18",                # From website
            "teaching_staff": "83",
            "admin_staff": "27",
            "region": "Yultar, Skardu, Gilgit-Baltistan",
            "mission": "Education For All",
            "principal": "Muhammad Kazim",
            "developed_by": "SoftTech Skardu",
            "taglines": [
                "Innovative Learning",
                "Future Ready Skills",
                "Global Perspective",
                "Igniting Passion for Learning"
            ],
            "achievements": [
                "Excellent Board Results year after year",
                "Creative and professional alumni network"
            ]
        },
        "professional_answer": (
            "Uswa Boys College Yultar (Uswa Public School & College, Boys) is located in "
            "Yultar, Skardu, in the scenic and culturally rich region of Gilgit-Baltistan, "
            "and was established in 1994. With a proud history of over three decades, the "
            "school currently serves around 1,843 students across 18 classes, with 83 "
            "teaching staff and 27 administrative staff under the leadership of Principal "
            "Muhammad Kazim. Our mission is simple yet powerful: 'Education For All'. "
            "We provide an inspiring and nurturing environment for students to grow "
            "academically, socially, and personally, with a focus on critical thinking, "
            "discipline, and leadership."
        )
    },

    # --------------------------------------------------------
    # 2. ADMISSIONS
    # --------------------------------------------------------
    "admissions": {
        "keywords": [
            "admission", "admissions", "dakhla", "dakhila", "apply", "join",
            "enroll", "enrollment", "registration", "register", "form", "online admission",
            "kaise admission", "admission kaise", "entry test", "interview", "documents"
        ],
        "data": {
            "process": [
                "Submit the Admission Form",
                "Appear for the Entry Test",
                "Attend the Interview"
            ],
            "online_admission": "Available — Apply online via the school website",
            "online_admission_link": "https://boysyultar.uswaeducation.com/Home/OnlineAdmission",
            "admission_type": "Simple, fair, merit-based admissions",
            "required_documents": [
                "School Leaving Certificate",
                "B-Form (Child Registration Certificate)",
                "Previous Mark Sheet",
                "Hope and Character Certificate"
            ],
            "age_criteria_class1": "4+ years",
            "admission_test": "Yes — an entry test is conducted for admission",
            "form_fee": "Rs. 500",
            "admission_timing": "March (every year)",
            "classes_offered": "Nursery to College level"
        },
        "professional_answer": (
            "Admissions at Uswa Boys College Yultar are simple, fair, and merit-based. "
            "The process has three steps:\n\n"
            "1. Submit the Admission Form (Form Fee: Rs. 500)\n"
            "2. Appear for the Entry Test\n"
            "3. Attend the Interview\n\n"
            "You can also apply online: https://boysyultar.uswaeducation.com/Home/OnlineAdmission\n\n"
            "Required Documents:\n"
            "- School Leaving Certificate\n"
            "- B-Form\n"
            "- Previous Mark Sheet\n"
            "- Hope and Character Certificate\n\n"
            "Admissions usually open in March. We offer classes from Nursery to College level. "
            "For Class 1, the minimum age is 4+ years."
        )
    },

    # --------------------------------------------------------
    # 3. FEE STRUCTURE
    # --------------------------------------------------------
    "fees": {
        "keywords": [
            "fee", "fees", "fis", "fees structure", "fee structure", "cost", "charges",
            "kitni fees", "fees kitni", "monthly fee", "tuition", "paisa", "rupees",
            "admission fee", "annual charges", "exam fee", "discount", "discounts",
            "concession", "kitne paise"
        ],
        "data": {
            "monthly_fees": {
                "Nursery / KG": "Rs. 2,800",
                "Class 1 - 5": "Rs. 3,200",
                "Class 6 - 8": "Rs. 3,400",
                "Class 9 - 10": "Rs. 3,800",
                "Class 11 - 12": "Rs. 4,000"
            },
            "admission_fee": "Rs. 6,000 (one-time)",
            "annual_charges": "Rs. 1,000",
            "examination_fee": "Rs. 500",
            "discounts": "Available (sibling discounts and concessions)",
            "payment_method": "Cash",
            "late_fee": "None"
        },
        "professional_answer": (
            "Here is the complete fee structure at Uswa Boys College Yultar:\n\n"
            "Monthly Tuition Fees:\n"
            "- Nursery / KG: Rs. 2,800\n"
            "- Class 1 - 5: Rs. 3,200\n"
            "- Class 6 - 8: Rs. 3,400\n"
            "- Class 9 - 10: Rs. 3,800\n"
            "- Class 11 - 12: Rs. 4,000\n\n"
            "Other Charges:\n"
            "- Admission Fee (one-time): Rs. 6,000\n"
            "- Annual Charges: Rs. 1,000\n"
            "- Examination Fee: Rs. 500\n\n"
            "Discounts and concessions are available, including for siblings. Payments are "
            "accepted in cash, and there are currently no late fee charges."
        )
    },

    # --------------------------------------------------------
    # 4. SCHOOL TIMINGS
    # --------------------------------------------------------
    "timings": {
        "keywords": [
            "timing", "timings", "time", "school time", "open", "close", "opening",
            "closing", "hours", "kab khulta", "kitne baje", "kab band", "recess",
            "break", "winter timing", "office hours", "working days", "din", "schedule"
        ],
        "data": {
            "start_time": "8:00 AM",
            "end_time": "2:15 PM",
            "working_days": "Monday to Saturday (6 days)",
            "weekly_off": "Sunday",
            "office_hours": "7:30 AM to 3:00 PM",
            "recess_break": "11:50 AM to 12:20 PM",
            "winter_timings": "9:00 AM to 2:00 PM"
        },
        "professional_answer": (
            "Our school timings are as follows:\n\n"
            "- School Hours: 8:00 AM to 2:15 PM (Monday to Saturday)\n"
            "- Weekly Off: Sunday\n"
            "- Recess Break: 11:50 AM - 12:20 PM\n"
            "- Winter Timings: 9:00 AM - 2:00 PM\n"
            "- Office Hours: 7:30 AM - 3:00 PM\n\n"
            "The office stays open from 7:30 AM to 3:00 PM for any queries or assistance."
        )
    },

    # --------------------------------------------------------
    # 5. HOLIDAYS
    # --------------------------------------------------------
    "holidays": {
        "keywords": [
            "holiday", "holidays", "chutti", "chuttiyan", "vacation", "vacations",
            "break", "summer break", "winter break", "eid", "eid holidays",
            "kab chutti", "chutti kab"
        ],
        "data": {
            "summer_break": "20 days",
            "winter_break": "75 days",
            "eid_holidays": "10 days per Eid",
            "spring_break": "None",
            "other_holidays": "National Holidays and Religious Holidays"
        },
        "professional_answer": (
            "Here is the holiday schedule at Uswa Boys College Yultar:\n\n"
            "- Summer Break: Approximately 20 days\n"
            "- Winter Break: Approximately 75 days (longer due to Skardu's cold climate)\n"
            "- Eid Holidays: 10 days for each Eid\n\n"
            "We also observe all National Holidays and Religious Holidays. Exact dates are "
            "announced in advance through official school notices."
        )
    },

    # --------------------------------------------------------
    # 6. TEACHERS & STAFF
    # --------------------------------------------------------
    "teachers": {
        "keywords": [
            "teacher", "teachers", "staff", "faculty", "ustad", "ustaad", "teaching staff",
            "academic staff", "admin staff", "principal", "kon kon", "teacher kitne",
            "kitne teachers", "qualified", "qualification"
        ],
        "data": {
            "principal": "Muhammad Kazim",
            "total_teachers": "83",               # From website (form had 109)
            "admin_staff": "27",                  # From website
            "qualifications": "Mostly M.Phil, M.Sc, MA, BS and BA degree holders",
            "staff_ratio": "50:50 (Male to Female)",
            "special_features": "Subject specialists for all subjects",
            "notable_faculty": [
                "Anila Maryam (M.Phil)",
                "Qaisar Abbas Mazahir (M.Phil)",
                "Ishrat Fatima (M.Phil)",
                "Siddiqa Batool (M.Sc, M.Phil)",
                "Muhammad Nazir (M.Sc)",
                "Muhammad Jaffar (MA Edu)",
                "Masooma Batool (MA Edu)"
            ]
        },
        "professional_answer": (
            "Uswa Boys College Yultar takes great pride in its qualified team:\n\n"
            "- Principal: Mr. Muhammad Kazim\n"
            "- Teaching Staff: 83 teachers\n"
            "- Administrative Staff: 27 members\n"
            "- Qualifications: Most teachers hold M.Phil, M.Sc, MA, BS and BA degrees\n"
            "- Staff Ratio: A balanced 50:50 male-to-female ratio\n\n"
            "We have dedicated subject specialists for all subjects, ensuring that students "
            "receive expert guidance in every area of their studies."
        )
    },

    # --------------------------------------------------------
    # 7. SUBJECTS & CURRICULUM
    # --------------------------------------------------------
    "subjects": {
        "keywords": [
            "subject", "subjects", "curriculum", "course", "courses", "syllabus",
            "board", "medium", "kya parhate", "kaunse subjects", "facilities",
            "lab", "library", "sports", "extra curricular", "activities", "academics"
        ],
        "data": {
            "primary": "Urdu, English, Mathematics, Phonics, Islamiat (Class 1-5)",
            "middle": "Urdu, English, Mathematics, Science, Computer, Islamiat (Class 6-8)",
            "secondary": "Urdu, English, Mathematics, Biology, Physics, Chemistry, Computer, Islamiat (Class 9-10)",
            "medium": "Both Urdu and English",
            "board": "Federal Board",
            "extra_curricular": "Sports, Debates, Science & IT Exhibitions",
            "facilities": "Computer Lab, Library, Science Lab, Sports Ground"
        },
        "professional_answer": (
            "Uswa Boys College Yultar follows the Federal Board curriculum, with instruction "
            "in both Urdu and English.\n\n"
            "Subjects by Level:\n"
            "- Primary (Class 1-5): Urdu, English, Mathematics, Phonics, Islamiat\n"
            "- Middle (Class 6-8): Urdu, English, Mathematics, Science, Computer, Islamiat\n"
            "- Secondary (Class 9-10): Urdu, English, Mathematics, Biology, Physics, Chemistry, Computer, Islamiat\n\n"
            "Beyond academics, we offer a rich range of extra-curricular activities including "
            "Sports, Debates, and Science & IT Exhibitions. Our campus facilities include a "
            "Computer Lab, Library, Science Lab, and a Sports Ground."
        )
    },

    # --------------------------------------------------------
    # 8. CONTACT INFORMATION
    # --------------------------------------------------------
    "contact": {
        "keywords": [
            "contact", "phone", "number", "call", "email", "address", "location",
            "where", "kahan", "rabta", "raabta", "website", "facebook", "whatsapp",
            "social media", "kahan hai", "map", "directions", "instagram", "youtube"
        ],
        "data": {
            "phone": ["05815-450869", "0346-9532217"],   # From official website
            "phone_old_form": "05815-555202",             # From original form (reference)
            "whatsapp": "0343-5576948",
            "address": "Uswa Boys College Yultar, Near Bus Stand, Airport Road, Skardu",
            "email": "info@uswaboysyultar.com",           # From official website
            "email_old_form": "uswaboysyultar@gmail.com", # From original form (reference)
            "website": "https://boysyultar.uswaeducation.com/",
            "lms_portal": "https://boysyultar.uswaeducation.com/Admin/AdminLogin",
            "facebook": "https://www.facebook.com/uswaboyscollegeskardu/",
            "instagram": "https://www.instagram.com/reel/CiKxQ8NJ8Uy/",
            "youtube": "https://www.youtube.com/watch?v=i3SpI2KW0tM",
            "principal_contact": "0343-5576948"
        },
        "professional_answer": (
            "You can reach Uswa Boys College Yultar through any of the following:\n\n"
            "- Phone: 05815-450869, 0346-9532217\n"
            "- WhatsApp: 0343-5576948\n"
            "- Email: info@uswaboysyultar.com\n"
            "- Address: Near Bus Stand, Airport Road, Skardu\n"
            "- Website: https://boysyultar.uswaeducation.com/\n"
            "- Facebook: facebook.com/uswaboyscollegeskardu\n\n"
            "Our office is open from 7:30 AM to 3:00 PM. Feel free to call, message, or visit us "
            "— we are always happy to help!"
        )
    },

    # --------------------------------------------------------
    # 9. VISION, MISSION & VALUES
    # --------------------------------------------------------
    "vision_mission": {
        "keywords": [
            "vision", "mission", "values", "goal", "goals", "aim", "purpose",
            "maqsad", "philosophy", "principles"
        ],
        "data": {
            "vision": (
                "To be a premier institution for education in the region, known for "
                "producing confident, capable, and compassionate leaders who make "
                "meaningful contributions to society, where every student is encouraged "
                "to reach their full potential in a progressive, inclusive, and "
                "empowering academic environment."
            ),
            "mission": (
                "To provide a nurturing environment that fosters academic excellence, "
                "personal growth, and the development of leadership skills, through quality "
                "teaching, innovative learning methods, and extracurricular engagement."
            ),
            "values": (
                "Rooted in academic excellence, moral integrity, and leadership — "
                "emphasizing critical thinking, collaboration, adaptability, cultural "
                "understanding, and ethical conduct, preparing students not just for "
                "exams, but for life."
            )
        },
        "professional_answer": (
            "Vision, Mission & Values of Uswa Boys College Yultar:\n\n"
            "VISION: To be a premier institution known for producing confident, capable, and "
            "compassionate leaders who contribute meaningfully to society, where every student "
            "is encouraged to reach their full potential.\n\n"
            "MISSION: To provide a nurturing environment that fosters academic excellence, "
            "personal growth, and leadership skills through quality teaching, innovative learning, "
            "and extracurricular engagement.\n\n"
            "VALUES: Rooted in academic excellence, moral integrity, and leadership - emphasizing "
            "critical thinking, collaboration, adaptability, and ethical conduct, preparing students "
            "not just for exams, but for life."
        )
    },

    # --------------------------------------------------------
    # 10. ACHIEVEMENTS / OUR STARS (Top Students)
    # --------------------------------------------------------
    "achievements": {
        "keywords": [
            "achievement", "achievements", "stars", "toppers", "topper", "top students",
            "position", "result", "results", "kamiyabi", "best students", "marks",
            "highest marks", "our stars"
        ],
        "data": {
            "top_students": [
                {"name": "Atif Ali", "marks": "1050/1100"},
                {"name": "Kubra Khan", "marks": "955/1000"},
                {"name": "Muhammad Hassan Khan", "marks": "900/1000"},
                {"name": "Akmal", "marks": "Topper"},
                {"name": "Basit Ali", "marks": "Topper"}
            ]
        },
        "professional_answer": (
            "Uswa Boys College Yultar is proud of its high-achieving students ('Our Stars'):\n\n"
            "- Atif Ali: 1050/1100\n"
            "- Kubra Khan: 955/1000\n"
            "- Muhammad Hassan Khan: 900/1000\n"
            "- Akmal and Basit Ali: among our top performers\n\n"
            "These outstanding results reflect the dedication of our students and the quality "
            "of teaching at our institution."
        )
    }
}


# ============================================================
# GREETINGS, THANKS & FALLBACK (chatbot ke liye)
# ============================================================
GREETINGS = {
    "keywords": ["hi", "hello", "salam", "salaam", "assalam", "aoa", "hey", "good morning",
                 "good afternoon", "good evening", "asalam o alaikum"],
    "answer": (
        "Assalam-o-Alaikum! Welcome to Uswa Boys College Yultar. "
        "How can I help you today? You can ask me about admissions, fees, timings, "
        "subjects, staff, contact details, and more."
    )
}

THANKS = {
    "keywords": ["thanks", "thank you", "shukriya", "shukria", "thank u", "thx"],
    "answer": "You're most welcome! If you have any other questions, feel free to ask. 😊"
}

FALLBACK_ANSWER = (
    "I'm sorry, I don't have information on that specific topic yet. "
    "You can ask me about:\n"
    "- Admissions & how to apply\n"
    "- Fee structure\n"
    "- School timings & holidays\n"
    "- Subjects & curriculum\n"
    "- Teachers & staff\n"
    "- Vision, mission & achievements\n"
    "- Contact information\n\n"
    "For anything else, please call us at 05815-450869."
)


# ============================================================
# CHATBOT ENGINE
# ============================================================
def get_response(user_message):
    """
    User ka message leta hai aur sabse behtareen jawab return karta hai.
    Yeh keyword-matching use karta hai: jis topic ke sabse zyada keywords
    message mein milte hain, wohi jawab diya jata hai.
    """
    if not user_message or not user_message.strip():
        return "Please type a question and I'll be happy to help!"

    msg = user_message.lower().strip()

    # 1) Greetings check
    if any(word in msg for word in GREETINGS["keywords"]):
        return GREETINGS["answer"]

    # 2) Thanks check
    if any(word in msg for word in THANKS["keywords"]):
        return THANKS["answer"]

    # 3) Topic matching - har topic ke liye score nikaalo
    best_topic = None
    best_score = 0
    for topic, content in SCHOOL_KNOWLEDGE.items():
        score = sum(1 for kw in content["keywords"] if kw in msg)
        if score > best_score:
            best_score = score
            best_topic = topic

    # 4) Agar koi topic mila to uska jawab do, warna fallback
    if best_topic and best_score > 0:
        return SCHOOL_KNOWLEDGE[best_topic]["professional_answer"]

    return FALLBACK_ANSWER


def get_answer(topic):
    """
    Seedha kisi topic ka jawab nikaalne ke liye.
    Misaal: get_answer("fees")
    """
    if topic in SCHOOL_KNOWLEDGE:
        return SCHOOL_KNOWLEDGE[topic].get("professional_answer", "Information available.")
    return "Sorry, I don't have information on that topic yet."


def get_data(topic):
    """
    Kisi topic ka structured data (dictionary) return karta hai.
    Misaal: get_data("fees")["monthly_fees"]
    """
    if topic in SCHOOL_KNOWLEDGE:
        return SCHOOL_KNOWLEDGE[topic].get("data", {})
    return {}


# ============================================================
# SIMPLE COMMAND-LINE CHATBOT (test ke liye)
# Run: python school_data.py
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("  USWA BOYS COLLEGE YULTAR - CHATBOT")
    print("  (Type 'quit' or 'exit' to stop)")
    print("=" * 60)
    print("\nBot: " + GREETINGS["answer"] + "\n")

    while True:
        try:
            user = input("You: ")
        except (EOFError, KeyboardInterrupt):
            print("\nBot: Allah Hafiz! 👋")
            break

        if user.lower().strip() in ("quit", "exit", "bye", "khuda hafiz", "allah hafiz"):
            print("Bot: Allah Hafiz! Take care. 👋")
            break

        print("\nBot: " + get_response(user) + "\n")