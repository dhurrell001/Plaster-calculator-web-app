from django.db import models

# Create your models here.


class Plaster(models.Model):
    plaster_name = models.CharField(max_length=255)
    plasterweight = models.DecimalField(max_digits=5, decimal_places=2)
    coverage_by_metre = models.FloatField()
    plaster_image = models.ImageField(
        upload_to='plaster_images/', blank=True, null=True)
    plaster_type = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.plaster_name
