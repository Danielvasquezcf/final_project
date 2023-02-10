from django.contrib import admin
from products.models import Products, Category


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display =  ('name', 'price', 'stock')
    list_filter = ('stock', 'price')
    search_fields = ['name']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display =  ['name']
    list_filter = ['name']
    search_fields = ['name']


