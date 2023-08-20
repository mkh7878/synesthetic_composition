"""
Module: mood_analysis.py
Author: Mae Horak for masters thesis - Synesthetic Composition 2023
Description: Analyses the key, mode, major/minor ect. of music being played
"""

from sound_inputs import intervals
import time

class KeyAnaylsis:

    def determine_key(self,  captured_notes):

        """
        According to the Krumhansl and Kessler 1982 theory of tonal hierarchies, the key of the piece is likely the note
        played most, and then it's possible to see whether the key is major or minor based on if the major or minor 3rd is
        played more than the other.
        *********************************************************************************************
        captured_notes is a list in intervals.py of all notes captured
        It determines which note should be updated, use note value to index into recurrence list
        and tallies up how many times each note has been played
        *********************************************************************************************
        :return: int - The likely key value.
        :return: str - Whether the key is major or minor.
        :return: str - The letter representation of the likely key.
        """
        for note in range(len(captured_notes)):
            note_to_tally = captured_notes[note]
            intervals.interval_recurrence_list[note_to_tally] += 1

        how_many_times = 0
        likely_key = 0

        for tally in range(12):
            if intervals.interval_recurrence_list[tally] > how_many_times:
                how_many_times = intervals.interval_recurrence_list[tally]
                likely_key = tally

        """
        A major scale uses the major third (+4 intervals) while the minor scale uses the minor third (+5 intervals)
        To estimate if the key is major or minor we see which (major or minor third) is used more often
        And see the major_or_minor value to true or false (default is true)
        """

        key_major_third =  (12-(8-likely_key))%12
        #print('major third:', intervals.notes[key_major_third])
        key_minor_third = (12-(9-likely_key))%12
        #print('minor third:', intervals.notes[key_minor_third])

        likely_key_letter = intervals.notes[likely_key]

        if intervals.interval_recurrence_list[key_major_third] > intervals.interval_recurrence_list[key_minor_third]:
            major_or_minor = 'major'
            intervals.major = True

        elif intervals.interval_recurrence_list[key_minor_third] > intervals.interval_recurrence_list[key_major_third]:
            major_or_minor = 'minor'
            intervals.major = False

        else:
            print('The music is in the key of', likely_key_letter, ', but we can not yet determine if it is major or minor.')
            major_or_minor = 'can not yet determine if it is major or minor'

        intervals.current_key = likely_key

        return likely_key, major_or_minor, likely_key_letter

    def song_key_analysis(self):
        """
        waits a set number of seconds and then estimates the key of the music being played
        """
        time.sleep(10)
        likely_key, major_or_minor, likely_key_letter = determine_key(intervals.captured_notes)

        print('Likely Key:', likely_key_letter)
        print('Major or Minor:', major_or_minor)


class DetermineXY:

    def determine_xy_function(self, current_interval):

        if len(intervals.captured_notes) > 0:
            current_interval = intervals.captured_notes[-1]

        # Calculate changes in x and y coordinates based on the interval and current note
        x_change, y_change = 0, 0
        if current_interval in [0, 4, 5]:
            #print('y up')
            y_change = 10
        elif current_interval in [1, 6, 11]:
            y_change = -10
            #print('y down')
        elif current_interval in [2, 8, 9, 10]:
            x_change = 10
            #print('x up')
        elif current_interval in [3, 7]:
            #print('x down')
            x_change = -10

        return x + x_change, y + y_change


