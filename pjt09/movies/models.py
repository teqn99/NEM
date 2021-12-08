from django.db import models
from django.conf import settings
import datetime
from datetime import datetime

class Genre(models.Model):
    genre_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.genre_name


class Actor(models.Model):
    actor_name = models.CharField(max_length=100, null=True)
    profile_path = models.CharField(max_length=200, null=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_actor')

    
    def __str__(self):
        return self.actor_name


class Director(models.Model):
    director_name = models.CharField(max_length=100, null=True)
    profile_path = models.CharField(max_length=200, null=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_director')


    def __str__(self):
        return self.director_name



class Movie(models.Model):
    title = models.CharField(max_length=255, null=True)
    popularity = models.FloatField(null=True)
    poster_path = models.CharField(max_length=200, null=True)
    release_date = models.DateField(null=True)
    vote_average = models.FloatField(null=True)
    vote_count = models.IntegerField(null=True)
    overview = models.TextField(null=True)
    genres = models.ManyToManyField(Genre)
    original_title = models.CharField(max_length=255, null=True)
    trailer = models.CharField(max_length=255, null=True)
    actors_info = models.ManyToManyField(Actor)
    director_info = models.ManyToManyField(Director)
    # original_language = models.CharField(max_length=50, null=True)
    # video = models.BooleanField(null=True)
    wish_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='wish_movies')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')

    def get_release_year(self):
        return datetime.now().year - self.release_date.year

    def __str__(self):
        return f'{self.overview[:50]}...'


class Review(models.Model):
    # title = models.CharField(max_length=100)
    content = models.CharField(max_length=140)
    score = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    # genres = models.ForeignKey(Genre, on_delete=models.CASCADE)
    happy_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='happy_reviews')
    sad_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='sad_reviews')
    angry_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='angry_reviews')

    class Meta:
        ordering = ['pk']
    