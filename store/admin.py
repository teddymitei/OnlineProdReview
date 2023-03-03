from django.contrib import admin
# Register your models here.
# tell what models to access in the admin area
from .models import Category, Product
# to register models
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # what features to show in the list
    list_display = ['name','slug']
    # slug field will get filled automautically when type something into name 
    prepopulated_fields = {'slug':('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','author','slug','price','in_stock','created','updated']
    list_filter = ['in_stock','is_active']
    list_editable = ['price','in_stock']
    prepopulated_fields = {'slug':('title',)}