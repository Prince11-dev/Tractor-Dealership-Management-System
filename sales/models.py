from django.db import models
from customers.models import Customer
from inventory.models import Tractor

class Sale(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    tractor = models.ForeignKey(Tractor, on_delete=models.CASCADE)
    sale_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.customer} - {self.tractor}"

# Create your models here.
