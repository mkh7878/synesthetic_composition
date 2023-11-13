"""
Module: midi_input_font.py
Author: Mae Horak for masters thesis - Synesthetic Composition 2023
Description:
Takes the input from midi keyboard and plays the note using a midi font (sounds like piano) for the duration that the
key is held down.
Adds interval to list of intervals and prints music note to console for analysis

"""

import fluidsynth
import mido
from sound_inputs import intervals, mood_analysis
import threading
import time
from video_output.images import ImageSwitcherApp
from video_output.save_to_csv import CsvWriter

class MidiInputFont:

    """
    Sets MIDI font, initialises FluidSynth

    play_midi_font:
        Determines which musical note is being played, adds it to the list of intervals.
        Uses function from the Image Switcher to change the x and y coordinates.
        This determines which image is displayed in the kivy application
        Plays a note that sounds like a piano (from MIDI font) for duration of the key being pressed

    """

    def __init__(self):
        # Replace with the path to your GM.sf2 SoundFont file
        soundfont_file = "FluidR3 GM.sf2"
        sample_rate = 44100  # Adjust as needed to match your audio hardware

        # Initialize FluidSynth and set the SoundFont with the sample rate
        self.fs = fluidsynth.Synth()
        self.fs.start(driver="coreaudio", midi_driver="coremidi")  # Adjust the driver options as needed
        sfid = self.fs.sfload(soundfont_file)
        self.fs.program_select(0, sfid, 0, 0)

        # Initialize MIDI input
        self.midi_input = mido.open_input()

        # Lock for capturing notes
        self.captured_notes_lock = threading.Lock()

        # Create Instance of KeyAnalysis
        self.key_analysis = mood_analysis.KeyAnaylsis

        # Create an instance of ImageSwitcherApp
        self.image_switcher_app = ImageSwitcherApp()

        # Create an instance of CsvWriter
        self.csv_writer = CsvWriter()

    def play_midi_font(self):
        # Dictionary to keep track of active notes and their corresponding timestamps
        active_notes = {}  # Key: note number, Value: timestamp

        try:
            while True:
                current_time = time.time()

                for msg in self.midi_input.iter_pending():
                    # If a key is being pressed on the MIDI keyboard
                    if msg.type == "note_on":

                        msg.velocity = min(msg.velocity + 20, 127)  # Make it 20 units louder, max 127
                        self.fs.noteon(0, msg.note, msg.velocity)

                        # Determines which musical note is being played and prints it's letter value
                        current_note = msg.note % 12
                        print(intervals.notes[current_note])

                        # Determines which interval is being played relative to key
                        self.key_analysis.determine_interval_from_key(self)

                        # Prints mood of music
                        if intervals.rel_interval_mood is not None:
                            print(intervals.rel_interval_mood)

                        with self.captured_notes_lock:
                            intervals.captured_notes.append(current_note)

                        # uses function from the Image Switcher to change the x and y coordinates
                        # This determines which image is displayed in the kivy application
                        self.x_coor, self.y_coor = self.image_switcher_app.determine_color()

                        intervals.y_coordinate = self.y_coor
                        intervals.x_coordinate = self.x_coor

                        # Store the timestamp when the note was turned on
                        active_notes[msg.note] = current_time

                        # Add data to CSV file using self.csv_writer
                        self.csv_writer.addDataRow(
                            msg.note,  # Captured Note
                            intervals.current_key,  # Current Key
                            intervals.rel_interval_mood,  # Mood
                            self.x_coor,  # X Coordinate
                            self.y_coor  # Y Coordinate
                        )

                    elif msg.type == "note_off":

                        if msg.note in active_notes:
                            # Calculate the duration the note was held down
                            note_on_time = active_notes[msg.note]
                            note_duration = current_time - note_on_time

                            # Append the note duration directly to the list in intervals module
                            intervals.note_durations.append(note_duration)

                            # Play the note for the calculated duration
                            self.fs.noteoff(0, msg.note)

                            # Remove the note from the active notes dictionary
                            del active_notes[msg.note]

                time.sleep(0.01)  # Small delay to reduce CPU usage


        except KeyboardInterrupt:
            pass

        # Clean up
        self.midi_input.close()
        self.fs.delete()


