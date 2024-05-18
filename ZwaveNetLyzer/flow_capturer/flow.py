#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import List
from .packet import Packet
from ..protocols import Protocols


class Flow(ABC):
    """
    Abstract base class representing a flow for network packets.

    Attributes:
        protocol (Protocols): The protocol used by the flow.
        _activity_timeout (int): The time in seconds that a flow should wait
            for additional packets before being closed.
        _max_duration (int): The maximum duration in seconds that a flow is allowed to be open.
        _start_time (float): The timestamp of the first packet in the flow.
        _end_time (float): The timestamp of the last packet in the flow.
        _packets (List[Packet]): The list of packets contained in the flow.
    """
    protocol: Protocols

    def __init__(self, packet: Packet, activity_timeout: int, max_duration: int):
        """
        Initializes a new instance of the Flow class.

        Args:
            packet (Packet): The first packet in the flow.
            activity_timeout (int): The time in seconds that a flow should wait
                for additional packets before being closed.
            max_duration (int): The maximum duration in seconds that a flow is allowed to be open.
        """
        self.protocol = packet.get_protocol()
        self._activity_timeout = activity_timeout
        self._max_duration = max_duration
        self._start_time = packet.get_timestamp()
        self._end_time = packet.get_timestamp()
        self._packets: List[Packet] = []
        self._forward_packets: List[Packet] = []
        self._backward_packets: List[Packet] = []
        self.add_packet(packet=packet)

    @abstractmethod
    def __str__(self) -> str:
        """
        Gets the string representation of the flow.

        Returns:
            str: The string representation of the flow.
        """
        pass

    @abstractmethod
    def is_ended(self, new_packet_timestamp: float) -> bool:
        """
        Checks whether the flow has closed or should be closed based on the provided timestamp.

        Args:
            new_packet_timestamp (float): The timestamp of the new packet to be added to the flow.

        Returns:
            bool: True if the flow is closed or should be closed, False otherwise.
        """
        pass

    def get_protocol(self) -> Protocols:
        """
        Gets the protocol used by the flow.

        Returns:
            Protocols: The protocol used by the flow.
        """
        return self.protocol

    def get_packets(self) -> List[Packet]:
        """
        Gets the list of packets contained in the flow.

        Returns:
            List[Packet]: The list of packets contained in the flow.
        """
        return self._packets
    
    def get_forward_packets(self) -> List[Packet]:
        """
        Retrieves the list of forward packets.

        Returns:
            List[Packet]: The list of forward packets.
        """
        return self._forward_packets

    def get_backward_packets(self) -> List[Packet]:
        """
        Retrieves the list of backward packets.

        Returns:
            List[Packet]: The list of backward packets.
        """
        return self._backward_packets

    def get_timestamp(self) -> float:
        """
        Gets the timestamp of the first packet in the flow.

        Returns:
            float: The timestamp of the first packet in the flow.
        """
        return self._start_time

    def add_packet(self, packet: Packet) -> None:
        """
        Adds a packet to the flow.

        Args:
            packet (Packet): The packet to be added to the flow.
        """
        self._packets.append(packet)
        if self._is_forward_packet(packet):
            self._forward_packets.append(packet)
        else:
            self._backward_packets.append(packet)

        self._end_time = packet.get_timestamp()

    def _is_forward_packet(self, packet: Packet) -> bool:
        """
        Determines if the given packet is a forward packet.
        
        Args:
            packet (Packet): The packet to evaluate.
        
        Returns:
            bool: True if the packet is a forward packet, False otherwise.
        """
        raise NotImplementedError("This method needs to be implemented.")

    def get_duration(self) -> float:
        """
        Gets the duration of the flow in seconds.

        Returns:
            float: The duration of the flow in seconds.
        """
        return (self._end_time - self._start_time).total_seconds()

    def activity_timeout(self) -> bool:
        """
        Checks whether the flow has exceeded its activity timeout.

        Returns:
            bool: True if the flow has exceeded its activity timeout, False otherwise.
        """

        if self.get_duration(self) > self._activity_timeout:
            return True
        return False
