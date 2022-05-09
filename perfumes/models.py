from django.db import models


class Perfume(models.Model):
    """Perfume is the art that makes memory speak."""

    perfume_name = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)
    notes = models.CharField(max_length=250)
    description = models.CharField(max_length=350)
    price = models.FloatField()
    comment = models.CharField(max_length=500)
    perfume_image = models.CharField(max_length=4000)

    def __str__(self):
        return f"{self.perfume_name} - {self.brand}"
