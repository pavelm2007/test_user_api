from django.contrib.auth.models import AbstractUser
from django.db import models

from users.enums import GenderTypes


class User(AbstractUser):
    gender = models.CharField(max_length=32, choices=GenderTypes.choices(), blank=True)
    age = models.PositiveIntegerField(blank=True, null=True)
