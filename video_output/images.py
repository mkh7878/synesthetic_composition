from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.relativelayout import RelativeLayout
from kivy.clock import Clock
from sound_inputs import intervals  # You may need to adjust this import
from collections import deque

class ImageSwitcherApp(App):
    def build(self):
        self.frames = [
            f'output_images/img{x}_{y}.png' for x in range(20) for y in range(20)
        ]
        self.current_frame = 0
        self.frame_rate = 30  # Frames per second
        self.frame_interval = 1.0 / self.frame_rate

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
        self.determine_color()

    def determine_color(self):
        if len(intervals.captured_notes) > 1:
            current_interval = intervals.captured_notes[-1]  # Most recently captured note

            # Determine the next frame based on intervals
            next_frame = self.current_frame  # Initialize with the current frame

            if current_interval in [0, 4, 5]:
                if next_frame % 20 != 19:
                    next_frame += 1
            elif current_interval in [1, 6, 11]:
                if next_frame % 20 != 0:
                    next_frame -= 1
            elif current_interval in [2, 8, 9, 10]:
                if next_frame // 20 != 19:
                    next_frame += 20
            elif current_interval in [3, 7]:
                if next_frame // 20 != 0:
                    next_frame -= 20

            if next_frame != self.current_frame:
                self.current_frame = next_frame
                self.image.source = self.frames[self.current_frame]

if __name__ == '__main__':
    ImageSwitcherApp().run()
