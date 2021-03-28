from collections import defaultdict

from swagger_server.models import InlineResponse400, CouriersIdsAP, OrdersIdsAP, \
    InlineResponse4001


class ValidationException(Exception):
    def __hash__(self):
        return hash(self.__class__.__name__)

    def __eq__(self, other):
        return self.__class__.__name__ == other.__class__.__name__


class InvalidCouriersException(ValidationException):
    def __init__(self, invalid_list, *args, **kwargs):
        super().__init__(args, kwargs)
        self.invalid_list = invalid_list


class InvalidOrdersException(ValidationException):
    def __init__(self, invalid_list, *args, **kwargs):
        super().__init__(args, kwargs)
        self.invalid_list = invalid_list


def invalid_couriers_exception_handler(exception: InvalidCouriersException):
    c = CouriersIdsAP.from_dict({
        "couriers": [{"id": id, "cause_of": '; '.join(cause_of)} for id, cause_of in exception.invalid_list]
    })
    return InlineResponse400(validation_error=c).to_str(), 400


def invalid_orders_exception_handler(exception: InvalidOrdersException):
    c = OrdersIdsAP.from_dict({
        "orders": [{"id": id, "cause_of": '; '.join(cause_of)} for id, cause_of in exception.invalid_list]
    })
    return InlineResponse4001(validation_error=c).to_str(), 400


def produce_exception(data, errors, id_field, exception):
    errors = [(list(e.absolute_path), e.message) for e in errors if len(e.absolute_path) >= 2]
    errors = [(data[path[0]][path[1]][id_field], message) for path, message in errors]
    result = defaultdict(list)
    for id, message in errors:
        result[id].append(message)
    raise exception(result.items())


def invalid_couriers_exception_producer(data, errors):
    produce_exception(data, errors, 'courier_id', InvalidCouriersException)


def invalid_orders_exception_producer(data, errors):
    produce_exception(data, errors, 'order_id', InvalidCouriersException)


EXCEPTION_HANDLERS = {
    InvalidCouriersException: invalid_couriers_exception_handler,
    InvalidOrdersException:   invalid_orders_exception_handler,
}

EXCEPTION_PRODUCERS = {
    'couriers': invalid_couriers_exception_producer,
    'orders':   invalid_orders_exception_producer,
}
