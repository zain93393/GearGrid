from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class Ad(models.Model):
    CAR_TRANSMISSION_CHOICES = [
        ('automatic', 'Automatic'),
        ('manual', 'Manual'),
        ('semi-automatic', 'Semi-Automatic'),
    ]

    CAR_COMPANY_CHOICES = [
        ('suzuki', 'Suzuki'),
        ('honda', 'Honda'),
        ('toyota', 'Toyota'),
        ('other', 'Other'),
    ]

    CAR_YEAR_CHOICES = [(year, str(year)) for year in range(2001, 2023)]

    CAR_CITY_CHOICES = [
        ('rawalpindi', 'Rawalpindi'),
        ('islamabad', 'Islamabad'),
        ('karachi', 'Karachi'),
        ('lahore', 'Lahore'),
        ('faisalabad', 'Faisalabad'),
        ('peshawar', 'Peshawar'),
    ]

    SELLER_NUMBER_REGEX = '^03\d{2}-\d{7}$'
    seller_number_validator = RegexValidator(
        regex=SELLER_NUMBER_REGEX,
        message='Enter a valid seller number. Example: 0316-5336290'
    )


    id = models.AutoField(primary_key=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    car_company = models.CharField(max_length=100, choices=CAR_COMPANY_CHOICES)
    car_model = models.CharField(max_length=100)
    car_year = models.PositiveIntegerField(choices=CAR_YEAR_CHOICES)
    transmission_type = models.CharField(max_length=15, choices=CAR_TRANSMISSION_CHOICES)
    car_city = models.CharField(max_length=100, choices=CAR_CITY_CHOICES)
    car_price = models.DecimalField(max_digits=10, decimal_places=2)
    car_description = models.TextField()
    seller_number = models.CharField(max_length=12, validators=[seller_number_validator])
    image = models.ImageField(default='default.jpg',upload_to='car_pictures/', blank=True, null=True)

    def __str__(self):
        return f"{self.car_year} {self.get_car_company_display()} {self.car_model}"