from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    total_pages = models.PositiveIntegerField()
    published_year = models.PositiveIntegerField()
    description = models.TextField()

    def __str__(self):
        return self.title
    