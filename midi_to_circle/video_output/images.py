"""
Module: images.py
Author: Mae Horak for masters thesis - Synesthetic Composition 2023
Description:
Opens folder containing images of a grid labeled with their x and y coordinates. Each corner coordinate is a clear image
All in between are morphs between the different images.

The ImageSwitcherApp displays the images using kivy (https://kivy.org/) and updates with new images when triggered

"""

from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.relativelayout import RelativeLayout
from kivy.clock import Clock
from sound_inputs import intervals  # You may need to adjust this import

class ImageSwitcherApp(App):
    """
        build: Establishes naming convention of images, frame rate, x and y coordinates and creates an Image widget

        update_image: checks the "intervals" module to see if the x and y coordinates have been updated, if so
        it updates the image source

        determine_color: takes as input the current "mood" of the music, updates the new coordinates
        :return: int - x coordinate
        :return: int - y coordinate

    """

    def build(self):

        self.frames = [
            # The naming convention for the paintings - the x and y coordinate are in the image name
            f'output_paintings/img{x}_{y}.png' for x in range(30) for y in range(30)
        ]

        self.current_frame = 0
        self.frame_rate = 30  # Frames per second
        self.frame_interval = 1.0 / self.frame_rate
        self.x_coordinate = 15
        self.y_coordinate = 15
        self.random_event = True

        # Create a RelativeLayout to hold the Image widget
        self.layout = RelativeLayout()

        # Create an Image widget and add it to the layout
        self.image = Image(
            source=self.frames[self.current_frame], allow_stretch=True, keep_ratio=False
        )
        self.layout.add_widget(self.image)

        # Schedule the image update method
        Clock.schedule_interval(self.update_image, self.frame_interval)

        return self.layout

    def update_image(self, dt):

        # Determine the new image source based on x and y coordinates
        self.y_coor = intervals.y_coordinate
        self.x_coor = intervals.x_coordinate
        new_source = self.frames[self.y_coor * 30 + self.x_coor]

        # Update the image source
        self.image.source = new_source

    def determine_color(self):

        self.x_coordinate = intervals.x_coordinate
        self.y_coordinate = intervals.y_coordinate

        if intervals.rel_interval_mood == 'good':

            if self.x_coordinate > 1:
                self.x_coordinate -= 1
            if self.y_coordinate > 1:
                self.y_coordinate -= 1

        elif intervals.rel_interval_mood == 'exciting':

            if self.x_coordinate < 29:
                self.x_coordinate += 1
            if self.y_coordinate > 1:
                self.y_coordinate -= 1

        elif intervals.rel_interval_mood == 'evil':

            if self.x_coordinate > 2:
                self.x_coordinate -= 2
            if self.y_coordinate < 28:
                self.y_coordinate += 2

        elif intervals.rel_interval_mood == 'moody':

            if self.x_coordinate < 28:
                self.x_coordinate += 2
            if self.y_coordinate < 28:
                self.y_coordinate += 2

        return self.x_coordinate, self.y_coordinate

