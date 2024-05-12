#!/usr/bin/env python3

import statistics
from scipy import stats
from ...pipe_capturer import Pipe
from ...pipe_capturer.pipes import EtherCatPipe
from ...pipe_capturer import Packet
from ...pipe_capturer.packets import EtherCatPacket
from ..feature import Feature
from ...protocols import Protocols

class EtherCATTotalHeaderBytes(Feature):
    protocol = Protocols.EtherCAT
    name = "total_header_bytes"
    def extract(self, pipe: Pipe) -> int:
        header_bytes = [packet.get_header_bytes() for packet in pipe.get_packets()]
        return sum(header_bytes)


class EtherCATMaxHeaderBytes(Feature):
    protocol = Protocols.EtherCAT
    name = "max_header_bytes"
    def extract(self, pipe: Pipe) -> int:
        header_bytes = [packet.get_header_bytes() for packet in pipe.get_packets()]
        return max(header_bytes)


class EtherCATMinHeaderBytes(Feature):
    protocol = Protocols.EtherCAT
    name = "min_header_bytes"
    def extract(self, pipe: Pipe) -> int:
        header_bytes = [packet.get_header_bytes() for packet in pipe.get_packets()]
        return min(header_bytes)


class EtherCATMeanHeaderBytes(Feature):
    protocol = Protocols.EtherCAT
    name = "mean_header_bytes"
    def extract(self, pipe: Pipe) -> float:
        header_bytes = [packet.get_header_bytes() for packet in pipe.get_packets()]
        return format(statistics.mean(header_bytes), self.floating_point_unit)


class EtherCATModeHeaderBytes(Feature):
    protocol = Protocols.EtherCAT
    name = "mode_header_bytes"
    def extract(self, pipe: Pipe) -> float:
        header_bytes = [packet.get_header_bytes() for packet in pipe.get_packets()]
        return format(float(stats.mode(header_bytes)[0]), self.floating_point_unit)


class EtherCATVarianceHeaderBytes(Feature):
    protocol = Protocols.EtherCAT
    name = "variance_header_bytes"
    def extract(self, pipe: Pipe) -> float:
        header_bytes = [packet.get_header_bytes() for packet in pipe.get_packets()]
        return format(statistics.pvariance(header_bytes), self.floating_point_unit)


class EtherCATStandardDeviationHeaderBytes(Feature):
    protocol = Protocols.EtherCAT
    name = "standard_deviation_header_bytes"
    def extract(self, pipe: Pipe) -> float:
        header_bytes = [packet.get_header_bytes() for packet in pipe.get_packets()]
        return format(statistics.pstdev(header_bytes), self.floating_point_unit)


class EtherCATMedianHeaderBytes(Feature):
    protocol = Protocols.EtherCAT
    name = "median_header_bytes"
    def extract(self, pipe: Pipe) -> float:
        header_bytes = [packet.get_header_bytes() for packet in pipe.get_packets()]
        return format(statistics.median(header_bytes), self.floating_point_unit)


class EtherCATSkewnessHeaderBytes(Feature):
    protocol = Protocols.EtherCAT
    name = "skewness_header_bytes"
    def extract(self, pipe: Pipe) -> float:
        header_bytes = [packet.get_header_bytes() for packet in pipe.get_packets()]
        return format(stats.skew(header_bytes), self.floating_point_unit)


class EtherCATCoefficientOfVariationHeaderBytes(Feature):
    protocol = Protocols.EtherCAT
    name = "coefficient_of_variation_header_bytes"
    def extract(self, pipe: Pipe) -> float:
        header_bytes = [packet.get_header_bytes() for packet in pipe.get_packets()]
        return format(stats.variation(header_bytes), self.floating_point_unit)


class EtherCATMaxPayloadBytes(Feature):
    protocol = Protocols.EtherCAT
    name = "max_payload_bytes"
    def extract(self, pipe: Pipe) -> int:
        payload_bytes = [packet.get_payload_bytes() for packet in pipe.get_packets()]
        return max(payload_bytes)


class EtherCATTotalPayloadBytes(Feature):
    protocol = Protocols.EtherCAT
    name = "total_payload_bytes"
    def extract(self, pipe: Pipe) -> int:
        payload_bytes = [packet.get_payload_bytes() for packet in pipe.get_packets()]
        return sum(payload_bytes)


class EtherCATMinPayloadBytes(Feature):
    protocol = Protocols.EtherCAT
    name = "min_payload_bytes"
    def extract(self, pipe: Pipe) -> int:
        payload_bytes = [packet.get_payload_bytes() for packet in pipe.get_packets()]
        return min(payload_bytes)


class EtherCATMeanPayloadBytes(Feature):
    protocol = Protocols.EtherCAT
    name = "mean_payload_bytes"
    def extract(self, pipe: Pipe) -> float:
        payload_bytes = [packet.get_payload_bytes() for packet in pipe.get_packets()]
        return format(statistics.mean(payload_bytes), self.floating_point_unit)


class EtherCATModePayloadBytes(Feature):
    protocol = Protocols.EtherCAT
    name = "mode_payload_bytes"
    def extract(self, pipe: Pipe) -> float:
        payload_bytes = [packet.get_payload_bytes() for packet in pipe.get_packets()]
        return format(float(stats.mode(payload_bytes)[0]), self.floating_point_unit)


class EtherCATVariancePayloadBytes(Feature):
    protocol = Protocols.EtherCAT
    name = "variance_payload_bytes"
    def extract(self, pipe: Pipe) -> float:
        payload_bytes = [packet.get_payload_bytes() for packet in pipe.get_packets()]
        return format(statistics.pvariance(payload_bytes), self.floating_point_unit)


class EtherCATStandardDeviationPayloadBytes(Feature):
    protocol = Protocols.EtherCAT
    name = "standard_deviation_payload_bytes"
    def extract(self, pipe: Pipe) -> float:
        payload_bytes = [packet.get_payload_bytes() for packet in pipe.get_packets()]
        return format(statistics.pstdev(payload_bytes), self.floating_point_unit)


class EtherCATMedianPayloadBytes(Feature):
    protocol = Protocols.EtherCAT
    name = "median_payload_bytes"
    def extract(self, pipe: Pipe) -> float:
        payload_bytes = [packet.get_payload_bytes() for packet in pipe.get_packets()]
        return format(statistics.median(payload_bytes), self.floating_point_unit)


class EtherCATSkewnessPayloadBytes(Feature):
    protocol = Protocols.EtherCAT
    name = "skewness_payload_bytes"
    def extract(self, pipe: Pipe) -> float:
        payload_bytes = [packet.get_payload_bytes() for packet in pipe.get_packets()]
        return format(stats.skew(payload_bytes), self.floating_point_unit)


class EtherCATCoefficientOfVariationPayloadBytes(Feature):
    protocol = Protocols.EtherCAT
    name = "coefficient_of_variation_payload_bytes"
    def extract(self, pipe: Pipe) -> float:
        payload_bytes = [packet.get_payload_bytes() for packet in pipe.get_packets()]
        return format(stats.variation(payload_bytes), self.floating_point_unit)


class EtherCATTotalPacketLen(Feature):
    protocol = Protocols.EtherCAT
    name = "total_packets_len"
    def extract(self, pipe: Pipe) -> int:
        packet_len = [packet.get_packet_len() for packet in pipe.get_packets()]
        return sum(packet_len)


class EtherCATMaxPacketLen(Feature):
    protocol = Protocols.EtherCAT
    name = "max_packets_len"
    def extract(self, pipe: Pipe) -> int:
        packet_len = [packet.get_packet_len() for packet in pipe.get_packets()]
        return max(packet_len)


class EtherCATMinPacketLen(Feature):
    protocol = Protocols.EtherCAT
    name = "min_packets_len"
    def extract(self, pipe: Pipe) -> int:
        packet_len = [packet.get_packet_len() for packet in pipe.get_packets()]
        return min(packet_len)


class EtherCATMeanPacketLen(Feature):
    protocol = Protocols.EtherCAT
    name = "mean_packets_len"
    def extract(self, pipe: Pipe) -> float:
        packet_len = [packet.get_packet_len() for packet in pipe.get_packets()]
        return format(statistics.mean(packet_len), self.floating_point_unit)


class EtherCATModePacketLen(Feature):
    protocol = Protocols.EtherCAT
    name = "mode_packets_len"
    def extract(self, pipe: Pipe) -> float:
        packet_len = [packet.get_packet_len() for packet in pipe.get_packets()]
        return format(float(stats.mode(packet_len)[0]), self.floating_point_unit)


class EtherCATVariancePacketLen(Feature):
    protocol = Protocols.EtherCAT
    name = "variance_packets_len"
    def extract(self, pipe: Pipe) -> float:
        packet_len = [packet.get_packet_len() for packet in pipe.get_packets()]
        return format(statistics.pvariance(packet_len), self.floating_point_unit)


class EtherCATStandardDeviationPacketLen(Feature):
    protocol = Protocols.EtherCAT
    name = "standard_deviation_packets_len"
    def extract(self, pipe: Pipe) -> float:
        packet_len = [packet.get_packet_len() for packet in pipe.get_packets()]
        return format(statistics.pstdev(packet_len), self.floating_point_unit)


class EtherCATMedianPacketLen(Feature):
    protocol = Protocols.EtherCAT
    name = "median_packets_len"
    def extract(self, pipe: Pipe) -> float:
        packet_len = [packet.get_packet_len() for packet in pipe.get_packets()]
        return format(statistics.median(packet_len), self.floating_point_unit)


class EtherCATSkewnessPacketLen(Feature):
    protocol = Protocols.EtherCAT
    name = "skewness_packets_len"
    def extract(self, pipe: Pipe) -> float:
        packet_len = [packet.get_packet_len() for packet in pipe.get_packets()]
        return format(stats.skew(packet_len), self.floating_point_unit)


class EtherCATCoefficientOfVariationPacketLen(Feature):
    protocol = Protocols.EtherCAT
    name = "coefficient_of_variation_packets_len"
    def extract(self, pipe: Pipe) -> float:
        packet_len = [packet.get_packet_len() for packet in pipe.get_packets()]
        return format(stats.variation(packet_len), self.floating_point_unit)


class EtherCATTotalDataLen(Feature):
    protocol = Protocols.EtherCAT
    name = "total_data_len"
    def extract(self, pipe: Pipe) -> int:
        data_len = [packet.get_data_len() for packet in pipe.get_packets()]
        return sum(data_len)


class EtherCATMaxDataLen(Feature):
    protocol = Protocols.EtherCAT
    name = "max_data_len"
    def extract(self, pipe: Pipe) -> int:
        data_len = [packet.get_data_len() for packet in pipe.get_packets()]
        return max(data_len)


class EtherCATMinDataLen(Feature):
    protocol = Protocols.EtherCAT
    name = "min_data_len"
    def extract(self, pipe: Pipe) -> int:
        data_len = [packet.get_data_len() for packet in pipe.get_packets()]
        return min(data_len)


class EtherCATMeanDataLen(Feature):
    protocol = Protocols.EtherCAT
    name = "mean_data_len"
    def extract(self, pipe: Pipe) -> float:
        data_len = [packet.get_data_len() for packet in pipe.get_packets()]
        return format(statistics.mean(data_len), self.floating_point_unit)


class EtherCATModeDataLen(Feature):
    protocol = Protocols.EtherCAT
    name = "mode_data_len"
    def extract(self, pipe: Pipe) -> float:
        data_len = [packet.get_data_len() for packet in pipe.get_packets()]
        return format(float(stats.mode(data_len)[0]), self.floating_point_unit)


class EtherCATVarianceDataLen(Feature):
    protocol = Protocols.EtherCAT
    name = "variance_data_len"
    def extract(self, pipe: Pipe) -> float:
        data_len = [packet.get_data_len() for packet in pipe.get_packets()]
        return format(statistics.pvariance(data_len), self.floating_point_unit)


class EtherCATStandardDeviationDataLen(Feature):
    protocol = Protocols.EtherCAT
    name = "standard_deviation_data_len"
    def extract(self, pipe: Pipe) -> float:
        data_len = [packet.get_data_len() for packet in pipe.get_packets()]
        return format(statistics.pstdev(data_len), self.floating_point_unit)


class EtherCATMedianDataLen(Feature):
    protocol = Protocols.EtherCAT
    name = "median_data_len"
    def extract(self, pipe: Pipe) -> float:
        data_len = [packet.get_data_len() for packet in pipe.get_packets()]
        return format(statistics.median(data_len), self.floating_point_unit)


class EtherCATSkewnessDataLen(Feature):
    protocol = Protocols.EtherCAT
    name = "skewness_data_len"
    def extract(self, pipe: Pipe) -> float:
        data_len = [packet.get_data_len() for packet in pipe.get_packets()]
        return format(stats.skew(data_len), self.floating_point_unit)


class EtherCATCoefficientOfVariationDataLen(Feature):
    protocol = Protocols.EtherCAT
    name = "coefficient_of_variation_data_len"
    def extract(self, pipe: Pipe) -> float:
        data_len = [packet.get_data_len() for packet in pipe.get_packets()]
        return format(stats.variation(data_len), self.floating_point_unit)
