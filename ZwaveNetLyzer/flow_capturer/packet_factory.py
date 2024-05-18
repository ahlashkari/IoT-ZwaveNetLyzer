#!/usr/bin/env python3

from typing import Type
from .packet import Packet
from .packets import ZwavePacket
from ..protocols import Protocols

class PacketFactory:
    """Factory class for creating Packet objects."""

    def __new__(cls):
        raise TypeError("This is a static class and cannot be instantiated.")

    @staticmethod
    def create(raw_packet) -> Type[Packet]:
        """Create a new Packet object based on the given Scapy packet."""
        new_packet: Type[Packet] = None
        protocol = PacketFactory.find_protocol(raw_packet)
        if protocol == Protocols.Zwave:
            new_packet = ZwavePacket(packet_info=raw_packet)

        return [new_packet]

    @staticmethod
    def find_protocol(raw_packet) -> Protocols:
        """Determine the protocol of the given Scapy packet."""
        if 'ApiType' in raw_packet:
            return Protocols.Zwave