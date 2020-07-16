from __future__ import unicode_literals

from django.db import models


class Genre(models.Model):

    name = models.CharField(max_length=500)

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"

    def __str__(self):
        return self.name


class Movie(models.Model):

    popularity = models.FloatField()
    director = models.CharField(max_length=500)
    genre = models.ManyToManyField(Genre)
    imdb_score = models.FloatField()
    name = models.CharField(max_length=500)



    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"

    def __str__(self):
        return self.name


