import threading

class EventTrigger:
    def __init__(self):
        self.note_event = threading.Event()  # Create an event object

    def trigger_event(self):
        self.note_event.set()  # Set the event to notify waiting threads

    def wait_for_note_event(self):
        self.note_event.wait()  # Wait for the event to be set
        self.note_event.clear()  # Clear the event for the next wait
