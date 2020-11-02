from django.shortcuts import render
from django.views.generic.base import View
from .models import Announcement

# Create your views here.
def index(request):
    return render(request, 'home/index.html')

class AnnouncementView(View):
    def get(self, request):
        announcement = Announcement.objects.all()
        return render(request, "home/index.html", {"announce_list": announcement})