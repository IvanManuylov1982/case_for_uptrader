from django.contrib import admin
from .models import Menu


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'slug', 'name', 'parent', 'order')


# @admin.register(SubMenu)
# class SubMenuAdmin(admin.ModelAdmin):
#     list_display = ('id', 'menu', 'name')
#
#
# @admin.register(ListMenu)
# class ListMenu(admin.ModelAdmin):
#     list_display = ('id', 'menu', 'list_name')


