"""
Module: animating_paintings.py
Author: Mae Horak for masters thesis - Synesthetic Composition 2023
Description: Loads in a folder of png files of paintings. Uses imageio to create an mp4 video
at a determined frame rate.

"""


import os
import imageio

# Folder containing the frames
folder_name = 'painting_animations1'

# Output video file
output_file = 'animation_paintings10fpsagain.mp4'

# Create a list of image file paths
image_files = [os.path.join(folder_name, f) for f in os.listdir(folder_name) if f.endswith('.png')]

# Extract frame numbers from filenames
frame_numbers = [int(os.path.basename(f).split('_')[2].rstrip('.png')) for f in image_files]

# Sort the image files based on frame numbers
sorted_files = [x for _, x in sorted(zip(frame_numbers, image_files))]

# Create the video using imageio
with imageio.get_writer(output_file, fps=10) as writer:
    for image_file in sorted_files:
        image = imageio.imread(image_file)
        writer.append_data(image)

print(f"Video '{output_file}' created successfully.")
