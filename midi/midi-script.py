import pretty_midi

# Define parameters for a 2-minute rhythmic MIDI file
bpm = 120  # Beats per minute (2 beats per second)
beat_duration = 60 / bpm  # Time per beat in seconds
total_duration_seconds = 120  # Full duration of 2 minutes
total_beats = total_duration_seconds * bpm / 60  # Total beats in the MIDI file

# Create a new MIDI object
midi = pretty_midi.PrettyMIDI()

# Create instrument tracks
piano = pretty_midi.Instrument(program=0)  # Instruction cues
drums = pretty_midi.Instrument(program=116, is_drum=True)  # Percussion for rhythm

# Define movement instructions with rhythmic alignment (loop every 24 beats)
movement_sequence = [
    (0, "Walking"),
    (4, "Walking Upstairs"),
    (8, "Walking Downstairs"),
    (12, "Writing '1'"),
    (16, "Writing '2'"),
    (20, "Writing '3'")
]

# Define MIDI notes for instructions
movement_notes = {
    "Walking": 60,  # C4
    "Walking Upstairs": 62,  # D4
    "Walking Downstairs": 64,  # E4
    "Writing '1'": 65,  # F4
    "Writing '2'": 67,  # G4
    "Writing '3'": 69  # A4
}

# Add metronome beats (hi-hat sound every beat for 2 minutes)
for beat in range(int(total_beats)):  # 2 minutes worth of beats
    start_time = beat * beat_duration
    note = pretty_midi.Note(
        velocity=100, pitch=42,  # Hi-hat sound
        start=start_time, end=start_time + 0.1
    )
    drums.notes.append(note)

# Add instructional cues (repeat sequence every 24 beats)
for cycle in range(int(total_beats // 24)):  # Repeat sequence multiple times
    for beat_offset, movement in movement_sequence:
        start_time = (cycle * 24 + beat_offset) * beat_duration
        note = pretty_midi.Note(
            velocity=100, pitch=movement_notes[movement],
            start=start_time, end=start_time + 0.5  # Short cue note
        )
        piano.notes.append(note)

# Add instruments to the MIDI file
midi.instruments.append(drums)
midi.instruments.append(piano)

# Save the MIDI file
midi.write("midi/har_rhythmic_instructions.mid")

print("MIDI file saved as har_rhythmic_instructions.mid")
