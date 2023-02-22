from django import template
from do_menu.models import Menu


register = template.Library()


@register.inclusion_tag('do_menu/list_menu.html')
def draw_menu(name):
    menu = Menu.objects.get(name=name)
    # sub_menu = []
    # if name:
    #     id_menu = Menu.objects.get(name=name).id
    #     #sub_menu = SubMenu.objects.filter(menu=id_menu)
    return {'menu': menu}
