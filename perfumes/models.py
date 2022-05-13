from django.db import models

from users.models import PerfumesUser
from brands.models import Brand


NOTES = [
    ('berg', 'Bergamot'),  ('b-orange', 'Bitter Orange'), ('g-fruit', 'Grapefruit'),
    ('lemon', 'Lemongrass'), ('mandarin',
                              'Mandarin'), ('b-currant', 'Blackcurrant'),
    ('j-berry', 'Juniper Berry'), ('pear', 'Pear'), ('cherry', 'Cherry Blossom'),
    ('gard', 'Gardenia'), ('gera', 'Geranium'),
    ('jas', 'Jasmine'), ('lav', 'Lavender'),
    ('hed', 'Hedione'), ('lilly', 'Lily of the Valley'), ('mag', 'Magnolia'),
    ('peo', 'Peony'), ('rose', 'Rose'), ('tub', 'Tuberose'),
    ('ylg', 'Ylang Ylang'), ('amber', 'Amber'), ('card', 'Cardamom'),
    ('path', 'Patchouli'), ('saff', 'Saffron'), ('tob', 'Tobacco'),
    ('van', 'Vanilla'), ('oud', 'Oud'), ('ced', 'Cedarwood'),
    ('oak', 'Oakmoss'), ('sand', 'Sandalwood'), ('vet', 'Vetiver')
]


class Perfume(models.Model):
    """Perfume is the art that makes memory speak."""

    perfume_name = models.CharField(max_length=20)
    notes = models.CharField(
        max_length=400,
        choices=NOTES,
        default='N/A')

    brand = models.ForeignKey(
        Brand, null=True, blank=True, on_delete=models.CASCADE, related_name="perfumes")

    description = models.CharField(max_length=4000, null=True, blank=True)
    price = models.FloatField(null=False, blank=False)
    comment = models.CharField(max_length=500, null=True, blank=True)
    perfume_image = models.CharField(max_length=4000, null=False, blank=False)

    creator = models.ForeignKey(
        PerfumesUser, related_name="perfumes", null=True, blank=True, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.perfume_name} - {self.brand}"
