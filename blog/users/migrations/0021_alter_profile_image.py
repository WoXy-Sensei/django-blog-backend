# Generated by Django 4.2.4 on 2023-08-30 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_remove_profile_slug_profile_username_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='default/profile.png', null=True, upload_to='profiles/'),
        ),
    ]
