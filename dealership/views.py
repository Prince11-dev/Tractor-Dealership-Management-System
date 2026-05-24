from django.shortcuts import render
from customers.models import Customer
from inventory.models import Tractor
from sales.models import Sale

def home(request):
    customer_count = Customer.objects.count()
    tractor_count = Tractor.objects.count()
    sales_count = Sale.objects.count()

    context = {
        'customer_count': customer_count,
        'tractor_count': tractor_count,
        'sales_count': sales_count,
    }

    return render(request, 'home.html', context)