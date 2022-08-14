from django.db import models


class Data(models.Model):
    strain = models.FloatField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{:.2f}".format(self.strain)

    class Meta:
        ordering = ['-created']