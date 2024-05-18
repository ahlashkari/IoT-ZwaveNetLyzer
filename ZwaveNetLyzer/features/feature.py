#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Union
from ..pipe_capturer import Pipe
from ..protocols import Protocols

class Feature(ABC):
    """Abstract base class for feature extraction."""
    name: str
    protocol: Protocols
    floating_point_unit: str

    @abstractmethod
    def extract(self, pipe: Pipe) -> Union[float, int, str]:
        """
        Abstract method to extract a feature value from a given pipe. Subclasses must override this method
        to provide a custom implementation of feature extraction for each defined feature.

        Args:
            pipe (Pipe): The pipe from which the feature value is extracted.

        Returns:
            The extracted feature value, which can be a float, integer, or string.
        """
        pass

    def set_floating_point_unit(self, floating_point_unit: str) -> None:
        """Sets the floating point unit for the feature."""
        self.floating_point_unit = floating_point_unit
