#!/usr/bin/env python3

from typing import List
from ..pipe_capturer.packet import Packet

def packets_delta_time_calculation(packets: List[Packet]):
    packets_time = [packet.get_timestamp() for packet in packets]
    if len(packets_time) == 1:
        return [-1]
    sorted_packets_time = sorted(packets_time)
    packets_time_delta = [(pkt - pkt_prev).total_seconds() for pkt_prev, pkt in
                            zip(sorted_packets_time[:-1], sorted_packets_time[1:])]
    return packets_time_delta
