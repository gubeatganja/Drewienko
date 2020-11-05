from django.urls import path
from .views import AnnouncementCreateView, AnnouncementListView, AnnouncementDetailView, AnnouncementUpdateView, \
    AnnouncementDeleteView

urlpatterns = [
    path('', AnnouncementListView.as_view(), name='announcement-home'),
    path('announcements/<int:pk>/', AnnouncementDetailView.as_view(), name='announcement-detail'),
    path('announcements/<int:pk>/update/', AnnouncementUpdateView.as_view(), name='announcement-update'),
    path('announcements/<int:pk>/delete/', AnnouncementDeleteView.as_view(), name='announcement-delete'),
    path('announcements/new/', AnnouncementCreateView.as_view(), name='announcement-create'),
]