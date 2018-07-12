# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Category, Product, Person

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'price', 'stock', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated', 'category']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Product, ProductAdmin)


class PersonAdmin(admin.ModelAdmin):
    list_display = ["id", "first_name", "middle_name", "last_name", "age", "weight", "is_married"]
    list_filter = ["is_married"]
    list_editable = ["first_name", "middle_name", "last_name", "age", "weight", "is_married"]
admin.site.register(Person, PersonAdmin)