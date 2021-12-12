from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegCustomerForm
from staffer.models import CarInfo, Customer



def index(request):
    car_info = CarInfo.objects.filter(car_colors='2')[:5]
    customer = Customer.objects.all()[:5]

    form = RegCustomerForm()
    if request.method == "POST":
        form = RegCustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    content = {
        'car_info': car_info,
        'customer':customer,
        'form':form,
    }
    return render(request, 'carbook/index.html', content)
   
    

def service(request):
    content={}
    return render(request, 'carbook/service.html', content)

def car(request):
   car_info = CarInfo.objects.all()
   content = {
        'car_info': car_info,
    }
   return render(request, 'carbook/car.html', content)

def car_info(request):
    pass


def about(request):
    pass

def contact(request):
    pass

def order(request):
    pass

