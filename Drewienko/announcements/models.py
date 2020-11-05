from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Category(models.Model):
    # name = models.CharField(choices=((1, 'szafy'), (2, 'komody'), (3, 'sofy'), (4, 'zestawy wypoczynkowe'), (5, 'meblościanki'), (6, 'ławy i stoliki'), (7, 'krzesła')), max_length=100)

    def __str__(self):
        return self.name



class Announcement(models.Model):
    title = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='announc_photos')
    content = models.TextField()
    city = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(choices=(('szafy', 'szafy'), ('komody', 'komody'), ('sofy', 'sofy'), ('zestawy wypoczynkowe', 'zestawy wypoczynkowe'), ('meblościanki', 'meblościanki'), ('ławy i stoliki', 'ławy i stoliki'), ('krzesła', 'krzesła')), max_length=100)
    shipping = models.CharField(choices=(('tak', 'tak'), ('nie', 'nie')), default='nie', max_length=100)
    sell_or_exchange = models.CharField(choices=(('na sprzedaż', 'na sprzedaż'), ('na wymianę', 'na wymianę'), ('na sprzedaż lub wymianę', 'na sprzedaż lub wymianę')), max_length=100)

    def __str__(self):
        return self.title


