# Generated by Django 4.2.4 on 2023-09-05 15:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0022_alter_profile_biography_alter_profile_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='recommended_by',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='recommended_user', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='ref_code',
            field=models.CharField(blank=True, max_length=12),
        ),
    ]