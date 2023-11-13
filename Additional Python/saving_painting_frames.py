"""
Module: saving_painting_frames.py
Author: Mae Horak for masters thesis - Synesthetic Composition 2023
Description: Using the folder of paintings labeled with x and y coordinates,
this program creates a new folder then loads a csv file, and uses the x and y coordinates
listed in each row of the file to locate the appropriately labeled painting and save a
copy into the new folder.

"""


import pandas as pd
import os
import shutil

# Load your CSV file
csv_file_path = 'results01/1.csv'
df = pd.read_csv(csv_file_path)

# Folder containing the original paintings
paintings_folder = 'output_paintings'

# Create a new folder to save the painting animations
output_folder = 'painting_animations1'
os.makedirs(output_folder, exist_ok=True)

# Loop through each row in the DataFrame
for index, row in df.iterrows():
    x_coordinate = row[3] - 1  # Assuming 4th column is x coordinates
    y_coordinate = row[4] - 1  # Assuming 5th column is y coordinates

    # Generate the filename based on the coordinates
    image_filename = f'img{x_coordinate}_{y_coordinate}.png'

    # Full path to the original painting
    original_painting_path = os.path.join(paintings_folder, image_filename)

    # Check if the painting exists
    if os.path.exists(original_painting_path):
        # Full path to save the copy in the new folder
        output_painting_path = os.path.join(output_folder, f'output_painting_{index}.png')

        # Copy the painting to the new folder
        shutil.copyfile(original_painting_path, output_painting_path)
        print(f"Image for row {index} saved successfully.")
    else:
        print(f"Image for row {index} not found.")

print("All images saved successfully.")
