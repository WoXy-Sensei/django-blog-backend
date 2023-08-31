from django.core.exceptions import ValidationError
from datetime import date

def validate_age(value):
    today = date.today()
    birthdate = value
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    if age < 18:
        raise ValidationError(
            (f"user must be at least 18 years"),
        )