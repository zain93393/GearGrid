# Generated by Django 4.2.7 on 2023-12-24 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_remove_ad_car_picture_ad_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
