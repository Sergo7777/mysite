from django.contrib import admin

# Register your models here.
from .models import Table, Order, Stock, CategoryMenu, Food
class TableAdmin(admin.ModelAdmin):
	list_display = ['id', 'seats',]

class OrderAdmin(admin.ModelAdmin):
	list_display = ['id', 'date', 'name', 'email', 'table']

class StockAdmin(admin.ModelAdmin):
	list_display = ['id',  'name', 'image', 'discount', 'description']

class FoodAdmin(admin.ModelAdmin):
	list_display = ['name', 'image', 'price', 'portion', 'description', 'category']

class CategoryMenuAdmin(admin.ModelAdmin):
	list_display = ['id',  'name', 'image']

admin.site.register(Table, TableAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Stock, StockAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(CategoryMenu, CategoryMenuAdmin)