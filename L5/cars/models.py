from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Review(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    stars = models.IntegerField(
        default=5, validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    review = models.TextField()

    def __str__(self):
        return self.first_name + " " + self.last_name
