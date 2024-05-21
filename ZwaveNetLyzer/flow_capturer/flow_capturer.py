#!/usr/bin/env python3

import csv
import os

from ..config_loader import ConfigLoader, ZwaveConfigLoader
from .packet import Packet
from .packet_factory import PacketFactory
from .flow_factory import FlowFactory
from .flow import Flow
from typing import List

class FlowCapturer:
    """
    A class that captures packets from an input file and creates flows.

    Args:
        config (ConfigLoader): The configuration loader for packet capturing.
    """

    def __init__(self, config: ConfigLoader):
        self.finished_flows: List[Flow] = []
        self.ongoing_flows = {}
        self.config = config
        self.flows_counter = 0

    def process_packets(self, packet_reader):
        """
        Processes packets from the packet reader and adds them to flows.

        Args:
            packet_reader: An iterable reader that provides packets.

        Returns:
            list: A list of finished Flow objects.
        """
        packet_counter = 0
        for packet in packet_reader:
            packet_counter += 1
            iot_netlyzer_packet = PacketFactory.create(raw_packet=packet)
            self.add_packet_to_flow(iot_netlyzer_packet)
            if packet_counter % self.config.read_packets_count_value_log_info == 0:
                    print(f">> {packet_counter} number of packets has been processed so far...")

        print(f">> End of reading from {self.config.input_file_address}")
        print(f">> {packet_counter} packets analyzed in total.")
        print(f">> {self.flows_counter} flows created in total.")
        print(">> Preparing the output file...")

        list_of_ongoing_flows = list(self.ongoing_flows.values())
        self.finished_flows.extend(list_of_ongoing_flows)
        return self.finished_flows

    def capture(self) -> List[Flow]:
        """
        Captures packets, creates flows, and returns the list of finished flows.

        Returns:
            list: A list of finished Flow objects.
        """
        raise NotImplementedError("capture method must be implemented by subclasses")

    def add_packet_to_flow(self, packets: List[Packet]) -> None:
        """
        Adds each packet to an ongoing flow or creates a new flow if no ongoing flow is found.

        Args:
            packets (List[Packet]): The list of Packet objects to add to ongoing flows.

        Returns:
            None
        """
        for packet in packets:
            possible_flow_ids = packet.get_possible_flow_ids()
            flow_id = possible_flow_ids[0]
            alternative_flow_id = possible_flow_ids[1]
            if flow_id not in self.ongoing_flows:
                if alternative_flow_id not in self.ongoing_flows:
                    self.create_new_flow(packet=packet, flow_id=flow_id)
                    continue
                flow_id = alternative_flow_id

            flow: Flow = self.ongoing_flows[flow_id]
            if flow.is_ended(new_packet_timestamp=packet.get_timestamp()):
                self.finished_flows.append(flow)
                del self.ongoing_flows[flow_id]
                self.create_new_flow(packet=packet, flow_id=flow_id)
                continue

            flow.add_packet(packet)

    def create_new_flow(self, packet: Packet, flow_id: str) -> None:
        """
        Creates a new Flow object with the specified packet and adds it to the ongoing flows dictionary.

        Args:
            packet (Packet): The Packet object to create the new Flow with.
            flow_id (str): The ID of the flow.

        Returns:
            None
        """
        self.flows_counter += 1
        new_flow = FlowFactory.create(packet=packet, config=self.config)
        self.ongoing_flows[flow_id] = new_flow


class ZwaveFlowCapturer(FlowCapturer):
    """
    A class to capture and process Z-Wave packets.

    Args:
        zwave_config (ZwaveConfigLoader): The configuration loader specific to Z-Wave.
    """

    def __init__(self, zwave_config: ZwaveConfigLoader):
        super().__init__(zwave_config)

    def capture(self) -> List[Flow]:
        """
        Capture Z-Wave packets from a CSV file and process them into flows.

        Returns:
            list: A list of finished Flow objects.
        """
        with open(self.config.input_file_address, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=';')
            return self.process_packets(csv_reader)