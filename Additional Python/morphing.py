"""
Module: morphing.py
Author: Mae Horak for masters thesis - Synesthetic Composition 2023
Description: Takes 4 images and creates a grid of morphs between them, naming with x and y coordinates.

"""
import cv2
import os

# Load your four corner images
image1 = cv2.imread('surreal/good.png')
image2 = cv2.imread('surreal/evil.png')
image3 = cv2.imread('surreal/exciting.png')
image4 = cv2.imread('surreal/moody.png')

# Ensure all corner images have the same dimensions
if image1.shape != image2.shape != image3.shape != image4.shape:
    raise ValueError("All corner images must have the same dimensions.")

# Define the size of the grid
grid_size = (20, 20)

# Create an output directory (if it doesn't exist)
output_dir = 'output_paintings'
os.makedirs(output_dir, exist_ok=True)

# Perform interpolation and save the interpolated frames
for y in range(grid_size[1]):
    for x in range(grid_size[0]):
        # Calculate interpolation factors
        alpha_x = x / (grid_size[0] - 1)  # Interpolation factor for columns
        alpha_y = y / (grid_size[1] - 1)  # Interpolation factor for rows

        # Interpolate between the corner images
        top_row = cv2.addWeighted(image1, 1 - alpha_x, image2, alpha_x, 0)
        bottom_row = cv2.addWeighted(image3, 1 - alpha_x, image4, alpha_x, 0)
        interpolated_frame = cv2.addWeighted(top_row, 1 - alpha_y, bottom_row, alpha_y, 0)

        # Save the interpolated frame with its X and Y coordinates
        filename = os.path.join(output_dir, f'img{x}_{y}.png')
        cv2.imwrite(filename, interpolated_frame)
