from django.db import models
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator


# Create your models here.
class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(130)])
    heart_rate = models.IntegerField(
        default=50, validators=[MinValueValidator(1), MaxValueValidator(280)]
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} is {self.age} years old."
