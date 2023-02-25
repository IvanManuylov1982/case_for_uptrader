from django import template
from do_menu.models import Menu


register = template.Library()


@register.inclusion_tag('do_menu/list_menu.html', takes_context=True)
def draw_menu(context, slug):
    menu = Menu.objects.get(slug=slug)
    return {'menu': menu, 'context': context['category']}
