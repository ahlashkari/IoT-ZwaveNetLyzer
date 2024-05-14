#!/usr/bin/env python3

from ...pipe_capturer.pipes import ZwaveFlow
from ..feature import Feature
from ...protocols import Protocols


class ZwaveNumberOfUniqueCommands(Feature):
    protocol = Protocols.Zwave
    name = "number_of_unique_commands"
    def extract(self, zwave_flow: ZwaveFlow) -> int:
        commands = {packet.get_command() for packet in zwave_flow.get_packets()}
        return len(commands)
