# """
# Module: event_handler.py
# Author: Mae Horak for masters thesis - Synesthetic Composition 2023
# Description: Is the note being triggered?
# """
# from sound_inputs import intervals
# from queue import Queue
#
# class EventHandler:
#     def __init__(self):
#         self.note_event_queue = Queue()
#
#     def trigger_event(self, current_note_interval):
#         self.note_event_queue.put(current_note_interval)
#
#     def process_events(self):
#         while True:
#             if len(intervals.captured_notes) > 0:
#                 current_interval = intervals.captured_notes[-1]
#                 print(current_interval)