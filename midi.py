import pretty_midi

# Load the existing "piano only" MIDI file
midi_path = "midi\piano-Do-Re-Mi-(From-'The-Sound-Of-Music').mid"
midi = pretty_midi.PrettyMIDI(midi_path)

# Define constants
bpm = 170
beat_duration = 60 / bpm  # Time per beat in seconds
intro_duration = 8  # 8 seconds of metronome before the music starts
total_beats_intro = int(intro_duration / beat_duration)  # Number of beats in 8 sec

# Create new MIDI object for the modified version
modified_midi = pretty_midi.PrettyMIDI()

# Create new instrument tracks for metronome and rhythm cues
metronome = pretty_midi.Instrument(program=115, is_drum=True)  # Quieter metronome (woodblock)
rhythm_cues = pretty_midi.Instrument(program=118, is_drum=True)  # Louder rhythmic cues

# Define MIDI note mappings
note_metronome = 37  # Side stick for metronome (soft beat)
note_rhythm = 39  # Hand clap for movement cues (strong beat)

# Generate metronome for the 8-second intro
for beat in range(0, total_beats_intro, 2):
    start_time = beat * beat_duration
    metronome.notes.append(pretty_midi.Note(
        velocity=40, pitch=note_metronome, start=start_time, end=start_time + 0.1
    ))

# Shift all existing notes forward by 8 seconds
shift_time = intro_duration  # Move all music forward by 8 seconds

for instrument in midi.instruments:
    new_instrument = pretty_midi.Instrument(program=instrument.program, is_drum=instrument.is_drum)
    for note in instrument.notes:
        new_note = pretty_midi.Note(
            velocity=note.velocity,
            pitch=note.pitch,
            start=note.start + shift_time,  # Shift forward
            end=note.end + shift_time
        )
        new_instrument.notes.append(new_note)
    modified_midi.instruments.append(new_instrument)

# Generate rhythmic beats every 8 beats (starting after metronome intro)
total_duration = midi.get_end_time() + shift_time
total_beats = int(total_duration / beat_duration)

for beat in range(total_beats_intro, total_beats, 8):
    start_time = beat * beat_duration
    rhythm_cues.notes.append(pretty_midi.Note(
        velocity=100, pitch=note_rhythm, start=start_time, end=start_time + 0.2
    ))

# Add the new metronome and rhythm cue tracks
modified_midi.instruments.append(metronome)
# modified_midi.instruments.append(rhythm_cues)

# Save the new MIDI file
new_midi_filename = "midi\modified-piano-Do-Re-Mi-(From-'The-Sound-Of-Music').mid"
modified_midi.write(new_midi_filename)

print(f"✅ MIDI file saved as {new_midi_filename}")
