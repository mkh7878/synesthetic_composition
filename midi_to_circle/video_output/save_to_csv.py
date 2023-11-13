"""
Module: save_to_csv.py
Author: Mae Horak for masters thesis - Synesthetic Composition 2023
Description: Saves data about the music being played to a csv file for analysis

"""

import csv
import os


class CsvWriter:
    """
        generate_file_name: generates a new csv file

        createCsv: defines the data for the csv including the 5 columns

        addDataRow: adds a new row of data each time it is triggered (when a note is played)

    """

    def __init__(self):
        self.folder_name = 'csvs'
        self.base_name = 'syncomp'
        self.suffix = 1
        self.file_name = self.generate_file_name()

    def generate_file_name(self):
        # Generate a new CSV file name with a number suffix
        while True:
            file_name = os.path.join(self.folder_name, f'{self.base_name}_{self.suffix}.csv')
            if not os.path.exists(file_name):
                return file_name
            self.suffix += 1

    def createCsv(self):
        # Check if the folder exists, and create it if it doesn't
        if not os.path.exists(self.folder_name):
            os.makedirs(self.folder_name)

        # Define the data for the CSV file (5 columns)
        data = [
            ["Captured Note", "Current Key", "Mood", "X Coordinate", "Y Coordinate"],
        ]

        # Create and write to the CSV file
        with open(self.file_name, mode='w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)

            # Write the data to the CSV file
            csv_writer.writerows(data)

        print(f"New CSV file '{self.file_name}' created in '{self.folder_name}'.")

    def addDataRow(self, captured_note, current_key, mood, x_coordinate, y_coordinate):
        # Append a new row of data to the CSV file
        with open(self.file_name, mode='a', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([captured_note, current_key, mood, x_coordinate, y_coordinate])
