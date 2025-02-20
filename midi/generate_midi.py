import pretty_midi

# Define BPM from analysis
bpm = 99.38  
beat_duration = 60 / bpm  # Time per beat in seconds

# Create a new MIDI object
midi = pretty_midi.PrettyMIDI()

# Create instrument tracks
metronome = pretty_midi.Instrument(program=115, is_drum=True)  # Quieter metronome (woodblock)
rhythm_cues = pretty_midi.Instrument(program=118, is_drum=True)  # Louder rhythmic cues

# Define measure and movement cue structure (based on YAML reference)
cue_timing = {
    "moving": 0,  # Start cue
    "walk": [8, 16, 24, 32, 40],  # Key movement beats
    "turn back": [48],  # Turning point
    "stop": [64],  # End
}

# Define MIDI note mappings
note_metronome = 37  # Side stick for metronome
note_rhythm = 39  # Hand clap for movement cues

# Generate metronome (soft beat every beat)
for beat in range(0, 80):  # Assuming an 80-beat sequence
    start_time = beat * beat_duration
    metronome.notes.append(pretty_midi.Note(
        velocity=60, pitch=note_metronome, start=start_time, end=start_time + 0.1
    ))

# Add rhythmic beats for movement cues
for label, beats in cue_timing.items():
    if isinstance(beats, list):
        for beat in beats:
            start_time = beat * beat_duration
            rhythm_cues.notes.append(pretty_midi.Note(
                velocity=100, pitch=note_rhythm, start=start_time, end=start_time + 0.2
            ))

# Add instruments to MIDI file
midi.instruments.append(metronome)
midi.instruments.append(rhythm_cues)

# Save the MIDI file locally
midi_filename = "rhythmic_instructions.mid"
midi.write(midi_filename)

print(f"MIDI file saved as {midi_filename}")
