# Generated by Django 4.2.4 on 2023-08-29 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_remove_customuser_birth_day'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='birth_day',
            field=models.CharField(default='1', max_length=50),
        ),
    ]
