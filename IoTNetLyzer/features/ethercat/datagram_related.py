#!/usr/bin/env python3

import statistics
from scipy import stats
from collections import Counter
from ...pipe_capturer import Pipe
from ...pipe_capturer.pipes import EtherCatPipe
from ...pipe_capturer import Packet
from ...pipe_capturer.packets import EtherCatPacket
from ..feature import Feature
from ...protocols import Protocols
from typing import Set


class EtherCATNumberOfUniqueCommands(Feature):
    protocol = Protocols.EtherCAT
    name = "number_of_unique_commands"
    def extract(self, pipe: Pipe) -> int:
        commands = {packet.get_command() for packet in pipe.get_packets()}
        return len(commands)


class EtherCATUniqueCommands(Feature):
    protocol = Protocols.EtherCAT
    name = "unique_commands"
    def extract(self, pipe: Pipe) -> Set[str]:
        return {packet.get_command() for packet in pipe.get_packets()}


class EtherCATNumberOfNOPCommands(Feature):
    protocol = Protocols.EtherCAT
    name = "number_of_NOP_commands"
    def extract(self, pipe: Pipe) -> Set[str]:
        NOP_command_code = 0
        return sum(1 for packet in pipe.get_packets() if packet.get_command() == NOP_command_code)


class EtherCATNumberOfAPRDCommands(Feature):
    protocol = Protocols.EtherCAT
    name = "number_of_APRD_commands"
    def extract(self, pipe: Pipe) -> Set[str]:
        APRD_command_code = 1
        return sum(1 for packet in pipe.get_packets() if packet.get_command() == APRD_command_code)


class EtherCATNumberOfAPWRCommands(Feature):
    protocol = Protocols.EtherCAT
    name = "number_of_APWR_commands"
    def extract(self, pipe: Pipe) -> Set[str]:
        APWR_command_code = 2
        return sum(1 for packet in pipe.get_packets() if packet.get_command() == APWR_command_code)


class EtherCATNumberOfAPRWCommands(Feature):
    protocol = Protocols.EtherCAT
    name = "number_of_APRW_commands"
    def extract(self, pipe: Pipe) -> Set[str]:
        APRW_command_code = 3
        return sum(1 for packet in pipe.get_packets() if packet.get_command() == APRW_command_code)


class EtherCATNumberOfFPRDCommands(Feature):
    protocol = Protocols.EtherCAT
    name = "number_of_FPRD_commands"
    def extract(self, pipe: Pipe) -> Set[str]:
        FPRD_command_code = 4
        return sum(1 for packet in pipe.get_packets() if packet.get_command() == FPRD_command_code)


class EtherCATNumberOfFPWRCommands(Feature):
    protocol = Protocols.EtherCAT
    name = "number_of_FPWR_commands"
    def extract(self, pipe: Pipe) -> Set[str]:
        FPWR_command_code = 5
        return sum(1 for packet in pipe.get_packets() if packet.get_command() == FPWR_command_code)


class EtherCATNumberOfFPRWCommands(Feature):
    protocol = Protocols.EtherCAT
    name = "number_of_FPRW_commands"
    def extract(self, pipe: Pipe) -> Set[str]:
        FPRW_command_code = 6
        return sum(1 for packet in pipe.get_packets() if packet.get_command() == FPRW_command_code)


class EtherCATNumberOfBRDCommands(Feature):
    protocol = Protocols.EtherCAT
    name = "number_of_BRD_commands"
    def extract(self, pipe: Pipe) -> Set[str]:
        BRD_command_code = 7
        return sum(1 for packet in pipe.get_packets() if packet.get_command() == BRD_command_code)


class EtherCATNumberOfBWRCommands(Feature):
    protocol = Protocols.EtherCAT
    name = "number_of_BWR_commands"
    def extract(self, pipe: Pipe) -> Set[str]:
        BWR_command_code = 8
        return sum(1 for packet in pipe.get_packets() if packet.get_command() == BWR_command_code)


class EtherCATNumberOfBRWCommands(Feature):
    protocol = Protocols.EtherCAT
    name = "number_of_BRW_commands"
    def extract(self, pipe: Pipe) -> Set[str]:
        BRW_command_code = 9
        return sum(1 for packet in pipe.get_packets() if packet.get_command() == BRW_command_code)


class EtherCATNumberOfLRDCommands(Feature):
    protocol = Protocols.EtherCAT
    name = "number_of_LRD_commands"
    def extract(self, pipe: Pipe) -> Set[str]:
        LRD_command_code = 10
        return sum(1 for packet in pipe.get_packets() if packet.get_command() == LRD_command_code)


class EtherCATNumberOfLWRCommands(Feature):
    protocol = Protocols.EtherCAT
    name = "number_of_LWR_commands"
    def extract(self, pipe: Pipe) -> Set[str]:
        LWR_command_code = 11
        return sum(1 for packet in pipe.get_packets() if packet.get_command() == LWR_command_code)


class EtherCATNumberOfLRWCommands(Feature):
    protocol = Protocols.EtherCAT
    name = "number_of_LRW_commands"
    def extract(self, pipe: Pipe) -> Set[str]:
        LRW_command_code = 12
        return sum(1 for packet in pipe.get_packets() if packet.get_command() == LRW_command_code)


class EtherCATNumberOfARMWCommands(Feature):
    protocol = Protocols.EtherCAT
    name = "number_of_ARMW_commands"
    def extract(self, pipe: Pipe) -> Set[str]:
        ARMW_command_code = 13
        return sum(1 for packet in pipe.get_packets() if packet.get_command() == ARMW_command_code)



class EtherCATNumberOfDuplicateIndices(Feature):
    protocol = Protocols.EtherCAT
    name = "number_of_duplicate_indices"
    def extract(self, pipe: Pipe) -> int:
        indices = [packet.get_index() for packet in pipe.get_packets()]
        counted = Counter(indices)
        number_of_duplicate_indices = [value for value, frequency in counted.items() if frequency > 1]
        return number_of_duplicate_indices


class EtherCATNumberOfCirculatingDatagrams(Feature):
    protocol = Protocols.EtherCAT
    name = "number_of_circulating_datagrams"
    def extract(self, pipe: Pipe) -> int:
        return sum(1 for packet in pipe.get_packets() if packet.get_circulating() == 1)


class EtherCATNumberOfCirculatingDatagrams(Feature):
    protocol = Protocols.EtherCAT
    name = "number_of_not_circulating_datagrams"
    def extract(self, pipe: Pipe) -> int:
        return sum(1 for packet in pipe.get_packets() if packet.get_circulating() == 0)


class EtherCATNumberOfLastDatagrams(Feature):
    protocol = Protocols.EtherCAT
    name = "number_of_last_datagrams"
    def extract(self, pipe: Pipe) -> int:
        return sum(1 for packet in pipe.get_packets() if packet.get_next() == 0)


class EtherCATNumberOfNotLastDatagrams(Feature):
    protocol = Protocols.EtherCAT
    name = "number_of_not_last_datagrams"
    def extract(self, pipe: Pipe) -> int:
        return sum(1 for packet in pipe.get_packets() if packet.get_next() == 1)


class EtherCATUniqueInterruptRequestsValues(Feature):
    protocol = Protocols.EtherCAT
    name = "unique_interrupt_request_values"
    def extract(self, pipe: Pipe) -> int:
        return {packet.get_interupt_request() for packet in pipe.get_packets()}


class EtherCATUniqueWorkingCounterValues(Feature):
    protocol = Protocols.EtherCAT
    name = "unique_working_counter_values"
    def extract(self, pipe: Pipe) -> int:
        return {packet.get_working_counter() for packet in pipe.get_packets()}


class EtherCATDataValues(Feature):
    protocol = Protocols.EtherCAT
    name = "data_values"
    def extract(self, pipe: Pipe) -> int:
        return [packet.get_data() for packet in pipe.get_packets()]