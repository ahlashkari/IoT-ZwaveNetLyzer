#!/usr/bin/env python3

import argparse
from .iot_network_analyzer import IoTNetLyzer

def args_parser() -> argparse.ArgumentParser:
    """Parse command line arguments.

    Returns:
        argparse.ArgumentParser: An ArgumentParser object.
    """
    parser = argparse.ArgumentParser(prog='IoTNetLyzer')
    parser.add_argument('-c', '--config-file', action='store', help='Json config file address.')
    parser.add_argument('-o', '--online-capturing', action='store_true',
                        help='Capturing mode. The default mode is offline capturing.')
    return parser


def main() -> None:
    """The main function of the program."""
    parsed_args = args_parser().parse_args()
    config_file_address = "./IoTNetLyzer/config.json" if parsed_args.config_file is None else parsed_args.config_file
    online_capturing = parsed_args.online_capturing
    iot_network_analyzer = IoTNetLyzer(config_file_address, online_capturing)
    iot_network_analyzer.run()


if __name__ == "__main__":
    main()
