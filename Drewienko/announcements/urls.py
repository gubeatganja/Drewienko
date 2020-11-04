from django.urls import path
from .views import AnnouncementCreateView

urlpatterns = [
    path('announcements/new/', AnnouncementCreateView.as_view(), name='announcement-create'),
]