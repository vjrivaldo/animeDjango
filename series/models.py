from django.db import models

# Create your models here.


class Animepopular(models.Model):
    animeId = models.CharField(max_length=100)
    animeTitle = models.CharField(max_length=100)
    animeImg = models.CharField(max_length=100)
    releasedDate = models.CharField(max_length=100)
    animeUrl = models.CharField(max_length=100)


class Detailanime(models.Model):
    animeId = models.CharField(max_length=100 ,blank=True, null=True)
    animeTitle = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    releasedDate = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    otherNames = models.CharField(max_length=100)
    synopsis = models.CharField(max_length=100)
    animeImg = models.CharField(max_length=100)
    totalEpisodes = models.CharField(max_length=100)

class Topratedanime(models.Model):
    animeId = models.CharField(max_length=100)
    animeTitle = models.CharField(max_length=100)
    animeImg = models.CharField(max_length=100)
    latestEpisode = models.CharField(max_length=100)
    animeUrl = models.CharField(max_length=100)


class MovieAnime(models.Model):
    animeId = models.CharField(max_length=100)
    animeTitle = models.CharField(max_length=100)
    animeImg = models.CharField(max_length=100)
    releasedDate = models.CharField(max_length=100)
    animeUrl = models.CharField(max_length=100)
    