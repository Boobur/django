from django.shortcuts import render, redirect
from .forms import CarInfoForm, ColorForm, CustomerForm, VendorForm, OrderForm
from .models import Color, CarInfo, Vendor, Customer,CarOrder2
from django.contrib.auth.decorators import login_required



def index(request):
    if request.user.is_authenticated:
        return render(request, 'staffer/index.html')
    else:
        return redirect('/users/login/')

#Продовец---------------------------------------------------
def vendor(request):
    vendor = Vendor.objects.all()
    content = {
        'vendor' : vendor
    }
    return render(request, 'staffer/vendor.html', content)

def create_vendor(request):
    form = VendorForm()
    if request.method == "POST":
        form = VendorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/staffer/vendor/')

    content = {'form':form}
    return render(request, 'staffer/forms/create_vendor.html', content)

def update_vendor(request, pk):
    vendor = Vendor.objects.get(id = pk)
    form = VendorForm(instance=vendor)
    if request.method == "POST":
        form = VendorForm(request.POST, instance=vendor)
        if form.is_valid():
            form.save()
            return redirect('/staffer/vendor/')
    
    content = {'form':form}
    return render(request, 'staffer/forms/create_vendor.html', content) 

def delete_vendor(request, pk):
    vendor = Vendor.objects.get(id = pk)
    vendor.delete()
    return redirect('/staffer/vendor/')
#Продовец---------------------------------------------------

def customer(request):
    customer = Customer.objects.all()
    content={
        'customer': customer
    }
    return render(request, 'staffer/customer.html', content)

def create_customer(request):
    form = CustomerForm()
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/staffer/customer/')

    content = {'form':form}
    return render(request, 'staffer/forms/create_customer.html', content)

def update_customer(request, pk):
    customer = Customer.objects.get(id = pk)
    form = CustomerForm(instance=customer)
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('/staffer/customer/')
    
    content = {'form':form}
    return render(request, 'staffer/forms/create_customer.html', content) 

def delete_customer(request, pk):
    customer = Customer.objects.get(id = pk)
    customer.delete()
    return redirect('/staffer/customer/')


def car_info(request):
    cars = CarInfo.objects.all()
    content = {
        'cars': cars,
    }
    return render(request, 'staffer/car-info.html', content)

def create_car_info(request):
    form = CarInfoForm()
    if request.method == "POST":
        form = CarInfoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/staffer/car-info/')

    content = {'form':form}
    return render(request, 'staffer/forms/create_car_info.html', content)

def update_car_info(request, pk):
    cars = CarInfo.objects.get(id = pk)
    form = CarInfoForm(instance=cars)
    if request.method == "POST":
        form = CarInfoForm(request.POST, instance=cars)
        if form.is_valid():
            form.save()
            return redirect('/staffer/car-info/')
    
    content = {'form':form}
    return render(request, 'staffer/forms/create_car_info.html', content) 

def delete_car_info(request, pk):
    cars = CarInfo.objects.get(id = pk)
    cars.delete()
    return redirect('/staffer/car-info/')


def car_base(request):
    return render(request, 'staffer/car-base.html')


def car_summ(request):
    return render(request, 'staffer/car-summ.html')


def order(request):
    orders = CarOrder2.objects.all()
    content = {
        'orders': orders
    }
    return render(request, 'staffer/order.html', content)

def create_order(request):
    form = OrderForm()
    if request.method == "POST":
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/staffer/order/')

    content = {'form':form}
    return render(request, 'staffer/forms/create_order.html', content)

def update_order(request, pk):
    orders = CarOrder2.objects.get(id = pk)
    form = OrderForm(instance=orders)
    if request.method == "POST":
        form = OrderForm(request.POST, instance=orders)
        if form.is_valid():
            form.save()
            return redirect('/staffer/order/')
    
    content = {'form':form}
    return render(request, 'staffer/forms/create_order.html', content)   

def delete_order(request, pk):
    orders = CarOrder2.objects.get(id = pk)
    orders.delete()
    return redirect('/staffer/order/')





def color(request):
    colors = Color.objects.all()
    count = 0
    content = {
        'all_colors':colors,
        'count':count,
    }
    return render(request, 'staffer/color.html', content)

def create_colors(request):
    form = ColorForm()
    if request.method == "POST":
        form = ColorForm(request.POST)
        if form.is_valid():
            car_colors = form.cleaned_data.get('countries')
            form.save()
            return redirect('color/')

    content = {'form':form}
    return render(request, 'staffer/forms/create_colors.html', content)



def charts(request):
    return render(request, 'staffer/charts.html')


def report(request):
    return render(request, 'staffer/report.html')


def handler404(request, exception):
    context = {}
    response = render(request, "staffer/404.html", context=context)
    response.status_code = 404
    return response