"""
Module: mood_analysis.py
Author: Mae Horak for masters thesis - Synesthetic Composition 2023
Description: Analyses the key, mode, major/minor ect. of music being played

According to the Krumhansl and Kessler 1982 theory of tonal hierarchies, the key of the piece is likely the note
played most, and then it's possible to see whether the key is major or minor based on if the major or minor 3rd is
played more than the other.
*********************************************************************************************
"""

from sound_inputs import intervals
import time


class KeyAnaylsis:

    """
    determine_key: updates the list of captured notes to see which interval has been played most often
        Then determines the likely key of song and estimates if it is major or minor
        :return: int - The likely key value.
        :return: str - Whether the key is major or minor.
        :return: str - The letter representation of the likely key.

    song_key_analysis: Continually checks what key the song is in.
        Waits a set number of seconds and then estimates the key of the music being played
        Prints key to terminal.

    determine_interval_from_key: Re-assigns intervals based on key, which is updated repeatedly.

    """

    def determine_key(self,  captured_notes):

        if len(intervals.captured_notes) > 50:
            # Get the last 30 notes from the captured_notes list
            last_30_notes = captured_notes[-50:]

            # Iterate over the last 30 notes
            for note in last_30_notes:
                note_to_tally = note
                intervals.interval_recurrence_list[note_to_tally] += 1

        else:

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
        # print('major third:', intervals.notes[key_major_third])
        key_minor_third = (12-(9-likely_key))%12
        # print('minor third:', intervals.notes[key_minor_third])

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

        while True:
        # Time it waits in seconds
            time.sleep(5)

            likely_key, major_or_minor, likely_key_letter = self.determine_key(intervals.captured_notes)

            intervals.current_key = likely_key

            print('Likely Key:', likely_key_letter)
            print('Major or Minor:', major_or_minor)

    def determine_interval_from_key(self):

        if intervals.current_key != None and len(intervals.captured_notes) > 1:
            current_key = intervals.current_key

            current_interval = intervals.captured_notes[-1]

            relative_current_interval = (current_interval - current_key)%12
            print(relative_current_interval)

            # happy
            if relative_current_interval in [0, 4, 5, 7]:
                intervals.rel_interval_mood = 'good'

            if relative_current_interval in [1, 6, 11]:
                intervals.rel_interval_mood = 'evil'

            if relative_current_interval in [2, 3, 10]:
                intervals.rel_interval_mood = 'exciting'

            if relative_current_interval in [8, 9]:
                intervals.rel_interval_mood = 'moody'
