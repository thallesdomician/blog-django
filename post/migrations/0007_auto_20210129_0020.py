# Generated by Django 2.2.17 on 2021-01-29 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_auto_20210128_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='header_image',
            field=models.ImageField(blank=True, default='default_thumbnail.jpg', null=True, upload_to='header/%Y/%m/'),
        ),
    ]
