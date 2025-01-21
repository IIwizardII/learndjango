from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pages = models.IntegerField()
    genre = models.CharField(max_length=100)
    
    def __str__(self):
        return f"Title: {self.title}"

