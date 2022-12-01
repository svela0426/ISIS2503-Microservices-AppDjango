from django.db import models

class Place(models.Model):
    variable = models.IntegerField(null=False, default=None)
    name = models.FloatField(null=True, blank=True, default=None)

    def __str__(self):
        return '%s %s' % (self.value, self.unit)