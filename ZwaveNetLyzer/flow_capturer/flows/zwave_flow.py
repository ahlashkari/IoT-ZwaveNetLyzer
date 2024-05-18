#!/usr/bin/env python3
    
from typing import Any
from datetime import datetime
from ..flow import Flow
from ..packets import ZwavePacket
from ...protocols import Protocols


class ZwaveFlow(Flow):
    """Represents a flow for Zwave packets."""

    def __init__(self, zwave_packet: ZwavePacket, activity_timeout: int, max_duration: int):
        """
        Initializes a new instance of the ZwaveFlow class.

        Args:
            packet (ZwavePacket): The initial packet to add to the flow.
            activity_timeout (int, optional): The maximum amount of time allowed without receiving any new packets. Defaults to 100000.
            max_duration (int, optional): The maximum amount of time allowed for the flow to run. Defaults to 1000000.
        """
        self.protocol = Protocols.Zwave
        self.__home_id = zwave_packet.get_home_id()
        self.__src_id = zwave_packet.get_src_id()
        self.__dst_id = zwave_packet.get_dst_id()
        super().__init__(packet=zwave_packet, activity_timeout=activity_timeout, max_duration=max_duration)

    def __str__(self) -> str:
        """
        Returns a string representation of the ZwaveFlow object.

        Returns:
            str: A string representation of the ZwaveFlow object.
        """
        return f"{self.__home_id}_{self.__src_id}_{self.__dst_id}_{self._start_time}"

    def is_ended(self, new_packet_timestamp: datetime) -> bool:
        """
        Determines whether the flow has ended.

        Args:
            new_packet_timestamp (datetime): The timestamp of the latest packet received.

        Returns:
            bool: True if the flow has ended, False otherwise.
        """
        duration = (new_packet_timestamp - self._start_time).total_seconds()
        if duration > self._max_duration:
            return True
        if duration > self._activity_timeout and len(self._packets) > 1:
            last_packet_timestamp = self._packets[-1].get_timestamp()
            if (new_packet_timestamp - last_packet_timestamp).total_seconds() > self._activity_timeout:
                return True
        return False
    
    def get_home_id(self):
        return self.__home_id

    def get_src_id(self):
        return self.__src_id

    def get_dst_id(self):
        return self.__dst_id
    
    def get_forward_packets(self):
        return self._forward_packets

    def _is_forward_packet(self, packet: ZwavePacket):
        if packet.get_src_id() == self.__src_id:
            return True
        return False