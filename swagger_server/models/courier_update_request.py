# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class CourierUpdateRequest(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, courier_type: str=None, regions: List[int]=None, working_hours: List[str]=None):  # noqa: E501
        """CourierUpdateRequest - a model defined in Swagger

        :param courier_type: The courier_type of this CourierUpdateRequest.  # noqa: E501
        :type courier_type: str
        :param regions: The regions of this CourierUpdateRequest.  # noqa: E501
        :type regions: List[int]
        :param working_hours: The working_hours of this CourierUpdateRequest.  # noqa: E501
        :type working_hours: List[str]
        """
        self.swagger_types = {
            'courier_type': str,
            'regions': List[int],
            'working_hours': List[str]
        }

        self.attribute_map = {
            'courier_type': 'courier_type',
            'regions': 'regions',
            'working_hours': 'working_hours'
        }
        self._courier_type = courier_type
        self._regions = regions
        self._working_hours = working_hours

    @classmethod
    def from_dict(cls, dikt) -> 'CourierUpdateRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CourierUpdateRequest of this CourierUpdateRequest.  # noqa: E501
        :rtype: CourierUpdateRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def courier_type(self) -> str:
        """Gets the courier_type of this CourierUpdateRequest.


        :return: The courier_type of this CourierUpdateRequest.
        :rtype: str
        """
        return self._courier_type

    @courier_type.setter
    def courier_type(self, courier_type: str):
        """Sets the courier_type of this CourierUpdateRequest.


        :param courier_type: The courier_type of this CourierUpdateRequest.
        :type courier_type: str
        """
        allowed_values = ["foot", "bike", "car"]  # noqa: E501
        if courier_type not in allowed_values:
            raise ValueError(
                "Invalid value for `courier_type` ({0}), must be one of {1}"
                .format(courier_type, allowed_values)
            )

        self._courier_type = courier_type

    @property
    def regions(self) -> List[int]:
        """Gets the regions of this CourierUpdateRequest.


        :return: The regions of this CourierUpdateRequest.
        :rtype: List[int]
        """
        return self._regions

    @regions.setter
    def regions(self, regions: List[int]):
        """Sets the regions of this CourierUpdateRequest.


        :param regions: The regions of this CourierUpdateRequest.
        :type regions: List[int]
        """

        self._regions = regions

    @property
    def working_hours(self) -> List[str]:
        """Gets the working_hours of this CourierUpdateRequest.


        :return: The working_hours of this CourierUpdateRequest.
        :rtype: List[str]
        """
        return self._working_hours

    @working_hours.setter
    def working_hours(self, working_hours: List[str]):
        """Sets the working_hours of this CourierUpdateRequest.


        :param working_hours: The working_hours of this CourierUpdateRequest.
        :type working_hours: List[str]
        """

        self._working_hours = working_hours
