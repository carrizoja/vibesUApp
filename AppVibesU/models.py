from django.db import models
from django.contrib.auth.models import User


# Create your models here.
#Song Class
class Song(models.Model):
    title = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    album = models.CharField(max_length=50)
    length = models.CharField(max_length=10)
    link_address_image = models.CharField(max_length=250)
    link_address_mp3_track = models.CharField(max_length=250, null=True)
    plays = models.IntegerField()
    is_favorite = models.BooleanField(default=False)
    def __str__(self):
        return self.title
    
#Artist Class
class Artist(models.Model):
    name = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    listeners = models.IntegerField()
    link_address_image = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    def __str__(self):
        return self.name
    
#Album Class
class Album(models.Model):
    title = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    link_address_image = models.CharField(max_length=250)
    release_date = models.CharField(max_length=4)
    amount_of_songs = models.IntegerField()
    album_duration = models.CharField(max_length=10)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
 #Podcast Class
class Podcast(models.Model):
    title = models.CharField(max_length=50)
    host = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    link_address_image = models.CharField(max_length=250)
    release_date = models.CharField(max_length=4)
    amount_of_episodes = models.IntegerField()
    podcast_duration = models.CharField(max_length=10)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
#User Avatar
class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.image}"
