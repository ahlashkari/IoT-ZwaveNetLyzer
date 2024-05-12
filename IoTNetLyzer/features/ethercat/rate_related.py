#!/usr/bin/env python3

import statistics
from scipy import stats
from ...pipe_capturer import Pipe
from ...pipe_capturer import Packet
from ..feature import Feature
from ...protocols import Protocols


class PacketsCount(Feature):
    protocol = Protocols.EtherCAT
    name = "packets_count"
    def extract(self, pipe: Pipe) -> int:
        return len(pipe.get_packets())


class EtherCATHeaderBytesRate(Feature):
    protocol = Protocols.EtherCAT
    name = "header_bytes_rate"
    def extract(self, pipe: Pipe) -> float:
        header_bytes = [packet.get_header_bytes() for packet in pipe.get_packets()]
        try:
            return sum(header_bytes) / pipe.get_duration()
        except ZeroDivisionError:
            return 0


class EtherCATPayloadBytesRate(Feature):
    protocol = Protocols.EtherCAT
    name = "payload_bytes_rate"
    def extract(self, pipe: Pipe) -> float:
        payload_bytes = [packet.get_payload_bytes() for packet in pipe.get_packets()]
        try:
            return sum(payload_bytes) / pipe.get_duration()
        except ZeroDivisionError:
            return 0


class EtherCATPacketLenRate(Feature):
    protocol = Protocols.EtherCAT
    name = "packet_len_rate"
    def extract(self, pipe: Pipe) -> float:
        packet_len = [packet.get_packet_len() for packet in pipe.get_packets()]
        try:
            return sum(packet_len) / pipe.get_duration()
        except ZeroDivisionError:
            return 0


class EtherCatPacketsRate(Feature):
    protocol = Protocols.EtherCAT
    name = "packets_rate"
    def extract(self, pipe: Pipe) -> float:
        try:
            return len(pipe.get_packets()) / pipe.get_duration()
        except ZeroDivisionError:
            return 0