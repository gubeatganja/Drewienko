from django.contrib.auth import views as auth_views
from django.urls import path
from user.views import LoginView, logout_view, RegisterView

app_name = "user"

urlpatterns = [
    path('login', LoginView.as_view(), name="login"),
    path("logout", logout_view, name="logout"),
    path("register", RegisterView.as_view(), name="register"),

    # Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
    path('password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(
             template_name='auth/password_change_done.html'),
         name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(
        template_name='auth/password_change.html'),
         name='password_change'),

    path('password_reset/done/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='auth/password_reset_done.html'),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(),
         name='password_reset'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='auth/password_reset_complete.html'),
         name='password_reset_complete'),

]
