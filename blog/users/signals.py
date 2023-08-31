from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import CustomUser,Profile


@receiver(post_save, sender=CustomUser)
def user_activated(sender, instance,created, **kwargs):
    if instance.is_active and instance.first_login:
        Profile.objects.create(user=instance)
        instance.first_login = False
        instance.save()
