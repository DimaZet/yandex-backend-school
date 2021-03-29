from enum import Enum

from mongoengine import *

from swagger_server.models import CourierItem
from swagger_server.repository.validator import Validator


class Courier(Document):
    class CourierType(Enum):
        FOOT = "foot"
        BIKE = "bike"
        CAR = "car"

    COURIER_TYPE_WEIGHTS = {
        CourierType.FOOT: 10,
        CourierType.BIKE: 15,
        CourierType.CAR: 50,
    }

    COURIER_EARNINGS_MULTIPLY = {
        CourierType.FOOT: 2,
        CourierType.BIKE: 5,
        CourierType.CAR: 9,
    }

    mongo_id = IntField(primary_key=True)
    courier_type = EnumField(CourierType)
    regions = ListField(field=IntField(validation=Validator.is_positive_number))
    working_hours = ListField(field=StringField(regex="^\\d{2}:\\d{2}-\\d{2}:\\d{2}$"))
    assign_time = DateTimeField(null=True)#, default=datetime.datetime.utcnow())
    last_delivered_time = DateTimeField(null=True)#, default=datetime.datetime.utcnow())

    @staticmethod
    def from_dto(c):
        assert isinstance(c, CourierItem)
        created = Courier()
        created.mongo_id = c.courier_id
        created.courier_type = c.courier_type
        created.regions = c.regions
        created.working_hours = c.working_hours
        return created
