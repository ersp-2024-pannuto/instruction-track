# Re-run MIDI generation since execution state was reset

import pretty_midi

# Define BPM and total duration from analysis
bpm = 86  
beat_duration = 60 / bpm  # Time per beat in seconds
total_duration = 99.77  # As detected from the uploaded MIDI
total_beats = int(total_duration / beat_duration)  # Total beats

# Re-load the original MIDI file
midi_path = "midi\Climb-Ev'ry-Mountain-(From-'The-Sound-Of-Music').mid"
midi = pretty_midi.PrettyMIDI(midi_path)

# Create new instrument tracks for metronome and rhythmic beats
metronome = pretty_midi.Instrument(program=115, is_drum=True)  # Quieter metronome (woodblock)
rhythm_cues = pretty_midi.Instrument(program=118, is_drum=True)  # Louder rhythmic cues

# Define MIDI note mappings
note_metronome = 37  # Side stick for metronome (soft beat)
note_rhythm = 39  # Hand clap for movement cues (strong beat)

# Generate metronome (soft beat every beat)
for beat in range(total_beats):  # Ensuring duration consistency
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

# Save the modified MIDI file
midi_filename = "midi\modified-Climb-Ev'ry-Mountain-(From-'The-Sound-Of-Music').mid"
midi.write(midi_filename)

# Provide file for download
midi_filename
