# Generated by Django 4.2.4 on 2023-08-28 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='slug', editable=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=150, unique=True),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('content', models.TextField()),
                ('publish_date', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='posts.post')),
            ],
        ),
    ]
