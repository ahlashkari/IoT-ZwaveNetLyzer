#!/usr/bin/env python3

import statistics
from scipy import stats
from ...pipe_capturer import Packet
from ...pipe_capturer.pipes import ZwaveFlow
from ..feature import Feature
from ...protocols import Protocols
from .. import utils

class Duration(Feature):
    protocol = Protocols.Zwave
    name = "duration"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        return zwave_flow.get_duration()


class MaxPacketsTimeDelta(Feature):
    protocol = Protocols.Zwave
    name = "max_packets_time_delta"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        return max(utils.packets_delta_time_calculation(zwave_flow.get_packets()))


class MinPacketsTimeDelta(Feature):
    protocol = Protocols.Zwave
    name = "min_packets_time_delta"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        return min(utils.packets_delta_time_calculation(zwave_flow.get_packets()))


class MeanPacketsTimeDelta(Feature):
    protocol = Protocols.Zwave
    name = "mean_packets_time_delta"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        return format(statistics.mean(utils.packets_delta_time_calculation(zwave_flow.get_packets())), self.floating_point_unit)


class ModePacketsTimeDelta(Feature):
    protocol = Protocols.Zwave
    name = "mode_packets_time_delta"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        return format(float(stats.mode(utils.packets_delta_time_calculation(zwave_flow.get_packets()))[0]), self.floating_point_unit)


class VariancePacketsTimeDelta(Feature):
    protocol = Protocols.Zwave
    name = "variance_packets_time_delta"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        return format(statistics.pvariance(utils.packets_delta_time_calculation(zwave_flow.get_packets())), self.floating_point_unit)


class StandardDeviationPacketsTimeDelta(Feature):
    protocol = Protocols.Zwave
    name = "standard_deviation_packets_time_delta"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        return format(statistics.pstdev(utils.packets_delta_time_calculation(zwave_flow.get_packets())), self.floating_point_unit)


class MedianPacketsTimeDelta(Feature):
    protocol = Protocols.Zwave
    name = "median_packets_time_delta"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        return format(statistics.median(utils.packets_delta_time_calculation(zwave_flow.get_packets())), self.floating_point_unit)


class SkewnessPacketsTimeDelta(Feature):
    protocol = Protocols.Zwave
    name = "skewness_packets_time_delta"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        packets_time_delta = [packet.get_timestamp() for packet in zwave_flow.get_packets()]
        return format(stats.skew(utils.packets_delta_time_calculation(zwave_flow.get_packets())), self.floating_point_unit)


class CoefficientOfVariationPacketsTimeDelta(Feature):
    protocol = Protocols.Zwave
    name = "coefficient_of_variation_packets_time_delta"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        return format(stats.variation(utils.packets_delta_time_calculation(zwave_flow.get_packets())), self.floating_point_unit)


class FwdMaxPacketsTimeDelta(Feature):
    protocol = Protocols.Zwave
    name = "fwd_max_packets_time_delta"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        return max(utils.packets_delta_time_calculation(zwave_flow.get_forward_packets()))


class FwdMinPacketsTimeDelta(Feature):
    protocol = Protocols.Zwave
    name = "fwd_min_packets_time_delta"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        return min(utils.packets_delta_time_calculation(zwave_flow.get_forward_packets()))


class FwdMeanPacketsTimeDelta(Feature):
    protocol = Protocols.Zwave
    name = "fwd_mean_packets_time_delta"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        return format(statistics.mean(utils.packets_delta_time_calculation(zwave_flow.get_forward_packets())), self.floating_point_unit)


class FwdModePacketsTimeDelta(Feature):
    protocol = Protocols.Zwave
    name = "fwd_mode_packets_time_delta"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        return format(float(stats.mode(utils.packets_delta_time_calculation(zwave_flow.get_forward_packets()))[0]), self.floating_point_unit)


class FwdVariancePacketsTimeDelta(Feature):
    protocol = Protocols.Zwave
    name = "fwd_variance_packets_time_delta"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        return format(statistics.pvariance(utils.packets_delta_time_calculation(zwave_flow.get_forward_packets())), self.floating_point_unit)


class FwdStandardDeviationPacketsTimeDelta(Feature):
    protocol = Protocols.Zwave
    name = "fwd_standard_deviation_packets_time_delta"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        return format(statistics.pstdev(utils.packets_delta_time_calculation(zwave_flow.get_forward_packets())), self.floating_point_unit)


class FwdMedianPacketsTimeDelta(Feature):
    protocol = Protocols.Zwave
    name = "fwd_median_packets_time_delta"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        return format(statistics.median(utils.packets_delta_time_calculation(zwave_flow.get_forward_packets())), self.floating_point_unit)


class FwdSkewnessPacketsTimeDelta(Feature):
    protocol = Protocols.Zwave
    name = "fwd_skewness_packets_time_delta"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        packets_time_delta = [packet.get_timestamp() for packet in zwave_flow.get_packets()]
        return format(stats.skew(utils.packets_delta_time_calculation(zwave_flow.get_forward_packets())), self.floating_point_unit)


class FwdCoefficientOfVariationPacketsTimeDelta(Feature):
    protocol = Protocols.Zwave
    name = "fwd_coefficient_of_variation_packets_time_delta"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        return format(stats.variation(utils.packets_delta_time_calculation(zwave_flow.get_forward_packets())), self.floating_point_unit)


class BwdMaxPacketsTimeDelta(Feature):
    protocol = Protocols.Zwave
    name = "bwd_max_packets_time_delta"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        return max(utils.packets_delta_time_calculation(zwave_flow.get_backward_packets()))


class BwdMinPacketsTimeDelta(Feature):
    protocol = Protocols.Zwave
    name = "bwd_min_packets_time_delta"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        return min(utils.packets_delta_time_calculation(zwave_flow.get_backward_packets()))


class BwdMeanPacketsTimeDelta(Feature):
    protocol = Protocols.Zwave
    name = "bwd_mean_packets_time_delta"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        return format(statistics.mean(utils.packets_delta_time_calculation(zwave_flow.get_backward_packets())), self.floating_point_unit)


class BwdModePacketsTimeDelta(Feature):
    protocol = Protocols.Zwave
    name = "bwd_mode_packets_time_delta"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        return format(float(stats.mode(utils.packets_delta_time_calculation(zwave_flow.get_backward_packets()))[0]), self.floating_point_unit)


class BwdVariancePacketsTimeDelta(Feature):
    protocol = Protocols.Zwave
    name = "bwd_variance_packets_time_delta"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        return format(statistics.pvariance(utils.packets_delta_time_calculation(zwave_flow.get_backward_packets())), self.floating_point_unit)


class BwdStandardDeviationPacketsTimeDelta(Feature):
    protocol = Protocols.Zwave
    name = "bwd_standard_deviation_packets_time_delta"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        return format(statistics.pstdev(utils.packets_delta_time_calculation(zwave_flow.get_backward_packets())), self.floating_point_unit)


class BwdMedianPacketsTimeDelta(Feature):
    protocol = Protocols.Zwave
    name = "bwd_median_packets_time_delta"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        return format(statistics.median(utils.packets_delta_time_calculation(zwave_flow.get_backward_packets())), self.floating_point_unit)


class BwdSkewnessPacketsTimeDelta(Feature):
    protocol = Protocols.Zwave
    name = "bwd_skewness_packets_time_delta"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        packets_time_delta = [packet.get_timestamp() for packet in zwave_flow.get_packets()]
        return format(stats.skew(utils.packets_delta_time_calculation(zwave_flow.get_backward_packets())), self.floating_point_unit)


class BwdCoefficientOfVariationPacketsTimeDelta(Feature):
    protocol = Protocols.Zwave
    name = "bwd_coefficient_of_variation_packets_time_delta"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        return format(stats.variation(utils.packets_delta_time_calculation(zwave_flow.get_backward_packets())), self.floating_point_unit)