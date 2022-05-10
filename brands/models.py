from django.db import models

# Create your models here.


class Brand (models.Model):

    brand_name = models.CharField(max_length=200)
    logo = models.CharField(max_length=4000, null=True, blank=True,)
    description = models.CharField(max_length=700, null=True, blank=True)
    creators = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=False)

    def __str__(self) -> str:
        return f"{self.brand_name}"
