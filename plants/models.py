from django.db import models


# Create your models here.
class Plants(models.Model):
    name = models.CharField(verbose_name="Plant's name", max_length=200)
    last_water = models.DateTimeField()
    next_water = models.DateField()

    def __str__(self):
        return self.name


# test
