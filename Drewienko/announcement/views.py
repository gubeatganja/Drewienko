from django.shortcuts import render
from .models import Announcement
from django.views.generic.base import View

def index(request):
    return render(request, 'announcement/index.html')

class AnnouncementView(View):
    def get(self, request):
        announcement = Announcement.objects.all()
        return render(request, "announcement/index.html", {"announce_list": announcement})