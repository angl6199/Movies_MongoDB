from djongo import models

# Create your models here.
class Movies(models.Model):
    show_id = models.CharField(max_length=10, blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    director = models.CharField(max_length=200, blank=True, null=True)
    cast = models.CharField(max_length=600, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    date_added = models.CharField(max_length=100, blank=True, null=True)
    release_year = models.PositiveIntegerField(blank=True, null=True)
    rating = models.CharField(max_length=100, blank=True, null=True)
    duration = models.CharField(max_length=100, blank=True, null=True)
    listed_in = models.CharField(max_length=600, blank=True, null=True)
    description = models.CharField(max_length=600, blank=True, null=True)
