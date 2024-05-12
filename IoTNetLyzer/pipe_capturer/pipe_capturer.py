#!/usr/bin/env python3

import csv

from scapy.all import PcapReader
from ..config_loader import ConfigLoader, ZwaveConfigLoader
from .packet import Packet
from .packet_factory import PacketFactory
from .pipe_factory import PipeFactory
from .pipe import Pipe
from typing import List

import os

class PipeCapturer:
    """A class that captures packets from a pcap file and creates pipes."""

    def __init__(self, config: ConfigLoader):
        self.finished_pipes: List[Pipe] = []
        self.ongoing_pipes = {}
        self.config = config
        self.pipes_counter = 0

    def process_packets(self, packet_reader):
        packet_counter = 0
        for packet in packet_reader:
            packet_counter += 1
            iot_netlyzer_packet = PacketFactory.create(packet_info=packet)
            self.add_packet_to_pipe(iot_netlyzer_packet)
            if packet_counter % self.config.read_packets_count_value_log_info == 0:
                    print(f">> {packet_counter} number of packets has been processed so far...")

        print(f">> End of reading from {self.config.pcap_file_address}")
        print(f">> {packet_counter} packets analyzed in total.")
        print(f">> {self.pipes_counter} pipes created in total.")
        print(">> Preparing the output file...")

        list_of_ongoing_pipes = list(self.ongoing_pipes.values())
        self.finished_pipes.extend(list_of_ongoing_pipes)
        return self.finished_pipes

    def capture(self) -> List[Pipe]:
        """
        Captures packets, creates pipes, and returns the list of finished pipes.

        Returns:
            list: A list of finished Pipe objects.
        """
        raise NotImplementedError("capture method must be implemented by subclasses")

    def add_packet_to_pipe(self, packets: List[Packet]) -> None:
        """
        Adds each packet to an ongoing pipe or creates a new pipe if no ongoing pipe is found.

        Args:
            packets (List[Packet]): The list of Packet objects to add to ongoing pipes.

        Returns:
            None
        """
        for packet in packets:
            pipe_id = packet.get_possible_pipe_id()
            if pipe_id not in self.ongoing_pipes:
                self.create_new_pipe(packet=packet, pipe_id=pipe_id)
                continue

            pipe: Pipe = self.ongoing_pipes[pipe_id]
            if pipe.is_ended(new_packet_timestamp=packet.get_timestamp()):
                self.finished_pipes.append(pipe)
                del self.ongoing_pipes[pipe_id]
                self.create_new_pipe(packet=packet, pipe_id=pipe_id)
                continue

            pipe.add_packet(packet)

    def create_new_pipe(self, packet: Packet, pipe_id: str) -> None:
        """
        Creates a new Pipe object with the specified packet and adds it to the ongoing pipes dictionary.

        Args:
            packet (Packet): The Packet object to create the new Pipe with.
            pipe_id (str): The ID of the pipe.

        Returns:
            None
        """
        self.pipes_counter += 1
        new_pipe = PipeFactory.create(packet=packet, config=self.config)
        self.ongoing_pipes[pipe_id] = new_pipe


class ZwaveFlowCapturer(PipeCapturer):
    def __init__(self, zwave_config: ZwaveConfigLoader):
        super().__init__(zwave_config)

    def capture(self) -> List[Pipe]:
        with open(self.config.input_file, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=';')
            return self.process_packets(csv_reader)


class EtherCatFlowCapturer(PipeCapturer):
    def __init__(self, config: ConfigLoader):
        super().__init__(config)

    def capture(self) -> List[Pipe]:
        with open(self.config.pcap_file_address, 'rb') as f:
            pcap_reader = PcapReader(f)
            return self.process_packets(pcap_reader)