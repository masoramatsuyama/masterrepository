from django.db import models

class Art(models.Model):
    artname = models.CharField(max_length=128)
    artbirth = models.DateField()
    artimage = models.ImageField(upload_to='media')
    artex = models.CharField(max_length=500)
    def __str__(self):
     return self.artname

class Artist(models.Model):
    artistname = models.CharField(max_length=20)
    fromm = models.CharField(max_length=128)
    artistex = models.CharField(max_length=500)
    artistimage = models.FileField(upload_to='media')
    video = models.FileField(upload_to='media', null=True, blank=True)
    link = models.CharField(max_length=300)
    myart = models.ManyToManyField(Art, blank=True)
    def __str__(self):
     return self.artistname
