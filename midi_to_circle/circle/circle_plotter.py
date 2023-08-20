"""
Module: circle_plotter
Author: Mae Horak for masters thesis - Synesthetic Composition 2023
Description: Draws Circle in Kivy window - Circle moves based on "mood" of music

This particular module written using the help of chatGPT
"""
import matplotlib.pyplot as plt

class CirclePlotter:
    def __init__(self):
        self.x_positions = []
        self.y_positions = []
        self.circle_radius = 0.1

    def plot_circle(self, x_coordinate, y_coordinate):
        plt.ion()  # Turn on interactive mode for continuous updating
        fig, ax = plt.subplots()

        self.x_positions.append(x_coordinate)
        self.y_positions.append(y_coordinate)

        ax.clear()
        ax.plot(self.x_positions, self.y_positions, 'bo')  # Plot circle positions
        ax.set_xlim(0, 11)  # Adjust x-axis limits
        ax.set_ylim(0, 1)   # Adjust y-axis limits
        ax.set_aspect('equal')  # Set aspect ratio to make the circle circular
        ax.add_artist(plt.Circle((x_coordinate, y_coordinate), self.circle_radius, color='r'))  # Plot the circle

        plt.draw()
        plt.pause(0.1)  # Pause to allow for continuous plotting
