#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import List
from .packet import Packet
from ..protocols import Protocols


class Pipe(ABC):
    """
    Abstract base class representing a pipe for network packets.

    Attributes:
        protocol (Protocols): The protocol used by the pipe.
        _activity_timeout (int): The time in seconds that a pipe should wait
            for additional packets before being closed.
        _max_duration (int): The maximum duration in seconds that a pipe is allowed to be open.
        _start_time (float): The timestamp of the first packet in the pipe.
        _end_time (float): The timestamp of the last packet in the pipe.
        _packets (List[Packet]): The list of packets contained in the pipe.
    """
    protocol: Protocols

    def __init__(self, packet: Packet, activity_timeout: int, max_duration: int):
        """
        Initializes a new instance of the Pipe class.

        Args:
            packet (Packet): The first packet in the pipe.
            activity_timeout (int): The time in seconds that a pipe should wait
                for additional packets before being closed.
            max_duration (int): The maximum duration in seconds that a pipe is allowed to be open.
        """
        self.protocol = packet.get_protocol()
        self._activity_timeout = activity_timeout
        self._max_duration = max_duration
        self._start_time = packet.get_timestamp()
        self._end_time = packet.get_timestamp()
        self._packets: List[Packet] = []
        self.add_packet(packet=packet)

    @abstractmethod
    def __str__(self) -> str:
        """
        Gets the string representation of the pipe.

        Returns:
            str: The string representation of the pipe.
        """
        pass

    @abstractmethod
    def is_ended(self, new_packet_timestamp: float) -> bool:
        """
        Checks whether the pipe has closed or should be closed based on the provided timestamp.

        Args:
            new_packet_timestamp (float): The timestamp of the new packet to be added to the pipe.

        Returns:
            bool: True if the pipe is closed or should be closed, False otherwise.
        """
        pass

    def get_protocol(self) -> Protocols:
        """
        Gets the protocol used by the pipe.

        Returns:
            Protocols: The protocol used by the pipe.
        """
        return self.protocol

    def get_packets(self) -> List[Packet]:
        """
        Gets the list of packets contained in the pipe.

        Returns:
            List[Packet]: The list of packets contained in the pipe.
        """
        return self._packets

    def get_timestamp(self) -> float:
        """
        Gets the timestamp of the first packet in the pipe.

        Returns:
            float: The timestamp of the first packet in the pipe.
        """
        return self._start_time

    def add_packet(self, packet: Packet) -> None:
        """
        Adds a packet to the pipe.

        Args:
            packet (Packet): The packet to be added to the pipe.
        """
        self._packets.append(packet)
        self._end_time = packet.get_timestamp()

    def get_duration(self) -> float:
        """
        Gets the duration of the pipe in seconds.

        Returns:
            float: The duration of the pipe in seconds.
        """
        return (self._end_time - self._start_time).total_seconds()

    def activity_timeout(self) -> bool:
        """
        Checks whether the pipe has exceeded its activity timeout.

        Returns:
            bool: True if the pipe has exceeded its activity timeout, False otherwise.
        """

        if self.get_duration(self) > self._activity_timeout:
            return True
        return False
