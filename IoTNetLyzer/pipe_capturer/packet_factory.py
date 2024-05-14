#!/usr/bin/env python3

from typing import Type
from scapy.contrib.ethercat import *
from scapy.packet import Packet as ScapyPacket
from typing import List
from .packet import Packet
from .packets import EtherCatPacket, ZwavePacket
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
        if protocol == Protocols.EtherCAT:
            datagrams = [EtherCatAPRD, EtherCatAPWR, EtherCatAPRW, EtherCatFPRD, EtherCatFPWR,
                         EtherCatFPRW, EtherCatBRD, EtherCatBWR, EtherCatBRW, EtherCatLRD,
                         EtherCatLWR, EtherCatLRW, EtherCatARMW, EtherCatFRMW]
            new_packets: List[EtherCatPacket] = []
            for datagram in datagrams:
                if datagram in raw_packet[EtherCat]:
                    new_packets.append(EtherCatPacket(scapy_packet=raw_packet,
                                                    datagram=raw_packet[EtherCat][datagram]))
            return new_packets

        if protocol == Protocols.Zwave:
            new_packet = ZwavePacket(packet_info=raw_packet)

        return [new_packet]

    @staticmethod
    def find_protocol(raw_packet) -> Protocols:
        """Determine the protocol of the given Scapy packet."""
        if 'ApiType' in raw_packet:
            return Protocols.Zwave

        if EtherCat in raw_packet:
            return Protocols.EtherCAT 