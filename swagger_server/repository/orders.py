from enum import Enum, auto

from mongoengine import *

from swagger_server import db
from swagger_server.models import OrderItem
from swagger_server.repository.courier import Courier
from swagger_server.repository.validator import Validator


class Order(db.Document):
    class OrderStatus(Enum):
        UNASSIGNED = "UNASSIGNED"
        ASSIGNED = "ASSIGNED"
        COMPLETED = "COMPLETED"

    mongo_id = IntField(primary_key=True)
    weight = FloatField(validation=Validator.is_positive_number)
    region = IntField(validation=Validator.is_positive_number)
    delivery_hours = ListField(field=StringField(regex="^\\d{2}:\\d{2}-\\d{2}:\\d{2}$"))
    status = EnumField(OrderStatus, default=OrderStatus.UNASSIGNED)
    assigned_to = IntField(null=True, default=None)
    delivery_start_time = DateTimeField(null=True)
    delivery_end_time = DateTimeField(null=True)
    taken_by = EnumField(Courier.CourierType, null=True)

    def to_dto(self):
        return OrderItem(
            order_id=self.mongo_id,
            weight=self.weight,
            region=self.region,
            delivery_hours=self.delivery_hours,
        )

    @staticmethod
    def from_dto(c):
        assert isinstance(c, OrderItem)
        created = Order()
        created.mongo_id = c.order_id
        created.weight = c.weight
        created.region = c.region
        created.delivery_hours = c.delivery_hours
        return created
