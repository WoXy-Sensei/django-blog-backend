# Generated by Django 4.2.4 on 2023-09-05 19:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0025_remove_profile_recommended_by_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='ref_code',
            new_name='ref',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='recommended_by',
        ),
        migrations.AddField(
            model_name='profile',
            name='recommended_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recommended_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='profile',
            name='ref_code',
            field=models.CharField(blank=True, max_length=12),
        ),
    ]
