# Generated by Django 2.2.17 on 2021-01-28 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20210128_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='slug', editable=False, max_length=100, unique=True),
        ),
    ]