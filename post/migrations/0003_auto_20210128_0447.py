# Generated by Django 2.2.17 on 2021-01-28 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20210128_0441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='slug', max_length=100, unique=True),
        ),
    ]