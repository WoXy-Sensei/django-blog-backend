# Generated by Django 4.2.4 on 2023-08-28 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_comment_level_comment_lft_comment_parent_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(blank=None, null=None, on_delete=django.db.models.deletion.CASCADE, to='posts.post'),
        ),
    ]