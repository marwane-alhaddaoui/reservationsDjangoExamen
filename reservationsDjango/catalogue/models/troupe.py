from django.db import models

class Troupe(models.Model):
    name = models.CharField(max_length=50, unique=True)
    logo_url = models.URLField(max_length=255, blank=True)

    def __str__(self):
        return self.name
