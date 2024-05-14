#!/usr/bin/env python3

from datetime import datetime
from ..packet import Packet
from ...protocols import Protocols


class ZwavePacket(Packet):
    """
    Represents an Zwave packet.

    Attributes:

    """

    def __init__(self, packet_info: dict):
        """
        Initializes a new instance of the ZwavePacket class.

        Args:
            packet_info (Dictionary): The dictionary that has the information of the packet.
        """
        self.protocol = Protocols.Zwave
        self.__date = packet_info['Date']
        self.__time = packet_info['Time']
        date_time_str = f"{self.__date} {self.__time}"
        self._timestamp = datetime.strptime(date_time_str, '%Y-%m-%d %I:%M:%S %p')
        self.__speed = packet_info['Speed']
        self.__channel = packet_info['Channel']
        self.__rssi = packet_info['Rssi']
        self.__home_id = packet_info['HomeId']
        self.__src_id = packet_info['Source']
        self.__dst_id = packet_info['Destination']
        self.__data = packet_info['Data']
        self.__class = packet_info['Class']
        self.__application = packet_info['Application']
        self.__payload = packet_info['Payload']
        self.__is_ack = packet_info['IsAck']
        self.__is_crc_ok = packet_info['IsCrcOk']
        self.__is_low = packet_info['IsLow']
        self.__is_substituted = packet_info['IsSubstituted']
        self.__is_unknown_header = packet_info['IsUnknownHeader']
        self.__is_wakeup_beam = packet_info['IsWakeupBeam']
        self.__hex_data = packet_info['Hex Data']
        self.payload_bytes = self.__calculate_payload_size()
        self.header_bytes = self.__calculate_header_size()

    def __contains__(self, item):
        return (item == Protocols.Zwave)

    def get_possible_pipe_id(self) -> str:
        """
        Gets the possible ID of the pipe associated with this packet.
        """
        return f"{self.__home_id}_{self.__src_id}_{self.__dst_id}"

    def __calculate_payload_size(self):
        if self.__payload is None:
            return 0
        # Remove spaces from payload to correctly count hex digit pairs
        payload_clean = self.__payload.replace(" ", "")
        return len(payload_clean) // 2

    def __calculate_header_size(self):
        hex_data_size = len(self.__hex_data) // 2
        return hex_data_size - self.payload_bytes

    def get_speed(self):
        return self.__speed

    def get_channel(self):
        return self.__channel

    def get_rssi(self):
        return self.__rssi

    def get_home_id(self):
        return self.__home_id

    def get_src_id(self):
        return self.__src_id

    def get_dst_id(self):
        return self.__dst_id

    def get_data(self):
        return self.__data

    def get_class(self):
        return self.__class

    def get_application(self):
        return self.__application

    def get_payload(self):
        return self.__payload

    def is_ack(self):
        return self.__is_ack

    def is_crc_ok(self):
        return self.__is_crc_ok

    def is_low(self):
        return self.__is_low

    def is_substituted(self):
        return self.__is_substituted

    def is_unknown_header(self):
        return self.__is_unknown_header

    def is_wakeup_beam(self):
        return self.__is_wakeup_beam

    def get_hex_data(self):
        return self.__hex_data