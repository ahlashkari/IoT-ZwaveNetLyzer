#!/usr/bin/env python3

from enum import Enum

class Protocols(Enum):
    EtherCAT = "EtherCAT"
    ZigBee = "ZigBee"
    Zwave = "Zwave"
    MQTT = "MQTT"

    def __str__(self):
        return self.value