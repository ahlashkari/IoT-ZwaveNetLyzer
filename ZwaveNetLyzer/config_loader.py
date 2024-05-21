#!/usr/bin/env python3

import json

class ConfigLoader:

    """
    This class loads the configuration from a JSON file.

    Attributes:
    -----------
    config_file_address : str
        The address of the configuration file.
    input_file_address : str
        The address of the pcap file.
    output_file_path : str
        The address of the output CSV file.
    floating_point_unit : str
        The unit for floating point values.
    features_ignore_list : list
        The list of features to be ignored.
    label : str
        The label for the output file.
    read_packets_count_value_log_info : int
        The number of packets to be read for logging.
    max_rows_number : int
        The maximum number of rows for the output file.
    """

    def __init__(self, config_file_address: str):
        self.config_file_address = config_file_address
        self.input_file_address: str = None
        self.output_file_address: str = "./"
        self.floating_point_unit: str = ".4f"
        self.features_ignore_list: list = []
        self.label = "Unknown"
        self.read_packets_count_value_log_info = 10000
        self.max_rows_number = 800000
        self.read_config_file()

    def read_config_file(self) -> None:
        """
        Reads the configuration file and sets the class attributes.
        """
        try:
            with open(self.config_file_address) as config_file:
                for key, value in json.loads(config_file.read()).items():
                    setattr(self, key, value)
                if self.input_file_address is None:
                    raise Exception("Please specify the 'input_file_address' in the config file.")
        except Exception as error:
            print(f"Error reading {self.config_file_address}: {str(error)}. "\
                    "Default values will be used.")


class ZwaveConfigLoader(ConfigLoader):
    def __init__(self, zwave_config_file_address: str):
        """
            This class loads the Zwave configuration from a JSON file.

            Attributes:
            -----------
            max_zwave_flow_duration : int
                The maximum duration of a Zwave flow.
            zwave_activity_timeout : int
                The timeout duration for Zwave activity.

        """
        self.max_zwave_flow_duration: int = 1200
        self.zwave_activity_timeout: int = 600
        super().__init__(zwave_config_file_address)
