from django.db import models
from django.contrib.auth.models import User


class Engineer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE, related_name="engineer")
    name = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=17, null=True, unique=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)