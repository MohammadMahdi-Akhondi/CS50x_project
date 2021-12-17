from django.db import models
from django.contrib.auth.models import User


class Passwords(models.Model):
    password = models.CharField(max_length=25)
    website = models.CharField(max_length=50, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="passwords")