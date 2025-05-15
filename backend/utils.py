import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

MODEL = "gpt-4o"  # or "gpt-4"

def call_openai(prompt: str) -> str:
    print("📤 Prompt sent to OpenAI:\n", prompt[:300], "...\n")
    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.8,
        )
        return response.choices[0].message.content
    except Exception as e:
        print("❌ OpenAI API call failed:", e)
        return "OpenAI error."
