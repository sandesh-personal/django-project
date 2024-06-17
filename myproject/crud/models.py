from django.db import models

# Create your models here.
class Classroom(models.Model):
    name = models.CharField(max_length=20)
    section = models.CharField(max_length=5)
    
class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=50)
    
class Teachers(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=50)