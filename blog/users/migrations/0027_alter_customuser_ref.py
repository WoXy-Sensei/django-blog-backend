# Generated by Django 4.2.4 on 2023-09-05 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0026_rename_ref_code_customuser_ref_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='ref',
            field=models.CharField(blank=None, max_length=12, null=None),
        ),
    ]
