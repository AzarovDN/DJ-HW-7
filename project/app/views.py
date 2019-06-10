from django.shortcuts import render

from .models import Route


def stations(request):

    route = request.GET.get('route')
    routes = Route.objects.all()

    context = {'routes': routes}

    if route:
        route_obj = Route.objects.get(name=route)
        stations = route_obj.stations.all()

        x = (stations.first().latitude + stations.last().latitude)/2
        y = (stations.first().longitude + stations.last().longitude)/2
        center = {
            'x': x,
            'y': y
        }

        context['stations'] = stations
        context['center'] = center

    return render(request, 'stations.html', context)