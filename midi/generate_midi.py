import pretty_midi

# Define BPM and total duration
bpm = 99.38  
beat_duration = 60 / bpm  # Time per beat in seconds
total_duration = 120  # 2 minutes in seconds
total_beats = int(total_duration / beat_duration)  # Total beats

# Create a new MIDI object
midi = pretty_midi.PrettyMIDI()

# Create instrument tracks
metronome = pretty_midi.Instrument(program=115, is_drum=True)  # Quieter metronome (woodblock)
rhythm_cues = pretty_midi.Instrument(program=118, is_drum=True)  # Louder rhythmic cues

# Define MIDI note mappings
note_metronome = 37  # Side stick for metronome
note_rhythm = 39  # Hand clap for movement cues

# Generate metronome (soft beat every beat)
for beat in range(total_beats):  # Ensuring 2-minute duration
    start_time = beat * beat_duration
    metronome.notes.append(pretty_midi.Note(
        velocity=60, pitch=note_metronome, start=start_time, end=start_time + 0.1
    ))

# Generate rhythmic beats every 8 beats
for beat in range(0, total_beats, 8):  
    start_time = beat * beat_duration
    rhythm_cues.notes.append(pretty_midi.Note(
        velocity=100, pitch=note_rhythm, start=start_time, end=start_time + 0.2
    ))

# Add instruments to MIDI file
midi.instruments.append(metronome)
midi.instruments.append(rhythm_cues)

# Save the MIDI file locally
midi_filename = "midi/rhythmic_instructions.mid"
midi.write(midi_filename)

print(f"MIDI file saved as {midi_filename}")
