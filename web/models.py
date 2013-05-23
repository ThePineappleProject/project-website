from django.db import models

# Create your models here.

class Plant(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

class Cultivar(models.Model):
    plant = models.ForeignKey(Plant)
    name = models.CharField(max_length=200)
    temp_low = models.FloatField()
    temp_high = models.FloatField()
    elevation_low = models.IntegerField(default=0)
    elevation_high = models.IntegerField()
    soil_type = models.CharField(max_length=200)
    ph_low = models.FloatField()
    ph_high = models.FloatField()
    sunlight = models.CharField(max_length=200)
    precipitation_low = models.IntegerField()
    precipitation_high = models.IntegerField()
    crop_duration = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name