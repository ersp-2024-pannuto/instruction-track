from gtts import gTTS
import os

# Ensure TTS directory exists
tts_dir = "tts_audio"
os.makedirs(tts_dir, exist_ok=True)

# Generate countdown voice clips (8 to 1)
for i in range(8, 0, -1):
    tts_path = os.path.join(tts_dir, f"countdown_{i}.mp3")
    tts = gTTS(text=str(i), lang='en', slow=False)
    tts.save(tts_path)
    print(f"Generated: {tts_path}")

# Define voice instructions
voice_cues = {
    "walk": "walk",
    "turn back": "turn back",
    "stop": "stop"
}

# Generate TTS audio files
for cue, text in voice_cues.items():
    tts_path = os.path.join(tts_dir, f"{cue}.mp3")
    tts = gTTS(text=text, lang='en', slow=False)
    tts.save(tts_path)
    print(f"Generated: {tts_path}")

print("✅ All TTS voice cues have been saved in the 'tts_audio' folder.")
