"""
Module: midi_input.py
Author: Mae Horak for masters thesis - Synesthetic Composition 2023
Description:
Takes the input from midi keyboard and plays the note using a basic sine wave
Adds interval to list of intervals and prints music note to console for analysis

"""

import mido
import numpy as np
import queue
import sounddevice as sd
from sound_inputs import intervals, mood_analysis
import threading


class MidiInput:

    """
    find_midi_device: sets backend, gets input names of MIDI devices, sets first device on the list as input device

    generate_sine_wave: generates sine wave

    play_sound: uses the sine wave from generate_sine_wave method to play sound

    music_music: sets frequency and duration of note and triggers play_sound function when a MIDI key is pressed
                 adds the interval number to the captured_notes list in intervals.py and prints musical note to console
    """

    def __init__(self):

        # self.note_queue = queue.Queue()  # Create a queue for note intervals
        self.previous_note = None
        self.input_name = None
        self.port = None
        self.captured_notes_lock = threading.Lock()

    def find_midi_device(self):
        mido.set_backend('mido.backends.portmidi')
        input_names = mido.get_input_names()
        print("Available MIDI input devices:")

        for name in input_names:
            print(name)

        if input_names:
            self.input_name = input_names[0]  # Assuming your MIDI keyboard is the first device in the list
            print(f"Using MIDI input device: {self.input_name}")
            self.port = mido.open_input(self.input_name)
            print(f"Connected to {self.input_name}...")

    def generate_sine_wave(self, frequency, duration, sample_rate):
        t = np.linspace(0, duration, int(duration * sample_rate), endpoint=False)
        wave = np.sin(2 * np.pi * frequency * t)
        return wave

    def play_sound(self, frequency, duration, sample_rate=44100):
        audio_data = self.generate_sine_wave(frequency, duration, sample_rate)
        sd.play(audio_data, sample_rate, blocking=True)  # Use blocking=True to ensure audio is played

    def music_music(self):

        while True:
            for message in self.port.iter_pending():

                if message.type == 'note_on':

                    frequency = 2 ** ((message.note - 69) / 12) * 440
                    duration = 0.1  # Duration in seconds
                    self.play_sound(frequency, duration)

                    current_note = message.note % 12
                    # Prints what note is being played to console
                    print(intervals.notes[current_note])

                    # Prints entire list of intervals that have been played for debugging
                    # print(intervals.captured_notes)

                    with self.captured_notes_lock:
                        # Adds note to list of captured notes
                        intervals.captured_notes.append(current_note)

                # If I want to have something happen when the note ends...
                # elif message.type == 'note_off':







