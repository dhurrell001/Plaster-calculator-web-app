from django.db import models
from django.core.validators import URLValidator

# Create your models here.


class Plaster(models.Model):
    plaster_name = models.CharField(max_length=255)
    plasterweight = models.DecimalField(max_digits=5, decimal_places=2)
    coverage_kg_per_mm_per_metre = models.FloatField()
    plaster_image = models.ImageField(
        upload_to='plaster_images/', blank=True, null=True)
    plaster_type = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    pdf_file = models.FileField(
        upload_to='pdfs/',  # Specify the directory for uploaded PDFs
        blank=True,
        null=True)
    tds_url = models.URLField(max_length=200, validators=[URLValidator()])

    def __str__(self):
        return self.plaster_name
