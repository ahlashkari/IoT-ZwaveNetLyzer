#!/usr/bin/env python3

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
        self.header_bytes = None
        self.payload_bytes = None
        self.timestamp = None
        self.__date = packet_info['Date']
        self.__time = packet_info['Time']
        self.__speed = packet_info['Speed']
        self.__channel = packet_info['Channel']
        self.__rssi = packet_info['Rssi']
        self.__home_id = packet_info['HomeId']
        self.__src = packet_info['Source']
        self.__dst = packet_info['Destination']
        self.__data = packet_info['Data']
        self.__class = packet_info['Class']
        self.__application = packet_info['Application']
        self.__payload = packet_info['Payload']
        self.__is_ack = packet_info['IsAck']
        self.__is_crc_ok = packet_info['IsCrcOk']
        self.__is_low = packet_info['IsLow']
        self.__is_substitued = packet_info['IsSubstituted']
        self.__is_unknown_header = packet_info['IsUnknownHeader']
        self.__is_wakeup_beam = packet_info['IsWakeupBeam']
        self.__hex_data = packet_info['Hex Data']

    def __contains__(self, item):
        return (item == Protocols.Zwave)

    def get_possible_pipe_id(self) -> str:
        """
        Gets the possible ID of the pipe associated with this packet.
        """
        return None
