"""
Module: color_window.py
Author: Mae Horak for masters thesis - Synesthetic Composition 2023
Description:
Opens up a kivy window which changes colors based on the intervals being played.

"""
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle
from kivy.clock import Clock  # Import Clock for scheduled updates
from sound_inputs import intervals

class ColorChangeBox(BoxLayout):

    def __init__(self, **kwargs):
        super(ColorChangeBox, self).__init__(**kwargs)
        self.orientation = 'vertical'

        with self.canvas.before:
            self.color = Color(0, 0, 0, 1)  # Initialize with black color
            self.rect = Rectangle(pos=self.pos, size=self.size)

        # Schedule the color update method
        Clock.schedule_interval(self.update_rectangle, 1.0 / 30.0)  # Update every 1/30th of a second

    def change_color(self):
        color_tuple = self.determine_color()
        if color_tuple is not None:
            r, g, b = color_tuple
            self.color.r = r
            self.color.g = g
            self.color.b = b

    def determine_color(self):

        if len(intervals.captured_notes) > 1:

            current_interval = intervals.captured_notes[-1]  # Most recently captured note

            if current_interval in [0, 4, 5]:
                return 1, 0, 0

            elif current_interval in [1, 6, 11]:
                return 0, 1, 0

            elif current_interval in [2, 8, 9, 10]:
                return 0, 0, 1

            elif current_interval in [3, 7]:
                return 1, 1, 1

    def update_rectangle(self, dt):
        self.change_color()

class SynestheticApp(App):
    def build(self):
        layout = ColorChangeBox()
        return layout

if __name__ == "__main__":
    SynestheticApp().run()
