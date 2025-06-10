# # utils/tts.py

# import requests
# import os

# def text_to_speech(text, output_file="output.wav"):
#     """
#     Convert text to speech using Cartesia API and save it to output.wav
#     """
#     try:
#         print("🗣️  Sending text to Cartesia TTS...")

#         response = requests.post(
#             url="https://api.cartesia.ai/v1/speech",
#             json={
#                 "text": text,
#                 "voice": "samantha"  # You can try voices: 'samantha', 'steve', etc.
#             },
#             stream=True
#         )

#         if response.status_code != 200:
#             print(f"❌ Error from Cartesia API: {response.status_code}")
#             print(response.text)
#             return

#         with open(output_file, "wb") as f:
#             for chunk in response.iter_content(chunk_size=1024):
#                 if chunk:
#                     f.write(chunk)

#         print(f"✅ Audio saved to {output_file}")

#     except Exception as e:
#         print(f"❌ Exception in Cartesia TTS: {e}")


# utils/tts.py
import pyttsx3

engine = pyttsx3.init()

def speak_text(text: str) -> None:
    # Save spoken response directly to output.wav
    engine.save_to_file(text, "output.wav")
    engine.runAndWait()

