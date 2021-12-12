from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('vendor/', vendor, name='vend'),
    path('create_vendor/', create_vendor, name='create_vendor'),
    path('update_vendor/<str:pk>/', update_vendor, name='update_vendor'),
    path('delete_vendor/<str:pk>/', delete_vendor, name='delete_vendor'),

    path('customer/', customer, name='cust'),
    path('create_customer/', create_customer, name='create_customer'),
    path('update_customer/<str:pk>/', update_customer, name='update_customer'),
    path('delete_customer/<str:pk>/', delete_customer, name='delete_customer'),
    
    path('car-info/', car_info, name='carinfo'),
    path('create_car_info/', create_car_info, name='create_car_info'),
    path('update_car_info/<str:pk>/', update_car_info, name='update_car_info'),
    path('delete_car_info/<str:pk>/', delete_car_info, name='delete_car_info'),

    path('car-base/', car_base, name='carbase'),
    path('car-summ/', car_summ, name='carsumm'),

    path('order/', order, name='order'),
    path('create_order/', create_order, name='create_order'),
    path('update_order/<str:pk>/', update_order, name='update_order'),
    path('delete_order/<str:pk>/',delete_order, name='delete_order'),
    
    path('color/', color, name='color'),
    path('create_colors/', create_colors, name='create_colors'),

    path('charts/', charts, name='charts'),
    path('report/', report, name='report'),
    
       

]

