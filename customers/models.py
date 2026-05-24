from django.db import models

class Customer(models.Model):
    customer_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    village = models.CharField(max_length=100)

    def __str__(self):
        return self.customer_name

# Create your models here.
