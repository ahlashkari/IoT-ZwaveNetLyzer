#!/usr/bin/env python3

import statistics
from scipy import stats
from statistics import pstdev, variance, mean
from ...pipe_capturer.pipes import ZwaveFlow
from ..feature import Feature
from ...protocols import Protocols


class TotalHeaderBytes(Feature):
    protocol = Protocols.Zwave
    name = "total_header_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        header_bytes = [packet.get_header_bytes() for packet in zwave_flow.get_packets()]
        return sum(header_bytes)


class MaxHeaderBytes(Feature):
    protocol = Protocols.Zwave
    name = "max_header_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        header_bytes = [packet.get_header_bytes() for packet in zwave_flow.get_packets()]
        return max(header_bytes)


class MinHeaderBytes(Feature):
    protocol = Protocols.Zwave
    name = "min_header_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        header_bytes = [packet.get_header_bytes() for packet in zwave_flow.get_packets()]
        return min(header_bytes)


class MeanHeaderBytes(Feature):
    protocol = Protocols.Zwave
    name = "mean_header_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        header_bytes = [packet.get_header_bytes() for packet in zwave_flow.get_packets()]
        return format(statistics.mean(header_bytes), self.floating_point_unit)


class ModeHeaderBytes(Feature):
    protocol = Protocols.Zwave
    name = "mode_header_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        header_bytes = [packet.get_header_bytes() for packet in zwave_flow.get_packets()]
        return format(float(stats.mode(header_bytes)[0]), self.floating_point_unit)


class VarianceHeaderBytes(Feature):
    protocol = Protocols.Zwave
    name = "variance_header_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        header_bytes = [packet.get_header_bytes() for packet in zwave_flow.get_packets()]
        return format(statistics.pvariance(header_bytes), self.floating_point_unit)


class StandardDeviationHeaderBytes(Feature):
    protocol = Protocols.Zwave
    name = "standard_deviation_header_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        header_bytes = [packet.get_header_bytes() for packet in zwave_flow.get_packets()]
        return format(statistics.pstdev(header_bytes), self.floating_point_unit)


class MedianHeaderBytes(Feature):
    protocol = Protocols.Zwave
    name = "median_header_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        header_bytes = [packet.get_header_bytes() for packet in zwave_flow.get_packets()]
        return format(statistics.median(header_bytes), self.floating_point_unit)


class SkewnessHeaderBytes(Feature):
    protocol = Protocols.Zwave
    name = "skewness_header_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        header_bytes = [packet.get_header_bytes() for packet in zwave_flow.get_packets()]
        return format(stats.skew(header_bytes), self.floating_point_unit)


class CoefficientOfVariationHeaderBytes(Feature):
    protocol = Protocols.Zwave
    name = "coefficient_of_variation_header_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        header_bytes = [packet.get_header_bytes() for packet in zwave_flow.get_packets()]
        return format(stats.variation(header_bytes), self.floating_point_unit)


class MaxPayloadBytes(Feature):
    protocol = Protocols.Zwave
    name = "max_payload_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        payload_bytes = [packet.get_payload_bytes() for packet in zwave_flow.get_packets()]
        return max(payload_bytes)


class TotalPayloadBytes(Feature):
    protocol = Protocols.Zwave
    name = "total_payload_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        payload_bytes = [packet.get_payload_bytes() for packet in zwave_flow.get_packets()]
        return sum(payload_bytes)


class MinPayloadBytes(Feature):
    protocol = Protocols.Zwave
    name = "min_payload_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        payload_bytes = [packet.get_payload_bytes() for packet in zwave_flow.get_packets()]
        return min(payload_bytes)


class MeanPayloadBytes(Feature):
    protocol = Protocols.Zwave
    name = "mean_payload_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        payload_bytes = [packet.get_payload_bytes() for packet in zwave_flow.get_packets()]
        return format(statistics.mean(payload_bytes), self.floating_point_unit)


class ModePayloadBytes(Feature):
    protocol = Protocols.Zwave
    name = "mode_payload_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        payload_bytes = [packet.get_payload_bytes() for packet in zwave_flow.get_packets()]
        return format(float(stats.mode(payload_bytes)[0]), self.floating_point_unit)


class VariancePayloadBytes(Feature):
    protocol = Protocols.Zwave
    name = "variance_payload_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        payload_bytes = [packet.get_payload_bytes() for packet in zwave_flow.get_packets()]
        return format(statistics.pvariance(payload_bytes), self.floating_point_unit)


class StandardDeviationPayloadBytes(Feature):
    protocol = Protocols.Zwave
    name = "standard_deviation_payload_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        payload_bytes = [packet.get_payload_bytes() for packet in zwave_flow.get_packets()]
        return format(statistics.pstdev(payload_bytes), self.floating_point_unit)


class MedianPayloadBytes(Feature):
    protocol = Protocols.Zwave
    name = "median_payload_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        payload_bytes = [packet.get_payload_bytes() for packet in zwave_flow.get_packets()]
        return format(statistics.median(payload_bytes), self.floating_point_unit)


class SkewnessPayloadBytes(Feature):
    protocol = Protocols.Zwave
    name = "skewness_payload_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        payload_bytes = [packet.get_payload_bytes() for packet in zwave_flow.get_packets()]
        return format(stats.skew(payload_bytes), self.floating_point_unit)


class CoefficientOfVariationPayloadBytes(Feature):
    protocol = Protocols.Zwave
    name = "coefficient_of_variation_payload_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        payload_bytes = [packet.get_payload_bytes() for packet in zwave_flow.get_packets()]
        return format(stats.variation(payload_bytes), self.floating_point_unit)


class TotalPacketLen(Feature):
    protocol = Protocols.Zwave
    name = "total_packets_len"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        packet_len = [packet.get_packet_len() for packet in zwave_flow.get_packets()]
        return sum(packet_len)


class MaxPacketLen(Feature):
    protocol = Protocols.Zwave
    name = "max_packets_len"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        packet_len = [packet.get_packet_len() for packet in zwave_flow.get_packets()]
        return max(packet_len)


class MinPacketLen(Feature):
    protocol = Protocols.Zwave
    name = "min_packets_len"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        packet_len = [packet.get_packet_len() for packet in zwave_flow.get_packets()]
        return min(packet_len)


class MeanPacketLen(Feature):
    protocol = Protocols.Zwave
    name = "mean_packets_len"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        packet_len = [packet.get_packet_len() for packet in zwave_flow.get_packets()]
        return format(statistics.mean(packet_len), self.floating_point_unit)


class ModePacketLen(Feature):
    protocol = Protocols.Zwave
    name = "mode_packets_len"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        packet_len = [packet.get_packet_len() for packet in zwave_flow.get_packets()]
        return format(float(stats.mode(packet_len)[0]), self.floating_point_unit)


class VariancePacketLen(Feature):
    protocol = Protocols.Zwave
    name = "variance_packets_len"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        packet_len = [packet.get_packet_len() for packet in zwave_flow.get_packets()]
        return format(statistics.pvariance(packet_len), self.floating_point_unit)


class StandardDeviationPacketLen(Feature):
    protocol = Protocols.Zwave
    name = "standard_deviation_packets_len"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        packet_len = [packet.get_packet_len() for packet in zwave_flow.get_packets()]
        return format(statistics.pstdev(packet_len), self.floating_point_unit)


class MedianPacketLen(Feature):
    protocol = Protocols.Zwave
    name = "median_packets_len"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        packet_len = [packet.get_packet_len() for packet in zwave_flow.get_packets()]
        return format(statistics.median(packet_len), self.floating_point_unit)


class SkewnessPacketLen(Feature):
    protocol = Protocols.Zwave
    name = "skewness_packets_len"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        packet_len = [packet.get_packet_len() for packet in zwave_flow.get_packets()]
        return format(stats.skew(packet_len), self.floating_point_unit)


class CoefficientOfVariationPacketLen(Feature):
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


class FwdTotalHeaderBytes(Feature):
    protocol = Protocols.Zwave
    name = "fwd_total_header_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        header_bytes = [packet.get_header_bytes() for packet in zwave_flow.get_forward_packets()]
        return sum(header_bytes)


class FwdMaxHeaderBytes(Feature):
    protocol = Protocols.Zwave
    name = "fwd_max_header_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        header_bytes = [packet.get_header_bytes() for packet in zwave_flow.get_forward_packets()]
        return max(header_bytes)


class FwdMinHeaderBytes(Feature):
    protocol = Protocols.Zwave
    name = "fwd_min_header_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        header_bytes = [packet.get_header_bytes() for packet in zwave_flow.get_forward_packets()]
        return min(header_bytes)


class FwdMeanHeaderBytes(Feature):
    protocol = Protocols.Zwave
    name = "fwd_mean_header_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        header_bytes = [packet.get_header_bytes() for packet in zwave_flow.get_forward_packets()]
        return format(statistics.mean(header_bytes), self.floating_point_unit)


class FwdModeHeaderBytes(Feature):
    protocol = Protocols.Zwave
    name = "fwd_mode_header_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        header_bytes = [packet.get_header_bytes() for packet in zwave_flow.get_forward_packets()]
        return format(float(stats.mode(header_bytes)[0]), self.floating_point_unit)


class FwdVarianceHeaderBytes(Feature):
    protocol = Protocols.Zwave
    name = "fwd_variance_header_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        header_bytes = [packet.get_header_bytes() for packet in zwave_flow.get_forward_packets()]
        return format(statistics.pvariance(header_bytes), self.floating_point_unit)


class FwdStandardDeviationHeaderBytes(Feature):
    protocol = Protocols.Zwave
    name = "fwd_standard_deviation_header_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        header_bytes = [packet.get_header_bytes() for packet in zwave_flow.get_forward_packets()]
        return format(statistics.pstdev(header_bytes), self.floating_point_unit)


class FwdMedianHeaderBytes(Feature):
    protocol = Protocols.Zwave
    name = "fwd_median_header_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        header_bytes = [packet.get_header_bytes() for packet in zwave_flow.get_forward_packets()]
        return format(statistics.median(header_bytes), self.floating_point_unit)


class FwdSkewnessHeaderBytes(Feature):
    protocol = Protocols.Zwave
    name = "fwd_skewness_header_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        header_bytes = [packet.get_header_bytes() for packet in zwave_flow.get_forward_packets()]
        return format(stats.skew(header_bytes), self.floating_point_unit)


class FwdCoefficientOfVariationHeaderBytes(Feature):
    protocol = Protocols.Zwave
    name = "fwd_coefficient_of_variation_header_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        header_bytes = [packet.get_header_bytes() for packet in zwave_flow.get_forward_packets()]
        return format(stats.variation(header_bytes), self.floating_point_unit)


class FwdMaxPayloadBytes(Feature):
    protocol = Protocols.Zwave
    name = "fwd_max_payload_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        payload_bytes = [packet.get_payload_bytes() for packet in zwave_flow.get_forward_packets()]
        return max(payload_bytes)


class FwdTotalPayloadBytes(Feature):
    protocol = Protocols.Zwave
    name = "fwd_total_payload_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        payload_bytes = [packet.get_payload_bytes() for packet in zwave_flow.get_forward_packets()]
        return sum(payload_bytes)


class FwdMinPayloadBytes(Feature):
    protocol = Protocols.Zwave
    name = "fwd_min_payload_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        payload_bytes = [packet.get_payload_bytes() for packet in zwave_flow.get_forward_packets()]
        return min(payload_bytes)


class FwdMeanPayloadBytes(Feature):
    protocol = Protocols.Zwave
    name = "fwd_mean_payload_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        payload_bytes = [packet.get_payload_bytes() for packet in zwave_flow.get_forward_packets()]
        return format(statistics.mean(payload_bytes), self.floating_point_unit)


class FwdModePayloadBytes(Feature):
    protocol = Protocols.Zwave
    name = "fwd_mode_payload_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        payload_bytes = [packet.get_payload_bytes() for packet in zwave_flow.get_forward_packets()]
        return format(float(stats.mode(payload_bytes)[0]), self.floating_point_unit)


class FwdVariancePayloadBytes(Feature):
    protocol = Protocols.Zwave
    name = "fwd_variance_payload_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        payload_bytes = [packet.get_payload_bytes() for packet in zwave_flow.get_forward_packets()]
        return format(statistics.pvariance(payload_bytes), self.floating_point_unit)


class FwdStandardDeviationPayloadBytes(Feature):
    protocol = Protocols.Zwave
    name = "fwd_standard_deviation_payload_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        payload_bytes = [packet.get_payload_bytes() for packet in zwave_flow.get_forward_packets()]
        return format(statistics.pstdev(payload_bytes), self.floating_point_unit)


class FwdMedianPayloadBytes(Feature):
    protocol = Protocols.Zwave
    name = "fwd_median_payload_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        payload_bytes = [packet.get_payload_bytes() for packet in zwave_flow.get_forward_packets()]
        return format(statistics.median(payload_bytes), self.floating_point_unit)


class FwdSkewnessPayloadBytes(Feature):
    protocol = Protocols.Zwave
    name = "fwd_skewness_payload_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        payload_bytes = [packet.get_payload_bytes() for packet in zwave_flow.get_forward_packets()]
        return format(stats.skew(payload_bytes), self.floating_point_unit)


class FwdCoefficientOfVariationPayloadBytes(Feature):
    protocol = Protocols.Zwave
    name = "fwd_coefficient_of_variation_payload_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        payload_bytes = [packet.get_payload_bytes() for packet in zwave_flow.get_forward_packets()]
        return format(stats.variation(payload_bytes), self.floating_point_unit)


class FwdTotalPacketLen(Feature):
    protocol = Protocols.Zwave
    name = "fwd_total_packets_len"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        packet_len = [packet.get_packet_len() for packet in zwave_flow.get_forward_packets()]
        return sum(packet_len)


class FwdMaxPacketLen(Feature):
    protocol = Protocols.Zwave
    name = "fwd_max_packets_len"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        packet_len = [packet.get_packet_len() for packet in zwave_flow.get_forward_packets()]
        return max(packet_len)


class FwdMinPacketLen(Feature):
    protocol = Protocols.Zwave
    name = "fwd_min_packets_len"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        packet_len = [packet.get_packet_len() for packet in zwave_flow.get_forward_packets()]
        return min(packet_len)


class FwdMeanPacketLen(Feature):
    protocol = Protocols.Zwave
    name = "fwd_mean_packets_len"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        packet_len = [packet.get_packet_len() for packet in zwave_flow.get_forward_packets()]
        return format(statistics.mean(packet_len), self.floating_point_unit)


class FwdModePacketLen(Feature):
    protocol = Protocols.Zwave
    name = "fwd_mode_packets_len"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        packet_len = [packet.get_packet_len() for packet in zwave_flow.get_forward_packets()]
        return format(float(stats.mode(packet_len)[0]), self.floating_point_unit)


class FwdVariancePacketLen(Feature):
    protocol = Protocols.Zwave
    name = "fwd_variance_packets_len"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        packet_len = [packet.get_packet_len() for packet in zwave_flow.get_forward_packets()]
        return format(statistics.pvariance(packet_len), self.floating_point_unit)


class FwdStandardDeviationPacketLen(Feature):
    protocol = Protocols.Zwave
    name = "fwd_standard_deviation_packets_len"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        packet_len = [packet.get_packet_len() for packet in zwave_flow.get_forward_packets()]
        return format(statistics.pstdev(packet_len), self.floating_point_unit)


class FwdMedianPacketLen(Feature):
    protocol = Protocols.Zwave
    name = "fwd_median_packets_len"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        packet_len = [packet.get_packet_len() for packet in zwave_flow.get_forward_packets()]
        return format(statistics.median(packet_len), self.floating_point_unit)


class FwdSkewnessPacketLen(Feature):
    protocol = Protocols.Zwave
    name = "fwd_skewness_packets_len"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        packet_len = [packet.get_packet_len() for packet in zwave_flow.get_forward_packets()]
        return format(stats.skew(packet_len), self.floating_point_unit)


class FwdCoefficientOfVariationPacketLen(Feature):
    protocol = Protocols.Zwave
    name = "fwd_coefficient_of_variation_packets_len"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        packet_len = [packet.get_packet_len() for packet in zwave_flow.get_forward_packets()]
        return format(stats.variation(packet_len), self.floating_point_unit)


class FwdTotalDataFieldSize(Feature):
    protocol = Protocols.Zwave
    name = "fwd_total_data_field_size"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        data_sizes = [len(packet.get_data()) for packet in zwave_flow.get_forward_packets() if packet.get_data()]
        return sum(data_sizes)


class FwdMaxDataFieldSize(Feature):
    protocol = Protocols.Zwave
    name = "fwd_max_data_field_size"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        data_sizes = [len(packet.get_data()) for packet in zwave_flow.get_forward_packets() if packet.get_data()]
        return max(data_sizes)


class FwdMinDataFieldSize(Feature):
    protocol = Protocols.Zwave
    name = "fwd_min_data_field_size"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        data_sizes = [len(packet.get_data()) for packet in zwave_flow.get_forward_packets() if packet.get_data()]
        return min(data_sizes)


class FwdMeanDataFieldSize(Feature):
    protocol = Protocols.Zwave
    name = "fwd_mean_data_field_size"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        data_sizes = [len(packet.get_data()) for packet in zwave_flow.get_forward_packets() if packet.get_data()]
        return format(statistics.mean(data_sizes), self.floating_point_unit)


class FwdModeDataFieldSize(Feature):
    protocol = Protocols.Zwave
    name = "fwd_mode_data_field_size"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        data_sizes = [len(packet.get_data()) for packet in zwave_flow.get_forward_packets() if packet.get_data()]
        return format(float(stats.mode(data_sizes)[0]), self.floating_point_unit)


class FwdVarianceDataFieldSize(Feature):
    protocol = Protocols.Zwave
    name = "fwd_variance_data_field_size"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        data_sizes = [len(packet.get_data()) for packet in zwave_flow.get_forward_packets() if packet.get_data()]
        return format(statistics.pvariance(data_sizes), self.floating_point_unit)


class FwdStdDataFieldSize(Feature):
    protocol = Protocols.Zwave
    name = "fwd_std_data_field_size"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        data_sizes = [len(packet.get_data()) for packet in zwave_flow.get_forward_packets() if packet.get_data()]
        return format(statistics.pstdev(data_sizes), self.floating_point_unit)


class FwdSkewnessDataFieldSize(Feature):
    protocol = Protocols.Zwave
    name = "fwd_skewness_data_field_size"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        data_sizes = [len(packet.get_data()) for packet in zwave_flow.get_forward_packets() if packet.get_data()]
        return format(stats.skew(data_sizes), self.floating_point_unit)


class FwdCoefficientOfVariationDataFieldSize(Feature):
    protocol = Protocols.Zwave
    name = "fwd_coefficient_of_variation_data_field_size"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        data_sizes = [len(packet.get_data()) for packet in zwave_flow.get_forward_packets() if packet.get_data()]
        return format(stats.variation(data_sizes), self.floating_point_unit)


class FwdMedianDataFieldSize(Feature):
    protocol = Protocols.Zwave
    name = "fwd_median_data_field_size"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        data_sizes = [len(packet.get_data()) for packet in zwave_flow.get_forward_packets() if packet.get_data()]
        return format(statistics.median(data_sizes), self.floating_point_unit)


class BwdTotalHeaderBytes(Feature):
    protocol = Protocols.Zwave
    name = "bwd_total_header_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        header_bytes = [packet.get_header_bytes() for packet in zwave_flow.get_backward_packets()]
        return sum(header_bytes)


class BwdMaxHeaderBytes(Feature):
    protocol = Protocols.Zwave
    name = "bwd_max_header_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        header_bytes = [packet.get_header_bytes() for packet in zwave_flow.get_backward_packets()]
        return max(header_bytes)


class BwdMinHeaderBytes(Feature):
    protocol = Protocols.Zwave
    name = "bwd_min_header_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        header_bytes = [packet.get_header_bytes() for packet in zwave_flow.get_backward_packets()]
        return min(header_bytes)


class BwdMeanHeaderBytes(Feature):
    protocol = Protocols.Zwave
    name = "bwd_mean_header_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        header_bytes = [packet.get_header_bytes() for packet in zwave_flow.get_backward_packets()]
        return format(statistics.mean(header_bytes), self.floating_point_unit)


class BwdModeHeaderBytes(Feature):
    protocol = Protocols.Zwave
    name = "bwd_mode_header_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        header_bytes = [packet.get_header_bytes() for packet in zwave_flow.get_backward_packets()]
        return format(float(stats.mode(header_bytes)[0]), self.floating_point_unit)


class BwdVarianceHeaderBytes(Feature):
    protocol = Protocols.Zwave
    name = "bwd_variance_header_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        header_bytes = [packet.get_header_bytes() for packet in zwave_flow.get_backward_packets()]
        return format(statistics.pvariance(header_bytes), self.floating_point_unit)


class BwdStandardDeviationHeaderBytes(Feature):
    protocol = Protocols.Zwave
    name = "bwd_standard_deviation_header_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        header_bytes = [packet.get_header_bytes() for packet in zwave_flow.get_backward_packets()]
        return format(statistics.pstdev(header_bytes), self.floating_point_unit)


class BwdMedianHeaderBytes(Feature):
    protocol = Protocols.Zwave
    name = "bwd_median_header_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        header_bytes = [packet.get_header_bytes() for packet in zwave_flow.get_backward_packets()]
        return format(statistics.median(header_bytes), self.floating_point_unit)


class BwdSkewnessHeaderBytes(Feature):
    protocol = Protocols.Zwave
    name = "bwd_skewness_header_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        header_bytes = [packet.get_header_bytes() for packet in zwave_flow.get_backward_packets()]
        return format(stats.skew(header_bytes), self.floating_point_unit)


class BwdCoefficientOfVariationHeaderBytes(Feature):
    protocol = Protocols.Zwave
    name = "bwd_coefficient_of_variation_header_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        header_bytes = [packet.get_header_bytes() for packet in zwave_flow.get_backward_packets()]
        return format(stats.variation(header_bytes), self.floating_point_unit)


class BwdMaxPayloadBytes(Feature):
    protocol = Protocols.Zwave
    name = "bwd_max_payload_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        payload_bytes = [packet.get_payload_bytes() for packet in zwave_flow.get_backward_packets()]
        return max(payload_bytes)


class BwdTotalPayloadBytes(Feature):
    protocol = Protocols.Zwave
    name = "bwd_total_payload_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        payload_bytes = [packet.get_payload_bytes() for packet in zwave_flow.get_backward_packets()]
        return sum(payload_bytes)


class BwdMinPayloadBytes(Feature):
    protocol = Protocols.Zwave
    name = "bwd_min_payload_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        payload_bytes = [packet.get_payload_bytes() for packet in zwave_flow.get_backward_packets()]
        return min(payload_bytes)


class BwdMeanPayloadBytes(Feature):
    protocol = Protocols.Zwave
    name = "bwd_mean_payload_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        payload_bytes = [packet.get_payload_bytes() for packet in zwave_flow.get_backward_packets()]
        return format(statistics.mean(payload_bytes), self.floating_point_unit)


class BwdModePayloadBytes(Feature):
    protocol = Protocols.Zwave
    name = "bwd_mode_payload_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        payload_bytes = [packet.get_payload_bytes() for packet in zwave_flow.get_backward_packets()]
        return format(float(stats.mode(payload_bytes)[0]), self.floating_point_unit)


class BwdVariancePayloadBytes(Feature):
    protocol = Protocols.Zwave
    name = "bwd_variance_payload_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        payload_bytes = [packet.get_payload_bytes() for packet in zwave_flow.get_backward_packets()]
        return format(statistics.pvariance(payload_bytes), self.floating_point_unit)


class BwdStandardDeviationPayloadBytes(Feature):
    protocol = Protocols.Zwave
    name = "bwd_standard_deviation_payload_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        payload_bytes = [packet.get_payload_bytes() for packet in zwave_flow.get_backward_packets()]
        return format(statistics.pstdev(payload_bytes), self.floating_point_unit)


class BwdMedianPayloadBytes(Feature):
    protocol = Protocols.Zwave
    name = "bwd_median_payload_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        payload_bytes = [packet.get_payload_bytes() for packet in zwave_flow.get_backward_packets()]
        return format(statistics.median(payload_bytes), self.floating_point_unit)


class BwdSkewnessPayloadBytes(Feature):
    protocol = Protocols.Zwave
    name = "bwd_skewness_payload_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        payload_bytes = [packet.get_payload_bytes() for packet in zwave_flow.get_backward_packets()]
        return format(stats.skew(payload_bytes), self.floating_point_unit)


class BwdCoefficientOfVariationPayloadBytes(Feature):
    protocol = Protocols.Zwave
    name = "bwd_coefficient_of_variation_payload_bytes"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        payload_bytes = [packet.get_payload_bytes() for packet in zwave_flow.get_backward_packets()]
        return format(stats.variation(payload_bytes), self.floating_point_unit)


class BwdTotalPacketLen(Feature):
    protocol = Protocols.Zwave
    name = "bwd_total_packets_len"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        packet_len = [packet.get_packet_len() for packet in zwave_flow.get_backward_packets()]
        return sum(packet_len)


class BwdMaxPacketLen(Feature):
    protocol = Protocols.Zwave
    name = "bwd_max_packets_len"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        packet_len = [packet.get_packet_len() for packet in zwave_flow.get_backward_packets()]
        return max(packet_len)


class BwdMinPacketLen(Feature):
    protocol = Protocols.Zwave
    name = "bwd_min_packets_len"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        packet_len = [packet.get_packet_len() for packet in zwave_flow.get_backward_packets()]
        return min(packet_len)


class BwdMeanPacketLen(Feature):
    protocol = Protocols.Zwave
    name = "bwd_mean_packets_len"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        packet_len = [packet.get_packet_len() for packet in zwave_flow.get_backward_packets()]
        return format(statistics.mean(packet_len), self.floating_point_unit)


class BwdModePacketLen(Feature):
    protocol = Protocols.Zwave
    name = "bwd_mode_packets_len"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        packet_len = [packet.get_packet_len() for packet in zwave_flow.get_backward_packets()]
        return format(float(stats.mode(packet_len)[0]), self.floating_point_unit)


class BwdVariancePacketLen(Feature):
    protocol = Protocols.Zwave
    name = "bwd_variance_packets_len"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        packet_len = [packet.get_packet_len() for packet in zwave_flow.get_backward_packets()]
        return format(statistics.pvariance(packet_len), self.floating_point_unit)


class BwdStandardDeviationPacketLen(Feature):
    protocol = Protocols.Zwave
    name = "bwd_standard_deviation_packets_len"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        packet_len = [packet.get_packet_len() for packet in zwave_flow.get_backward_packets()]
        return format(statistics.pstdev(packet_len), self.floating_point_unit)


class BwdMedianPacketLen(Feature):
    protocol = Protocols.Zwave
    name = "bwd_median_packets_len"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        packet_len = [packet.get_packet_len() for packet in zwave_flow.get_backward_packets()]
        return format(statistics.median(packet_len), self.floating_point_unit)


class BwdSkewnessPacketLen(Feature):
    protocol = Protocols.Zwave
    name = "bwd_skewness_packets_len"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        packet_len = [packet.get_packet_len() for packet in zwave_flow.get_backward_packets()]
        return format(stats.skew(packet_len), self.floating_point_unit)


class BwdCoefficientOfVariationPacketLen(Feature):
    protocol = Protocols.Zwave
    name = "bwd_coefficient_of_variation_packets_len"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        packet_len = [packet.get_packet_len() for packet in zwave_flow.get_backward_packets()]
        return format(stats.variation(packet_len), self.floating_point_unit)


class BwdTotalDataFieldSize(Feature):
    protocol = Protocols.Zwave
    name = "bwd_total_data_field_size"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        data_sizes = [len(packet.get_data()) for packet in zwave_flow.get_backward_packets() if packet.get_data()]
        return sum(data_sizes)


class BwdMaxDataFieldSize(Feature):
    protocol = Protocols.Zwave
    name = "bwd_max_data_field_size"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        data_sizes = [len(packet.get_data()) for packet in zwave_flow.get_backward_packets() if packet.get_data()]
        return max(data_sizes)


class BwdMinDataFieldSize(Feature):
    protocol = Protocols.Zwave
    name = "bwd_min_data_field_size"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        data_sizes = [len(packet.get_data()) for packet in zwave_flow.get_backward_packets() if packet.get_data()]
        return min(data_sizes)


class BwdMeanDataFieldSize(Feature):
    protocol = Protocols.Zwave
    name = "bwd_mean_data_field_size"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        data_sizes = [len(packet.get_data()) for packet in zwave_flow.get_backward_packets() if packet.get_data()]
        return format(statistics.mean(data_sizes), self.floating_point_unit)


class BwdModeDataFieldSize(Feature):
    protocol = Protocols.Zwave
    name = "bwd_mode_data_field_size"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        data_sizes = [len(packet.get_data()) for packet in zwave_flow.get_backward_packets() if packet.get_data()]
        return format(float(stats.mode(data_sizes)[0]), self.floating_point_unit)


class BwdVarianceDataFieldSize(Feature):
    protocol = Protocols.Zwave
    name = "bwd_variance_data_field_size"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        data_sizes = [len(packet.get_data()) for packet in zwave_flow.get_backward_packets() if packet.get_data()]
        return format(statistics.pvariance(data_sizes), self.floating_point_unit)


class BwdStdDataFieldSize(Feature):
    protocol = Protocols.Zwave
    name = "bwd_std_data_field_size"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        data_sizes = [len(packet.get_data()) for packet in zwave_flow.get_backward_packets() if packet.get_data()]
        return format(statistics.pstdev(data_sizes), self.floating_point_unit)


class BwdSkewnessDataFieldSize(Feature):
    protocol = Protocols.Zwave
    name = "bwd_skewness_data_field_size"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        data_sizes = [len(packet.get_data()) for packet in zwave_flow.get_backward_packets() if packet.get_data()]
        return format(stats.skew(data_sizes), self.floating_point_unit)


class BwdCoefficientOfVariationDataFieldSize(Feature):
    protocol = Protocols.Zwave
    name = "bwd_coefficient_of_variation_data_field_size"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        data_sizes = [len(packet.get_data()) for packet in zwave_flow.get_backward_packets() if packet.get_data()]
        return format(stats.variation(data_sizes), self.floating_point_unit)


class BwdMedianDataFieldSize(Feature):
    protocol = Protocols.Zwave
    name = "bwd_median_data_field_size"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        data_sizes = [len(packet.get_data()) for packet in zwave_flow.get_backward_packets() if packet.get_data()]
        return format(statistics.median(data_sizes), self.floating_point_unit)