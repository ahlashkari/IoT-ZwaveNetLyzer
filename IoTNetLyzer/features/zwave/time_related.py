#!/usr/bin/env python3

import statistics
from scipy import stats
from ...pipe_capturer import Packet
from ...pipe_capturer.pipes import ZwaveFlow
from ..feature import Feature
from ...protocols import Protocols
from .. import utils

class ZwaveDuration(Feature):
    protocol = Protocols.Zwave
    name = "duration"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        return zwave_flow.get_duration()


class ZwaveMaxPacketsTimeDelta(Feature):
    protocol = Protocols.Zwave
    name = "max_packets_time_delta"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        return max(utils.packets_delta_time_calculation(zwave_flow))


class ZwaveMinPacketsTimeDelta(Feature):
    protocol = Protocols.Zwave
    name = "min_packets_time_delta"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        return min(utils.packets_delta_time_calculation(zwave_flow))


class ZwaveMeanPacketsTimeDelta(Feature):
    protocol = Protocols.Zwave
    name = "mean_packets_time_delta"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        return format(statistics.mean(utils.packets_delta_time_calculation(zwave_flow)), self.floating_point_unit)


class ZwaveModePacketsTimeDelta(Feature):
    protocol = Protocols.Zwave
    name = "mode_packets_time_delta"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        return format(float(stats.mode(utils.packets_delta_time_calculation(zwave_flow))[0]), self.floating_point_unit)


class ZwaveVariancePacketsTimeDelta(Feature):
    protocol = Protocols.Zwave
    name = "variance_packets_time_delta"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        return format(statistics.pvariance(utils.packets_delta_time_calculation(zwave_flow)), self.floating_point_unit)


class ZwaveStandardDeviationPacketsTimeDelta(Feature):
    protocol = Protocols.Zwave
    name = "standard_deviation_packets_time_delta"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        return format(statistics.pstdev(utils.packets_delta_time_calculation(zwave_flow)), self.floating_point_unit)


class ZwaveMedianPacketsTimeDelta(Feature):
    protocol = Protocols.Zwave
    name = "median_packets_time_delta"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        return format(statistics.median(utils.packets_delta_time_calculation(zwave_flow)), self.floating_point_unit)


class ZwaveSkewnessPacketsTimeDelta(Feature):
    protocol = Protocols.Zwave
    name = "skewness_packets_time_delta"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        packets_time_delta = [packet.get_timestamp() for packet in zwave_flow.get_packets()]
        return format(stats.skew(utils.packets_delta_time_calculation(zwave_flow)), self.floating_point_unit)


class ZwaveCoefficientOfVariationPacketsTimeDelta(Feature):
    protocol = Protocols.Zwave
    name = "coefficient_of_variation_packets_time_delta"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        return format(stats.variation(utils.packets_delta_time_calculation(zwave_flow)), self.floating_point_unit)