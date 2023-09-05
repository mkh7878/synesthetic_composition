""""
Module: intervals.py
Author: Mae Horak for masters thesis - Synesthetic Composition 2023
Description:
Stores lists and dictionaries of information relating to the music being played.

These are accessed and used from other modules.

"""

# Lists of intervals and other info need for audio analysis
notes = ['C', 'C#', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'Ab', 'A', 'Bb', 'B']

# Holds values of which note (determined by index value) has been played however many times
interval_recurrence_list = [0,0,0,0,0,0,0,0,0,0,0,0]

# Hold captured notes
captured_notes = []

# Current key of music determined using analyze function in mood.py
current_key = None

# Is the key major or minor?
major = True

# Tells how the interval should affect x and y coordinates
plotting_intervals = {
    0: 'plus_Y',
    1: 'minus_Y',
    2: 'plus_X',
    3: 'minus_X',
    4: 'plus_Y',
    5: 'plus_Y',
    6: 'minus_Y',
    7: 'minus_X',
    8: 'plus_X',
    9: 'plus_X',
    10: 'plus_X',
    11: 'minus_Y'
}





