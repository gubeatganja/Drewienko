from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView, FormView
from users.forms.sign_up_form import SignUpForm


class ChangePassword(FormView, LoginRequiredMixin):
    login_url = "/login"
    template_name = "auth/change_password.html"
    form_class = PasswordChangeForm

    def get_form(self):
        if self.request.POST:
            return self.form_class(self.request.user, self.request.POST)
        return self.form_class(self.request.user)

    def form_valid(self, form):
        messages.success(request=self.request, message="Hasło zmienione prawidłowo")
        form.save()
        return redirect(reverse('index'))

    def get_success_url(self) -> str:
        return reverse("index")


class RegisterView(CreateView):
    template_name = "auth/register.html"
    form_class = SignUpForm

    def form_valid(self, form):
        messages.success(self.request, "Użytkownik zarejestrowany. Możesz się zalogować.")
        return super(RegisterView, self).form_valid(form)

    def get_success_url(self) -> str:
        return reverse("index")


class LoginView(View):
    template_name = "auth/login.html"

    def get(self, request):
        if request.user.is_authenticated:
            return redirect("index")
        return render(request, self.template_name, {})

    def post(self, request):
        username: str = request.POST.get("username")
        password: str = request.POST.get("password")

        user: User or None = authenticate(username=username,
                                          password=password)

        if user:
            login(request, user)
            return redirect("index")

        messages.error(request, "Nie ma takiego użytkownika")
        return redirect("user:login")


def logout_view(request):
    logout(request)
    return redirect("index")
