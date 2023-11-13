"""
Module: animating_csv.py
Author: Mae Horak for masters thesis - Synesthetic Composition 2023
Description: A folder of pngs of a graph have been saved
This program goes through them in order and saves them as a video animation mp4 file.

"""


import subprocess
import os

# Folder containing the frames
folder_name = 'csv1_animation_frames'

# Output video file
output_file = 'csv1_animation.mp4'

# Run ffmpeg command to create the video
ffmpeg_command = [
    'ffmpeg',
    '-framerate', '30',  # Frames per second
    '-pattern_type', 'glob',
    '-i', f'{folder_name}/*.png',
    '-c:v', 'libx264',
    '-pix_fmt', 'yuv420p',
    output_file
]

subprocess.run(ffmpeg_command).wait()

print(f"Video '{output_file}' created successfully.")