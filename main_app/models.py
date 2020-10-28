from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=150)
    pages = models.CharField(max_length=5)
    year_published = models.IntegersField(max_length=8)
    category = models.CharField(max_length=30)
    lccn = models.CharField(max_length=15)
    synopsis = models.TextField(max_length=500)
