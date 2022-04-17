from django.db import models

class Event(models.Model):
    sportType = models.CharField('Вид спорта', max_length=20, default='')
    description = models.TextField('Описание', default='')
    longitude = models.FloatField('Долгота', default=0)
    latitude = models.FloatField('Широта', default=0)
    requiredNumber = models.IntegerField('Необходимое количество', default=0)
    def __str__(self):
        return self.sportType
