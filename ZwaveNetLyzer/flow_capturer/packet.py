#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import List
from ..protocols import Protocols


class Packet(ABC):
    """Abstract base class for packets"""
    protocol: Protocols
    header_bytes: int
    payload_bytes: int
    packet_len: int
    _timestamp: str

    @abstractmethod
    def get_possible_flow_ids() -> List[str]:
        """Get the possible IDs of the flow that the packet belongs to"""
        pass
    
    def get_protocol(self):
        """Get the IoT protocol of the packet"""
        return self.protocol
    
    def get_timestamp(self):
        """Get the timestamp of the packet"""
        return self._timestamp
    
    def __len__(self):
        """Get the length of the packet"""
        return self.header_bytes + self.payload_bytes
    
    def get_header_bytes(self):
        """Get the header size of the packet"""
        return self.header_bytes

    def get_payload_bytes(self):
        """Get the payload size of the packet"""
        return self.payload_bytes
    
    def get_packet_len(self):
        """Get the whole size of the packets"""
        return self.header_bytes + self.payload_bytes
