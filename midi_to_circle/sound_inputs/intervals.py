""""
Module: intervals.py
Author: Mae Horak for masters thesis - Synesthetic Composition 2023
Description:
Stores lists and dictionaries of information relating to the music being played.

These are accessed and used from other modules.

"""


# Hold captured notes
captured_notes = []

# Current key of music determined using analyze function in mood.py
current_key = None

# Holds values of which note (determined by index value) has been played however many times
interval_recurrence_list = [0,0,0,0,0,0,0,0,0,0,0,0]

# Is the key major or minor?
major = True

# Lists of intervals and other info need for audio analysis
notes = ['C', 'C#', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'Ab', 'A', 'Bb', 'B']

# List of note durations
note_durations = []

# What is the mood of interval?
rel_interval_mood = None

# the x and y coordinates begin at the centre of the 30x30 grid
x_coordinate = 15
y_coordinate = 15

