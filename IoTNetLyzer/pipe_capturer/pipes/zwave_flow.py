#!/usr/bin/env python3
    
from typing import Any
from datetime import datetime
from ..pipe import Pipe
from ..packets import ZwavePacket
from ...protocols import Protocols


class ZwaveFlow(Pipe):
    """Represents a flow for Zwave packets."""

    def __init__(self, zwave_packet: ZwavePacket, activity_timeout: int, max_duration: int):
        """
        Initializes a new instance of the EtherCatPipe class.

        Args:
            packet (EtherCatPacket): The initial packet to add to the pipe.
            activity_timeout (int, optional): The maximum amount of time allowed without receiving any new packets. Defaults to 100000.
            max_duration (int, optional): The maximum amount of time allowed for the pipe to run. Defaults to 1000000.
        """
        super().__init__(packet=zwave_packet, activity_timeout=activity_timeout, max_duration=max_duration)
        self.protocol = Protocols.Zwave
        self.__home_id = zwave_packet['HomeId']
        self.__src_id = zwave_packet['Source']
        self.__dst_id = zwave_packet['Destination']

    def __str__(self) -> str:
        """
        Returns a string representation of the EtherCatPipe object.

        Returns:
            str: A string representation of the EtherCatPipe object.
        """
        return f"{self.__home_id}_{self.__src_id}_{self.__dst_id}_{self._start_time}"

    def is_ended(self, new_packet_timestamp: datetime) -> bool:
        """
        Determines whether the pipe has ended.

        Args:
            new_packet_timestamp (datetime): The timestamp of the latest packet received.

        Returns:
            bool: True if the pipe has ended, False otherwise.
        """
        duration = (new_packet_timestamp - self._start_time).total_seconds()
        if duration > self._max_duration:
            return True
        if duration > self._activity_timeout and len(self._packets) > 1:
            last_packet_timestamp = self._packets[-1].get_timestamp()
            if (new_packet_timestamp - last_packet_timestamp).total_seconds() > self._activity_timeout:
                return True
        return False