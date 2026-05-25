from django.shortcuts import render, redirect
from .models import Sale
from customers.models import Customer
from inventory.models import Tractor

def sales_list(request):
    sales = Sale.objects.all()

    context = {
        'sales': sales
    }

    return render(request,'sales.html',context)


def add_sale(request):

    customers = Customer.objects.all()
    tractors = Tractor.objects.all()

    if request.method=="POST":

        customer = Customer.objects.get(
            id=request.POST['customer']
        )

        tractor = Tractor.objects.get(
            id=request.POST['tractor']
        )

        sale_date=request.POST['sale_date']
        amount=request.POST['amount']

        Sale.objects.create(
            customer=customer,
            tractor=tractor,
            sale_date=sale_date,
            amount=amount
        )

        return redirect('sales')

    context={
        'customers':customers,
        'tractors':tractors
    }

    return render(request,'add_sale.html',context)


def update_sale(request,id):

    sale = Sale.objects.get(id=id)

    customers = Customer.objects.all()
    tractors = Tractor.objects.all()

    if request.method=="POST":

        sale.customer=Customer.objects.get(
            id=request.POST['customer']
        )

        sale.tractor=Tractor.objects.get(
            id=request.POST['tractor']
        )

        sale.sale_date=request.POST['sale_date']
        sale.amount=request.POST['amount']

        sale.save()

        return redirect('sales')

    context={
        'sale':sale,
        'customers':customers,
        'tractors':tractors
    }

    return render(request,'update_sale.html',context)


def delete_sale(request,id):

    sale=Sale.objects.get(id=id)
    sale.delete()

    return redirect('sales')
# Create your views here.
