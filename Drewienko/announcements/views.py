from django.shortcuts import render
from django.views.generic import CreateView
from .models import Announcement

# Create your views here.



class AnnouncementCreateView(CreateView):
    model = Announcement
    fields = ['title'] #, 'picture', 'content', 'city', 'date_posted', 'author', 'price', 'category', 'shipping', 'sell_or_exchange']
    template_name = "announcements/announcement_form.html"
