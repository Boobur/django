from django.contrib import admin
from .models import *

class VendorAdmin(admin.ModelAdmin):
    list_display = ('id', 'surname', 'name', 'phone')
    list_display_links = ('surname',)
    search_fields = ('surname', 'name')


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'surname', 'name', 'phone1', 'phone2')
    list_display_links = ('surname',)
    search_fields = ('surname', 'name')

admin.site.register(Vendor, VendorAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(CarInfo)
admin.site.register(CarCategory)
admin.site.register(CarOrder2)
admin.site.register(Color)
