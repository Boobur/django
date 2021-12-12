from django.forms import ModelForm, TextInput, Select, Textarea, NumberInput
from .models import CarInfo, Color, Customer, Vendor, CarOrder2

class CarInfoForm(ModelForm):
    
    class Meta:
        model = CarInfo
        fields = ['car_name', 'car_colors', 'description', 'full_text', 'car_photo', 'car_category']
        colors = Color.objects.all()
        lst_data = []
        lst_num = []
        for item in colors:
            lst_data.append(item.colors)
        for item in range(len(lst_data)-1):
            lst_num.append(item)
        zipped = zip(lst_num, lst_data)
        zipped = tuple(zipped) 
        widgets = {
            "car_name": TextInput(attrs = {
                'class': 'form-control',
            }),


            "car_colors": Select(
            choices = zipped,
            attrs = {
                'class': 'form-control',
            }),

            "description": TextInput(attrs = {
                'class': 'form-control',
            }),

            "full_text": Textarea(attrs = {
                'class': 'form-control',
            }),

            "car_category": Select(attrs = {
                'class': 'form-control',
            }),
  
        }

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        widgets = {
             "surname": TextInput(attrs = {
                'class': 'form-control',
            }),
            "name": TextInput(attrs = {
                'class': 'form-control',
            }),
            "phone1": TextInput(attrs = {
                'class': 'form-control',
            }),
            "phone2": TextInput(attrs = {
                'class': 'form-control',
            }),
            "email": TextInput(attrs = {
                'class': 'form-control',
            }),
            "address": TextInput(attrs = {
                'class': 'form-control',
            }),
         }
        
class VendorForm(ModelForm):
    class Meta:
        model = Vendor
        fields = '__all__'
        widgets = {
             "surname": TextInput(attrs = {
                'class': 'form-control',
            }),
            "name": TextInput(attrs = {
                'class': 'form-control',
            }),
            "phone": TextInput(attrs = {
                'class': 'form-control',
            }),
            "email": TextInput(attrs = {
                'class': 'form-control',
            }),
            "address": TextInput(attrs = {
                'class': 'form-control',
            }),
         }      

class OrderForm(ModelForm):
    
    class Meta:
        PAY_CHOICES =(
        ("1", "Наличнами"),
        ("2", "Картой"),
        ("3", "Перечисление"),
        ("4", "Кредит"),
        )
        model = CarOrder2
        fields = '__all__'
        widgets = {

            "cust_surname": TextInput(attrs = {
                'class': 'form-control',
            }),
            "cust_name": TextInput(attrs = {
                'class': 'form-control',
            }),
            "cust_phone": TextInput(attrs = {
                'class': 'form-control',
            }),
            "car_name": TextInput(attrs = {
                'class': 'form-control',
            }),
            "car_color": TextInput(attrs = {
                'class': 'form-control',
            }),
            "car_position": NumberInput(attrs = {
                'class': 'form-control',
            }),
            "car_year": NumberInput(attrs = {
                'class': 'form-control',
            }),
            "payment": Select(
                choices = PAY_CHOICES,
                attrs = {
                'class': 'form-control',
            }),
            "quantity": NumberInput(attrs = {
                'class': 'form-control',
            }),
         }



class ColorForm(ModelForm):
    class Meta:
        model = Color
        fields = '__all__'





