from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)



class Announcement(models.Model):
    title = models.CharField(max_length=100)
    # picture = models.BinaryField(editable=True)
    # content = models.TextField()
    # city = models.CharField(max_length=100)
    # date_posted = models.DateTimeField(default=timezone.now)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    # price = models.DecimalField(max_digits=5, decimal_places=2)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # shipping = models.CharField(choices=(('yes', 'shipping is possible'), ('no', 'shipping is not possible')), default='no', max_length=100)
    # sell_or_exchange = models.CharField(choices=(('sell', 'for sell'), ('exchange', 'for exchange'), ('sell or exchange', 'for sell or exchange')), default='sell', max_length=20)

    def __str__(self):
        return self.title


