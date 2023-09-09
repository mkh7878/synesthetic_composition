from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.relativelayout import RelativeLayout
from kivy.core.window import Window
from kivy.clock import Clock  # Import Clock for scheduled updates
from sound_inputs import intervals

class ImageSwitcherApp(App):
    def build(self):
        self.frames = ["frames/image1.png", "frames/image2.png", "frames/image3.png", "frames/image4.png"]
        self.current_frame = 0

        # Create a RelativeLayout to hold the Image widget
        self.layout = RelativeLayout()

        # Create an Image widget and add it to the layout
        self.image = Image(source=self.frames[self.current_frame], allow_stretch=True, keep_ratio=False)
        self.layout.add_widget(self.image)

        # Schedule the image update method
        Clock.schedule_interval(self.update_image, 1.0 / 30.0)  # Update every 1/30th of a second

        return self.layout

    def update_image(self, dt):
        self.determine_color()

    def determine_color(self):
        if len(intervals.captured_notes) > 1:
            current_interval = intervals.captured_notes[-1]  # Most recently captured note

            # Based on "mood" of intervals.
            if current_interval in [0, 4, 5]:
                self.current_frame = 0

            elif current_interval in [1, 6, 11]:
                self.current_frame = 1

            elif current_interval in [2, 8, 9, 10]:
                self.current_frame = 2

            elif current_interval in [3, 7]:
                self.current_frame = 3

            # Update the displayed image
            self.image.source = self.frames[self.current_frame]

if __name__ == '__main__':
    ImageSwitcherApp().run()
