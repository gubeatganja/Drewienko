from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import Announcement

# Create your views here.



class AnnouncementCreateView(LoginRequiredMixin, CreateView):
    model = Announcement
    fields = ['title', 'picture', 'content', 'city', 'price', 'category', 'shipping', 'sell_or_exchange']


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

class AnnouncementUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Announcement
    fields = ['title', 'picture', 'content', 'city', 'date_posted', 'author', 'price', 'category', 'shipping',
              'sell_or_exchange']
    template_name = "announcements/announcement_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        ann = self.get_object()
        if self.request.user == ann.author:
            return True
        return False

class AnnouncementDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Announcement
    success_url = '/'

    def test_func(self):
        ann = self.get_object()
        if self.request.user == ann.author:
            return True
        return False