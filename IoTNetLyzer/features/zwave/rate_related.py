#!/usr/bin/env python3

import statistics
from scipy import stats
from ...pipe_capturer import Pipe
from ...pipe_capturer import Packet
from ...pipe_capturer.pipes import ZwaveFlow
from ..feature import Feature
from ...protocols import Protocols


class ZwavePacketsCount(Feature):
    protocol = Protocols.Zwave
    name = "packets_count"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        return len(zwave_flow.get_packets())


class ZwaveHeaderBytesRate(Feature):
    protocol = Protocols.Zwave
    name = "header_bytes_rate"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        header_bytes = [packet.get_header_bytes() for packet in zwave_flow.get_packets()]
        try:
            return sum(header_bytes) / zwave_flow.get_duration()
        except ZeroDivisionError:
            return 0


class ZwavePayloadBytesRate(Feature):
    protocol = Protocols.Zwave
    name = "payload_bytes_rate"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        payload_bytes = [packet.get_payload_bytes() for packet in zwave_flow.get_packets()]
        try:
            return sum(payload_bytes) / zwave_flow.get_duration()
        except ZeroDivisionError:
            return 0


class ZwavePacketLenRate(Feature):
    protocol = Protocols.Zwave
    name = "packet_len_rate"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        packet_len = [packet.get_packet_len() for packet in zwave_flow.get_packets()]
        try:
            return sum(packet_len) / zwave_flow.get_duration()
        except ZeroDivisionError:
            return 0


class ZwavePacketsRate(Feature):
    protocol = Protocols.Zwave
    name = "packets_rate"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        try:
            return len(zwave_flow.get_packets()) / zwave_flow.get_duration()
        except ZeroDivisionError:
            return 0