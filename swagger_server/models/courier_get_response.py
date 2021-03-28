# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class CourierGetResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, courier_id: int=None, courier_type: str=None, regions: List[int]=None, working_hours: List[str]=None, rating: float=None, earnings: int=None):  # noqa: E501
        """CourierGetResponse - a model defined in Swagger

        :param courier_id: The courier_id of this CourierGetResponse.  # noqa: E501
        :type courier_id: int
        :param courier_type: The courier_type of this CourierGetResponse.  # noqa: E501
        :type courier_type: str
        :param regions: The regions of this CourierGetResponse.  # noqa: E501
        :type regions: List[int]
        :param working_hours: The working_hours of this CourierGetResponse.  # noqa: E501
        :type working_hours: List[str]
        :param rating: The rating of this CourierGetResponse.  # noqa: E501
        :type rating: float
        :param earnings: The earnings of this CourierGetResponse.  # noqa: E501
        :type earnings: int
        """
        self.swagger_types = {
            'courier_id': int,
            'courier_type': str,
            'regions': List[int],
            'working_hours': List[str],
            'rating': float,
            'earnings': int
        }

        self.attribute_map = {
            'courier_id': 'courier_id',
            'courier_type': 'courier_type',
            'regions': 'regions',
            'working_hours': 'working_hours',
            'rating': 'rating',
            'earnings': 'earnings'
        }
        self._courier_id = courier_id
        self._courier_type = courier_type
        self._regions = regions
        self._working_hours = working_hours
        self._rating = rating
        self._earnings = earnings

    @classmethod
    def from_dict(cls, dikt) -> 'CourierGetResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CourierGetResponse of this CourierGetResponse.  # noqa: E501
        :rtype: CourierGetResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def courier_id(self) -> int:
        """Gets the courier_id of this CourierGetResponse.


        :return: The courier_id of this CourierGetResponse.
        :rtype: int
        """
        return self._courier_id

    @courier_id.setter
    def courier_id(self, courier_id: int):
        """Sets the courier_id of this CourierGetResponse.


        :param courier_id: The courier_id of this CourierGetResponse.
        :type courier_id: int
        """
        if courier_id is None:
            raise ValueError("Invalid value for `courier_id`, must not be `None`")  # noqa: E501

        self._courier_id = courier_id

    @property
    def courier_type(self) -> str:
        """Gets the courier_type of this CourierGetResponse.


        :return: The courier_type of this CourierGetResponse.
        :rtype: str
        """
        return self._courier_type

    @courier_type.setter
    def courier_type(self, courier_type: str):
        """Sets the courier_type of this CourierGetResponse.


        :param courier_type: The courier_type of this CourierGetResponse.
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
        """Gets the regions of this CourierGetResponse.


        :return: The regions of this CourierGetResponse.
        :rtype: List[int]
        """
        return self._regions

    @regions.setter
    def regions(self, regions: List[int]):
        """Sets the regions of this CourierGetResponse.


        :param regions: The regions of this CourierGetResponse.
        :type regions: List[int]
        """
        if regions is None:
            raise ValueError("Invalid value for `regions`, must not be `None`")  # noqa: E501

        self._regions = regions

    @property
    def working_hours(self) -> List[str]:
        """Gets the working_hours of this CourierGetResponse.


        :return: The working_hours of this CourierGetResponse.
        :rtype: List[str]
        """
        return self._working_hours

    @working_hours.setter
    def working_hours(self, working_hours: List[str]):
        """Sets the working_hours of this CourierGetResponse.


        :param working_hours: The working_hours of this CourierGetResponse.
        :type working_hours: List[str]
        """
        if working_hours is None:
            raise ValueError("Invalid value for `working_hours`, must not be `None`")  # noqa: E501

        self._working_hours = working_hours

    @property
    def rating(self) -> float:
        """Gets the rating of this CourierGetResponse.


        :return: The rating of this CourierGetResponse.
        :rtype: float
        """
        return self._rating

    @rating.setter
    def rating(self, rating: float):
        """Sets the rating of this CourierGetResponse.


        :param rating: The rating of this CourierGetResponse.
        :type rating: float
        """

        self._rating = rating

    @property
    def earnings(self) -> int:
        """Gets the earnings of this CourierGetResponse.


        :return: The earnings of this CourierGetResponse.
        :rtype: int
        """
        return self._earnings

    @earnings.setter
    def earnings(self, earnings: int):
        """Sets the earnings of this CourierGetResponse.


        :param earnings: The earnings of this CourierGetResponse.
        :type earnings: int
        """
        if earnings is None:
            raise ValueError("Invalid value for `earnings`, must not be `None`")  # noqa: E501

        self._earnings = earnings
