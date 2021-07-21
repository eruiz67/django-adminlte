import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
#from django.core.validators import  MaxValueValidator, MinValueValidator, RegexValidator


def present_or_future_date(value):
    if value > datetime.date.today():
        raise ValidationError("La fecha no puede estar en el futuro")
    return value


def past_date(value):
    if value < datetime.date.today():
        raise ValidationError("La fecha no puede estar en el pasado")
    return value
