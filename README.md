#  Real-Time AI Voice Agent

A modular real-time AI voice agent that:
- Listens to user audio input
- Transcribes it using Deepgram or OpenAI Whisper
- Generates intelligent responses using OpenAI GPT
- Speaks responses using ElevenLabs or pyttsx3 (offline TTS fallback)
- Logs detailed latency metrics in an Excel file

>  API keys are stored securely in a `.env` file (excluded from Git)

---

## Features

-  **STT (Speech-to-Text)** with Deepgram or Whisper
-  **LLM-based Response** using OpenAI GPT
-  **TTS (Text-to-Speech)** with ElevenLabs or offline pyttsx3
-  **Latency Tracking**: EOU Delay, TTFT, TTFB
-  **Modular Structure** for easy extension and debugging

---

##  Project Structure

ai-voice-agent/
│
├── main.py # Main execution script
├── stt.json # STT provider configurations
├── .env # Secret API keys (not tracked)
├── logs/
│ └── session_metrics.xlsx # Latency logs
├── utils/
│ ├── stt.py # Transcription logic
│ ├── llm.py # GPT response logic
│ ├── tts.py # TTS synthesis (ElevenLabs/pyttsx3)
│ └── metrics.py # Latency calculation + logging
├── requirements.txt # Python dependencies
└── README.md # Project overview (this file)

yaml
Copy
Edit

---

## ⚙️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/BhushanBagul15/ai-agent.git
cd ai-agent


.env
OPENAI_API_KEY=your_openai_key
DEEPGRAM_API_KEY=your_deepgram_key
ELEVENLABS_API_KEY=your_elevenlabs_key
LIVEKIT_URL=wss://your-livekit-url
LIVEKIT_API_KEY=your_livekit_api_key
LIVEKIT_API_SECRET=your_livekit_api_secret

Run the Agent
python main.py


You can test with a sample audio file like harvard.wav
