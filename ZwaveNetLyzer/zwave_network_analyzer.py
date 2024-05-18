#!/usr/bin/python3

import warnings
from .flow_capturer import ZwaveFlowCapturer
from .feature_extractor import FeatureExtractor
from .writers import Writer, CSVWriter
from .config_loader import ZwaveConfigLoader


class ZwaveNetLyzer:
    """A class to analyze a given pcap file and extract features from captured packets."""

    def __init__(self, zwave_config_file_address: str):
        """
        Initialize the ZwaveNetLyzer object with the given configuration file address and capturing mode.
        """
        print("You initiated ZwaveNetLyzer!")
        self.__zwave_config_file_address = zwave_config_file_address
        warnings.filterwarnings("ignore")

    def run(self):
        """
        Analyze the pcap file and extract features from captured flows.
        """
        zwave_config = ZwaveConfigLoader(self.__zwave_config_file_address)
        print(f">> Analyzing the {zwave_config.input_file_address}...")
        flow_capturer = ZwaveFlowCapturer(zwave_config=zwave_config)
        flows = flow_capturer.capture()
        data = FeatureExtractor.execute(flows=flows,
                                        floating_point_unit=zwave_config.floating_point_unit,
                                        features_ignore_list=zwave_config.features_ignore_list,
                                        label=zwave_config.label)
        writer = Writer(CSVWriter())
        for protocol in data.keys():
            if len(data[protocol]) == 0:
                continue
            file_address = zwave_config.output_file_address
            writer.write(file_address=file_address, data=data[protocol])
        print(">> Results are ready!")