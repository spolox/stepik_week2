from django import template

import data
register = template.Library()


@register.inclusion_tag('header.html', takes_context=True)
def show_header(context):
    context['departures'] = data.departures
    return context


