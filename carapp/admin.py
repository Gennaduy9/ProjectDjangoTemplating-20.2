# admin
# !777%_z2


from django.contrib import admin

from carapp.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'description', 'category', 'photo', 'price', 'color', 'created', 'available',)
    prepopulated_fields = {"slug": ("name",)}
    list_filter = ('category',)
    search_fields = ('name', 'description',)

