from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class PerfumesUser(AbstractUser):
    age = models.CharField(max_length=50)
    is_premium = models.BooleanField(default=False)
