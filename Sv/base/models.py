from unicodedata import name
from django.db import models

# Create your models here.
class doctor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    time = models.CharField(max_length=20)

    def __str__(self):
       return f"{self.id},{self.name},{self.time}"

    
class customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    def __str__(self):
       return f"{self.id},{self.name},{self.phone}"
class registererForm(models.Model):
    id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    doctor = models.CharField(max_length=20)
    schedule = models.CharField(max_length=20)
    def __str__(self):
       return f"{self.id},{self.customer_name},{self.phone},{self.doctor},{self.schedule}"
