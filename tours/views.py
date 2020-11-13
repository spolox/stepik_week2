import random

from django.http import Http404
from django.http import HttpResponseNotFound
from django.views.generic.base import TemplateView

import data


def custom_handler404(request, exception):
    return HttpResponseNotFound('Извините, страница не найдена.')


def custom_handler500(request):
    return HttpResponseNotFound('Внутреняя ошибка сервака. Приносим свои извинения, повторите попытку позже')


class MainView(TemplateView):
    template_name = "tours/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subtitle'] = data.subtitle
        context['description'] = data.description
        keys = list(data.tours.keys())
        random.shuffle(keys)
        context['tours'] = dict((key, value) for (key, value) in data.tours.items() if key in keys[:6])
        return context


class DepartureView(TemplateView):
    template_name = "tours/departure.html"

    def get_context_data(self, departure, **kwargs):
        context = super().get_context_data(**kwargs)
        if departure not in data.departures:
            raise Http404
        context['tours'] = dict((key, value) for (key, value) in data.tours.items() if value['departure'] == departure)
        context['departure'] = departure
        return context


class TourView(TemplateView):
    template_name = "tours/tour.html"

    def get_context_data(self, tour_id, **kwargs):
        context = super().get_context_data(**kwargs)
        tour = data.tours.get(tour_id)
        if tour is None:
            raise Http404
        context['tour'] = tour
        return context
