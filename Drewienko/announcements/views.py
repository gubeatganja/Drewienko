from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView
from .models import Announcement

# Create your views here.



class AnnouncementCreateView(CreateView):
    model = Announcement
    fields = ['title', 'picture', 'content', 'city', 'date_posted', 'author', 'price', 'category', 'shipping', 'sell_or_exchange']
    template_name = "announcements/announcement_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AnnouncementListView(ListView):
    model = Announcement
    template_name = 'announcements/home.html'
    context_object_name = 'ann_items'
    ordering = ['-date_posted']

class AnnouncementDetailView(DetailView):
    model = Announcement
    template_name = 'announcements/announcement_detail.html'