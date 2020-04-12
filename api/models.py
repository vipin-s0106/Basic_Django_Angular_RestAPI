from django.db import models

# Create your models here.


class Movie(models.Model):
    movie_name = models.CharField(max_length=150,null=False)
    caption_image = models.FileField(null=True,blank=True)
    desc = models.CharField(max_length=150)
    year = models.IntegerField()

    def __str__(self):
        return self.movie_name