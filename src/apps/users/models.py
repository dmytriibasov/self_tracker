from django.contrib.auth.models import AbstractUser
from django.db import models


class CardUser(AbstractUser):
    avatar = models.ImageField(
        null=True,
        verbose_name='Profile picture',
        blank=True,
    )

    def get_absolute_url(self):
        return f'user/{self.id}/'
