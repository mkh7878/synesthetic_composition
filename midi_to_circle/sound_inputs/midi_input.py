"""
Module: midi_input.py
Author: Mae Horak for masters thesis - Synesthetic Composition 2023
Description:
Takes the input from midi keyboard and plays the note using a basic sine wave or a midi font
"""

import mido
import numpy as np
import queue
import sounddevice as sd
from sound_inputs import intervals, mood_analysis
from utils.event_handler import EventHandler
import threading


class MidiInput:

    """
    This class handles the midi input, sets backend, plays sine wave
    Creates a queue for note intervals to continually update which note is being played
    """

    event_handler = EventHandler()

    def __init__(self, event):

        self.note_queue = queue.Queue()  # Create a queue for note intervals
        self.previous_note = None
        self.input_name = None
        self.port = None
        self.captured_notes_lock = threading.Lock()
        self.event = event  # Assign the event object passed from main

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
        """
        If the note is being pressed on midi keyboard, play sine wave
        :queue: int - the interval of the current note being played

        """

        while True:
            for message in self.port.iter_pending():

                if message.type == 'note_on':

                    self.event = threading.Event()
                    self.event_handler.note_pressed = True

                    if self.event_handler.note_pressed == True:
                        # print('new note pressed!')

                        frequency = 2 ** ((message.note - 69) / 12) * 440
                        duration = 0.1  # Duration in seconds
                        self.play_sound(frequency, duration)

                        current_note = message.note % 12
                        print(intervals.notes[current_note])
                        print(intervals.captured_notes)

                    with self.captured_notes_lock:
                        intervals.captured_notes.append(current_note)

                    if self.note_queue.qsize() == 0:
                        self.note_queue.put(current_note)

                    else:
                        self.note_queue.put(current_note)

                    if len(intervals.captured_notes) > 1:
                        with self.captured_notes_lock:
                            if current_note != intervals.captured_notes[-2]:
                                self.event_handler.new_note = True
                                self.event.set()


                elif message.type == 'note_off':

                    self.event_handler.note_pressed = False

                    self.event_handler.note_off = True

                    self.event_handler.new_note = False






