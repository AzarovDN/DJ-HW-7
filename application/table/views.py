import csv

from django.shortcuts import render
from django.views import View

from .models import Column, FileName


CSV_FILENAME = 'phones.csv'
COLUMNS = [
    {'name': 'id', 'width': 1},
    {'name': 'name', 'width': 3},
    {'name': 'price', 'width': 2},
    {'name': 'release_date', 'width': 2},
    {'name': 'lte_exists', 'width': 1},
]

f_name = FileName.objects.create(path=CSV_FILENAME)

for column in COLUMNS:
    print(column['width'])
    Column.objects.create(name=column['name'], width=column['width'], file=f_name)

COLUMNS = Column.objects.filter(file=f_name)


class TableView(View):

    def get(self, request):
        with open(f_name.path, 'rt') as csv_file:
            header = []
            table = []
            table_reader = csv.reader(csv_file, delimiter=';')
            for table_row in table_reader:
                if not header:
                    header = {idx: value for idx, value in enumerate(table_row)}
                else:
                    row = {header.get(idx) or 'col{:03d}'.format(idx): value
                           for idx, value in enumerate(table_row)}
                    table.append(row)
            result = render(request, 'table.html', {'columns': COLUMNS, 'table': table, 'csv_file': f_name.path})
        return result
