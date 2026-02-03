# 🎙 Voice-Enabled Chatbot (Offline)

## Overview
This project implements a **fully offline voice-to-voice conversational chatbot**.
It records speech from a microphone, transcribes it using Whisper, and responds verbally in **Hindi** using an open-source TTS model.

## Features
- Local Speech-to-Text using Whisper Small
- Hindi Text-to-Speech
- English & Hindi speech input
- Fully offline (no external APIs)
- Python 3.8+

---

## 🧠 System Architecture

Microphone
↓
Speech-to-Text (Whisper Small)
↓
(Optional Translation to Hindi)
↓
Text-to-Speech (Hindi)
↓
Speaker Output

---


## 🧩 Models Used

### 🔹 Speech-to-Text (STT)
- **Model:** `openai/whisper-small`
- **Library:** Hugging Face Transformers
- **Reason:** Supports English and Hindi with good accuracy and runs locally.

---

### 🔹 Text-to-Speech (TTS)
- **Model:** `facebook/mms-tts-hin`
- **Library:** Hugging Face Transformers
- **Reason:** Open-source Hindi TTS model with natural speech output and local inference.

---

### 🔹 Translation (English → Hindi)
- **Model:** `Helsinki-NLP/opus-mt-en-hi`
- **Purpose:** Ensures the spoken response is fully in Hindi when the input is English.
- **Note:** Translation is skipped if the input is already in Hindi.

---

## 📁 Project Structure

voice-chatbot/
│
├── main.py # Orchestrates the full pipeline
├── audio_utils.py # Handles microphone recording
├── stt.py # Speech-to-text using Whisper
├── translate.py # English → Hindi translation
├── tts.py # Hindi text-to-speech and playback
│
├── requirements.txt # Project dependencies
├── README.md # Documentation
│
└── input.wav # Recorded audio (auto-overwritten)


---

## 📄 Code Explanation

### 🔸 `audio_utils.py`
- Records audio from the microphone
- Saves clean WAV audio
- Automatically overwrites previous recordings

---

### 🔸 `stt.py`
- Uses Whisper Small for transcription
- Converts speech into text (English or Hindi)
- Runs fully offline

---

### 🔸 `translate.py`
- Translates English text to Hindi using a local model
- Ensures complete Hindi speech output

---

### 🔸 `tts.py`
- Converts Hindi text to speech
- Plays the synthesized audio via speakers

---

### 🔸 `main.py`
Controls the full application flow:
1. Record audio
2. Transcribe speech
3. Translate to Hindi (if required)
4. Synthesize Hindi speech
5. Play audio response

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone <your-github-repo-link>
cd voice-chatbot
```
### 2️⃣ Create & Activate Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```
### 3️⃣ Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```
### ▶️ Run the Application
```bash
python main.py
```
