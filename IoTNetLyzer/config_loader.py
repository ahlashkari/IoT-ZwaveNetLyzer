#!/usr/bin/env python3

import json

class ConfigLoader:

    """
    This class loads the configuration from a JSON file.

    Attributes:
    -----------
    config_file_address : str
        The address of the configuration file.
    pcap_file_address : str
        The address of the pcap file.
    output_file_path : str
        The path to the output directory.
    interface_name : str
        The name of the network interface to be used.
    max_ethercat_pipe_duration : int
        The maximum duration of an EtherCAT pipe.
    max_zigbee_pipe_duration : int
        The maximum duration of a Zigbee pipe.
    ethercat_activity_timeout : int
        The timeout duration for EtherCAT activity.
    zigbee_activity_timeout : int
        The timeout duration for Zigbee activity.
    protocols : list
        The list of protocols to be used.
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
        self.pcap_file_address: str = "./test.pcap"
        self.output_file_path: str = "./"
        self.interface_name: str = "eth0"
        self.max_ethercat_pipe_duration: int = 120000
        self.max_zigbee_pipe_duration: int = 120000
        self.ethercat_activity_timeout: int = 5000
        self.zigbee_activity_timeout: int = 5000
        self.protocols: list = []
        self.floating_point_unit: str = ".64f"
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
        except Exception as error:
            print(f"Error reading {self.config_file_address}: {str(error)}. "\
                    "Default values will be used.")


class ZwaveConfigLoader:
    def __init__(self, zwave_config_file_address: str):
        super().__init__(zwave_config_file_address)
