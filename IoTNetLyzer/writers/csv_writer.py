#!/usr/bin/env python3

import csv
from .strategy import Strategy


class CSVWriter(Strategy):
    """A class to write data to a CSV file."""

    def write(self, file_address: str, data: list):
        """Write data to a CSV file with the given file address.

        Args:
            file_address (str): The file address to write the data to.
            data (list): A list of dictionaries containing the data to be written.

        Returns:
            None.
        """

        writing_mode = 'w'
        with open(file_address, writing_mode, newline='') as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
