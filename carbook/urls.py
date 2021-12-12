from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home_user'),
    path('service/', service, name='service'),
    path('car/', car, name='car'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('order/', order, name='order_user'),
]