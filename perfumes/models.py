from django.db import models

from users.models import PerfumesUser
from brands.models import Brand


NOTES = [
    'Bergamot', 'Bitter Orange', 'Grapefruit',
    'Lemongrass', 'Mandarin', 'Blackcurrant', 'Juniper Berry', 'Pear',
    'Cherry Blossom', 'Frangipani', 'Gardenia', 'Geranium',
    'Jasmine', 'Lavender', 'Lily', 'Lily of the Valley', 'Magnolia',
    'Peony', 'Rose', 'Tuberose', 'Ylang Ylang', 'Amber', 'Cardamom',
    'Patchouli', 'Saffron', 'Tobacco', 'Vanilla', 'Oud', 'Cedarwood',
    'Oakmoss', 'Sandalwood', 'Vetiver'
]


class Perfume(models.Model):
    """Perfume is the art that makes memory speak."""

    perfume_name = models.CharField(max_length=20)
    notes = models.CharField(
        max_length=20,
        choices=NOTES.sort())

    brand_name = models.ForeignKey(
        Brand, null=True, blank=True, on_delete=models.CASCADE, related_name="perfumes")

    description = models.CharField(max_length=350, null=True, blank=True)
    price = models.FloatField(null=False, blank=False)
    comment = models.CharField(max_length=500, null=True, blank=True)
    perfume_image = models.CharField(max_length=4000, null=False, blank=False)

    createdBy = models.ForeignKey(
        PerfumesUser, related_name="perfumes", null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.perfume_name} - {self.brand_name}"
