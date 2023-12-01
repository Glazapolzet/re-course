from django.contrib import admin
from .models import Category, Product
from modeltranslation.admin import TabbedTranslationAdmin


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']

    prepopulated_fields = {'slug': ('name',)}
    
    
class TranslatedCategoryAdmin(CategoryAdmin, TabbedTranslationAdmin):
    pass


admin.site.register(Category, TranslatedCategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']

    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product,  ProductAdmin)
