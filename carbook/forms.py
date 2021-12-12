from django.forms import ModelForm, TextInput, Select, Textarea
from staffer.models import Customer

class RegCustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        widgets = {
             "surname": TextInput(attrs = {
                'class': 'form-control',
                'placeholder':"Фамилия",
            }),
            "name": TextInput(attrs = {
                'class': 'form-control',
                'placeholder':"Имя",
            }),
            "phone1": TextInput(attrs = {
                'class': 'form-control',
                'placeholder':"+998900000000",
            }),
            "phone2": TextInput(attrs = {
                'class': 'form-control',
                'placeholder':"+998900000000",
            }),
            "email": TextInput(attrs = {
                'class': 'form-control',
                'placeholder':"E-mail",
            }),
            "address": TextInput(attrs = {
                'class': 'form-control',
                'placeholder':"Таш об. Гор. Янгиюл д9 кв 30",
            }),
         }