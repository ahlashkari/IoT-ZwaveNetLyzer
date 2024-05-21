#!/usr/bin/env python3

from typing import Type
from ..config_loader import ConfigLoader
from .packet import Packet
from .flow import Flow
from .flows import ZwaveFlow
from ..protocols import Protocols


class FlowFactory:
    """Factory class for creating Flow objects."""

    def __new__(cls) -> None:
        raise TypeError("This is a static class and cannot be instantiated.")

    @staticmethod
    def create(packet: Packet, config: ConfigLoader) -> Type[Flow]:
        """Create a new Flow object based on the given Packet and ConfigLoader objects."""
        new_flow: Type[Flow] = None
        if packet.protocol == Protocols.Zwave:
            new_flow = ZwaveFlow(zwave_packet=packet,
                                 activity_timeout=config.zwave_activity_timeout,
                                 max_duration=config.max_zwave_flow_duration)

        return new_flow
