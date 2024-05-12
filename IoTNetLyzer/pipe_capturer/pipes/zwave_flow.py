#!/usr/bin/env python3
    
from typing import Any
from datetime import datetime
from ..pipe import Pipe
from ..packets import ZwavePacket
from ...protocols import Protocols


class ZwaveFlow(Pipe):
    """Represents a pipe for EtherCAT packets."""

    def __init__(self, packet: ZwavePacket, activity_timeout: int, max_duration: int):
        """
        Initializes a new instance of the EtherCatPipe class.

        Args:
            packet (EtherCatPacket): The initial packet to add to the pipe.
            activity_timeout (int, optional): The maximum amount of time allowed without receiving any new packets. Defaults to 100000.
            max_duration (int, optional): The maximum amount of time allowed for the pipe to run. Defaults to 1000000.
        """
        super().__init__(packet=packet, activity_timeout=activity_timeout, max_duration=max_duration)
        self.protocol = Protocols.Zwave

    def __str__(self) -> str:
        """
        Returns a string representation of the EtherCatPipe object.

        Returns:
            str: A string representation of the EtherCatPipe object.
        """
        return None

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