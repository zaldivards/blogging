from django.shortcuts import render, redirect
from django.views.generic import RedirectView, FormView, CreateView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from .forms import SignupForm, LoginForm


# Create your views here.


class SignupView(CreateView):
    form_class = SignupForm
    success_url = reverse_lazy('post_list')
    template_name = 'users/signup.html'

    def form_valid(self, form):
        valid = super().form_valid(form)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        new_user = authenticate(username=username, password=password)
        login(self.request, new_user)
        return valid


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'users/login.html'
    success_url = reverse_lazy('post_list')

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(self.get_success_url())
        else:
            return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)


class LogoutView(RedirectView):
    pattern_name = 'post_list'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)
