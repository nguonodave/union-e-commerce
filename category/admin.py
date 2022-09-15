from django.contrib import admin
from . models import Category

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ('category_name', 'slug') # fields to be displayed at the front page of the table in the database dashboard

admin.site.register(Category, CategoryAdmin)
