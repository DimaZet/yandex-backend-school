import connexion
from flask import Response

from swagger_server.models.courier_get_response import CourierGetResponse  # noqa: E501
from swagger_server.models.courier_item import CourierItem  # noqa: E501
from swagger_server.models.courier_update_request import CourierUpdateRequest  # noqa: E501
from swagger_server.models.couriers_ids import CouriersIds  # noqa: E501
from swagger_server.models.couriers_post_request import CouriersPostRequest  # noqa: E501
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.orders_assign_post_request import OrdersAssignPostRequest  # noqa: E501
from swagger_server.models.orders_complete_post_request import OrdersCompletePostRequest  # noqa: E501
from swagger_server.models.orders_complete_post_response import OrdersCompletePostResponse  # noqa: E501
from swagger_server.models.orders_ids import OrdersIds  # noqa: E501
from swagger_server.models.orders_post_request import OrdersPostRequest  # noqa: E501
from swagger_server.service.mega_service import *


def couriers_courier_id_get(courier_id):  # noqa: E501
    """couriers_courier_id_get

    Get courier info # noqa: E501

    :param courier_id: 
    :type courier_id: int

    :rtype: CourierGetResponse
    """
    courier = get_courier_or_throw_404(courier_id)
    rating, earnings = get_courier_statistic(courier_id, courier.assign_time)
    return CourierGetResponse(
        courier.mongo_id,
        courier.courier_type.value,
        courier.regions,
        courier.working_hours,
        rating=rating,
        earnings=earnings
    )


def couriers_courier_id_patch(courier_id, body=None):  # noqa: E501
    """couriers_courier_id_patch

    Update courier by id # noqa: E501

    :param courier_id: 
    :type courier_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: CourierItem
    """
    if connexion.request.is_json:
        body = CourierUpdateRequest.from_dict(connexion.request.get_json())  # noqa: E501
        courier = get_courier_or_throw_404(courier_id)
        body = {k: v for k, v in body.to_dict().items() if v is not None}
        if len(body) > 0:
            for k, v in body.items():
                setattr(courier, k, v)
            courier.save()
            if courier.assign_time is not None:
                orders_after_patch(courier.mongo_id)
        return CourierItem(
            courier.mongo_id,
            courier.courier_type.value,
            courier.regions,
            courier.working_hours
        )
    raise BadRequest


def couriers_post(body=None):  # noqa: E501
    """couriers_post

    Import couriers # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: CouriersIds
    """

    if connexion.request.is_json:
        body = CouriersPostRequest.from_dict(connexion.request.get_json())  # noqa: E501
        couriers_models = list(map(Courier.from_dto, body.data))
        for c in couriers_models:
            c.save()
        return Response(CouriersIds(couriers=[CouriersIdsCouriers(id=c.mongo_id) for c in couriers_models]).to_str(), 201)
    raise BadRequest


def orders_assign_post(body=None):  # noqa: E501
    """orders_assign_post

    Assign orders to a courier by id # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse200
    """

    if connexion.request.is_json:
        body = OrdersAssignPostRequest.from_dict(connexion.request.get_json())  # noqa: E501
        return orders_assign(body.courier_id)
    raise BadRequest


def orders_complete_post(body=None):  # noqa: E501
    """orders_complete_post

    Marks orders as completed # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: OrdersCompletePostResponse
    """
    if connexion.request.is_json:
        body = OrdersCompletePostRequest.from_dict(connexion.request.get_json())  # noqa: E501
        return orders_complete(body.courier_id, body.order_id, body.complete_time)
    raise BadRequest


def orders_post(body=None):  # noqa: E501
    """orders_post

    Import orders # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: OrdersIds
    """
    if connexion.request.is_json:
        body = OrdersPostRequest.from_dict(connexion.request.get_json())  # noqa: E501
        orders_models = list(map(Order.from_dto, body.data))
        for o in orders_models:
            o.save()
        return Response(OrdersIds(orders=[CouriersIdsCouriers(id=o.mongo_id) for o in orders_models]).to_str(), 201)
    raise BadRequest
