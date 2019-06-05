from django.db import models


class Route(models.Model):
    name = models.CharField(max_length=128)


class Station(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    routes = models.ManyToManyField(Route, related_name="stations", null=True)
    name = models.CharField(max_length=128)