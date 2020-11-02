from django.urls import path
from . import views

urlpatterns = [
    path('', views.AnnouncementView.as_view()),
]