#!/usr/bin/env python3

from enum import Enum

class Protocols(Enum):
    Zwave = "Zwave"
    EtherCAT = "EtherCAT"
    ZigBee = "ZigBee"
    MQTT = "MQTT"

    def __str__(self):
        return self.value