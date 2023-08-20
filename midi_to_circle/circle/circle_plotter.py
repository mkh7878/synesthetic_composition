"""
Module: circle_plotter
Author: Mae Horak for masters thesis - Synesthetic Composition 2023
Description: Draws Circle in Kivy window - Circle moves based on "mood" of music
"""

from kivy.app import App
from kivy.clock import mainthread
from kivy.graphics import Ellipse, Color
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget


class CircleWidget(Widget):
    def __init__(self, **kwargs):
        super(CircleWidget, self).__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (400, 400)

        self.x_coordinate = 150  # Initialize x coordinate
        self.y_coordinate = 150  # Initialize y coordinate
        self.delta_x = 0
        self.delta_y = 0

        with self.canvas:
            self.circle_color = Color(1, 1, 1)
            self.circle = Ellipse(pos=(self.x_coordinate, self.y_coordinate), size=(100, 100))

    @mainthread
    def update_circle_position(self):
        print("Before update:")
        print("x_coordinate:", self.x_coordinate)
        print("y_coordinate:", self.y_coordinate)
        print("delta_x:", self.delta_x)
        print("delta_y:", self.delta_y)

        self.x_coordinate += self.delta_x
        self.y_coordinate += self.delta_y
        self.circle.pos = (self.x_coordinate, self.y_coordinate)
        self.canvas.ask_update()

        print("After update:")
        print("x_coordinate:", self.x_coordinate)
        print("y_coordinate:", self.y_coordinate)

        print("delta_x:", self.delta_x)
        print("delta_y:", self.delta_y)

class CircleApp(App):
    def build(self):
        circle_widget = CircleWidget()
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text="Use arrow keys to control the circle's position."))
        layout.add_widget(circle_widget)
        return layout

    def update_circle_from_analysis(self, x, y):
        circle_widget = self.root.children[1]  # Get the CircleWidget instance from the layout
        circle_widget.update_circle_position(x, y)

