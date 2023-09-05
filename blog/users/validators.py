from django.core.exceptions import ValidationError
from datetime import date
from django.apps import apps

def validate_age(value):
    today = date.today()
    birthdate = value
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    if age < 18:
        raise ValidationError(
            (f"user must be at least 18 years"),
        )
    
def validate_ref_code(value):
    if value != None:
        try:
            ProfileModel = apps.get_model('users', 'Profile')
            ProfileModel.objects.get(ref_code = value)
        except ProfileModel.DoesNotExist:
            raise ValidationError("Reference code did not match any user",400)