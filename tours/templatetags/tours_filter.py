from django import template
from django.http import Http404

import data

register = template.Library()


@register.filter(name='range')
def get_range(number):
    return range(number)


@register.filter(name='get_departure')
def get_departure(departure_code, first_lower):
    departure = data.departures.get(departure_code)
    if departure is None:
        raise Http404
    if first_lower:
        return departure[0].lower() + departure[1:]
    else:
        return departure


@register.filter(name='get_min')
def get_min(objects, value):
    seq = [x[value] for x in objects.values()]
    return min(seq)


@register.filter(name='get_max')
def get_max(objects, value):
    seq = [x[value] for x in objects.values()]
    return max(seq)
