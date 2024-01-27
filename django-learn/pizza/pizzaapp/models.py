from django.db import models

# Create your models here.
class PizzaModel(models.Model):
    name=models.CharField(max_length=20)
    price=models.CharField(max_length=10)

class OrderModel(models.Model):
    username=models.CharField(max_length=10)
    phone=models.CharField(max_length=10)
    address=models.CharField(max_length=200)
    ordereditems=models.CharField(max_length=500)
    status=models.CharField(max_length=20)