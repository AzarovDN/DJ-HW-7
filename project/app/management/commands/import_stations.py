from django.core.management.base import BaseCommand
import csv
from app.models import Station, Route


class Command(BaseCommand):
    help = 'Загружаем данные в модель'

    def handle(self, *args, **kwargs):

        with open('moscow_bus_stations.csv', 'r', newline='', encoding='cp1251') as csvfile:
            data = csv.DictReader(csvfile, delimiter=';')
            n = 0
            for line in data:
                n +=1
                print(n)
                station = Station.objects.create(longitude=line['Longitude_WGS84'],
                                                 latitude=line['Latitude_WGS84'],
                                                 name=line['StationName'])

                route_numbers_list = line['RouteNumbers'].split(';')
                routes = []

                for route in Route.objects.all():
                    routes.append(route.name)

                if not routes:
                    for route in route_numbers_list:
                        station.routes.add(Route.objects.create(name=route))
                else:
                    for route in route_numbers_list:
                        if route in routes:
                            station.routes.add(Route.objects.get(name=route))
                        else:
                            station.routes.add(Route.objects.create(name=route))

