import re

from mongoengine import ValidationError


class Validator:
    @staticmethod
    def is_positive_number(number):
        if not number > 0:
            raise ValidationError

    @staticmethod
    def is_duration_between_HH_MM(duration: str):
        if re.fullmatch(r'^\d{2}:\d{2}-\d{2}:\d{2}$', duration) is None:
            raise ValidationError
