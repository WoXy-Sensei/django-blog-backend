from djoser.signals import user_activated
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import CustomUser,Profile


@receiver(user_activated)
def user_activated_signal(sender, user, request, **kwargs):
    print("activated")
    if user.is_active and user.first_login:
        profile = Profile.objects.create(user=user)
        if user.ref is not None:
            user = Profile.objects.get(ref_code=user.ref).user
            profile.recommended_by = user
            profile.save()
        
        user.first_login = False
        user.save() 
    