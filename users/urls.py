from django.urls import path, include
from .views import *

urlpatterns = [
    path('register/', register_page, name="register"),
    path('login/', login_page, name="login"),
    path('logout/', logout_user, name="logout"),

]