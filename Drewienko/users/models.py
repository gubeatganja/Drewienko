from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Telefon powinien być podany w następującym formacie : '+999999999'. Up to 15 digits allowed.")
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    city = models.CharField("City", max_length=1024)
    avatar = models.ImageField(upload_to='avatars', blank=True)

    class Meta:
        verbose_name = "Użytkownik"
        verbose_name_plural = "Użytkownicy"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


"""I defined signals so our Profile model will be automatically 
created/updated when we create/update User instances."""
