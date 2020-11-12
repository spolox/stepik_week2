import random

from django.views.generic.base import TemplateView
from django.http import Http404

import data



class MainView(TemplateView):
    template_name = "tours/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subtitle'] = data.subtitle
        context['description'] = data.description
        keys = list(data.tours.keys())
        random.shuffle(keys)
        keys = keys[:6]
        tours = data.tours.copy()
        context['tours'] = dict((key, value) for (key, value) in tours.items() if key in keys)
        return context


class DepartureView(TemplateView):
    template_name = "tours/departure.html"

    def get_context_data(self, departure, **kwargs):
        context = super().get_context_data(**kwargs)
        tours = data.tours.copy()
        context['tours'] = dict((key, value) for (key, value) in tours.items() if value['departure'] == departure)
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
