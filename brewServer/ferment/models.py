from django.db import models

# Create your models here.
class Data(models.Model):
    brew_name = models.CharField(max_length=100)
    #Store numbers up to 9999 with two decimal places
    temperature = models.DecimalField(max_digits=6, decimal_places=2)
    time = models.TimeField()
