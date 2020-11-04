from django.contrib import admin
from .models import Category, Announcement

# Register your models here.
admin.site.register(Category)
admin.site.register(Announcement)