# Generated by Django 4.2.4 on 2023-08-29 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='birth_day',
        ),
        migrations.AddField(
            model_name='customuser',
            name='birth_day',
            field=models.DateField(blank=True, null=True),
        ),
    ]