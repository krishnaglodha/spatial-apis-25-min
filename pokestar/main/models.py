from django.contrib.gis.db import models

# Create your models here.
class Cities(models.Model):
    name = models.CharField(max_length=100)
    adm0name = models.CharField(max_length=100)
    geometry = models.PointField(srid=4326)

    def __str__(self):
        return self.name

