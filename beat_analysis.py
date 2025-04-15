''' This script analyzes the beat of a MIDI file using librosa.
It loads the MIDI file, computes the onset envelope to detect beat-like events,'''
import os
import librosa
import matplotlib.pyplot as plt

# Load the extracted audio file
MIDI_FILE = "instruction_synth/midi"
def analyze_beat(file_name):
    try:
        file_path = os.path.join(MIDI_FILE, f"{file_name}.mid")
        y, sr = librosa.load(file_path, sr=44100)
    except Exception as e:
        print(f"Error loading file {file_name}: {e}")
        return  # Exit the function if the file cannot be loaded

    # Compute onset envelope (detects beat-like events)
    onset_env = librosa.onset.onset_strength(y=y, sr=sr)
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr, onset_envelope=onset_env)  # Detect tempo (BPM)
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
    return

if __name__ == "__main__":
    # Example usage
    analyze_beat("Yankee_doodle_Saloon_style")

