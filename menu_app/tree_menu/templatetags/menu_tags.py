from django import template
from django.template.loader import render_to_string
from django.urls import resolve
from tree_menu.models import MenuItem

register = template.Library()

@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    current_url = resolve(context['request'].path_info).url_name
    menu_items = MenuItem.objects.filter(
        name=menu_name
    ).get_descendants(
        include_self=True
    ).prefetch_related('children')
    
    expanded_items = set()
    for item in menu_items:
        if item.get_url() == context['request'].path_info:
            expanded_items.update(item.get_ancestors(include_self=True))
            expanded_items.update(item.get_children())
    
    context = {
        'menu_items': menu_items,
        'current_url': current_url,
        'expanded_items': expanded_items,
    }

    menu_html = render_to_string('tree_menu/menu.html', context)

    return menu_html