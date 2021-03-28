# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.courier_get_response import CourierGetResponse  # noqa: E501
from swagger_server.models.courier_item import CourierItem  # noqa: E501
from swagger_server.models.courier_update_request import CourierUpdateRequest  # noqa: E501
from swagger_server.models.couriers_ids import CouriersIds  # noqa: E501
from swagger_server.models.couriers_post_request import CouriersPostRequest  # noqa: E501
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.inline_response400 import InlineResponse400  # noqa: E501
from swagger_server.models.inline_response4001 import InlineResponse4001  # noqa: E501
from swagger_server.models.orders_assign_post_request import OrdersAssignPostRequest  # noqa: E501
from swagger_server.models.orders_complete_post_request import OrdersCompletePostRequest  # noqa: E501
from swagger_server.models.orders_complete_post_response import OrdersCompletePostResponse  # noqa: E501
from swagger_server.models.orders_ids import OrdersIds  # noqa: E501
from swagger_server.models.orders_post_request import OrdersPostRequest  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_couriers_courier_id_get(self):
        """Test case for couriers_courier_id_get

        
        """
        response = self.client.open(
            '/couriers/{courier_id}'.format(courier_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_couriers_courier_id_patch(self):
        """Test case for couriers_courier_id_patch

        
        """
        body = CourierUpdateRequest()
        response = self.client.open(
            '/couriers/{courier_id}'.format(courier_id=56),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_couriers_post(self):
        """Test case for couriers_post

        
        """
        body = CouriersPostRequest()
        response = self.client.open(
            '/couriers',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_orders_assign_post(self):
        """Test case for orders_assign_post

        
        """
        body = OrdersAssignPostRequest()
        response = self.client.open(
            '/orders/assign',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_orders_complete_post(self):
        """Test case for orders_complete_post

        
        """
        body = OrdersCompletePostRequest()
        response = self.client.open(
            '/orders/complete',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_orders_post(self):
        """Test case for orders_post

        
        """
        body = OrdersPostRequest()
        response = self.client.open(
            '/orders',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
