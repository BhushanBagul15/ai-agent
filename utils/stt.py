# utils/stt.py
import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()
DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY")


def transcribe_audio(audio_path):
    from dotenv import load_dotenv
    load_dotenv()
    import requests
    import os

    deepgram_api_key = os.getenv("DEEPGRAM_API_KEY")

    with open(audio_path, "rb") as audio:
        response = requests.post(
            "https://api.deepgram.com/v1/listen",
            headers={
                "Authorization": f"Token {deepgram_api_key}",
                "Content-Type": "audio/wav",
            },
            data=audio,
        )

    result = response.json()
    print("🔍 Deepgram response:", result)  # ← ADD THIS LINE

    # Now check if result has 'results' before trying to access it
    if "results" in result:
        return result["results"]["channels"][0]["alternatives"][0]["transcript"]
    else:
        raise ValueError(f"Deepgram failed to transcribe. Response: {result}")
