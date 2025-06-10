# utils/llm.py

import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_response(prompt):
    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",  # or "llama3-70b-8192", "gemma-7b-it"
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error generating response: {str(e)}"
