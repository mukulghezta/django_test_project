from django.db import models


class Artist(models.Model):
    id          = models.AutoField(primary_key=True)
    artist_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

 
class Album(models.Model):
    id              = models.AutoField(primary_key=True)
    album_name      = models.CharField(max_length=100)
    artist_name     = models.OneToOneField(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return self.album_name


class Song(models.Model):
    id              = models.AutoField(primary_key=True)
    song_name       = models.CharField(max_length=100)
    album_name      = models.OneToOneField(Artist, on_delete=models.CASCADE)
    artist_name     = models.OneToOneField(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return self.song_name