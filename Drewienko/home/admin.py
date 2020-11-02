from django.contrib import admin
from .models import Category, Announcement, User

admin.site.register(Category)
admin.site.register(Announcement)
admin.site.register(User)