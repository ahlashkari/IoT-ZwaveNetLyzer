#!/usr/bin/env python3

from ..pipe_capturer import Pipe

def packets_delta_time_calculation(pipe: Pipe):
    packets_time = [packet.get_timestamp() for packet in pipe.get_packets()]
    if len(packets_time) == 1:
        return [-1]
    sorted_packets_time = sorted(packets_time)
    packets_time_delta = [(pkt - pkt_prev).total_seconds() for pkt_prev, pkt in
                            zip(sorted_packets_time[:-1], sorted_packets_time[1:])]
    return packets_time_delta
