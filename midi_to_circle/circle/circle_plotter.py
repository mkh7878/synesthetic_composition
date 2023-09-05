"""
Module: circle_plotter
Author: Mae Horak for masters thesis - Synesthetic Composition 2023
Description: Draws Circle in Kivy window - Circle moves based on "mood" of music

This particular module written using the help of chatGPT
"""
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from sound_inputs import intervals
import threading


class CirclePlotter:

    graph_size = 100

    def __init__(self, event):
        self.circle_radius = 0.1
        self.captured_notes_lock = threading.Lock()
        self.event = event

    def determine_xy_function(self, x, y):

        current_interval = intervals.captured_notes[-1] #most recently captured note

        # Calculate changes in x and y coordinates based on the interval and current note
        x_change, y_change = 0, 0
        if current_interval in [0, 4, 5]:
            #print('y up')
            y_change = 1
        elif current_interval in [1, 6, 11]:
            y_change = -1
            #print('y down')
        elif current_interval in [2, 8, 9, 10]:
            x_change = 1
            #print('x up')
        elif current_interval in [3, 7]:
            #print('x down')
            x_change = -1

        return x + x_change, y + y_change

    def update_plot(self, frame):
        self.ax.clear()

        if len(intervals.captured_notes) == 0:
            x_coordinate = 0
            y_coordinate = 0
        else:
            x_coordinate, y_coordinate = self.determine_xy_function(self.x_positions[-1], self.y_positions[-1])

        self.x_positions.append(x_coordinate)
        self.y_positions.append(y_coordinate)

        self.ax.plot(self.x_positions, self.y_positions, 'bo')
        self.ax.set_xlim(-self.graph_size, self.graph_size)
        self.ax.set_ylim(-self.graph_size, self.graph_size)
        self.ax.set_aspect('equal')
        self.ax.add_artist(plt.Circle((x_coordinate, y_coordinate), self.circle_radius, color='r'))


    def start_plot(self):
        self.fig, self.ax = plt.subplots()  # Create the figure and axis here
        self.x_positions = []
        self.y_positions = []

        while not self.event.is_set():  # Continue until the event is set
            self.update_plot(None)
            plt.pause(0.1)  # Pause briefly before updating the plot

        plt.show()


