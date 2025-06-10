# main.py
from utils.stt import transcribe_audio
from utils.llm import generate_response
# from utils.tts import text_to_speech
from utils.tts import speak_text
from utils.metrics import log_metrics
import time

def run_agent(audio_path):
    start_time = time.time()
    
    transcript = transcribe_audio(audio_path)
    eou_time = time.time()

    response = generate_response(transcript)
    ttft_time = time.time()

    # text_to_speech(response)
    speak_text(response)

    ttfb_time = time.time()

    total_latency = ttfb_time - start_time

    log_metrics(
        eou_delay=eou_time - start_time,
        ttft=ttft_time - eou_time,
        ttfb=ttfb_time - ttft_time,
        total_latency=total_latency
    )

    print(f"User said: {transcript}")
    print(f"Agent replied: {response}")
    print("Response saved as output.wav")

# Test
if __name__ == "__main__":
    run_agent(r"C:\Users\bhush\OneDrive\Desktop\Projects\ai-voice-agent\questions_money.wav")


