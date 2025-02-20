import pretty_midi

# Load the MIDI file
midi_path = "midi\Climb-Ev'ry-Mountain-(From-'The-Sound-Of-Music').mid"  # Adjust file path if needed
midi = pretty_midi.PrettyMIDI(midi_path)

# Extract tempo and structure
tempo_changes, tempo_values = midi.get_tempo_changes()
instrument_list = [instr.name for instr in midi.instruments]
total_duration = midi.get_end_time()

# Get first tempo value
initial_tempo = tempo_values[0] if len(tempo_values) > 0 else None

# Print results
print(f"Initial Tempo: {initial_tempo} BPM")
print(f"Total Duration: {total_duration:.2f} seconds")
print(f"Instruments: {instrument_list}")
