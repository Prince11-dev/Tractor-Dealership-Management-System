from django.db import models

class Tractor(models.Model):

    tractor_name = models.CharField(max_length=100)
    model_no = models.CharField(max_length=50)
    company_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    horsepower = models.IntegerField()

    stock_quantity = models.IntegerField(default=0)

    STOCK_CHOICES = [
        ('Available','Available'),
        ('Low Stock','Low Stock'),
        ('Out of Stock','Out of Stock')
    ]

    stock_status = models.CharField(
        max_length=20,
        choices=STOCK_CHOICES,
        default='Available'
    )

    def __str__(self):
        return self.tractor_name