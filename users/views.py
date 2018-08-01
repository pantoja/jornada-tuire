from django.shortcuts import render
from django.views.generic import DetailView, UpdateView, CreateView
from users.models import User
from django.urls import reverse_lazy
from users.mixins import ProfileAccessMixin
from django.contrib.auth.views import LoginView, LogoutView


class ProfileView(DetailView):
    model = User
    template_name = 'profile.html'
    context_object_name = 'profile'


class ProfileEditView(ProfileAccessMixin, UpdateView):
    model = User
    fields = ('picture', 'username')
    template_name = 'profile_edit.html'
    
    def get_success_url(self):
        return reverse_lazy('users:profile', args=[self.object.pk])


class UserLoginView(LoginView):
    template_name = 'login.html'
    redirect_autheticated_user = True

class UserLogoutView(LogoutView):
    pass

class UserSignUpView(CreateView):
    model = User
    form_class = UserSignUpForm
    template_name = 'signup.html'