import data


def get_title(request):
    return {
        'title': data.title,
        'departures': data.departures,
    }
