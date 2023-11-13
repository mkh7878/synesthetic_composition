"""
Module: graphing_from_csv.py
Author: Mae Horak for masters thesis - Synesthetic Composition 2023
Description: For each row of a csv file a 30x30 graph is created using the x and y coordinates in the
corresponding columns and a png image of the graph is saved.

"""

import pandas as pd
import matplotlib.pyplot as plt
import os

# Load your CSV file
file_path = 'results01/1.csv'
df = pd.read_csv(file_path)

# Create a folder to save frames
folder_name = 'csv1_animation_frames'
os.makedirs(folder_name, exist_ok=True)

# Loop through each row in the DataFrame
for index, row in df.iterrows():
    # Set up the plot
    fig, ax = plt.subplots()
    ax.set_xlim(0, 30)
    ax.set_ylim(0, 30)

    # Plot the pink dot at the specified x and y coordinates
    ax.plot(row[3], row[4], 'ro')  # Assuming 4th column is x coordinates, 5th column is y coordinates

    # Save the frame as a PNG file
    file_name = os.path.join(folder_name, f'frame_{index:04d}.png')
    plt.savefig(file_name, format='png', dpi=300)
    plt.close()

print("Frames saved successfully.")
