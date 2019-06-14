from django.shortcuts import render

from .models import Route


def stations(request):

    route = request.GET.get('route')
    routes = Route.objects.all()

    context = {'routes': routes,
               'route': route}

    if route:
        route_obj = Route.objects.get(name=route)
        stations = route_obj.stations.all()
        stations_y = stations.order_by('latitude')
        stations_x = stations.order_by('longitude')

        y = (stations_y.first().latitude + stations_y.last().latitude)/2
        x = (stations_x.first().longitude + stations_x.last().longitude)/2

        center = {
            'x': x,
            'y': y
        }

        print(stations_y.first().latitude, stations_y.last().latitude)
        print(stations.first().longitude, stations.first().longitude)
        print(x, y)

        context['stations'] = stations
        context['center'] = center

    return render(request, 'stations.html', context)
