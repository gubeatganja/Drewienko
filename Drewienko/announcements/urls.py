from django.urls import path
from .views import AnnouncementCreateView, AnnouncementListView, AnnouncementDetailView

urlpatterns = [
    path('', AnnouncementListView.as_view(), name='announcement-home'),
    path('announcements/detail/<int:pk>', AnnouncementDetailView.as_view(), name='announcement-detail'),
    path('announcements/new/', AnnouncementCreateView.as_view(), name='announcement-create'),
]