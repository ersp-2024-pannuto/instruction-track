import pretty_midi
import mido
import os
from pydub import AudioSegment

# Define paths
midi_file = "midi\modified-Climb-Ev'ry-Mountain-(From-'The-Sound-Of-Music').mid"  # Ensure this file exists
soundfont_path = "soundfonts\GeneralUser-GS.sf2"  # Ensure you have a compatible SoundFont
tts_folder = "tts_audio"
output_mp3 = "final_instructions.mp3"

# Ensure TTS files exist
tts_files = {
    "walk": os.path.join(tts_folder, "walk.mp3"),
    "turn back": os.path.join(tts_folder, "turn back.mp3"),
    "stop": os.path.join(tts_folder, "stop.mp3")
}

# Generate countdown TTS (8 to 1)
countdown_files = []
for i in range(8, 0, -1):
    tts_path = os.path.join(tts_folder, f"count_{i}.mp3")
    if not os.path.exists(tts_path):
        from gtts import gTTS
        tts = gTTS(text=str(i), lang='en', slow=False)
        tts.save(tts_path)
    countdown_files.append(AudioSegment.from_mp3(tts_path))

# Convert MIDI to WAV using FluidSynth
def midi_to_wav(midi_file, output_wav, soundfont):
    """ Converts MIDI to WAV using FluidSynth. """
    from midi2audio import FluidSynth
    fs = FluidSynth(soundfont)
    fs.midi_to_audio(midi_file, output_wav)

# Convert WAV to MP3
def wav_to_mp3(input_wav, output_mp3):
    """ Converts WAV to MP3 using pydub. """
    audio = AudioSegment.from_wav(input_wav)
    audio.export(output_mp3, format="mp3")

# Overlay TTS onto the MP3
def overlay_tts(mp3_file, tts_files, countdown_files, output_file):
    """ Overlays TTS voice cues onto the MP3 at correct times. """
    music = AudioSegment.from_mp3(mp3_file)
    midi = pretty_midi.PrettyMIDI(midi_file)

    # Define measure points where TTS cues should play
    cue_timing = {
        "walk": [8],  # Just before first music beat
        "turn back": [48],  # Example "turn back" point
        "stop": [47]  # Ensure "stop" plays right before "turn back"
    }

    # Adjust TTS volume (make it louder than the music but not unbearable)
    tts_volume_boost = 8  # Increase volume (adjust as needed)

    # Create countdown overlayed on the first 8 metronome beats
    beat_duration = 60 / 86  # BPM 86
    countdown_overlay = AudioSegment.silent(duration=0)
    for i, count in enumerate(countdown_files):
        start_time_ms = i * beat_duration * 1000  # Place each number at a beat interval
        countdown_overlay = countdown_overlay.overlay(count, position=start_time_ms)

    # Overlay countdown on the first 8 beats of the MP3
    music = countdown_overlay.overlay(music, position=0)

    # Overlay "walk" right before the first beat of music
    walk_audio = AudioSegment.from_mp3(tts_files["walk"]).apply_gain(tts_volume_boost)
    walk_start_time = 8 * beat_duration * 1000 - 500  # Just before first music beat
    music = music.overlay(walk_audio, position=walk_start_time)

    # Overlay "stop" and "turn back"
    for cue, measures in cue_timing.items():
        tts_audio = AudioSegment.from_mp3(tts_files[cue]).apply_gain(tts_volume_boost)
        for measure in measures:
            start_time_ms = measure * beat_duration * 1000 * 4  # 4 beats per measure
            music = music.overlay(tts_audio, position=start_time_ms)

    # Export final file
    music.export(output_file, format="mp3")
    print(f"✅ Final MP3 saved as {output_file}")

# Convert MIDI to WAV
output_wav = "temp_music.wav"
midi_to_wav(midi_file, output_wav, soundfont_path)

# Convert WAV to MP3
output_mp3 = "temp_music.mp3"
wav_to_mp3(output_wav, output_mp3)

# Overlay TTS and save final MP3
overlay_tts(output_mp3, tts_files, countdown_files, "final_instructions.mp3")

# Cleanup temp files
os.remove(output_wav)
os.remove(output_mp3)

print("✅ Process complete! `final_instructions.mp3` is ready.")