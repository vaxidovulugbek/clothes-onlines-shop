from django.contrib import admin

from . import models


# Register your models here.
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Color)
class ColorAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Size)
class SizeAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    pass
