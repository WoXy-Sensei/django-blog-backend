# Generated by Django 4.2.4 on 2023-08-30 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_remove_customuser_birth_day_customuser_birthdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='first_login',
            field=models.BooleanField(default=True),
        ),
    ]
