# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.courier_item import CourierItem  # noqa: F401,E501
from swagger_server import util


class CouriersPostRequest(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, data: List[CourierItem]=None):  # noqa: E501
        """CouriersPostRequest - a model defined in Swagger

        :param data: The data of this CouriersPostRequest.  # noqa: E501
        :type data: List[CourierItem]
        """
        self.swagger_types = {
            'data': List[CourierItem]
        }

        self.attribute_map = {
            'data': 'data'
        }
        self._data = data

    @classmethod
    def from_dict(cls, dikt) -> 'CouriersPostRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CouriersPostRequest of this CouriersPostRequest.  # noqa: E501
        :rtype: CouriersPostRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self) -> List[CourierItem]:
        """Gets the data of this CouriersPostRequest.


        :return: The data of this CouriersPostRequest.
        :rtype: List[CourierItem]
        """
        return self._data

    @data.setter
    def data(self, data: List[CourierItem]):
        """Sets the data of this CouriersPostRequest.


        :param data: The data of this CouriersPostRequest.
        :type data: List[CourierItem]
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data
