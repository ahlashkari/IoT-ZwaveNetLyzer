#!/usr/bin/env python3

import math
from statistics import pstdev, variance, mean
from scipy.stats import skew, kurtosis
from math import log2
from numpy import corrcoef
from collections import Counter
from itertools import groupby
from ...pipe_capturer.pipes import ZwaveFlow
from ..feature import Feature
from ...protocols import Protocols


class ZwaveFlowHomeID(Feature):
    protocol = Protocols.Zwave
    name = "home_id"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        return zwave_flow.get_home_id()


class ZwaveFlowSrcID(Feature):
    protocol = Protocols.Zwave
    name = "src_id"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        return zwave_flow.get_src_id()


class ZwaveFlowDstID(Feature):
    protocol = Protocols.Zwave
    name = "dst_id"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        return zwave_flow.get_dst_id()


class AverageSpeed(Feature):
    protocol = Protocols.Zwave
    name = "average_speed"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        speeds = [packet.get_speed() for packet in zwave_flow.get_packets()]
        return sum(speeds) / len(speeds) if speeds else 0


class MedianSpeed(Feature):
    protocol = Protocols.Zwave
    name = "median_speed"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        speeds = sorted([packet.get_speed() for packet in zwave_flow.get_packets()])
        mid = len(speeds) // 2
        return (speeds[mid] + speeds[~mid]) / 2 if speeds else 0


class ModeSpeed(Feature):
    protocol = Protocols.Zwave
    name = "mode_speed"    
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        speeds = [packet.get_speed() for packet in zwave_flow.get_packets()]
        if not speeds:
            return 0
        return max(set(speeds), key=speeds.count)


class StdDevSpeed(Feature):
    protocol = Protocols.Zwave
    name = "stddev_speed"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        speeds = [packet.get_speed() for packet in zwave_flow.get_packets()]
        return format(pstdev(speeds), self.floating_point_unit) if speeds else 0


class MinSpeed(Feature):
    protocol = Protocols.Zwave
    name = "min_speed"    
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        speeds = [packet.get_speed() for packet in zwave_flow.get_packets()]
        return min(speeds) if speeds else 0


class MaxSpeed(Feature):
    protocol = Protocols.Zwave
    name = "max_speed"    
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        speeds = [packet.get_speed() for packet in zwave_flow.get_packets()]
        return max(speeds) if speeds else 0


class SpeedRange(Feature):
    protocol = Protocols.Zwave
    name = "speed_range"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        speeds = [packet.get_speed() for packet in zwave_flow.get_packets()]
        return max(speeds) - min(speeds) if speeds else 0


class SpeedVariance(Feature):
    protocol = Protocols.Zwave
    name = "speed_variance"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        speeds = [packet.get_speed() for packet in zwave_flow.get_packets()]
        return format(variance(speeds), self.floating_point_unit) if len(speeds) > 1 else 0


class CoeffVariationSpeed(Feature):
    protocol = Protocols.Zwave
    name = "coeff_variation_speed"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        speeds = [packet.get_speed() for packet in zwave_flow.get_packets()]
        avg_speed = mean(speeds) if speeds else 0
        return format((pstdev(speeds) / avg_speed), self.floating_point_unit) if avg_speed != 0 else 0


class SpeedSkewness(Feature):
    protocol = Protocols.Zwave
    name = "speed_skewness"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        speeds = [packet.get_speed() for packet in zwave_flow.get_packets()]
        return format(skew(speeds), self.floating_point_unit) if speeds else 0


class FwdAverageSpeed(Feature):
    protocol = Protocols.Zwave
    name = "fwd_average_speed"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        speeds = [packet.get_speed() for packet in zwave_flow.get_forward_packets()]
        return sum(speeds) / len(speeds) if speeds else 0


class FwdMedianSpeed(Feature):
    protocol = Protocols.Zwave
    name = "fwd_median_speed"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        speeds = sorted([packet.get_speed() for packet in zwave_flow.get_forward_packets()])
        mid = len(speeds) // 2
        return (speeds[mid] + speeds[~mid]) / 2 if speeds else 0


class FwdModeSpeed(Feature):
    protocol = Protocols.Zwave
    name = "fwd_mode_speed"    
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        speeds = [packet.get_speed() for packet in zwave_flow.get_forward_packets()]
        if not speeds:
            return 0
        return max(set(speeds), key=speeds.count)


class FwdStdDevSpeed(Feature):
    protocol = Protocols.Zwave
    name = "fwd_stddev_speed"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        speeds = [packet.get_speed() for packet in zwave_flow.get_forward_packets()]
        return format(pstdev(speeds), self.floating_point_unit) if speeds else 0


class FwdMinSpeed(Feature):
    protocol = Protocols.Zwave
    name = "fwd_min_speed"    
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        speeds = [packet.get_speed() for packet in zwave_flow.get_forward_packets()]
        return min(speeds) if speeds else 0


class FwdMaxSpeed(Feature):
    protocol = Protocols.Zwave
    name = "fwd_max_speed"    
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        speeds = [packet.get_speed() for packet in zwave_flow.get_forward_packets()]
        return max(speeds) if speeds else 0


class FwdSpeedRange(Feature):
    protocol = Protocols.Zwave
    name = "fwd_speed_range"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        speeds = [packet.get_speed() for packet in zwave_flow.get_forward_packets()]
        return max(speeds) - min(speeds) if speeds else 0


class FwdSpeedVariance(Feature):
    protocol = Protocols.Zwave
    name = "fwd_speed_variance"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        speeds = [packet.get_speed() for packet in zwave_flow.get_forward_packets()]
        return format(variance(speeds), self.floating_point_unit) if len(speeds) > 1 else 0


class FwdCoeffVariationSpeed(Feature):
    protocol = Protocols.Zwave
    name = "fwd_coeff_variation_speed"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        speeds = [packet.get_speed() for packet in zwave_flow.get_forward_packets()]
        avg_speed = mean(speeds) if speeds else 0
        return format((pstdev(speeds) / avg_speed), self.floating_point_unit) if avg_speed != 0 else 0


class FwdSpeedSkewness(Feature):
    protocol = Protocols.Zwave
    name = "fwd_speed_skewness"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        speeds = [packet.get_speed() for packet in zwave_flow.get_forward_packets()]
        return format(skew(speeds), self.floating_point_unit) if speeds else 0


class BwdAverageSpeed(Feature):
    protocol = Protocols.Zwave
    name = "bwd_average_speed"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        speeds = [packet.get_speed() for packet in zwave_flow.get_backward_packets()]
        return sum(speeds) / len(speeds) if speeds else 0


class BwdMedianSpeed(Feature):
    protocol = Protocols.Zwave
    name = "bwd_median_speed"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        speeds = sorted([packet.get_speed() for packet in zwave_flow.get_backward_packets()])
        mid = len(speeds) // 2
        return (speeds[mid] + speeds[~mid]) / 2 if speeds else 0


class BwdModeSpeed(Feature):
    protocol = Protocols.Zwave
    name = "bwd_mode_speed"    
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        speeds = [packet.get_speed() for packet in zwave_flow.get_backward_packets()]
        if not speeds:
            return 0
        return max(set(speeds), key=speeds.count)


class BwdStdDevSpeed(Feature):
    protocol = Protocols.Zwave
    name = "bwd_stddev_speed"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        speeds = [packet.get_speed() for packet in zwave_flow.get_backward_packets()]
        return format(pstdev(speeds), self.floating_point_unit) if speeds else 0


class BwdMinSpeed(Feature):
    protocol = Protocols.Zwave
    name = "bwd_min_speed"    
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        speeds = [packet.get_speed() for packet in zwave_flow.get_backward_packets()]
        return min(speeds) if speeds else 0


class BwdMaxSpeed(Feature):
    protocol = Protocols.Zwave
    name = "bwd_max_speed"    
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        speeds = [packet.get_speed() for packet in zwave_flow.get_backward_packets()]
        return max(speeds) if speeds else 0


class BwdSpeedRange(Feature):
    protocol = Protocols.Zwave
    name = "bwd_speed_range"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        speeds = [packet.get_speed() for packet in zwave_flow.get_backward_packets()]
        return max(speeds) - min(speeds) if speeds else 0


class BwdSpeedVariance(Feature):
    protocol = Protocols.Zwave
    name = "bwd_speed_variance"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        speeds = [packet.get_speed() for packet in zwave_flow.get_backward_packets()]
        return format(variance(speeds), self.floating_point_unit) if len(speeds) > 1 else 0


class BwdCoeffVariationSpeed(Feature):
    protocol = Protocols.Zwave
    name = "bwd_coeff_variation_speed"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        speeds = [packet.get_speed() for packet in zwave_flow.get_backward_packets()]
        avg_speed = mean(speeds) if speeds else 0
        return format((pstdev(speeds) / avg_speed), self.floating_point_unit) if avg_speed != 0 else 0


class BwdSpeedSkewness(Feature):
    protocol = Protocols.Zwave
    name = "bwd_speed_skewness"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        speeds = [packet.get_speed() for packet in zwave_flow.get_backward_packets()]
        return format(skew(speeds), self.floating_point_unit) if speeds else 0


class CountEachPacketClass(Feature):
    protocol = Protocols.Zwave
    name = "count_each_packet_class"
    def extract(self, zwave_flow: ZwaveFlow) -> dict:
        classes = [packet.get_class() for packet in zwave_flow.get_packets()]
        class_count = {}
        for cls in classes:
            if cls in class_count:
                class_count[cls] += 1
            else:
                class_count[cls] = 1
        return class_count


class ProportionEachPacketClass(Feature):
    protocol = Protocols.Zwave
    name = "proportion_each_packet_class"
    def extract(self, zwave_flow: ZwaveFlow) -> dict:
        classes = [packet.get_class() for packet in zwave_flow.get_packets()]
        class_count = {}
        total = len(classes)
        for cls in classes:
            class_count[cls] = class_count.get(cls, 0) + 1
        return {cls: (count / total * 100) for cls, count in class_count.items()} if total else {}


class ProportionEachApplicationType(Feature):
    protocol = Protocols.Zwave
    name = "proportion_each_application_type"
    def extract(self, zwave_flow: ZwaveFlow) -> dict:
        applications = [packet.get_application() for packet in zwave_flow.get_packets()]
        app_count = {}
        total = len(applications)
        for app in applications:
            app_count[app] = app_count.get(app, 0) + 1
        return {app: (count / total * 100) for app, count in app_count.items()} if total else {}


class FwdCountEachPacketClass(Feature):
    protocol = Protocols.Zwave
    name = "fwd_count_each_packet_class"
    def extract(self, zwave_flow: ZwaveFlow) -> dict:
        classes = [packet.get_class() for packet in zwave_flow.get_forward_packets()]
        class_count = {}
        for cls in classes:
            if cls in class_count:
                class_count[cls] += 1
            else:
                class_count[cls] = 1
        return class_count


class FwdProportionEachPacketClass(Feature):
    protocol = Protocols.Zwave
    name = "fwd_proportion_each_packet_class"
    def extract(self, zwave_flow: ZwaveFlow) -> dict:
        classes = [packet.get_class() for packet in zwave_flow.get_forward_packets()]
        class_count = {}
        total = len(classes)
        for cls in classes:
            class_count[cls] = class_count.get(cls, 0) + 1
        return {cls: (count / total * 100) for cls, count in class_count.items()} if total else {}


class FwdProportionEachApplicationType(Feature):
    protocol = Protocols.Zwave
    name = "fwd_proportion_each_application_type"
    def extract(self, zwave_flow: ZwaveFlow) -> dict:
        applications = [packet.get_application() for packet in zwave_flow.get_forward_packets()]
        app_count = {}
        total = len(applications)
        for app in applications:
            app_count[app] = app_count.get(app, 0) + 1
        return {app: (count / total * 100) for app, count in app_count.items()} if total else {}


class BwdCountEachPacketClass(Feature):
    protocol = Protocols.Zwave
    name = "bwd_count_each_packet_class"
    def extract(self, zwave_flow: ZwaveFlow) -> dict:
        classes = [packet.get_class() for packet in zwave_flow.get_backward_packets()]
        class_count = {}
        for cls in classes:
            if cls in class_count:
                class_count[cls] += 1
            else:
                class_count[cls] = 1
        return class_count


class BwdProportionEachPacketClass(Feature):
    protocol = Protocols.Zwave
    name = "bwd_proportion_each_packet_class"
    def extract(self, zwave_flow: ZwaveFlow) -> dict:
        classes = [packet.get_class() for packet in zwave_flow.get_backward_packets()]
        class_count = {}
        total = len(classes)
        for cls in classes:
            class_count[cls] = class_count.get(cls, 0) + 1
        return {cls: (count / total * 100) for cls, count in class_count.items()} if total else {}


class BwdProportionEachApplicationType(Feature):
    protocol = Protocols.Zwave
    name = "bwd_proportion_each_application_type"
    def extract(self, zwave_flow: ZwaveFlow) -> dict:
        applications = [packet.get_application() for packet in zwave_flow.get_backward_packets()]
        app_count = {}
        total = len(applications)
        for app in applications:
            app_count[app] = app_count.get(app, 0) + 1
        return {app: (count / total * 100) for app, count in app_count.items()} if total else {}


class AverageRSSI(Feature):
    protocol = Protocols.Zwave
    name = "average_rssi"    
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        rssis = [packet.get_rssi() for packet in zwave_flow.get_packets()]
        return sum(rssis) / len(rssis) if rssis else 0


class MedianRSSI(Feature):
    protocol = Protocols.Zwave
    name = "median_rssi"    
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        rssis = sorted([packet.get_rssi() for packet in zwave_flow.get_packets()])
        mid = len(rssis) // 2
        return (rssis[mid] + rssis[~mid]) / 2 if rssis else 0


class ModeRSSI(Feature):
    protocol = Protocols.Zwave
    name = "mode_rssi"    
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        rssis = [packet.get_rssi() for packet in zwave_flow.get_packets()]
        if not rssis:
            return 0
        return max(set(rssis), key=rssis.count)


class StdDevRSSI(Feature):
    protocol = Protocols.Zwave
    name = "stddev_rssi"    
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        rssis = [packet.get_rssi() for packet in zwave_flow.get_packets()]
        return format(pstdev(rssis), self.floating_point_unit) if rssis else 0


class MinRSSI(Feature):
    protocol = Protocols.Zwave
    name = "min_rssi"  
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        rssis = [packet.get_rssi() for packet in zwave_flow.get_packets()]
        return min(rssis) if rssis else 0


class MaxRSSI(Feature):
    protocol = Protocols.Zwave
    name = "max_rssi"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        rssis = [packet.get_rssi() for packet in zwave_flow.get_packets()]
        return max(rssis) if rssis else 0


class RSSIRange(Feature):
    protocol = Protocols.Zwave
    name = "rssi_range"    
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        rssis = [packet.get_rssi() for packet in zwave_flow.get_packets()]
        return max(rssis) - min(rssis) if rssis else 0


class RSSIVariance(Feature):
    protocol = Protocols.Zwave
    name = "rssi_variance"    
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        rssis = [packet.get_rssi() for packet in zwave_flow.get_packets()]
        return format(variance(rssis), self.floating_point_unit) if len(rssis) > 1 else 0


class CoeffVariationSpeed(Feature):
    protocol = Protocols.Zwave
    name = "coeff_variation_rssi"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        rssis = [packet.get_rssi() for packet in zwave_flow.get_packets()]
        avg_rssi = mean(rssis) if rssis else 0
        return (pstdev(rssis) / avg_rssi) if avg_rssi != 0 else 0


class RSSISkewness(Feature):
    protocol = Protocols.Zwave
    name = "rssi_skewness"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        rssis = [packet.get_rssi() for packet in zwave_flow.get_packets()]
        return format(skew(rssis), self.floating_point_unit) if rssis else 0


class RSSIKurtosis(Feature):
    protocol = Protocols.Zwave
    name = "rssi_kurtosis"    
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        rssis = [packet.get_rssi() for packet in zwave_flow.get_packets()]
        return format(kurtosis(rssis), self.floating_point_unit) if rssis else 0


class FwdAverageRSSI(Feature):
    protocol = Protocols.Zwave
    name = "fwd_average_rssi"    
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        rssis = [packet.get_rssi() for packet in zwave_flow.get_forward_packets()]
        return sum(rssis) / len(rssis) if rssis else 0


class FwdMedianRSSI(Feature):
    protocol = Protocols.Zwave
    name = "fwd_median_rssi"    
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        rssis = sorted([packet.get_rssi() for packet in zwave_flow.get_forward_packets()])
        mid = len(rssis) // 2
        return (rssis[mid] + rssis[~mid]) / 2 if rssis else 0


class FwdModeRSSI(Feature):
    protocol = Protocols.Zwave
    name = "fwd_mode_rssi"    
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        rssis = [packet.get_rssi() for packet in zwave_flow.get_forward_packets()]
        if not rssis:
            return 0
        return max(set(rssis), key=rssis.count)


class FwdStdDevRSSI(Feature):
    protocol = Protocols.Zwave
    name = "fwd_stddev_rssi"    
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        rssis = [packet.get_rssi() for packet in zwave_flow.get_forward_packets()]
        return format(pstdev(rssis), self.floating_point_unit) if rssis else 0


class FwdMinRSSI(Feature):
    protocol = Protocols.Zwave
    name = "fwd_min_rssi"  
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        rssis = [packet.get_rssi() for packet in zwave_flow.get_forward_packets()]
        return min(rssis) if rssis else 0


class FwdMaxRSSI(Feature):
    protocol = Protocols.Zwave
    name = "fwd_max_rssi"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        rssis = [packet.get_rssi() for packet in zwave_flow.get_forward_packets()]
        return max(rssis) if rssis else 0


class FwdRSSIRange(Feature):
    protocol = Protocols.Zwave
    name = "fwd_rssi_range"    
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        rssis = [packet.get_rssi() for packet in zwave_flow.get_forward_packets()]
        return max(rssis) - min(rssis) if rssis else 0


class FwdRSSIVariance(Feature):
    protocol = Protocols.Zwave
    name = "fwd_rssi_variance"    
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        rssis = [packet.get_rssi() for packet in zwave_flow.get_forward_packets()]
        return format(variance(rssis), self.floating_point_unit) if len(rssis) > 1 else 0


class FwdCoeffVariationSpeed(Feature):
    protocol = Protocols.Zwave
    name = "fwd_coeff_variation_rssi"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        rssis = [packet.get_rssi() for packet in zwave_flow.get_forward_packets()]
        avg_rssi = mean(rssis) if rssis else 0
        return (pstdev(rssis) / avg_rssi) if avg_rssi != 0 else 0


class FwdRSSISkewness(Feature):
    protocol = Protocols.Zwave
    name = "fwd_rssi_skewness"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        rssis = [packet.get_rssi() for packet in zwave_flow.get_forward_packets()]
        return format(skew(rssis), self.floating_point_unit) if rssis else 0


class FwdRSSIKurtosis(Feature):
    protocol = Protocols.Zwave
    name = "fwd_rssi_kurtosis"    
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        rssis = [packet.get_rssi() for packet in zwave_flow.get_forward_packets()]
        return format(kurtosis(rssis), self.floating_point_unit) if rssis else 0


class BwdAverageRSSI(Feature):
    protocol = Protocols.Zwave
    name = "bwd_average_rssi"    
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        rssis = [packet.get_rssi() for packet in zwave_flow.get_backward_packets()]
        return sum(rssis) / len(rssis) if rssis else 0


class BwdMedianRSSI(Feature):
    protocol = Protocols.Zwave
    name = "bwd_median_rssi"    
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        rssis = sorted([packet.get_rssi() for packet in zwave_flow.get_backward_packets()])
        mid = len(rssis) // 2
        return (rssis[mid] + rssis[~mid]) / 2 if rssis else 0


class BwdModeRSSI(Feature):
    protocol = Protocols.Zwave
    name = "bwd_mode_rssi"    
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        rssis = [packet.get_rssi() for packet in zwave_flow.get_backward_packets()]
        if not rssis:
            return 0
        return max(set(rssis), key=rssis.count)


class BwdStdDevRSSI(Feature):
    protocol = Protocols.Zwave
    name = "bwd_stddev_rssi"    
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        rssis = [packet.get_rssi() for packet in zwave_flow.get_backward_packets()]
        return format(pstdev(rssis), self.floating_point_unit) if rssis else 0


class BwdMinRSSI(Feature):
    protocol = Protocols.Zwave
    name = "bwd_min_rssi"  
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        rssis = [packet.get_rssi() for packet in zwave_flow.get_backward_packets()]
        return min(rssis) if rssis else 0


class BwdMaxRSSI(Feature):
    protocol = Protocols.Zwave
    name = "bwd_max_rssi"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        rssis = [packet.get_rssi() for packet in zwave_flow.get_backward_packets()]
        return max(rssis) if rssis else 0


class BwdRSSIRange(Feature):
    protocol = Protocols.Zwave
    name = "bwd_rssi_range"    
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        rssis = [packet.get_rssi() for packet in zwave_flow.get_backward_packets()]
        return max(rssis) - min(rssis) if rssis else 0


class BwdRSSIVariance(Feature):
    protocol = Protocols.Zwave
    name = "bwd_rssi_variance"    
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        rssis = [packet.get_rssi() for packet in zwave_flow.get_backward_packets()]
        return format(variance(rssis), self.floating_point_unit) if len(rssis) > 1 else 0


class BwdCoeffVariationSpeed(Feature):
    protocol = Protocols.Zwave
    name = "bwd_coeff_variation_rssi"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        rssis = [packet.get_rssi() for packet in zwave_flow.get_backward_packets()]
        avg_rssi = mean(rssis) if rssis else 0
        return (pstdev(rssis) / avg_rssi) if avg_rssi != 0 else 0


class BwdRSSISkewness(Feature):
    protocol = Protocols.Zwave
    name = "bwd_rssi_skewness"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        rssis = [packet.get_rssi() for packet in zwave_flow.get_backward_packets()]
        return format(skew(rssis), self.floating_point_unit) if rssis else 0


class BwdRSSIKurtosis(Feature):
    protocol = Protocols.Zwave
    name = "bwd_rssi_kurtosis"    
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        rssis = [packet.get_rssi() for packet in zwave_flow.get_backward_packets()]
        return format(kurtosis(rssis), self.floating_point_unit) if rssis else 0


class TotalAcknowledgments(Feature):
    protocol = Protocols.Zwave
    name = "total_acknowledgments"   
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        return sum(1 for packet in zwave_flow.get_packets() if packet.is_ack())


class ProportionAcknowledgedPackets(Feature):
    protocol = Protocols.Zwave
    name = "proportion_acknowledged_packets"   
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        total_packets = len(zwave_flow.get_packets())
        acknowledged_packets = sum(1 for packet in zwave_flow.get_packets() if packet.is_ack())
        return (acknowledged_packets / total_packets * 100) if total_packets else 0


class TotalCRCErrors(Feature):
    protocol = Protocols.Zwave
    name = "total_crc_errors"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        return sum(1 for packet in zwave_flow.get_packets() if not packet.is_crc_ok())


class ProportionCRCErrors(Feature):
    protocol = Protocols.Zwave
    name = "proportion_crc_errors"    
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        total_packets = len(zwave_flow.get_packets())
        crc_error_packets = sum(1 for packet in zwave_flow.get_packets() if not packet.is_crc_ok())
        return (crc_error_packets / total_packets * 100) if total_packets else 0


class TotalSubstitutedPackets(Feature):
    protocol = Protocols.Zwave
    name = "total_substituted_packets"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        return sum(1 for packet in zwave_flow.get_packets() if packet.is_substituted())


class ProportionSubstitutedPackets(Feature):
    protocol = Protocols.Zwave
    name = "proportion_substituted_packets"    
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        total_packets = len(zwave_flow.get_packets())
        substituted_packets = sum(1 for packet in zwave_flow.get_packets() if packet.is_substituted())
        return (substituted_packets / total_packets * 100) if total_packets else 0


class CountPacketsWithUnknownHeaders(Feature):
    protocol = Protocols.Zwave
    name = "count_packets_with_unknown_headers"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        return sum(1 for packet in zwave_flow.get_packets() if packet.is_unknown_header())


class ProportionUnknownHeaderPackets(Feature):
    protocol = Protocols.Zwave
    name = "proportion_unknown_header_packets"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        total_packets = len(zwave_flow.get_packets())
        unknown_header_packets = sum(1 for packet in zwave_flow.get_packets() if packet.is_unknown_header())
        return (unknown_header_packets / total_packets * 100) if total_packets else 0


class CountWakeupBeams(Feature):
    protocol = Protocols.Zwave
    name = "count_wakeup_beams"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        return sum(1 for packet in zwave_flow.get_packets() if packet.is_wakeup_beam())


class ProportionWakeupBeamPackets(Feature):
    protocol = Protocols.Zwave
    name = "proportion_wakeup_beam_packets"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        total_packets = len(zwave_flow.get_packets())
        wakeup_beam_packets = sum(1 for packet in zwave_flow.get_packets() if packet.is_wakeup_beam())
        return (wakeup_beam_packets / total_packets * 100) if total_packets else 0


class UniqueHexPatternsCount(Feature):
    protocol = Protocols.Zwave
    name = "unique_hex_patterns_count"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        hex_patterns = set(packet.get_hex_data() for packet in zwave_flow.get_packets())
        return len(hex_patterns)


class FrequencyOfTopHexPatterns(Feature):
    protocol = Protocols.Zwave
    name = "frequency_of_top_hex_patterns"
    def extract(self, zwave_flow: ZwaveFlow) -> dict:
        hex_pattern_counts = {}
        for packet in zwave_flow.get_packets():
            hex_data = packet.get_hex_data()
            if hex_data in hex_pattern_counts:
                hex_pattern_counts[hex_data] += 1
            else:
                hex_pattern_counts[hex_data] = 1
        # Return the most frequent patterns, the slicing can be adjusted for more or less patterns
        return dict(sorted(hex_pattern_counts.items(), key=lambda item: item[1], reverse=True)[:5])


class EntropyOfHexData(Feature):
    protocol = Protocols.Zwave
    name = "entropy_of_hex_data"    
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        hex_pattern_counts = {}
        for packet in zwave_flow.get_packets():
            hex_data = packet.get_hex_data()
            hex_pattern_counts[hex_data] = hex_pattern_counts.get(hex_data, 0) + 1
        total = sum(hex_pattern_counts.values())
        entropy = -sum((count / total) * log2(count / total) for count in hex_pattern_counts.values())
        return entropy

class HexDataPatternLengthVariability(Feature):
    protocol = Protocols.Zwave
    name = "hex_data_pattern_length_variability"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        from statistics import pstdev
        lengths = [len(packet.get_hex_data()) for packet in zwave_flow.get_packets()]
        return format(pstdev(lengths), self.floating_point_unit) if lengths else 0


class CrossCorrelationSpeedRSSI(Feature):
    protocol = Protocols.Zwave
    name = "cross_correlation_speed_rssi"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        speeds = [packet.get_speed() for packet in zwave_flow.get_packets()]
        rssis = [packet.get_rssi() for packet in zwave_flow.get_packets()]
        if len(speeds) > 1 and len(rssis) > 1:
            return format(corrcoef(speeds, rssis)[0, 1], self.floating_point_unit)
        return 0  # Return 0 correlation if there's insufficient data


class TimeSeriesAnalysisPacketIntervals(Feature):
    protocol = Protocols.Zwave
    name = "time_series_analysis_packet_intervals"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        timestamps = [packet.get_timestamp() for packet in zwave_flow.get_packets()]
        if len(timestamps) < 2:
            return 0  # No intervals to analyze
        intervals = [(t2 - t1).total_seconds() for t1, t2 in zip(timestamps[:-1], timestamps[1:])]
        return sum(intervals) / len(intervals)  # Return average interval


class PercentagePacketsPerChannel(Feature):
    protocol = Protocols.Zwave
    name = "percentage_packets_per_channel"
    def extract(self, zwave_flow: ZwaveFlow) -> dict:
        channels = [packet.get_channel() for packet in zwave_flow.get_packets()]
        channel_count = {}
        total = len(channels)
        for channel in channels:
            channel_count[channel] = channel_count.get(channel, 0) + 1
        return {channel: (count / total * 100) for channel, count in channel_count.items()} if total else {}


class PercentageHighSpeedTransmissions(Feature):
    protocol = Protocols.Zwave
    name = "percentage_high_speed_transmissions"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        speeds = [packet.get_speed() for packet in zwave_flow.get_packets()]
        high_speed_threshold = 100
        high_speed_count = sum(1 for speed in speeds if speed > high_speed_threshold)
        total_packets = len(speeds)
        return (high_speed_count / total_packets * 100) if total_packets else 0


class TotalLowSignalPackets(Feature):
    protocol = Protocols.Zwave
    name = "total_low_signal_packets"    
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        return sum(1 for packet in zwave_flow.get_packets() if packet.is_low())


class PercentageLowSignalPackets(Feature):
    protocol = Protocols.Zwave
    name = "percentage_low_signal_packets"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        total_packets = len(zwave_flow.get_packets())
        low_signal_count = sum(1 for packet in zwave_flow.get_packets() if packet.is_low())
        return (low_signal_count / total_packets * 100) if total_packets else 0


class AverageChannelUsage(Feature):
    protocol = Protocols.Zwave
    name = "average_channel_usage"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        channels = [packet.get_channel() for packet in zwave_flow.get_packets()]
        channel_counts = Counter(channels)
        return format(mean(list(channel_counts.values())), self.floating_point_unit) if channels else 0

class MostCommonChannel(Feature):
    protocol = Protocols.Zwave
    name = "most_common_channel"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        channels = [packet.get_channel() for packet in zwave_flow.get_packets()]
        return Counter(channels).most_common(1)[0][0] if channels else None


class LeastCommonChannel(Feature):
    protocol = Protocols.Zwave
    name = "least_common_channel"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        channels = [packet.get_channel() for packet in zwave_flow.get_packets()]
        return Counter(channels).most_common()[-1][0] if channels else None


class ChannelTransitionCount(Feature):
    protocol = Protocols.Zwave
    name = "channel_transition_count"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        channels = [packet.get_channel() for packet in zwave_flow.get_packets()]
        return sum(1 for i in range(1, len(channels)) if channels[i] != channels[i-1])


class ChannelStability(Feature):
    protocol = Protocols.Zwave
    name = "channel_stability"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        channels = [packet.get_channel() for packet in zwave_flow.get_packets()]
        longest_streak = max(len(list(g)) for k, g in groupby(channels))
        return longest_streak


class EntropyOfChannelUsage(Feature):
    protocol = Protocols.Zwave
    name = "entropy_of_channel_usage"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        channels = [packet.get_channel() for packet in zwave_flow.get_packets()]
        channel_counts = Counter(channels)
        total = sum(channel_counts.values())
        entropy = -sum((count / total) * math.log2(count / total) for count in channel_counts.values()) if total > 0 else 0
        return entropy


class CommonDataPatterns(Feature):
    protocol = Protocols.Zwave
    name = "common_data_patterns"
    def extract(self, zwave_flow: ZwaveFlow) -> str:
        data_entries = [packet.get_data() for packet in zwave_flow.get_packets() if packet.get_data()]
        return Counter(data_entries).most_common(1)[0][0] if data_entries else None


class UniqueDataEntries(Feature):
    protocol = Protocols.Zwave
    name = "unique_data_entries"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        data_entries = {packet.get_data() for packet in zwave_flow.get_packets() if packet.get_data()}
        return len(data_entries)


class ClassDistribution(Feature):
    protocol = Protocols.Zwave
    name = "class_distribution"
    def extract(self, zwave_flow: ZwaveFlow) -> dict:
        classes = [packet.get_class() for packet in zwave_flow.get_packets()]
        return Counter(classes)
    

class MostCommonClass(Feature):
    protocol = Protocols.Zwave
    name = "most_common_class"
    def extract(self, zwave_flow: ZwaveFlow) -> str:
        classes = [packet.get_class() for packet in zwave_flow.get_packets()]
        return Counter(classes).most_common(1)[0][0] if classes else None


class LeastCommonClass(Feature):
    protocol = Protocols.Zwave
    name = "least_common_class"    
    def extract(self, zwave_flow: ZwaveFlow) -> str:
        classes = [packet.get_class() for packet in zwave_flow.get_packets()]
        return Counter(classes).most_common()[-1][0] if classes else None


class ApplicationUsageFrequency(Feature):
    protocol = Protocols.Zwave
    name = "application_usage_frequency"
    def extract(self, zwave_flow: ZwaveFlow) -> dict:
        applications = [packet.get_application() for packet in zwave_flow.get_packets()]
        return Counter(applications)


class MostCommonApplication(Feature):
    protocol = Protocols.Zwave
    name = "most_common_application"
    def extract(self, zwave_flow: ZwaveFlow) -> str:
        applications = [packet.get_application() for packet in zwave_flow.get_packets()]
        return Counter(applications).most_common(1)[0][0] if applications else None


class UniqueApplicationCount(Feature):
    protocol = Protocols.Zwave
    name = "unique_application_count"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        applications = {packet.get_application() for packet in zwave_flow.get_packets()}
        return len(applications)


class HeaderPatternConsistency(Feature):
    protocol = Protocols.Zwave
    name = "header_pattern_consistency"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        headers = [packet.get_header() for packet in zwave_flow.get_packets()]
        most_common_count = Counter(headers).most_common(1)[0][1] if headers else 0
        total_headers = len(headers)
        return most_common_count / total_headers if total_headers > 0 else 0


class HeaderComplexity(Feature):
    protocol = Protocols.Zwave
    name = "header_complexity"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        headers = [packet.get_header() for packet in zwave_flow.get_packets()]
        unique_headers = set(headers)
        total_headers = len(headers)
        return len(unique_headers) / total_headers if total_headers > 0 else 0


class PayloadToHeaderRatio(Feature):
    protocol = Protocols.Zwave
    name = "payload_size_to_header_size_ratio"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        packets = zwave_flow.get_packets()
        total_payload = sum(packet.get_payload_bytes() for packet in packets)
        total_header = sum(packet.get_header_bytes() for packet in packets)
        return total_payload / total_header if total_header > 0 else 0


class IncrementalDataChange(Feature):
    protocol = Protocols.Zwave
    name = "incremental_data_change"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        data_fields = [packet.get_payload() for packet in zwave_flow.get_packets() if packet.get_payload()]
        return sum(1 for i in range(1, len(data_fields)) if data_fields[i] != data_fields[i-1])


class HeaderEntropy(Feature):
    protocol = Protocols.Zwave
    name = "header_entropy"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        headers = [packet.get_header() for packet in zwave_flow.get_packets()]
        header_counts = Counter(headers)
        total = sum(header_counts.values())
        entropy = -sum((count / total) * math.log2(count / total) for count in header_counts.values()) if total > 0 else 0
        return format(entropy, self.floating_point_unit)


class TemporalStabilityOfClassType(Feature):
    protocol = Protocols.Zwave
    name = "temporal_stability_of_class_type"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        classes = [packet.get_class() for packet in zwave_flow.get_packets()]
        most_common_count = Counter(classes).most_common(1)[0][1] if classes else 0
        total_classes = len(classes)
        return most_common_count / total_classes if total_classes > 0 else 0


class TemporalStabilityOfApplicationType(Feature):
    protocol = Protocols.Zwave
    name = "temporal_stability_of_application_type"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        applications = [packet.get_application() for packet in zwave_flow.get_packets()]
        most_common_count = Counter(applications).most_common(1)[0][1] if applications else 0
        total_applications = len(applications)
        return most_common_count / total_applications if total_applications > 0 else 0


class DataFieldEntropy(Feature):
    protocol = Protocols.Zwave
    name = "data_field_entropy"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        data_fields = [packet.get_data() for packet in zwave_flow.get_packets() if packet.get_data()]
        data_field_counts = Counter(data_fields)
        total = sum(data_field_counts.values())
        entropy = -sum((count / total) * math.log2(count / total) for count in data_field_counts.values()) if total > 0 else 0
        return format(entropy, self.floating_point_unit)


class PayloadEntropy(Feature):
    protocol = Protocols.Zwave
    name = "payload_entropy"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        payloads = [packet.get_payload() for packet in zwave_flow.get_packets() if packet.get_payload()]
        payloads_counts = Counter(payloads)
        total = sum(payloads_counts.values())
        entropy = -sum((count / total) * math.log2(count / total) for count in payloads_counts.values()) if total > 0 else 0
        return format(entropy, self.floating_point_unit)


class CountOfSingleCastPackets(Feature):
    protocol = Protocols.Zwave
    name = "count_of_single_cast_packets"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        single_casts = [1 for packet in zwave_flow.get_packets() if packet.get_data() == 'SINGLECAST']
        return len(single_casts)


class ProportionOfSingleCastPackets(Feature):
    protocol = Protocols.Zwave
    name = "proportion_of_single_cast_packets"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        total_packets = len(zwave_flow.get_packets())
        single_casts = sum(1 for packet in zwave_flow.get_packets() if packet.get_data() == 'SINGLECAST')
        return (single_casts / total_packets * 100) if total_packets > 0 else 0


class CountOfACKPackets(Feature):
    protocol = Protocols.Zwave
    name = "count_of_ack_packets"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        return sum(1 for packet in zwave_flow.get_packets() if packet.get_data() == 'TRANSFER_ACKNOWLEDGE')


class ProportionOfACKPackets(Feature):
    protocol = Protocols.Zwave
    name = "proportion_of_ack_packets"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        total_packets = len(zwave_flow.get_packets())
        ack_frames = sum(1 for packet in zwave_flow.get_packets() if packet.get_data() == 'TRANSFER_ACKNOWLEDGE')
        return (ack_frames / total_packets * 100) if total_packets > 0 else 0


class CountOfMulticastPackets(Feature):
    protocol = Protocols.Zwave
    name = "count_of_multicast_packets"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        return sum(1 for packet in zwave_flow.get_packets() if packet.get_data() == 'MULTICAST')


class ProportionOfMulticastPackets(Feature):
    protocol = Protocols.Zwave
    name = "proportion_of_multicast_packets"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        total_packets = len(zwave_flow.get_packets())
        multicast_frames = sum(1 for packet in zwave_flow.get_packets() if packet.get_data() == 'MULTICAST')
        return (multicast_frames / total_packets * 100) if total_packets > 0 else 0


class CountOfBroadcastPackets(Feature):
    protocol = Protocols.Zwave
    name = "count_of_broadcast_packets"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        return sum(1 for packet in zwave_flow.get_packets() if packet.get_data() == 'BROADCAST')


class ProportionOfBroadcastPackets(Feature):
    protocol = Protocols.Zwave
    name = "proportion_of_broadcast_packets"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        total_packets = len(zwave_flow.get_packets())
        broadcast_frames = sum(1 for packet in zwave_flow.get_packets() if packet.get_data() == 'BROADCAST')
        return (broadcast_frames / total_packets * 100) if total_packets > 0 else 0


class CountOfExplorerAutoInclusionPackets(Feature):
    protocol = Protocols.Zwave
    name = "count_of_explorer_autoinclusion_packets"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        return sum(1 for packet in zwave_flow.get_packets() if packet.get_data() == 'EXPLORER_AUTOINCLUSION')


class ProportionOfExplorerAutoInclusionPackets(Feature):
    protocol = Protocols.Zwave
    name = "proportion_of_explorer_autoinclusion_packets"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        total_packets = len(zwave_flow.get_packets())
        explorer_autoinclusion = sum(1 for packet in zwave_flow.get_packets() if packet.get_data() == 'EXPLORER_AUTOINCLUSION')
        return (explorer_autoinclusion / total_packets * 100) if total_packets > 0 else 0


class FwdTotalAcknowledgments(Feature):
    protocol = Protocols.Zwave
    name = "fwd_total_acknowledgments"   
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        return sum(1 for packet in zwave_flow.get_forward_packets() if packet.is_ack())


class FwdProportionAcknowledgedPackets(Feature):
    protocol = Protocols.Zwave
    name = "fwd_proportion_acknowledged_packets"   
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        total_packets = len(zwave_flow.get_forward_packets())
        acknowledged_packets = sum(1 for packet in zwave_flow.get_forward_packets() if packet.is_ack())
        return (acknowledged_packets / total_packets * 100) if total_packets else 0


class FwdTotalCRCErrors(Feature):
    protocol = Protocols.Zwave
    name = "fwd_total_crc_errors"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        return sum(1 for packet in zwave_flow.get_forward_packets() if not packet.is_crc_ok())


class FwdProportionCRCErrors(Feature):
    protocol = Protocols.Zwave
    name = "fwd_proportion_crc_errors"    
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        total_packets = len(zwave_flow.get_forward_packets())
        crc_error_packets = sum(1 for packet in zwave_flow.get_forward_packets() if not packet.is_crc_ok())
        return (crc_error_packets / total_packets * 100) if total_packets else 0


class FwdTotalSubstitutedPackets(Feature):
    protocol = Protocols.Zwave
    name = "fwd_total_substituted_packets"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        return sum(1 for packet in zwave_flow.get_forward_packets() if packet.is_substituted())


class FwdProportionSubstitutedPackets(Feature):
    protocol = Protocols.Zwave
    name = "fwd_proportion_substituted_packets"    
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        total_packets = len(zwave_flow.get_forward_packets())
        substituted_packets = sum(1 for packet in zwave_flow.get_forward_packets() if packet.is_substituted())
        return (substituted_packets / total_packets * 100) if total_packets else 0


class FwdCountPacketsWithUnknownHeaders(Feature):
    protocol = Protocols.Zwave
    name = "fwd_count_packets_with_unknown_headers"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        return sum(1 for packet in zwave_flow.get_forward_packets() if packet.is_unknown_header())


class FwdProportionUnknownHeaderPackets(Feature):
    protocol = Protocols.Zwave
    name = "fwd_proportion_unknown_header_packets"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        total_packets = len(zwave_flow.get_forward_packets())
        unknown_header_packets = sum(1 for packet in zwave_flow.get_forward_packets() if packet.is_unknown_header())
        return (unknown_header_packets / total_packets * 100) if total_packets else 0


class FwdCountWakeupBeams(Feature):
    protocol = Protocols.Zwave
    name = "fwd_count_wakeup_beams"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        return sum(1 for packet in zwave_flow.get_forward_packets() if packet.is_wakeup_beam())


class FwdProportionWakeupBeamPackets(Feature):
    protocol = Protocols.Zwave
    name = "fwd_proportion_wakeup_beam_packets"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        total_packets = len(zwave_flow.get_forward_packets())
        wakeup_beam_packets = sum(1 for packet in zwave_flow.get_forward_packets() if packet.is_wakeup_beam())
        return (wakeup_beam_packets / total_packets * 100) if total_packets else 0


class FwdUniqueHexPatternsCount(Feature):
    protocol = Protocols.Zwave
    name = "fwd_unique_hex_patterns_count"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        hex_patterns = set(packet.get_hex_data() for packet in zwave_flow.get_forward_packets())
        return len(hex_patterns)


class FwdFrequencyOfTopHexPatterns(Feature):
    protocol = Protocols.Zwave
    name = "fwd_frequency_of_top_hex_patterns"
    def extract(self, zwave_flow: ZwaveFlow) -> dict:
        hex_pattern_counts = {}
        for packet in zwave_flow.get_forward_packets():
            hex_data = packet.get_hex_data()
            if hex_data in hex_pattern_counts:
                hex_pattern_counts[hex_data] += 1
            else:
                hex_pattern_counts[hex_data] = 1
        # Return the most frequent patterns, the slicing can be adjusted for more or less patterns
        return dict(sorted(hex_pattern_counts.items(), key=lambda item: item[1], reverse=True)[:5])


class FwdEntropyOfHexData(Feature):
    protocol = Protocols.Zwave
    name = "fwd_entropy_of_hex_data"    
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        hex_pattern_counts = {}
        for packet in zwave_flow.get_forward_packets():
            hex_data = packet.get_hex_data()
            hex_pattern_counts[hex_data] = hex_pattern_counts.get(hex_data, 0) + 1
        total = sum(hex_pattern_counts.values())
        entropy = -sum((count / total) * log2(count / total) for count in hex_pattern_counts.values())
        return entropy

class FwdHexDataPatternLengthVariability(Feature):
    protocol = Protocols.Zwave
    name = "fwd_hex_data_pattern_length_variability"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        from statistics import pstdev
        lengths = [len(packet.get_hex_data()) for packet in zwave_flow.get_forward_packets()]
        return format(pstdev(lengths), self.floating_point_unit) if lengths else 0


class FwdCrossCorrelationSpeedRSSI(Feature):
    protocol = Protocols.Zwave
    name = "fwd_cross_correlation_speed_rssi"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        speeds = [packet.get_speed() for packet in zwave_flow.get_forward_packets()]
        rssis = [packet.get_rssi() for packet in zwave_flow.get_forward_packets()]
        if len(speeds) > 1 and len(rssis) > 1:
            return format(corrcoef(speeds, rssis)[0, 1], self.floating_point_unit)
        return 0  # Return 0 correlation if there's insufficient data


class FwdTimeSeriesAnalysisPacketIntervals(Feature):
    protocol = Protocols.Zwave
    name = "fwd_time_series_analysis_packet_intervals"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        timestamps = [packet.get_timestamp() for packet in zwave_flow.get_forward_packets()]
        if len(timestamps) < 2:
            return 0  # No intervals to analyze
        intervals = [(t2 - t1).total_seconds() for t1, t2 in zip(timestamps[:-1], timestamps[1:])]
        return sum(intervals) / len(intervals)  # Return average interval


class FwdPercentagePacketsPerChannel(Feature):
    protocol = Protocols.Zwave
    name = "fwd_percentage_packets_per_channel"
    def extract(self, zwave_flow: ZwaveFlow) -> dict:
        channels = [packet.get_channel() for packet in zwave_flow.get_forward_packets()]
        channel_count = {}
        total = len(channels)
        for channel in channels:
            channel_count[channel] = channel_count.get(channel, 0) + 1
        return {channel: (count / total * 100) for channel, count in channel_count.items()} if total else {}


class FwdPercentageHighSpeedTransmissions(Feature):
    protocol = Protocols.Zwave
    name = "fwd_percentage_high_speed_transmissions"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        speeds = [packet.get_speed() for packet in zwave_flow.get_forward_packets()]
        high_speed_threshold = 100
        high_speed_count = sum(1 for speed in speeds if speed > high_speed_threshold)
        total_packets = len(speeds)
        return (high_speed_count / total_packets * 100) if total_packets else 0


class FwdTotalLowSignalPackets(Feature):
    protocol = Protocols.Zwave
    name = "fwd_total_low_signal_packets"    
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        return sum(1 for packet in zwave_flow.get_forward_packets() if packet.is_low())


class FwdPercentageLowSignalPackets(Feature):
    protocol = Protocols.Zwave
    name = "fwd_percentage_low_signal_packets"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        total_packets = len(zwave_flow.get_forward_packets())
        low_signal_count = sum(1 for packet in zwave_flow.get_forward_packets() if packet.is_low())
        return (low_signal_count / total_packets * 100) if total_packets else 0


class FwdAverageChannelUsage(Feature):
    protocol = Protocols.Zwave
    name = "fwd_average_channel_usage"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        channels = [packet.get_channel() for packet in zwave_flow.get_forward_packets()]
        channel_counts = Counter(channels)
        return format(mean(list(channel_counts.values())), self.floating_point_unit) if channels else 0

class FwdMostCommonChannel(Feature):
    protocol = Protocols.Zwave
    name = "fwd_most_common_channel"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        channels = [packet.get_channel() for packet in zwave_flow.get_forward_packets()]
        return Counter(channels).most_common(1)[0][0] if channels else None


class FwdLeastCommonChannel(Feature):
    protocol = Protocols.Zwave
    name = "fwd_least_common_channel"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        channels = [packet.get_channel() for packet in zwave_flow.get_forward_packets()]
        return Counter(channels).most_common()[-1][0] if channels else None


class FwdChannelTransitionCount(Feature):
    protocol = Protocols.Zwave
    name = "fwd_channel_transition_count"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        channels = [packet.get_channel() for packet in zwave_flow.get_forward_packets()]
        return sum(1 for i in range(1, len(channels)) if channels[i] != channels[i-1])


class FwdChannelStability(Feature):
    protocol = Protocols.Zwave
    name = "fwd_channel_stability"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        channels = [packet.get_channel() for packet in zwave_flow.get_forward_packets()]
        longest_streak = max(len(list(g)) for k, g in groupby(channels))
        return longest_streak


class FwdEntropyOfChannelUsage(Feature):
    protocol = Protocols.Zwave
    name = "fwd_entropy_of_channel_usage"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        channels = [packet.get_channel() for packet in zwave_flow.get_forward_packets()]
        channel_counts = Counter(channels)
        total = sum(channel_counts.values())
        entropy = -sum((count / total) * math.log2(count / total) for count in channel_counts.values()) if total > 0 else 0
        return entropy


class FwdCommonDataPatterns(Feature):
    protocol = Protocols.Zwave
    name = "fwd_common_data_patterns"
    def extract(self, zwave_flow: ZwaveFlow) -> str:
        data_entries = [packet.get_data() for packet in zwave_flow.get_forward_packets() if packet.get_data()]
        return Counter(data_entries).most_common(1)[0][0] if data_entries else None


class FwdUniqueDataEntries(Feature):
    protocol = Protocols.Zwave
    name = "fwd_unique_data_entries"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        data_entries = {packet.get_data() for packet in zwave_flow.get_forward_packets() if packet.get_data()}
        return len(data_entries)


class FwdClassDistribution(Feature):
    protocol = Protocols.Zwave
    name = "fwd_class_distribution"
    def extract(self, zwave_flow: ZwaveFlow) -> dict:
        classes = [packet.get_class() for packet in zwave_flow.get_forward_packets()]
        return Counter(classes)
    

class FwdMostCommonClass(Feature):
    protocol = Protocols.Zwave
    name = "fwd_most_common_class"
    def extract(self, zwave_flow: ZwaveFlow) -> str:
        classes = [packet.get_class() for packet in zwave_flow.get_forward_packets()]
        return Counter(classes).most_common(1)[0][0] if classes else None


class FwdLeastCommonClass(Feature):
    protocol = Protocols.Zwave
    name = "fwd_least_common_class"    
    def extract(self, zwave_flow: ZwaveFlow) -> str:
        classes = [packet.get_class() for packet in zwave_flow.get_forward_packets()]
        return Counter(classes).most_common()[-1][0] if classes else None


class FwdApplicationUsageFrequency(Feature):
    protocol = Protocols.Zwave
    name = "fwd_application_usage_frequency"
    def extract(self, zwave_flow: ZwaveFlow) -> dict:
        applications = [packet.get_application() for packet in zwave_flow.get_forward_packets()]
        return Counter(applications)


class FwdMostCommonApplication(Feature):
    protocol = Protocols.Zwave
    name = "fwd_most_common_application"
    def extract(self, zwave_flow: ZwaveFlow) -> str:
        applications = [packet.get_application() for packet in zwave_flow.get_forward_packets()]
        return Counter(applications).most_common(1)[0][0] if applications else None


class FwdUniqueApplicationCount(Feature):
    protocol = Protocols.Zwave
    name = "fwd_unique_application_count"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        applications = {packet.get_application() for packet in zwave_flow.get_forward_packets()}
        return len(applications)


class FwdHeaderPatternConsistency(Feature):
    protocol = Protocols.Zwave
    name = "fwd_header_pattern_consistency"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        headers = [packet.get_header() for packet in zwave_flow.get_forward_packets()]
        most_common_count = Counter(headers).most_common(1)[0][1] if headers else 0
        total_headers = len(headers)
        return most_common_count / total_headers if total_headers > 0 else 0


class FwdHeaderComplexity(Feature):
    protocol = Protocols.Zwave
    name = "fwd_header_complexity"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        headers = [packet.get_header() for packet in zwave_flow.get_forward_packets()]
        unique_headers = set(headers)
        total_headers = len(headers)
        return len(unique_headers) / total_headers if total_headers > 0 else 0


class FwdPayloadToHeaderRatio(Feature):
    protocol = Protocols.Zwave
    name = "fwd_payload_size_to_header_size_ratio"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        packets = zwave_flow.get_forward_packets()
        total_payload = sum(packet.get_payload_bytes() for packet in packets)
        total_header = sum(packet.get_header_bytes() for packet in packets)
        return total_payload / total_header if total_header > 0 else 0


class FwdIncrementalDataChange(Feature):
    protocol = Protocols.Zwave
    name = "fwd_incremental_data_change"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        data_fields = [packet.get_payload() for packet in zwave_flow.get_forward_packets() if packet.get_payload()]
        return sum(1 for i in range(1, len(data_fields)) if data_fields[i] != data_fields[i-1])


class FwdHeaderEntropy(Feature):
    protocol = Protocols.Zwave
    name = "fwd_header_entropy"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        headers = [packet.get_header() for packet in zwave_flow.get_forward_packets()]
        header_counts = Counter(headers)
        total = sum(header_counts.values())
        entropy = -sum((count / total) * math.log2(count / total) for count in header_counts.values()) if total > 0 else 0
        return format(entropy, self.floating_point_unit)


class FwdTemporalStabilityOfClassType(Feature):
    protocol = Protocols.Zwave
    name = "fwd_temporal_stability_of_class_type"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        classes = [packet.get_class() for packet in zwave_flow.get_forward_packets()]
        most_common_count = Counter(classes).most_common(1)[0][1] if classes else 0
        total_classes = len(classes)
        return most_common_count / total_classes if total_classes > 0 else 0


class FwdTemporalStabilityOfApplicationType(Feature):
    protocol = Protocols.Zwave
    name = "fwd_temporal_stability_of_application_type"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        applications = [packet.get_application() for packet in zwave_flow.get_forward_packets()]
        most_common_count = Counter(applications).most_common(1)[0][1] if applications else 0
        total_applications = len(applications)
        return most_common_count / total_applications if total_applications > 0 else 0


class FwdDataFieldEntropy(Feature):
    protocol = Protocols.Zwave
    name = "fwd_data_field_entropy"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        data_fields = [packet.get_data() for packet in zwave_flow.get_forward_packets() if packet.get_data()]
        data_field_counts = Counter(data_fields)
        total = sum(data_field_counts.values())
        entropy = -sum((count / total) * math.log2(count / total) for count in data_field_counts.values()) if total > 0 else 0
        return format(entropy, self.floating_point_unit)


class FwdPayloadEntropy(Feature):
    protocol = Protocols.Zwave
    name = "fwd_payload_entropy"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        payloads = [packet.get_payload() for packet in zwave_flow.get_forward_packets() if packet.get_payload()]
        payloads_counts = Counter(payloads)
        total = sum(payloads_counts.values())
        entropy = -sum((count / total) * math.log2(count / total) for count in payloads_counts.values()) if total > 0 else 0
        return format(entropy, self.floating_point_unit)


class FwdCountOfSingleCastPackets(Feature):
    protocol = Protocols.Zwave
    name = "fwd_count_of_single_cast_packets"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        single_casts = [1 for packet in zwave_flow.get_forward_packets() if packet.get_data() == 'SINGLECAST']
        return len(single_casts)


class FwdProportionOfSingleCastPackets(Feature):
    protocol = Protocols.Zwave
    name = "fwd_proportion_of_single_cast_packets"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        total_packets = len(zwave_flow.get_forward_packets())
        single_casts = sum(1 for packet in zwave_flow.get_forward_packets() if packet.get_data() == 'SINGLECAST')
        return (single_casts / total_packets * 100) if total_packets > 0 else 0


class FwdCountOfACKPackets(Feature):
    protocol = Protocols.Zwave
    name = "fwd_count_of_ack_packets"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        return sum(1 for packet in zwave_flow.get_forward_packets() if packet.get_data() == 'TRANSFER_ACKNOWLEDGE')


class FwdProportionOfACKPackets(Feature):
    protocol = Protocols.Zwave
    name = "fwd_proportion_of_ack_packets"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        total_packets = len(zwave_flow.get_forward_packets())
        ack_frames = sum(1 for packet in zwave_flow.get_forward_packets() if packet.get_data() == 'TRANSFER_ACKNOWLEDGE')
        return (ack_frames / total_packets * 100) if total_packets > 0 else 0


class FwdCountOfMulticastPackets(Feature):
    protocol = Protocols.Zwave
    name = "fwd_count_of_multicast_packets"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        return sum(1 for packet in zwave_flow.get_forward_packets() if packet.get_data() == 'MULTICAST')


class FwdProportionOfMulticastPackets(Feature):
    protocol = Protocols.Zwave
    name = "fwd_proportion_of_multicast_packets"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        total_packets = len(zwave_flow.get_forward_packets())
        multicast_frames = sum(1 for packet in zwave_flow.get_forward_packets() if packet.get_data() == 'MULTICAST')
        return (multicast_frames / total_packets * 100) if total_packets > 0 else 0


class FwdCountOfBroadcastPackets(Feature):
    protocol = Protocols.Zwave
    name = "fwd_count_of_broadcast_packets"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        return sum(1 for packet in zwave_flow.get_forward_packets() if packet.get_data() == 'BROADCAST')


class FwdProportionOfBroadcastPackets(Feature):
    protocol = Protocols.Zwave
    name = "fwd_proportion_of_broadcast_packets"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        total_packets = len(zwave_flow.get_forward_packets())
        broadcast_frames = sum(1 for packet in zwave_flow.get_forward_packets() if packet.get_data() == 'BROADCAST')
        return (broadcast_frames / total_packets * 100) if total_packets > 0 else 0


class FwdCountOfExplorerAutoInclusionPackets(Feature):
    protocol = Protocols.Zwave
    name = "fwd_count_of_explorer_autoinclusion_packets"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        return sum(1 for packet in zwave_flow.get_forward_packets() if packet.get_data() == 'EXPLORER_AUTOINCLUSION')


class FwdProportionOfExplorerAutoInclusionPackets(Feature):
    protocol = Protocols.Zwave
    name = "fwd_proportion_of_explorer_autoinclusion_packets"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        total_packets = len(zwave_flow.get_forward_packets())
        explorer_autoinclusion = sum(1 for packet in zwave_flow.get_forward_packets() if packet.get_data() == 'EXPLORER_AUTOINCLUSION')
        return (explorer_autoinclusion / total_packets * 100) if total_packets > 0 else 0


class BwdTotalAcknowledgments(Feature):
    protocol = Protocols.Zwave
    name = "bwd_total_acknowledgments"   
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        return sum(1 for packet in zwave_flow.get_backward_packets() if packet.is_ack())


class BwdProportionAcknowledgedPackets(Feature):
    protocol = Protocols.Zwave
    name = "bwd_proportion_acknowledged_packets"   
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        total_packets = len(zwave_flow.get_backward_packets())
        acknowledged_packets = sum(1 for packet in zwave_flow.get_backward_packets() if packet.is_ack())
        return (acknowledged_packets / total_packets * 100) if total_packets else 0


class BwdTotalCRCErrors(Feature):
    protocol = Protocols.Zwave
    name = "bwd_total_crc_errors"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        return sum(1 for packet in zwave_flow.get_backward_packets() if not packet.is_crc_ok())


class BwdProportionCRCErrors(Feature):
    protocol = Protocols.Zwave
    name = "bwd_proportion_crc_errors"    
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        total_packets = len(zwave_flow.get_backward_packets())
        crc_error_packets = sum(1 for packet in zwave_flow.get_backward_packets() if not packet.is_crc_ok())
        return (crc_error_packets / total_packets * 100) if total_packets else 0


class BwdTotalSubstitutedPackets(Feature):
    protocol = Protocols.Zwave
    name = "bwd_total_substituted_packets"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        return sum(1 for packet in zwave_flow.get_backward_packets() if packet.is_substituted())


class BwdProportionSubstitutedPackets(Feature):
    protocol = Protocols.Zwave
    name = "bwd_proportion_substituted_packets"    
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        total_packets = len(zwave_flow.get_backward_packets())
        substituted_packets = sum(1 for packet in zwave_flow.get_backward_packets() if packet.is_substituted())
        return (substituted_packets / total_packets * 100) if total_packets else 0


class BwdCountPacketsWithUnknownHeaders(Feature):
    protocol = Protocols.Zwave
    name = "bwd_count_packets_with_unknown_headers"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        return sum(1 for packet in zwave_flow.get_backward_packets() if packet.is_unknown_header())


class BwdProportionUnknownHeaderPackets(Feature):
    protocol = Protocols.Zwave
    name = "bwd_proportion_unknown_header_packets"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        total_packets = len(zwave_flow.get_backward_packets())
        unknown_header_packets = sum(1 for packet in zwave_flow.get_backward_packets() if packet.is_unknown_header())
        return (unknown_header_packets / total_packets * 100) if total_packets else 0


class BwdCountWakeupBeams(Feature):
    protocol = Protocols.Zwave
    name = "bwd_count_wakeup_beams"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        return sum(1 for packet in zwave_flow.get_backward_packets() if packet.is_wakeup_beam())


class BwdProportionWakeupBeamPackets(Feature):
    protocol = Protocols.Zwave
    name = "bwd_proportion_wakeup_beam_packets"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        total_packets = len(zwave_flow.get_backward_packets())
        wakeup_beam_packets = sum(1 for packet in zwave_flow.get_backward_packets() if packet.is_wakeup_beam())
        return (wakeup_beam_packets / total_packets * 100) if total_packets else 0


class BwdUniqueHexPatternsCount(Feature):
    protocol = Protocols.Zwave
    name = "bwd_unique_hex_patterns_count"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        hex_patterns = set(packet.get_hex_data() for packet in zwave_flow.get_backward_packets())
        return len(hex_patterns)


class BwdFrequencyOfTopHexPatterns(Feature):
    protocol = Protocols.Zwave
    name = "bwd_frequency_of_top_hex_patterns"
    def extract(self, zwave_flow: ZwaveFlow) -> dict:
        hex_pattern_counts = {}
        for packet in zwave_flow.get_backward_packets():
            hex_data = packet.get_hex_data()
            if hex_data in hex_pattern_counts:
                hex_pattern_counts[hex_data] += 1
            else:
                hex_pattern_counts[hex_data] = 1
        # Return the most frequent patterns, the slicing can be adjusted for more or less patterns
        return dict(sorted(hex_pattern_counts.items(), key=lambda item: item[1], reverse=True)[:5])


class BwdEntropyOfHexData(Feature):
    protocol = Protocols.Zwave
    name = "bwd_entropy_of_hex_data"    
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        hex_pattern_counts = {}
        for packet in zwave_flow.get_backward_packets():
            hex_data = packet.get_hex_data()
            hex_pattern_counts[hex_data] = hex_pattern_counts.get(hex_data, 0) + 1
        total = sum(hex_pattern_counts.values())
        entropy = -sum((count / total) * log2(count / total) for count in hex_pattern_counts.values())
        return entropy

class BwdHexDataPatternLengthVariability(Feature):
    protocol = Protocols.Zwave
    name = "bwd_hex_data_pattern_length_variability"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        from statistics import pstdev
        lengths = [len(packet.get_hex_data()) for packet in zwave_flow.get_backward_packets()]
        return format(pstdev(lengths), self.floating_point_unit) if lengths else 0


class BwdCrossCorrelationSpeedRSSI(Feature):
    protocol = Protocols.Zwave
    name = "bwd_cross_correlation_speed_rssi"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        speeds = [packet.get_speed() for packet in zwave_flow.get_backward_packets()]
        rssis = [packet.get_rssi() for packet in zwave_flow.get_backward_packets()]
        if len(speeds) > 1 and len(rssis) > 1:
            return format(corrcoef(speeds, rssis)[0, 1], self.floating_point_unit)
        return 0  # Return 0 correlation if there's insufficient data


class BwdTimeSeriesAnalysisPacketIntervals(Feature):
    protocol = Protocols.Zwave
    name = "bwd_time_series_analysis_packet_intervals"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        timestamps = [packet.get_timestamp() for packet in zwave_flow.get_backward_packets()]
        if len(timestamps) < 2:
            return 0  # No intervals to analyze
        intervals = [(t2 - t1).total_seconds() for t1, t2 in zip(timestamps[:-1], timestamps[1:])]
        return sum(intervals) / len(intervals)  # Return average interval


class BwdPercentagePacketsPerChannel(Feature):
    protocol = Protocols.Zwave
    name = "bwd_percentage_packets_per_channel"
    def extract(self, zwave_flow: ZwaveFlow) -> dict:
        channels = [packet.get_channel() for packet in zwave_flow.get_backward_packets()]
        channel_count = {}
        total = len(channels)
        for channel in channels:
            channel_count[channel] = channel_count.get(channel, 0) + 1
        return {channel: (count / total * 100) for channel, count in channel_count.items()} if total else {}


class BwdPercentageHighSpeedTransmissions(Feature):
    protocol = Protocols.Zwave
    name = "bwd_percentage_high_speed_transmissions"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        speeds = [packet.get_speed() for packet in zwave_flow.get_backward_packets()]
        high_speed_threshold = 100
        high_speed_count = sum(1 for speed in speeds if speed > high_speed_threshold)
        total_packets = len(speeds)
        return (high_speed_count / total_packets * 100) if total_packets else 0


class BwdTotalLowSignalPackets(Feature):
    protocol = Protocols.Zwave
    name = "bwd_total_low_signal_packets"    
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        return sum(1 for packet in zwave_flow.get_backward_packets() if packet.is_low())


class BwdPercentageLowSignalPackets(Feature):
    protocol = Protocols.Zwave
    name = "bwd_percentage_low_signal_packets"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        total_packets = len(zwave_flow.get_backward_packets())
        low_signal_count = sum(1 for packet in zwave_flow.get_backward_packets() if packet.is_low())
        return (low_signal_count / total_packets * 100) if total_packets else 0


class BwdAverageChannelUsage(Feature):
    protocol = Protocols.Zwave
    name = "bwd_average_channel_usage"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        channels = [packet.get_channel() for packet in zwave_flow.get_backward_packets()]
        channel_counts = Counter(channels)
        return format(mean(list(channel_counts.values())), self.floating_point_unit) if channels else 0

class BwdMostCommonChannel(Feature):
    protocol = Protocols.Zwave
    name = "bwd_most_common_channel"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        channels = [packet.get_channel() for packet in zwave_flow.get_backward_packets()]
        return Counter(channels).most_common(1)[0][0] if channels else None


class BwdLeastCommonChannel(Feature):
    protocol = Protocols.Zwave
    name = "bwd_least_common_channel"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        channels = [packet.get_channel() for packet in zwave_flow.get_backward_packets()]
        return Counter(channels).most_common()[-1][0] if channels else None


class BwdChannelTransitionCount(Feature):
    protocol = Protocols.Zwave
    name = "bwd_channel_transition_count"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        channels = [packet.get_channel() for packet in zwave_flow.get_backward_packets()]
        return sum(1 for i in range(1, len(channels)) if channels[i] != channels[i-1])


class BwdChannelStability(Feature):
    protocol = Protocols.Zwave
    name = "bwd_channel_stability"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        channels = [packet.get_channel() for packet in zwave_flow.get_backward_packets()]
        longest_streak = max(len(list(g)) for k, g in groupby(channels))
        return longest_streak


class BwdEntropyOfChannelUsage(Feature):
    protocol = Protocols.Zwave
    name = "bwd_entropy_of_channel_usage"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        channels = [packet.get_channel() for packet in zwave_flow.get_backward_packets()]
        channel_counts = Counter(channels)
        total = sum(channel_counts.values())
        entropy = -sum((count / total) * math.log2(count / total) for count in channel_counts.values()) if total > 0 else 0
        return entropy


class BwdCommonDataPatterns(Feature):
    protocol = Protocols.Zwave
    name = "bwd_common_data_patterns"
    def extract(self, zwave_flow: ZwaveFlow) -> str:
        data_entries = [packet.get_data() for packet in zwave_flow.get_backward_packets() if packet.get_data()]
        return Counter(data_entries).most_common(1)[0][0] if data_entries else None


class BwdUniqueDataEntries(Feature):
    protocol = Protocols.Zwave
    name = "bwd_unique_data_entries"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        data_entries = {packet.get_data() for packet in zwave_flow.get_backward_packets() if packet.get_data()}
        return len(data_entries)


class BwdClassDistribution(Feature):
    protocol = Protocols.Zwave
    name = "bwd_class_distribution"
    def extract(self, zwave_flow: ZwaveFlow) -> dict:
        classes = [packet.get_class() for packet in zwave_flow.get_backward_packets()]
        return Counter(classes)
    

class BwdMostCommonClass(Feature):
    protocol = Protocols.Zwave
    name = "bwd_most_common_class"
    def extract(self, zwave_flow: ZwaveFlow) -> str:
        classes = [packet.get_class() for packet in zwave_flow.get_backward_packets()]
        return Counter(classes).most_common(1)[0][0] if classes else None


class BwdLeastCommonClass(Feature):
    protocol = Protocols.Zwave
    name = "bwd_least_common_class"    
    def extract(self, zwave_flow: ZwaveFlow) -> str:
        classes = [packet.get_class() for packet in zwave_flow.get_backward_packets()]
        return Counter(classes).most_common()[-1][0] if classes else None


class BwdApplicationUsageFrequency(Feature):
    protocol = Protocols.Zwave
    name = "bwd_application_usage_frequency"
    def extract(self, zwave_flow: ZwaveFlow) -> dict:
        applications = [packet.get_application() for packet in zwave_flow.get_backward_packets()]
        return Counter(applications)


class BwdMostCommonApplication(Feature):
    protocol = Protocols.Zwave
    name = "bwd_most_common_application"
    def extract(self, zwave_flow: ZwaveFlow) -> str:
        applications = [packet.get_application() for packet in zwave_flow.get_backward_packets()]
        return Counter(applications).most_common(1)[0][0] if applications else None


class BwdUniqueApplicationCount(Feature):
    protocol = Protocols.Zwave
    name = "bwd_unique_application_count"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        applications = {packet.get_application() for packet in zwave_flow.get_backward_packets()}
        return len(applications)


class BwdHeaderPatternConsistency(Feature):
    protocol = Protocols.Zwave
    name = "bwd_header_pattern_consistency"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        headers = [packet.get_header() for packet in zwave_flow.get_backward_packets()]
        most_common_count = Counter(headers).most_common(1)[0][1] if headers else 0
        total_headers = len(headers)
        return most_common_count / total_headers if total_headers > 0 else 0


class BwdHeaderComplexity(Feature):
    protocol = Protocols.Zwave
    name = "bwd_header_complexity"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        headers = [packet.get_header() for packet in zwave_flow.get_backward_packets()]
        unique_headers = set(headers)
        total_headers = len(headers)
        return len(unique_headers) / total_headers if total_headers > 0 else 0


class BwdPayloadToHeaderRatio(Feature):
    protocol = Protocols.Zwave
    name = "bwd_payload_size_to_header_size_ratio"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        packets = zwave_flow.get_backward_packets()
        total_payload = sum(packet.get_payload_bytes() for packet in packets)
        total_header = sum(packet.get_header_bytes() for packet in packets)
        return total_payload / total_header if total_header > 0 else 0


class BwdIncrementalDataChange(Feature):
    protocol = Protocols.Zwave
    name = "bwd_incremental_data_change"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        data_fields = [packet.get_payload() for packet in zwave_flow.get_backward_packets() if packet.get_payload()]
        return sum(1 for i in range(1, len(data_fields)) if data_fields[i] != data_fields[i-1])


class BwdHeaderEntropy(Feature):
    protocol = Protocols.Zwave
    name = "bwd_header_entropy"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        headers = [packet.get_header() for packet in zwave_flow.get_backward_packets()]
        header_counts = Counter(headers)
        total = sum(header_counts.values())
        entropy = -sum((count / total) * math.log2(count / total) for count in header_counts.values()) if total > 0 else 0
        return format(entropy, self.floating_point_unit)


class BwdTemporalStabilityOfClassType(Feature):
    protocol = Protocols.Zwave
    name = "bwd_temporal_stability_of_class_type"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        classes = [packet.get_class() for packet in zwave_flow.get_backward_packets()]
        most_common_count = Counter(classes).most_common(1)[0][1] if classes else 0
        total_classes = len(classes)
        return most_common_count / total_classes if total_classes > 0 else 0


class BwdTemporalStabilityOfApplicationType(Feature):
    protocol = Protocols.Zwave
    name = "bwd_temporal_stability_of_application_type"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        applications = [packet.get_application() for packet in zwave_flow.get_backward_packets()]
        most_common_count = Counter(applications).most_common(1)[0][1] if applications else 0
        total_applications = len(applications)
        return most_common_count / total_applications if total_applications > 0 else 0


class BwdDataFieldEntropy(Feature):
    protocol = Protocols.Zwave
    name = "bwd_data_field_entropy"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        data_fields = [packet.get_data() for packet in zwave_flow.get_backward_packets() if packet.get_data()]
        data_field_counts = Counter(data_fields)
        total = sum(data_field_counts.values())
        entropy = -sum((count / total) * math.log2(count / total) for count in data_field_counts.values()) if total > 0 else 0
        return format(entropy, self.floating_point_unit)


class BwdPayloadEntropy(Feature):
    protocol = Protocols.Zwave
    name = "bwd_payload_entropy"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        payloads = [packet.get_payload() for packet in zwave_flow.get_backward_packets() if packet.get_payload()]
        payloads_counts = Counter(payloads)
        total = sum(payloads_counts.values())
        entropy = -sum((count / total) * math.log2(count / total) for count in payloads_counts.values()) if total > 0 else 0
        return format(entropy, self.floating_point_unit)


class BwdCountOfSingleCastPackets(Feature):
    protocol = Protocols.Zwave
    name = "bwd_count_of_single_cast_packets"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        single_casts = [1 for packet in zwave_flow.get_backward_packets() if packet.get_data() == 'SINGLECAST']
        return len(single_casts)


class BwdProportionOfSingleCastPackets(Feature):
    protocol = Protocols.Zwave
    name = "bwd_proportion_of_single_cast_packets"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        total_packets = len(zwave_flow.get_backward_packets())
        single_casts = sum(1 for packet in zwave_flow.get_backward_packets() if packet.get_data() == 'SINGLECAST')
        return (single_casts / total_packets * 100) if total_packets > 0 else 0


class BwdCountOfACKPackets(Feature):
    protocol = Protocols.Zwave
    name = "bwd_count_of_ack_packets"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        return sum(1 for packet in zwave_flow.get_backward_packets() if packet.get_data() == 'TRANSFER_ACKNOWLEDGE')


class BwdProportionOfACKPackets(Feature):
    protocol = Protocols.Zwave
    name = "bwd_proportion_of_ack_packets"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        total_packets = len(zwave_flow.get_backward_packets())
        ack_frames = sum(1 for packet in zwave_flow.get_backward_packets() if packet.get_data() == 'TRANSFER_ACKNOWLEDGE')
        return (ack_frames / total_packets * 100) if total_packets > 0 else 0


class BwdCountOfMulticastPackets(Feature):
    protocol = Protocols.Zwave
    name = "bwd_count_of_multicast_packets"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        return sum(1 for packet in zwave_flow.get_backward_packets() if packet.get_data() == 'MULTICAST')


class BwdProportionOfMulticastPackets(Feature):
    protocol = Protocols.Zwave
    name = "bwd_proportion_of_multicast_packets"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        total_packets = len(zwave_flow.get_backward_packets())
        multicast_frames = sum(1 for packet in zwave_flow.get_backward_packets() if packet.get_data() == 'MULTICAST')
        return (multicast_frames / total_packets * 100) if total_packets > 0 else 0


class BwdCountOfBroadcastPackets(Feature):
    protocol = Protocols.Zwave
    name = "bwd_count_of_broadcast_packets"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        return sum(1 for packet in zwave_flow.get_backward_packets() if packet.get_data() == 'BROADCAST')


class BwdProportionOfBroadcastPackets(Feature):
    protocol = Protocols.Zwave
    name = "bwd_proportion_of_broadcast_packets"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        total_packets = len(zwave_flow.get_backward_packets())
        broadcast_frames = sum(1 for packet in zwave_flow.get_backward_packets() if packet.get_data() == 'BROADCAST')
        return (broadcast_frames / total_packets * 100) if total_packets > 0 else 0


class BwdCountOfExplorerAutoInclusionPackets(Feature):
    protocol = Protocols.Zwave
    name = "bwd_count_of_explorer_autoinclusion_packets"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        return sum(1 for packet in zwave_flow.get_backward_packets() if packet.get_data() == 'EXPLORER_AUTOINCLUSION')


class BwdProportionOfExplorerAutoInclusionPackets(Feature):
    protocol = Protocols.Zwave
    name = "bwd_proportion_of_explorer_autoinclusion_packets"
    def extract(self, zwave_flow: ZwaveFlow) -> float:
        total_packets = len(zwave_flow.get_backward_packets())
        explorer_autoinclusion = sum(1 for packet in zwave_flow.get_backward_packets() if packet.get_data() == 'EXPLORER_AUTOINCLUSION')
        return (explorer_autoinclusion / total_packets * 100) if total_packets > 0 else 0