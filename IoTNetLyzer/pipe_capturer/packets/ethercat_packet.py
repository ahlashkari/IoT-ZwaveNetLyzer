#!/usr/bin/env python3

from scapy.packet import Packet as ScapyPacket
from datetime import datetime
from ..packet import Packet
from ...protocols import Protocols


class EtherCatPacket(Packet):
    """
    Represents an EtherCAT packet.

    Attributes:
        __src_mac (str): The source MAC address of the packet.
        __dst_mac (str): The destination MAC address of the packet.
        __logical_address (str): The logical address of the packet.
        __address_offset (str): The address offset of the packet.
    """

    def __init__(self, scapy_packet: ScapyPacket, datagram):
        """
        Initializes a new instance of the EtherCatPacket class.

        Args:
            scapy_packet (ScapyPacket): The Scapy packet instance to initialize from.
        """
        self.__src_mac = scapy_packet['Ethernet'].src
        self.__dst_mac = scapy_packet['Ethernet'].dst
        self.protocol = Protocols.EtherCAT
        self.__logical_address = datagram.adp
        self.__address_offset = datagram.ado
        self.__index = datagram.idx
        self.__command = datagram._cmd
        self.__circulating = True if datagram.c == 1 else False
        self.__next = datagram.next
        self.__interupt_request = datagram.irq
        self.__data = datagram.data
        self.__working_counter = datagram.wkc
        self.header_bytes = len(datagram)
        self.payload_bytes = len(datagram.payload)
        self.timestamp = datetime.fromtimestamp(float(scapy_packet.time))
        self.__data_len = datagram.len

    def get_possible_pipe_id(self) -> str:
        """
        Gets the possible ID of the pipe associated with this packet.
        """
        return f"{self.__src_mac}_{self.__logical_address}_{self.__address_offset}"

    def get_src_mac(self) -> str:
        """
        Gets the source MAC address of the packet.
        """
        return self.__src_mac

    def get_dst_mac(self) -> str:
        """
        Gets the destination MAC address of the packet.
        """
        return self.__dst_mac

    def get_logical_address(self) -> str:
        """
        Gets the logical address of the packet.
        """
        return self.__logical_address

    def get_address_offset(self) -> str:
        """
        Gets the address offset of the packet.
        """
        return self.__address_offset
    
    def get_index(self):
        return self.__index

    def get_command(self):
        return self.__command

    def get_circulating(self):
        return self.__circulating
    
    def get_next(self):
        return self.__next

    def get_interupt_request(self):
        return self.__interupt_request

    def get_data(self):
        return self.__data

    def get_working_counter(self):
        return self.__working_counter
    
    def get_data_len(self):
        return self.__data_len