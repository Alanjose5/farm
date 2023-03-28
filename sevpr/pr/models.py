from django.db import models


# Create your models here.
class farmer(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to="image")
    designation = models.TextField()


class farm(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to="imag")
    date = models.DateField(null=True)
class cli(models.Model):
    image = models.ImageField(upload_to="img")
    spe = models.TextField()
    name = models.CharField(max_length=400)