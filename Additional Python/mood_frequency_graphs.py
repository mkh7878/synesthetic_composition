"""
Module: mood_frequency_graphs.py
Author: Mae Horak for masters thesis - Synesthetic Composition 2023
Description: Used to create figure 9: Chart demonstrating the frequency with which participants
played each category of intervals using the 12 csv files I had available at the time

"""

import pandas as pd
import matplotlib.pyplot as plt
import os

# Folder containing CSV files
folder_path = 'results01/'

# Get a list of all CSV files in the folder
csv_files = [f for f in os.listdir(folder_path) if f.endswith(".csv")]

# Define colors for each mood
mood_colors = {
    'good': 'lightpink',
    'evil': 'purple',
    'moody': 'thistle',
    'exciting': 'deeppink'
}

# Create a plot with 12 rows, each representing a CSV file
fig, ax = plt.subplots(12, figsize=(6, 10))

# Loop through each CSV file and create a horizontal bar graph
for i, csv_file in enumerate(csv_files):
    df = pd.read_csv(os.path.join(folder_path, csv_file), header=None)

    # Calculate the count of each mood for the current CSV file
    mood_counts = [df.iloc[:, 2].str.count(mood).sum() for mood in mood_colors.keys()]

    # Create horizontal bar graphs for each mood
    for j, (mood, color) in enumerate(mood_colors.items()):
        ax[i].barh(j, mood_counts[j], color=color)

    # Customize the appearance of each row
    ax[i].set_xlim(0, max(mood_counts) + 1)
    ax[i].set_yticks([])  # Remove y-axis ticks
    ax[i].set_xticks([])  # Remove x-axis ticks
    ax[i].grid(axis='x')

# Adjust layout
plt.subplots_adjust(hspace=0.5)
plt.show()