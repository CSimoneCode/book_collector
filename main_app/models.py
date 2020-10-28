from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=150)
    synopsis = models.TextField(max_length=500)
    pages = models.CharField(max_length=5)
    year_published = models.IntegerField(max_length=7)
    genre = models.CharField(max_length=30) ### May make this a dropdown eventually
    lccn = models.CharField(max_length=15)
    quantity = models.IntegerField(max_length=4)

    def __str__(self):
        return self.title
    
