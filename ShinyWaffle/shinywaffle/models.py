from django.db import models


class Gallery(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Image(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
