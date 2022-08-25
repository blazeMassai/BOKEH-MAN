from django.contrib import admin
from .models import Products
# Register your models here.

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id' ,'name' ,'color' , 'price' , )
    list_per_page = 25
    list_editable = ('name' ,)


admin.site.register(Products, ProductsAdmin)
