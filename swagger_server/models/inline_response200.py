# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.assign_time import AssignTime  # noqa: F401,E501
from swagger_server.models.couriers_ids_couriers import CouriersIdsCouriers  # noqa: F401,E501
from swagger_server.models.orders_ids import OrdersIds  # noqa: F401,E501
from swagger_server import util


class InlineResponse200(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, assign_time: str=None, orders: List[CouriersIdsCouriers]=None):  # noqa: E501
        """InlineResponse200 - a model defined in Swagger

        :param assign_time: The assign_time of this InlineResponse200.  # noqa: E501
        :type assign_time: str
        :param orders: The orders of this InlineResponse200.  # noqa: E501
        :type orders: List[CouriersIdsCouriers]
        """
        self.swagger_types = {
            'assign_time': str,
            'orders': List[CouriersIdsCouriers]
        }

        self.attribute_map = {
            'assign_time': 'assign_time',
            'orders': 'orders'
        }
        self._assign_time = assign_time
        self._orders = orders

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse200':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200 of this InlineResponse200.  # noqa: E501
        :rtype: InlineResponse200
        """
        return util.deserialize_model(dikt, cls)

    @property
    def assign_time(self) -> str:
        """Gets the assign_time of this InlineResponse200.


        :return: The assign_time of this InlineResponse200.
        :rtype: str
        """
        return self._assign_time

    @assign_time.setter
    def assign_time(self, assign_time: str):
        """Sets the assign_time of this InlineResponse200.


        :param assign_time: The assign_time of this InlineResponse200.
        :type assign_time: str
        """

        self._assign_time = assign_time

    @property
    def orders(self) -> List[CouriersIdsCouriers]:
        """Gets the orders of this InlineResponse200.


        :return: The orders of this InlineResponse200.
        :rtype: List[CouriersIdsCouriers]
        """
        return self._orders

    @orders.setter
    def orders(self, orders: List[CouriersIdsCouriers]):
        """Sets the orders of this InlineResponse200.


        :param orders: The orders of this InlineResponse200.
        :type orders: List[CouriersIdsCouriers]
        """
        if orders is None:
            raise ValueError("Invalid value for `orders`, must not be `None`")  # noqa: E501

        self._orders = orders
