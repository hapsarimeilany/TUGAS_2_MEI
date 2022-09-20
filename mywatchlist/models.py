from django.db import models

class WatchList(models.Model):
    title = models.CharField(max_length=50)
    watched = models.CharField(max_length=50)
    rating = models.IntegerField()
    release_date = models.TextField()
    review = models.TextField()