from django.db import models


# Create your models here.
class Team(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/%y/%m/%d')
    facebook_link = models.URLField(max_length=100)
    twitter_link = models.URLField(max_length=100)
    google_plus_link = models.URLField(max_length=100)
    crated_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.fname
