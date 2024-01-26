# Generated by Django 4.2.7 on 2023-12-19 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_company', models.CharField(choices=[('suzuki', 'Suzuki'), ('honda', 'Honda'), ('toyota', 'Toyota'), ('other', 'Other')], max_length=100)),
                ('car_model', models.CharField(max_length=100)),
                ('car_year', models.PositiveIntegerField(choices=[(2001, '2001'), (2002, '2002'), (2003, '2003'), (2004, '2004'), (2005, '2005'), (2006, '2006'), (2007, '2007'), (2008, '2008'), (2009, '2009'), (2010, '2010'), (2011, '2011'), (2012, '2012'), (2013, '2013'), (2014, '2014'), (2015, '2015'), (2016, '2016'), (2017, '2017'), (2018, '2018'), (2019, '2019'), (2020, '2020'), (2021, '2021'), (2022, '2022')])),
                ('transmission_type', models.CharField(choices=[('automatic', 'Automatic'), ('manual', 'Manual'), ('semi-automatic', 'Semi-Automatic')], max_length=15)),
                ('car_city', models.CharField(choices=[('rawalpindi', 'Rawalpindi'), ('islamabad', 'Islamabad'), ('karachi', 'Karachi'), ('lahore', 'Lahore'), ('faisalabad', 'Faisalabad'), ('peshawar', 'Peshawar')], max_length=100)),
                ('car_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('car_description', models.TextField()),
            ],
        ),
    ]
