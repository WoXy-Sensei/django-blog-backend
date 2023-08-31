# Generated by Django 4.2.4 on 2023-08-30 09:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_profile_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='slug',
        ),
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.CharField(default='bardia', editable=False, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
