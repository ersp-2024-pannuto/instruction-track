from moviepy import VideoFileClip
import librosa
import numpy as np
import matplotlib.pyplot as plt

# Load the video file
video_path = "doremi_acc.mp4"
video = VideoFileClip(video_path)

# Extract audio and save as WAV
audio_path = "output_audio.wav"
video.audio.write_audiofile(audio_path)

# Load the extracted audio file with a lower sampling rate
audio, sr = librosa.load(audio_path, sr=None)
# Compute the onset envelope (detects beat-like events)
onset_env = librosa.onset.onset_strength(audio, sr=sr)

# Detect beats
tempo, beat_frames = librosa.beat.beat_track(y=audio, sr=sr, onset_envelope=onset_env)

# Convert beat frames to timestamps
beat_times = librosa.frames_to_time(beat_frames, sr=sr)

# Plot the beat structure
plt.figure(figsize=(12, 4))
plt.plot(librosa.times_like(onset_env, sr=sr), onset_env, label="Onset Strength")
plt.vlines(beat_times, ymin=0, ymax=max(onset_env), color="r", linestyle="--", label="Beats")
plt.xlabel("Time (s)")
plt.ylabel("Onset Strength")
plt.title(f"Detected Beats (Tempo: {tempo:.2f} BPM)")
plt.legend()
plt.show()

# Print detected tempo
print(f"Detected Tempo: {tempo:.2f} BPM")
print(f"First 10 Beat Times: {beat_times[:10]}")
