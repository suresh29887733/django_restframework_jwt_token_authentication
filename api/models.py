from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    village=models.CharField(max_length=200)