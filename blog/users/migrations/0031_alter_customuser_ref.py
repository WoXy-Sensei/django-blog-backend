# Generated by Django 4.2.4 on 2023-09-05 20:38

from django.db import migrations, models
import users.validators


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0030_alter_customuser_ref'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='ref',
            field=models.CharField(blank=True, max_length=12, null=True, validators=[users.validators.validate_ref_code]),
        ),
    ]