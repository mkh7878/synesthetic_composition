"""
Author: Mae Horak for masters thesis - Synesthetic Composition 2023

Description: What is synesthetic composition? It's an application I am
developing that uses imagery generated by machine learning that reacts
to live audio to combine the sense of hearing and sight.

This program takes input from a midi keyboard or live audio through a microphone
Then uses it to graph x and y coordinates that represent the "mood" of the music

https://github.com/mkh7878/synesthetic_composition

"""

# from circle.circle_plotter import CirclePlotter
# from sound_inputs import intervals, midi_input, mood_analysis
# from sound_inputs.midi_input import MidiInput
# from sound_inputs.mood_analysis import KeyAnaylsis
# from video_output.happy_sad import HappySad
# import threading
#


from circle.circle_plotter import CirclePlotter
from sound_inputs import intervals, midi_input, mood_analysis
from sound_inputs.midi_input import MidiInput
import threading


def main():
    event = threading.Event()

    # Create an instance of MidiInput class
    midi_input = MidiInput(event)
    midi_input.find_midi_device()

    # Start a thread for the music_music method
    music_thread = threading.Thread(target=midi_input.music_music)
    music_thread.start()

    plotter = CirclePlotter(event)
    circle_thread = threading.Thread(target=plotter.start_plot())
    circle_thread.start()

    #Prints current interval (for debugging)
    while True:
        current_note_interval = midi_input.note_queue.get()  # Get the interval from the queue
        print(current_note_interval)
        # Process the interval or perform other actions as needed

    #pass circleplotter the current note & update circle


if __name__ == "__main__":
    main()
