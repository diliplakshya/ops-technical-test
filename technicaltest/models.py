from django.db import models

class Home(models.Model):
    display_text = models.CharField(max_length=200)

class MetaData(models.Model):
    version = models.CharField(max_length=10)
    description = models.TextField()
    lastcommitsha = models.CharField(max_length=50, blank=True)
