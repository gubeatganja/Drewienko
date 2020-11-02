from django.db import models
from datetime import date

class Category(models.Model):
    name = models.CharField("Kategoria", max_length=150)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Kategoria"
        verbose_name_plural = "Kategorie"

class User(models.Model):
    name = models.CharField("Imię", max_length=150)
    email = models.EmailField()
    tel = models.CharField(max_length=12)
    city = models.CharField(max_length=60)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Użytkownik"
        verbose_name_plural = "Użytkownicy"

class Announcement(models.Model):
    title = models.CharField("Tytuł", max_length=150)
    price = models.DecimalField("Cena", max_digits=10, decimal_places=2, default=0, help_text="podaj cenę")
    photo = models.ImageField("Zdjęcie")
    description = models.TextField("Opis")
    category = models.ForeignKey(Category, verbose_name="Kategoria", on_delete=models.SET_NULL, null=True)
    name = models.ForeignKey(User, verbose_name="Użytkownik", on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField("data ogłoszenia", auto_now_add=True, blank=True)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Ogłoszenie"
        verbose_name_plural = "Ogłoszenia"
