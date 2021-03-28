from collections import defaultdict
from datetime import datetime, timedelta

from dateutil import parser
from jsonschema import ValidationError
from werkzeug.exceptions import NotFound, BadRequest

from swagger_server.models import InlineResponse200, CouriersIdsCouriers, OrdersCompletePostResponse
from swagger_server.repository.courier import Courier
from swagger_server.repository.orders import Order


def is_compatible_weight(courier_type: Courier.CourierType, weight: float):
    return Courier.COURIER_TYPE_WEIGHTS[courier_type] >= weight


def is_compatible_times(working_hours: Courier.working_hours, delivery_hours: Order.delivery_hours):
    for dh in delivery_hours:
        d_from, d_to = dh.split('-')
        for wh in working_hours:
            w_from, w_to = wh.split('-')
            if w_from <= d_to <= w_to or w_from <= d_from <= w_to:
                return True
    return False


def get_courier_statistic(courier_id):
    rating = None
    earnings = None
    courier = get_courier_or_throw_404(courier_id)
    kwargs = {}
    if courier.assign_time is not None:
        kwargs = {"delivery_end_time__lt": courier.assign_time}
    orders = Order.objects(
        assigned_to=courier.mongo_id,
        status=Order.OrderStatus.COMPLETED,
        **kwargs
    )
    if len(orders) > 0:
        earnings = 0
        orders_by_region = defaultdict(lambda: (timedelta(), 0))
        for o in orders:
            c = Courier.COURIER_EARNINGS_MULTIPLY[o.taken_by]
            earnings += c * 500
            summ, count = orders_by_region[o.region]
            summ += o.delivery_end_time - o.delivery_start_time
            count += 1
            orders_by_region[o.region] = (summ, count)
        t = min([s_c[0].total_seconds() / s_c[1] for region, s_c in orders_by_region.items()])
        rating = (60 * 60 - min(t, 60 * 60)) / (60 * 60) * 5
    return rating, earnings


def get_courier_or_throw_404(courier_id):
    courier = Courier.objects(mongo_id=courier_id).first()
    if courier is None:
        raise NotFound(description=f"not found courier with id {courier_id}")
    return courier


def get_order_or_throw_404(order_id):
    order = Order.objects(mongo_id=order_id).first()
    if order is None:
        raise NotFound(description=f"not found order with id {order_id}")
    return order


def orders_after_patch(courier_id):
    courier = get_courier_or_throw_404(courier_id)
    if courier.assign_time is not None:
        orders = get_assigned_orders(courier_id)
        unassigned_count = 0
        for o in orders:
            if not (is_compatible_weight(courier.courier_type, o.weight) and
                    is_compatible_times(courier.working_hours, o.delivery_hours) and
                    o.region in courier.regions):
                o.status = Order.OrderStatus.UNASSIGNED
                o.assigned_to = None
                o.taken_by = None
                o.save()
                unassigned_count += 1
        if len(orders) == unassigned_count:
            courier.assign_time = None
            courier.last_delivered_time = None
            courier.save()


def get_assigned_orders(courier_id):
    return Order.objects(status=Order.OrderStatus.ASSIGNED, assigned_to=courier_id)


def get_assigned_orders_count(courier_id):
    return Order.objects(status=Order.OrderStatus.ASSIGNED, assigned_to=courier_id).count()


def orders_assign(courier_id):
    courier = get_courier_or_throw_404(courier_id)
    orders = get_assigned_orders(courier_id)
    if len(orders) > 0:
        return InlineResponse200(
            assign_time=str(courier.assign_time),
            orders=[CouriersIdsCouriers(id=o.mongo_id) for o in orders]
        )
    orders = list(filter(
        lambda o: is_compatible_weight(courier.courier_type, o.weight),
        Order.objects(
            status=Order.OrderStatus.UNASSIGNED,
            region__in=courier.regions)))
    orders = list(filter(
        lambda o: is_compatible_times(courier.working_hours, o.delivery_hours),
        orders))
    if len(orders) > 0:
        for o in orders:
            o.status = Order.OrderStatus.ASSIGNED
            o.assigned_to = courier.mongo_id
            o.taken_by = courier.courier_type
            o.save()
        courier.assign_time = datetime.utcnow()
        courier.save()
        return InlineResponse200(
            assign_time=str(courier.assign_time),
            orders=[CouriersIdsCouriers(id=o.mongo_id) for o in orders]
        )
    else:
        return InlineResponse200()


def orders_complete(courier_id, order_id, complete_time):
    try:
        complete_time = parser.parse(complete_time)
    except Exception as e:
        raise BadRequest(description=f"bad complete_time format: {e}")
    try:
        courier = get_courier_or_throw_404(courier_id)
        order = get_order_or_throw_404(order_id)
    except NotFound as nf:
        raise BadRequest(description=nf.description)
    if order.assigned_to != courier.mongo_id:
        raise BadRequest(f"order with id {order_id} unassigned on courier with id {courier_id}")
    if order.status == order.OrderStatus.ASSIGNED:
        if courier.last_delivered_time is None:
            courier.last_delivered_time = courier.assign_time
            courier.save()
        order.delivery_start_time = courier.last_delivered_time
        order.delivery_end_time = complete_time
        order.status = Order.OrderStatus.COMPLETED
        order.save()

        courier.last_delivered_time = complete_time
        courier.save()

        if get_assigned_orders_count(courier_id) == 0:
            courier.last_delivered_time = None
            courier.assign_time = None
            courier.save()
    return OrdersCompletePostResponse(order_id=order_id)
