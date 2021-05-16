from django.contrib import admin
from .models import Product, Category, County

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "sku",
        "name",
        "category",
        "county",
        "price",
        "rating",
        "image",
    )

    ordering = ("sku",)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "friendly_name",
        "name",
    )


class CountyAdmin(admin.ModelAdmin):
    list_display = (
        "friendly_name",
        "name",
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(County, CountyAdmin)
