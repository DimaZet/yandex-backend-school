# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class AssignTime(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, assign_time: str=None):  # noqa: E501
        """AssignTime - a model defined in Swagger

        :param assign_time: The assign_time of this AssignTime.  # noqa: E501
        :type assign_time: str
        """
        self.swagger_types = {
            'assign_time': str
        }

        self.attribute_map = {
            'assign_time': 'assign_time'
        }
        self._assign_time = assign_time

    @classmethod
    def from_dict(cls, dikt) -> 'AssignTime':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AssignTime of this AssignTime.  # noqa: E501
        :rtype: AssignTime
        """
        return util.deserialize_model(dikt, cls)

    @property
    def assign_time(self) -> str:
        """Gets the assign_time of this AssignTime.


        :return: The assign_time of this AssignTime.
        :rtype: str
        """
        return self._assign_time

    @assign_time.setter
    def assign_time(self, assign_time: str):
        """Sets the assign_time of this AssignTime.


        :param assign_time: The assign_time of this AssignTime.
        :type assign_time: str
        """

        self._assign_time = assign_time
