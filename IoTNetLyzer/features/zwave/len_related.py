#!/usr/bin/env python3

import statistics
from scipy import stats
from statistics import pstdev, variance, mean
from ...pipe_capturer.pipes import ZwaveFlow
from ..feature import Feature
from ...protocols import Protocols


class ZwaveTotalHeaderBytes(Feature):
    protocol = Protocols.Zwave
    name = "total_header_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        header_bytes = [packet.get_header_bytes() for packet in zwave_flow.get_packets()]
        return sum(header_bytes)


class ZwaveMaxHeaderBytes(Feature):
    protocol = Protocols.Zwave
    name = "max_header_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        header_bytes = [packet.get_header_bytes() for packet in zwave_flow.get_packets()]
        return max(header_bytes)


class ZwaveMinHeaderBytes(Feature):
    protocol = Protocols.Zwave
    name = "min_header_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        header_bytes = [packet.get_header_bytes() for packet in zwave_flow.get_packets()]
        return min(header_bytes)


class ZwaveMeanHeaderBytes(Feature):
    protocol = Protocols.Zwave
    name = "mean_header_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        header_bytes = [packet.get_header_bytes() for packet in zwave_flow.get_packets()]
        return format(statistics.mean(header_bytes), self.floating_point_unit)


class ZwaveModeHeaderBytes(Feature):
    protocol = Protocols.Zwave
    name = "mode_header_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        header_bytes = [packet.get_header_bytes() for packet in zwave_flow.get_packets()]
        return format(float(stats.mode(header_bytes)[0]), self.floating_point_unit)


class ZwaveVarianceHeaderBytes(Feature):
    protocol = Protocols.Zwave
    name = "variance_header_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        header_bytes = [packet.get_header_bytes() for packet in zwave_flow.get_packets()]
        return format(statistics.pvariance(header_bytes), self.floating_point_unit)


class ZwaveStandardDeviationHeaderBytes(Feature):
    protocol = Protocols.Zwave
    name = "standard_deviation_header_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        header_bytes = [packet.get_header_bytes() for packet in zwave_flow.get_packets()]
        return format(statistics.pstdev(header_bytes), self.floating_point_unit)


class ZwaveMedianHeaderBytes(Feature):
    protocol = Protocols.Zwave
    name = "median_header_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        header_bytes = [packet.get_header_bytes() for packet in zwave_flow.get_packets()]
        return format(statistics.median(header_bytes), self.floating_point_unit)


class ZwaveSkewnessHeaderBytes(Feature):
    protocol = Protocols.Zwave
    name = "skewness_header_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        header_bytes = [packet.get_header_bytes() for packet in zwave_flow.get_packets()]
        return format(stats.skew(header_bytes), self.floating_point_unit)


class ZwaveCoefficientOfVariationHeaderBytes(Feature):
    protocol = Protocols.Zwave
    name = "coefficient_of_variation_header_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        header_bytes = [packet.get_header_bytes() for packet in zwave_flow.get_packets()]
        return format(stats.variation(header_bytes), self.floating_point_unit)


class ZwaveMaxPayloadBytes(Feature):
    protocol = Protocols.Zwave
    name = "max_payload_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        payload_bytes = [packet.get_payload_bytes() for packet in zwave_flow.get_packets()]
        return max(payload_bytes)


class ZwaveTotalPayloadBytes(Feature):
    protocol = Protocols.Zwave
    name = "total_payload_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        payload_bytes = [packet.get_payload_bytes() for packet in zwave_flow.get_packets()]
        return sum(payload_bytes)


class ZwaveMinPayloadBytes(Feature):
    protocol = Protocols.Zwave
    name = "min_payload_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        payload_bytes = [packet.get_payload_bytes() for packet in zwave_flow.get_packets()]
        return min(payload_bytes)


class ZwaveMeanPayloadBytes(Feature):
    protocol = Protocols.Zwave
    name = "mean_payload_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        payload_bytes = [packet.get_payload_bytes() for packet in zwave_flow.get_packets()]
        return format(statistics.mean(payload_bytes), self.floating_point_unit)


class ZwaveModePayloadBytes(Feature):
    protocol = Protocols.Zwave
    name = "mode_payload_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        payload_bytes = [packet.get_payload_bytes() for packet in zwave_flow.get_packets()]
        return format(float(stats.mode(payload_bytes)[0]), self.floating_point_unit)


class ZwaveVariancePayloadBytes(Feature):
    protocol = Protocols.Zwave
    name = "variance_payload_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        payload_bytes = [packet.get_payload_bytes() for packet in zwave_flow.get_packets()]
        return format(statistics.pvariance(payload_bytes), self.floating_point_unit)


class ZwaveStandardDeviationPayloadBytes(Feature):
    protocol = Protocols.Zwave
    name = "standard_deviation_payload_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        payload_bytes = [packet.get_payload_bytes() for packet in zwave_flow.get_packets()]
        return format(statistics.pstdev(payload_bytes), self.floating_point_unit)


class ZwaveMedianPayloadBytes(Feature):
    protocol = Protocols.Zwave
    name = "median_payload_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        payload_bytes = [packet.get_payload_bytes() for packet in zwave_flow.get_packets()]
        return format(statistics.median(payload_bytes), self.floating_point_unit)


class ZwaveSkewnessPayloadBytes(Feature):
    protocol = Protocols.Zwave
    name = "skewness_payload_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        payload_bytes = [packet.get_payload_bytes() for packet in zwave_flow.get_packets()]
        return format(stats.skew(payload_bytes), self.floating_point_unit)


class ZwaveCoefficientOfVariationPayloadBytes(Feature):
    protocol = Protocols.Zwave
    name = "coefficient_of_variation_payload_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        payload_bytes = [packet.get_payload_bytes() for packet in zwave_flow.get_packets()]
        return format(stats.variation(payload_bytes), self.floating_point_unit)


class ZwaveTotalPacketLen(Feature):
    protocol = Protocols.Zwave
    name = "total_packets_len"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        packet_len = [packet.get_packet_len() for packet in zwave_flow.get_packets()]
        return sum(packet_len)


class ZwaveMaxPacketLen(Feature):
    protocol = Protocols.Zwave
    name = "max_packets_len"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        packet_len = [packet.get_packet_len() for packet in zwave_flow.get_packets()]
        return max(packet_len)


class ZwaveMinPacketLen(Feature):
    protocol = Protocols.Zwave
    name = "min_packets_len"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        packet_len = [packet.get_packet_len() for packet in zwave_flow.get_packets()]
        return min(packet_len)


class ZwaveMeanPacketLen(Feature):
    protocol = Protocols.Zwave
    name = "mean_packets_len"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        packet_len = [packet.get_packet_len() for packet in zwave_flow.get_packets()]
        return format(statistics.mean(packet_len), self.floating_point_unit)


class ZwaveModePacketLen(Feature):
    protocol = Protocols.Zwave
    name = "mode_packets_len"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        packet_len = [packet.get_packet_len() for packet in zwave_flow.get_packets()]
        return format(float(stats.mode(packet_len)[0]), self.floating_point_unit)


class ZwaveVariancePacketLen(Feature):
    protocol = Protocols.Zwave
    name = "variance_packets_len"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        packet_len = [packet.get_packet_len() for packet in zwave_flow.get_packets()]
        return format(statistics.pvariance(packet_len), self.floating_point_unit)


class ZwaveStandardDeviationPacketLen(Feature):
    protocol = Protocols.Zwave
    name = "standard_deviation_packets_len"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        packet_len = [packet.get_packet_len() for packet in zwave_flow.get_packets()]
        return format(statistics.pstdev(packet_len), self.floating_point_unit)


class ZwaveMedianPacketLen(Feature):
    protocol = Protocols.Zwave
    name = "median_packets_len"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        packet_len = [packet.get_packet_len() for packet in zwave_flow.get_packets()]
        return format(statistics.median(packet_len), self.floating_point_unit)


class ZwaveSkewnessPacketLen(Feature):
    protocol = Protocols.Zwave
    name = "skewness_packets_len"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        packet_len = [packet.get_packet_len() for packet in zwave_flow.get_packets()]
        return format(stats.skew(packet_len), self.floating_point_unit)


class ZwaveCoefficientOfVariationPacketLen(Feature):
    protocol = Protocols.Zwave
    name = "coefficient_of_variation_packets_len"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        packet_len = [packet.get_packet_len() for packet in zwave_flow.get_packets()]
        return format(stats.variation(packet_len), self.floating_point_unit)


class TotalDataFieldSize(Feature):
    protocol = Protocols.Zwave
    name = "total_data_field_size"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        data_sizes = [len(packet.get_data()) for packet in zwave_flow.get_packets() if packet.get_data()]
        return sum(data_sizes)


class MaxDataFieldSize(Feature):
    protocol = Protocols.Zwave
    name = "max_data_field_size"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        data_sizes = [len(packet.get_data()) for packet in zwave_flow.get_packets() if packet.get_data()]
        return max(data_sizes)


class MinDataFieldSize(Feature):
    protocol = Protocols.Zwave
    name = "min_data_field_size"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        data_sizes = [len(packet.get_data()) for packet in zwave_flow.get_packets() if packet.get_data()]
        return min(data_sizes)


class MeanDataFieldSize(Feature):
    protocol = Protocols.Zwave
    name = "mean_data_field_size"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        data_sizes = [len(packet.get_data()) for packet in zwave_flow.get_packets() if packet.get_data()]
        return format(statistics.mean(data_sizes), self.floating_point_unit)


class ModeDataFieldSize(Feature):
    protocol = Protocols.Zwave
    name = "mode_data_field_size"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        data_sizes = [len(packet.get_data()) for packet in zwave_flow.get_packets() if packet.get_data()]
        return format(float(stats.mode(data_sizes)[0]), self.floating_point_unit)


class VarianceDataFieldSize(Feature):
    protocol = Protocols.Zwave
    name = "variance_data_field_size"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        data_sizes = [len(packet.get_data()) for packet in zwave_flow.get_packets() if packet.get_data()]
        return format(statistics.pvariance(data_sizes), self.floating_point_unit)


class StdDataFieldSize(Feature):
    protocol = Protocols.Zwave
    name = "std_data_field_size"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        data_sizes = [len(packet.get_data()) for packet in zwave_flow.get_packets() if packet.get_data()]
        return format(statistics.pstdev(data_sizes), self.floating_point_unit)


class SkewnessDataFieldSize(Feature):
    protocol = Protocols.Zwave
    name = "skewness_data_field_size"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        data_sizes = [len(packet.get_data()) for packet in zwave_flow.get_packets() if packet.get_data()]
        return format(stats.skew(data_sizes), self.floating_point_unit)


class CoefficientOfVariationDataFieldSize(Feature):
    protocol = Protocols.Zwave
    name = "coefficient_of_variation_data_field_size"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        data_sizes = [len(packet.get_data()) for packet in zwave_flow.get_packets() if packet.get_data()]
        return format(stats.variation(data_sizes), self.floating_point_unit)


class MedianDataFieldSize(Feature):
    protocol = Protocols.Zwave
    name = "median_data_field_size"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        data_sizes = [len(packet.get_data()) for packet in zwave_flow.get_packets() if packet.get_data()]
        return format(statistics.median(data_sizes), self.floating_point_unit)