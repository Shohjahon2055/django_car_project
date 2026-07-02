from django.db import models

# Create your models here.

class Car(models.Model):
    brand = models.CharField(max_length=100)
    model_name = models.CharField(max_length=100)
    year = models.IntegerField()
    color = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    engine_type = models.CharField(max_length=50)
    horsepower = models.IntegerField()
    mileage = models.IntegerField()
    fuel_type = models.CharField(max_length=30)
    transmission = models.CharField(max_length=30)
    is_available = models.BooleanField(default=True)
    vin_number = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100)
    release_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.brand} {self.model_name}"
