#!/usr/bin/python3

from .pipe_capturer import PipeCapturer, ZwaveFlowCapturer
from .feature_extractor import FeatureExtractor
from .writers import Writer, CSVWriter
from .config_loader import ConfigLoader, ZwaveConfigLoader


class IoTNetLyzer:
    """A class to analyze a given pcap file and extract features from captured packets."""

    def __init__(self, config_file_address: str, zwave_config_file_address: str):
        """
        Initialize the IoTNetLyzer object with the given configuration file address and capturing mode.
        """
        print("You initiated IoTNetLyzer!")
        self.__config_file_address = config_file_address
        self.__zwave_config_file_address = zwave_config_file_address

    def run(self):
        """
        Analyze the pcap file and extract features from captured pipes.
        """
        config = ConfigLoader(self.__config_file_address)
        zwave_config = ZwaveConfigLoader(self.__zwave_config_file_address)
        print(f">> Analyzing the {config.pcap_file_address}...")

        # if it is z-wave: 
        pipe_capturer = ZwaveFlowCapturer(zwave_config=zwave_config)
        # pipe_capturer = PipeCapturer(config=config)
        pipes = pipe_capturer.capture()
        data = FeatureExtractor.execute(pipes=pipes,
                                        floating_point_unit=config.floating_point_unit,
                                        features_ignore_list=config.features_ignore_list,
                                        label=config.label)
        writer = Writer(CSVWriter())
        for protocol in data.keys():
            file_address = config.output_file_path + "output-of-" + str(protocol) + '-pipes.csv'
            writer.write(file_address=file_address, data=data[protocol])
        print(">> Results are ready!")