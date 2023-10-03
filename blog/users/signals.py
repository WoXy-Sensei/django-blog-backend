from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import CustomUser,Profile


@receiver(post_save, sender=CustomUser)
def user_activated(sender, instance,created, **kwargs):
    if instance.is_active and instance.first_login:
        profile = Profile.objects.create(user=instance)
        if instance.ref != None:
            user = Profile.objects.get(ref_code = instance.ref).user
            profile.recommended_by = user
            profile.save()
        
        instance.first_login = False
        instance.save() 
    