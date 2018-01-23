

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class wish(models.Model):
    description = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse('home')





