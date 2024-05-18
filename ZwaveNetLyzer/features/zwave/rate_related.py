#!/usr/bin/env python3

import statistics
from scipy import stats
from ...flow_capturer import Flow
from ...flow_capturer import Packet
from ...flow_capturer.flows import ZwaveFlow
from ..feature import Feature
from ...protocols import Protocols


class PacketsCount(Feature):
    protocol = Protocols.Zwave
    name = "packets_count"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        return len(zwave_flow.get_packets())


class HeaderBytesRate(Feature):
    protocol = Protocols.Zwave
    name = "header_bytes_rate"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        header_bytes = [packet.get_header_bytes() for packet in zwave_flow.get_packets()]
        try:
            return sum(header_bytes) / zwave_flow.get_duration()
        except ZeroDivisionError:
            return 0


class PayloadBytesRate(Feature):
    protocol = Protocols.Zwave
    name = "payload_bytes_rate"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        payload_bytes = [packet.get_payload_bytes() for packet in zwave_flow.get_packets()]
        try:
            return sum(payload_bytes) / zwave_flow.get_duration()
        except ZeroDivisionError:
            return 0


class PacketLenRate(Feature):
    protocol = Protocols.Zwave
    name = "packet_len_rate"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        packet_len = [packet.get_packet_len() for packet in zwave_flow.get_packets()]
        try:
            return sum(packet_len) / zwave_flow.get_duration()
        except ZeroDivisionError:
            return 0


class PacketsRate(Feature):
    protocol = Protocols.Zwave
    name = "packets_rate"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        try:
            return len(zwave_flow.get_packets()) / zwave_flow.get_duration()
        except ZeroDivisionError:
            return 0


class FwdPacketsCount(Feature):
    protocol = Protocols.Zwave
    name = "fwd_packets_count"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        return len(zwave_flow.get_forward_packets())


class FwdHeaderBytesRate(Feature):
    protocol = Protocols.Zwave
    name = "fwd_header_bytes_rate"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        header_bytes = [packet.get_header_bytes() for packet in zwave_flow.get_forward_packets()]
        try:
            return sum(header_bytes) / zwave_flow.get_duration()
        except ZeroDivisionError:
            return 0


class FwdPayloadBytesRate(Feature):
    protocol = Protocols.Zwave
    name = "fwd_payload_bytes_rate"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        payload_bytes = [packet.get_payload_bytes() for packet in zwave_flow.get_forward_packets()]
        try:
            return sum(payload_bytes) / zwave_flow.get_duration()
        except ZeroDivisionError:
            return 0


class FwdPacketLenRate(Feature):
    protocol = Protocols.Zwave
    name = "fwd_packet_len_rate"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        packet_len = [packet.get_packet_len() for packet in zwave_flow.get_forward_packets()]
        try:
            return sum(packet_len) / zwave_flow.get_duration()
        except ZeroDivisionError:
            return 0


class FwdPacketsRate(Feature):
    protocol = Protocols.Zwave
    name = "fwd_packets_rate"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        try:
            return len(zwave_flow.get_forward_packets()) / zwave_flow.get_duration()
        except ZeroDivisionError:
            return 0


class BwdPacketsCount(Feature):
    protocol = Protocols.Zwave
    name = "bwd_packets_count"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        return len(zwave_flow.get_backward_packets())


class BwdHeaderBytesRate(Feature):
    protocol = Protocols.Zwave
    name = "bwd_header_bytes_rate"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        header_bytes = [packet.get_header_bytes() for packet in zwave_flow.get_backward_packets()]
        try:
            return sum(header_bytes) / zwave_flow.get_duration()
        except ZeroDivisionError:
            return 0


class BwdPayloadBytesRate(Feature):
    protocol = Protocols.Zwave
    name = "bwd_payload_bytes_rate"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        payload_bytes = [packet.get_payload_bytes() for packet in zwave_flow.get_backward_packets()]
        try:
            return sum(payload_bytes) / zwave_flow.get_duration()
        except ZeroDivisionError:
            return 0


class BwdPacketLenRate(Feature):
    protocol = Protocols.Zwave
    name = "bwd_packet_len_rate"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        packet_len = [packet.get_packet_len() for packet in zwave_flow.get_backward_packets()]
        try:
            return sum(packet_len) / zwave_flow.get_duration()
        except ZeroDivisionError:
            return 0


class BwdPacketsRate(Feature):
    protocol = Protocols.Zwave
    name = "bwd_packets_rate"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        try:
            return len(zwave_flow.get_backward_packets()) / zwave_flow.get_duration()
        except ZeroDivisionError:
            return 0