from django.contrib import admin
from . models import *

class LocationAdmin(admin.ModelAdmin):
    list_display = ('city',)

class CarDealerAdmin(admin.ModelAdmin):
    list_display = ('car_dealer','phone', 'location','earnings','type')

class CarAdmin(admin.ModelAdmin):
    list_display = ('name','img_preview','car_dealer','capacity', 'location','is_available','rent')

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user','phone', 'location','type')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user','car_dealer','car','rent','days','is_complete')


admin.site.register(Location, LocationAdmin)
admin.site.register(CarDealer, CarDealerAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)

# Register your models here.
