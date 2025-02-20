import librosa
import librosa.feature
import numpy as np
import matplotlib.pyplot as plt

# Load the extracted audio file
audio_file = "output_audio.wav"  # Make sure the file exists
y, sr = librosa.load(audio_file, sr=44100)

# Compute onset envelope (detects beat-like events)
onset_env = librosa.onset.onset_strength(y=y, sr=sr)

# Detect tempo (BPM)
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr, onset_envelope=onset_env)

# Convert beat frames to timestamps
beat_times = librosa.frames_to_time(beat_frames, sr=sr)

# Plot detected beats
plt.figure(figsize=(12, 4))
plt.plot(librosa.times_like(onset_env, sr=sr), onset_env, label="Onset Strength")
plt.vlines(beat_times, ymin=0, ymax=max(onset_env), color='r', linestyle="--", label="Detected Beats")
plt.xlabel("Time (s)")
plt.ylabel("Onset Strength")
plt.title(f"Detected Tempo: {float(tempo):.2f} BPM")
plt.legend()
plt.show()

print(f"Detected Tempo: {tempo:.2f} BPM")
print(f"First 10 Beat Times: {beat_times[:10]}")
