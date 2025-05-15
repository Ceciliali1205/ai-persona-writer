"""Utility wrapper around OpenAI ChatCompletion."""
import os
import openai
from dotenv import load_dotenv
load_dotenv()


openai.api_key = os.getenv("OPENAI_API_KEY")

MODEL = "gpt-4o"  # or any deployed model you prefer
print(" Loaded OpenAI key starts with:", os.getenv("OPENAI_API_KEY")[:10])

def call_openai(prompt: str) -> str:
    print("\n Sending prompt to OpenAI:\n", prompt[:500], "...\n")  # limit to first 500 chars
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.8,
    )
    return response.choices[0].message.content
