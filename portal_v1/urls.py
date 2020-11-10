from django.urls import path
from announcements.views import AnnouncementCreateView, AnnouncementListView, AnnouncementDetailView, \
    AnnouncementUpdateView, \
    AnnouncementDeleteView
from users.views import LoginView, logout_view, RegisterView, ChangePassword
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', AnnouncementListView.as_view(), name='announcement-home'),
    path('announcements/annouc-<int:pk>/', AnnouncementDetailView.as_view(), name='announcement-detail'),
    path('announcements/annouc-<int:pk>/update/', AnnouncementUpdateView.as_view(), name='announcement-update'),
    path('announcements/annouc-<int:pk>/delete/', AnnouncementDeleteView.as_view(), name='announcement-delete'),
    path('announcements/new/', AnnouncementCreateView.as_view(), name='announcement-create'),
    path('login/', LoginView.as_view(), name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
    path("change_password/", ChangePassword.as_view(), name="change_password"),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

