# Generated by Django 4.2.7 on 2023-12-19 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_ad_seller'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='car_picture',
            field=models.ImageField(blank=True, null=True, upload_to='car_pictures/'),
        ),
    ]
