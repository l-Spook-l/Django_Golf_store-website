from django.contrib.auth import logout, login
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from .forms import RegisterUserForm
from .forms import LoginUserForm


class RegisterUser(CreateView):
    # стандартная форма - django
    form_class = RegisterUserForm
    # form_class = UserCreationForm
    template_name = 'authorization/register.html'

    # перенаправление при упешной регистрации
    # success_url = reverse_lazy('login')

    def form_valid(self, form):
        # после успешной регистрации, сразу авторизуем польователя
        user = form.save()
        login(self.request, user)
        return redirect('store_home')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'authorization/login.html'

    def get_success_url(self):
        # если пользователь верно ввел данные, перенаправляем его на нужную стр.
        return reverse_lazy('store_home')


# class ProfileUser(DetailView):
#     # model = Product
#     model = User
#     template_name = 'authorization/profile.html'
#     context_object_name = 'user'


def logout_user(request):
    logout(request)
    return redirect('login')
