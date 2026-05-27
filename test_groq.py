from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
key = os.getenv("GROQ_API_KEY")

print("=" * 40)
if not key:
    print("MASLA: GROQ_API_KEY .env se nahi mili!")
else:
    print(f"Key mili: {key[:8]}...{key[-4:]}")
print("=" * 40)

try:
    client = Groq(api_key=key)
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": "say hello"}],
        max_tokens=50
    )
    print("AI ka jawab:", response.choices[0].message.content)
    print("SAB SAHI! Key kaam kar rahi hai!")
except Exception as e:
    print("ERROR aaya:")
    print(e)