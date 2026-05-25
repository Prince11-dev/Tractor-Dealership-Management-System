from django.shortcuts import render, redirect
from .models import Tractor

def tractor_list(request):
    tractors = Tractor.objects.all()

    context = {
        'tractors': tractors
    }

    return render(request,'tractors.html',context)


def add_tractor(request):

    if request.method == 'POST':

        tractor_name=request.POST['tractor_name']
        model_no=request.POST['model_no']
        company_name=request.POST['company_name']
        price=request.POST['price']
        horsepower=request.POST['horsepower']
        stock_quantity=request.POST['stock_quantity']

        stock_status='Available'

        if int(stock_quantity) < 5:
            stock_status='Low Stock'

        if int(stock_quantity)==0:
            stock_status='Out of Stock'

        Tractor.objects.create(
            tractor_name=tractor_name,
            model_no=model_no,
            company_name=company_name,
            price=price,
            horsepower=horsepower,
            stock_quantity=stock_quantity,
            stock_status=stock_status
        )

        return redirect('tractors')

    return render(request,'add_tractor.html')


def update_tractor(request,id):

    tractor=Tractor.objects.get(id=id)

    if request.method=="POST":

        tractor.tractor_name=request.POST['tractor_name']
        tractor.model_no=request.POST['model_no']
        tractor.company_name=request.POST['company_name']
        tractor.price=request.POST['price']
        tractor.horsepower=request.POST['horsepower']

        tractor.save()

        return redirect('tractors')

    context={
        'tractor':tractor
    }

    return render(request,'update_tractor.html',context)


def delete_tractor(request,id):

    tractor=Tractor.objects.get(id=id)
    tractor.delete()

    return redirect('tractors')