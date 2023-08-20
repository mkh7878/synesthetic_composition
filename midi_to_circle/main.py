from circle import circle_plotter
from sound_inputs import intervals, midi_input, mood_analysis

from sound_inputs.midi_input import MidiInput

def main():
    # Create an instance of MidiInput class
    midi_input = MidiInput()

    # Call the find_midi_device method
    midi_input.find_midi_device()

    midi_input.music_music()


if __name__ == "__main__":
    main()
