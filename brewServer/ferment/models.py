from django.db import models

class Data(models.Model):
    brew_name = models.CharField(max_length=100)
    #Store numbers up to 9999 with two decimal places
    temperature = models.DecimalField(max_digits=6, decimal_places=2)
    time = models.DateTimeField()

class Recipe(models.Model):
    recipe_name = models.CharField(max_length=100)
    recipe_style = models.CharField(max_length=100)

class BrewSession(models.Model):
    brew_date = models.DateField()
    bottle_date = models.DateField()
