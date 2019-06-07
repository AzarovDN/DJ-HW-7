from django.core.management.base import BaseCommand
import csv
from app.models import Station, Route

import pprint


class Command(BaseCommand):
    help = 'Загружаем данные в модель'

    def handle(self, *args, **kwargs):

        with open('moscow_bus_stations.csv', 'r', newline='', encoding='cp1251') as csvfile:
            data = csv.DictReader(csvfile, delimiter=';')
            for line in data:
                route_numbers_list = line['RouteNumbers'].split(';')
                routes = []

                for route in Route.objects.all():
                    routes.append(route.name)

                station = None

                if not routes:
                    print(1)
                    for route in route_numbers_list:
                        route_obj = Route.objects.create(name=route)
                        print(2)
                        if not station:
                            print(3)
                            route_obj.stations_set.create(longitude=line['Longitude_WGS84'],
                                                            latitude=line['Latitude_WGS84'],
                                                             name=line['StationName'])
                        # else:
                        #     print(4)
                        #     station.routes.set(Route.objects.create(name=route))
                print(5)

                break



            # по-другому решил обработать файл. Обработка выше
            



            # next(data)
            # for line in data:
            #     id, name, longitude, latitude, street, adm_area, district, route_numbers, \
            #     station_name, direction, pavilion, operating_org_name, entry_state, global_id, geo_data, some = line
            #     route_numbers_list = route_numbers.split(';')
            #
            #     for route in Route.objects.all():
            #         routes.append(route.name)
            #
            #     station = Station.objects.create(longitude=longitude, latitude=latitude, name=station_name)
            #
            #     if not routes:
            #         for route in route_numbers_list:
            #             station.routes.add(Route.objects.create(name=route))
            #     else:
            #         for route in route_numbers_list:
            #             if route in routes:
            #                 station.routes.add(Route.objects.get(name=route))
            #             else:
            #                 station.routes.add(Route.objects.create(name=route))