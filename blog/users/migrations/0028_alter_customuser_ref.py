# Generated by Django 4.2.4 on 2023-09-05 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0027_alter_customuser_ref'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='ref',
            field=models.CharField(max_length=12, null=True),
        ),
    ]
