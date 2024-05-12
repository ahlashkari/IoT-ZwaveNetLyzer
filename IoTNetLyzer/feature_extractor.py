#!/usr/bin/env python3

from datetime import datetime
from typing import List
from .features.ethercat import *
from .protocols import Protocols
from .pipe_capturer import Pipe


class FeatureExtractor:
    """A class to extract related features for each protocol from a given list of pipes."""

    @staticmethod
    def execute(pipes: List[Pipe], floating_point_unit: str, features_ignore_list: List = [],
                label: str = "") -> List:
        """
        Extract features from a list of pipes.

        Args:
            pipes: A list of Pipe objects to extract features from.
            floating_point_unit: A string indicating the unit to use for floating-point features.
            features_ignore_list: A list of feature names to ignore during extraction.
            label: A string label to assign to all extracted features.

        Returns:
            A list of dictionaries representing the extracted features, one for each Pipe object in `pipes`.
        """

        features = {
            Protocols.EtherCAT: [
                EtherCATDuration(),
                PacketsCount(),
                EtherCATHeaderBytesRate(),
                EtherCATPayloadBytesRate(),
                EtherCATPacketLenRate(),
                EtherCatPacketsRate(),
                EtherCATMaxHeaderBytes(),
                EtherCATTotalHeaderBytes(),
                EtherCATMinHeaderBytes(),
                EtherCATMeanHeaderBytes(),
                EtherCATModeHeaderBytes(),
                EtherCATVarianceHeaderBytes(),
                EtherCATStandardDeviationHeaderBytes(),
                EtherCATMedianHeaderBytes(),
                EtherCATSkewnessHeaderBytes(),
                EtherCATCoefficientOfVariationHeaderBytes(),
                EtherCATMaxPayloadBytes(),
                EtherCATTotalPayloadBytes(),
                EtherCATMinPayloadBytes(),
                EtherCATMeanPayloadBytes(),
                EtherCATModePayloadBytes(),
                EtherCATVariancePayloadBytes(),
                EtherCATStandardDeviationPayloadBytes(),
                EtherCATMedianPayloadBytes(),
                EtherCATSkewnessPayloadBytes(),
                EtherCATCoefficientOfVariationPayloadBytes(),
                EtherCATMaxPacketLen(),
                EtherCATTotalPacketLen(),
                EtherCATMinPacketLen(),
                EtherCATMeanPacketLen(),
                EtherCATModePacketLen(),
                EtherCATVariancePacketLen(),
                EtherCATStandardDeviationPacketLen(),
                EtherCATMedianPacketLen(),
                EtherCATSkewnessPacketLen(),
                EtherCATCoefficientOfVariationPacketLen(),
                EtherCATMaxPacketsTimeDelta(),
                EtherCATMinPacketsTimeDelta(),
                EtherCATMeanPacketsTimeDelta(),
                EtherCATModePacketsTimeDelta(),
                EtherCATVariancePacketsTimeDelta(),
                EtherCATStandardDeviationPacketsTimeDelta(),
                EtherCATMedianPacketsTimeDelta(),
                EtherCATSkewnessPacketsTimeDelta(),
                EtherCATCoefficientOfVariationPacketsTimeDelta(),
                EtherCATTotalDataLen(),
                EtherCATMaxDataLen(),
                EtherCATMinDataLen(),
                EtherCATMeanDataLen(),
                EtherCATModeDataLen(),
                EtherCATVarianceDataLen(),
                EtherCATStandardDeviationDataLen(),
                EtherCATMedianDataLen(),
                EtherCATSkewnessDataLen(),
                EtherCATCoefficientOfVariationDataLen(),
                EtherCATNumberOfUniqueCommands(),
                EtherCATUniqueCommands(),
                EtherCATNumberOfNOPCommands(),
                EtherCATNumberOfAPRDCommands(),
                EtherCATNumberOfAPWRCommands(),
                EtherCATNumberOfAPRWCommands(),
                EtherCATNumberOfFPRDCommands(),
                EtherCATNumberOfFPWRCommands(),
                EtherCATNumberOfFPRWCommands(),
                EtherCATNumberOfBRDCommands(),
                EtherCATNumberOfBWRCommands(),
                EtherCATNumberOfBRWCommands(),
                EtherCATNumberOfLRDCommands(),
                EtherCATNumberOfLWRCommands(),
                EtherCATNumberOfLRWCommands(),
                EtherCATNumberOfARMWCommands(),
                EtherCATNumberOfDuplicateIndices(),
                EtherCATNumberOfCirculatingDatagrams(),
                EtherCATNumberOfCirculatingDatagrams(),
                EtherCATNumberOfLastDatagrams(),
                EtherCATNumberOfNotLastDatagrams(),
                EtherCATUniqueInterruptRequestsValues(),
                EtherCATUniqueWorkingCounterValues(),
                # EtherCATDataValues(),
            ]
        }

        extracted_data = {
            Protocols.EtherCAT: []
        }
        for pipe in pipes:
            features_of_pipe = {
                "pipe_id": str(pipe),
                "timestamp": str(pipe.get_timestamp()),
                "protocol": str(pipe.get_protocol()),
                "label": label
            }

            for feature in features[pipe.get_protocol()]:
                if feature.name in features_ignore_list:
                    continue
                feature.set_floating_point_unit(floating_point_unit)
                features_of_pipe[feature.name] = feature.extract(pipe)

            extracted_data[pipe.get_protocol()].append(features_of_pipe)

        return extracted_data
