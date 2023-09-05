# Generated by Django 4.2.4 on 2023-09-05 17:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0024_alter_profile_recommended_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='recommended_by',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='ref_code',
        ),
        migrations.AddField(
            model_name='customuser',
            name='recommended_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recommended_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='customuser',
            name='ref_code',
            field=models.CharField(blank=True, max_length=12),
        ),
    ]
