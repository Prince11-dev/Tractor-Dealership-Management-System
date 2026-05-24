from django.shortcuts import render, redirect
from .models import Customer

def customer_list(request):
    customers = Customer.objects.all()

    context = {
        'customers': customers
    }

    return render(request,'customers.html',context)


def add_customer(request):

    if request.method == 'POST':
        customer_name = request.POST['customer_name']
        phone = request.POST['phone']
        address = request.POST['address']
        village = request.POST['village']

        Customer.objects.create(
            customer_name=customer_name,
            phone=phone,
            address=address,
            village=village
        )

        return redirect('customers')

    return render(request,'add_customer.html')


def update_customer(request,id):

    customer = Customer.objects.get(id=id)

    if request.method=="POST":

        customer.customer_name=request.POST['customer_name']
        customer.phone=request.POST['phone']
        customer.address=request.POST['address']
        customer.village=request.POST['village']

        customer.save()

        return redirect('customers')

    context={
        'customer':customer
    }

    return render(request,'update_customer.html',context)


def delete_customer(request,id):

    customer=Customer.objects.get(id=id)
    customer.delete()

    return redirect('customers')