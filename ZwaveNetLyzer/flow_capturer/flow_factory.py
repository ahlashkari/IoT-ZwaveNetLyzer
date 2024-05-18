#!/usr/bin/env python3

from typing import Type
from ..config_loader import ConfigLoader
from .packet import Packet
from .pipe import Pipe
from .pipes import EtherCatPipe, ZwaveFlow
from ..protocols import Protocols


class PipeFactory:
    """Factory class for creating Pipe objects."""

    def __new__(cls) -> None:
        raise TypeError("This is a static class and cannot be instantiated.")

    @staticmethod
    def create(packet: Packet, config: ConfigLoader) -> Type[Pipe]:
        """Create a new Pipe object based on the given Packet and ConfigLoader objects."""
        new_pipe: Type[Pipe] = None
        if packet.protocol == Protocols.EtherCAT:
            new_pipe = EtherCatPipe(packet=packet,
                                    activity_timeout=config.ethercat_activity_timeout,
                                    max_duration=config.max_ethercat_pipe_duration)

        if packet.protocol == Protocols.Zwave:
            new_pipe = ZwaveFlow(zwave_packet=packet,
                                    activity_timeout=config.ethercat_activity_timeout,
                                    max_duration=config.max_ethercat_pipe_duration)

        return new_pipe
