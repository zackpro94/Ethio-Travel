from django.db import models
from django.utils import timezone
from django.urls import reverse


# Create your models here.


class destination(models.Model):

    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250)
    img = models.ImageField(upload_to='')
    desc = models.CharField(max_length=100)
    detail = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('ethiotravel:dest_detail', args=[self.slug])

    def __str__(self):
        return self.name

    
class best_tips(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(default='null')

    def __str__(self):
        return self.title

class intros(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.title

class testimony(models.Model):
    title = models.CharField(max_length=30)
    testimonies = models.TextField()
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class discount(models.Model):
    value = models.IntegerField()
        

