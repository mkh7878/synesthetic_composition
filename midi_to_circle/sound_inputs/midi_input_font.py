"""
Module: midi_input_font.py
Author: Mae Horak for masters thesis - Synesthetic Composition 2023
Description:
Takes the input from midi keyboard and plays the note using a midi font (sounds like piano)
Adds interval to list of intervals and prints music note to console for analysis

"""

import fluidsynth
import mido
import threading
import time
from sound_inputs import intervals  # Assuming you have a module named 'intervals'
from sound_inputs import mood_analysis
from video_output.images import ImageSwitcherApp

class MidiInputFont:

    def __init__(self):
        # Replace with the path to your GM.sf2 SoundFont file
        soundfont_file = "FluidR3 GM.sf2"
        sample_rate = 44100  # Adjust as needed to match your audio hardware

        # Initialize FluidSynth and set the SoundFont with the sample rate
        self.fs = fluidsynth.Synth()
        self.fs.start(driver="coreaudio", midi_driver="coremidi")  # Adjust the driver options as needed
        sfid = self.fs.sfload(soundfont_file)
        self.fs.program_select(0, sfid, 0, 0)
        self.fs.setting('synth.sample-rate', sample_rate)  # Set the sample rate

        # Initialize MIDI input
        self.midi_input = mido.open_input()

        # Lock for capturing notes
        self.captured_notes_lock = threading.Lock()

        # Create Instance of KeyAnalysis
        self.key_analysis = mood_analysis.KeyAnaylsis

        # Create an instance of ImageSwitcherApp and store it as an attribute
        self.image_switcher_app = ImageSwitcherApp()
    #
    # def play_midi_font(self):
    #     # Main loop for receiving and playing MIDI notes
    #     try:
    #         while True:
    #             for msg in self.midi_input.iter_pending():
    #                 if msg.type == "note_on":
    #                     self.fs.noteon(0, msg.note, msg.velocity)
    #
    #                     # # Trigger the callback in ImageSwitcherApp to update the image
    #                     # if self.image_switcher_app is not None:
    #                     #     self.image_switcher_app.update_image_callback()
    #
    #                     current_note = msg.note % 12
    #                     # Prints what note is being played to console
    #                     print(intervals.notes[current_note])
    #
    #                     self.key_analysis.determine_interval_from_key(self)
    #
    #                     if intervals.rel_interval_mood != None:
    #                         print(intervals.rel_interval_mood)
    #
    #                     with self.captured_notes_lock:
    #                         # Adds note to list of captured notes
    #                         intervals.captured_notes.append(current_note)
    #
    #                 elif msg.type == "note_off":
    #                     self.fs.noteoff(0, msg.note)
    #             time.sleep(0.01)  # Small delay to reduce CPU usage
    #
    #     except KeyboardInterrupt:
    #         pass

    import threading
    import threading
    import time

    def play_midi_font(self):
        # Dictionary to keep track of active notes and their corresponding timestamps
        active_notes = {}  # Key: note number, Value: timestamp

        try:
            while True:
                current_time = time.time()

                for msg in self.midi_input.iter_pending():
                    if msg.type == "note_on":
                        self.fs.noteon(0, msg.note, msg.velocity)

                        current_note = msg.note % 12
                        print(intervals.notes[current_note])

                        self.key_analysis.determine_interval_from_key(self)

                        if intervals.rel_interval_mood is not None:
                            print(intervals.rel_interval_mood)

                        with self.captured_notes_lock:
                            intervals.captured_notes.append(current_note)

                        # Store the timestamp when the note was turned on
                        active_notes[msg.note] = current_time

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


