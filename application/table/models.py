from django.db import models


class FileName(models.Model):
    path = models.CharField(max_length=200)

    # def get_path(self):
    #     pass
    #
    # def set_path(self):
    #     pass


class Column(models.Model):
    name = models.CharField(max_length=50)
    width = models.IntegerField()
    file = models.ForeignKey(FileName, on_delete=models.CASCADE)