#!/usr/bin/env python3

import statistics
from scipy import stats
from ...pipe_capturer import Pipe
from ...pipe_capturer import Packet
from ..feature import Feature
from ...protocols import Protocols
from .. import utils

class EtherCATDuration(Feature):
    protocol = Protocols.EtherCAT
    name = "duration"
    def extract(self, pipe: Pipe) -> float:
        return pipe.get_duration()


class EtherCATMaxPacketsTimeDelta(Feature):
    protocol = Protocols.EtherCAT
    name = "max_packets_time_delta"
    def extract(self, pipe: Pipe) -> float:
        return max(utils.packets_delta_time_calculation(pipe))


class EtherCATMinPacketsTimeDelta(Feature):
    protocol = Protocols.EtherCAT
    name = "min_packets_time_delta"
    def extract(self, pipe: Pipe) -> int:
        return min(utils.packets_delta_time_calculation(pipe))


class EtherCATMeanPacketsTimeDelta(Feature):
    protocol = Protocols.EtherCAT
    name = "mean_packets_time_delta"
    def extract(self, pipe: Pipe) -> float:
        return format(statistics.mean(utils.packets_delta_time_calculation(pipe)), self.floating_point_unit)


class EtherCATModePacketsTimeDelta(Feature):
    protocol = Protocols.EtherCAT
    name = "mode_packets_time_delta"
    def extract(self, pipe: Pipe) -> float:
        return format(float(stats.mode(utils.packets_delta_time_calculation(pipe))[0]), self.floating_point_unit)


class EtherCATVariancePacketsTimeDelta(Feature):
    protocol = Protocols.EtherCAT
    name = "variance_packets_time_delta"
    def extract(self, pipe: Pipe) -> float:
        return format(statistics.pvariance(utils.packets_delta_time_calculation(pipe)), self.floating_point_unit)


class EtherCATStandardDeviationPacketsTimeDelta(Feature):
    protocol = Protocols.EtherCAT
    name = "standard_deviation_packets_time_delta"
    def extract(self, pipe: Pipe) -> float:
        return format(statistics.pstdev(utils.packets_delta_time_calculation(pipe)), self.floating_point_unit)


class EtherCATMedianPacketsTimeDelta(Feature):
    protocol = Protocols.EtherCAT
    name = "median_packets_time_delta"
    def extract(self, pipe: Pipe) -> float:
        return format(statistics.median(utils.packets_delta_time_calculation(pipe)), self.floating_point_unit)


class EtherCATSkewnessPacketsTimeDelta(Feature):
    protocol = Protocols.EtherCAT
    name = "skewness_packets_time_delta"
    def extract(self, pipe: Pipe) -> float:
        packets_time_delta = [packet.get_timestamp() for packet in pipe.get_packets()]
        return format(stats.skew(utils.packets_delta_time_calculation(pipe)), self.floating_point_unit)


class EtherCATCoefficientOfVariationPacketsTimeDelta(Feature):
    protocol = Protocols.EtherCAT
    name = "coefficient_of_variation_packets_time_delta"
    def extract(self, pipe: Pipe) -> float:
        return format(stats.variation(utils.packets_delta_time_calculation(pipe)), self.floating_point_unit)