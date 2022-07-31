from pydoc import describe
from django.contrib import admin
from .models import Menu, MenuBar

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'price', 'description', 'show')

admin.site.register(Menu, CategoryAdmin)
admin.site.register(MenuBar)
