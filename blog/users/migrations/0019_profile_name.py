# Generated by Django 4.2.4 on 2023-08-30 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_customuser_first_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(default='bardia ramez', max_length=50),
            preserve_default=False,
        ),
    ]