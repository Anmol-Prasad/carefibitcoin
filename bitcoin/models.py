from django.db import models


class Coindata(models.Model):
    name = models.CharField(max_length=40)
    symbol = models.CharField(max_length=10)
    price = models.CharField(max_length=40)
    newtime = models.CharField(max_length=40)

    def __str__(self):
        return self.name
