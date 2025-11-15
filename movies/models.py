from django.db import models
class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    director_name = models.CharField(max_length=150)
    publication_year = models.PositiveBigIntegerField()
    synopsis = models.TextField()
    image_url = models.URLField(blank=True, null=True)
    def __str__(self):
        return f"{self.title} ({self.publication_year})"
# Create your models here.
