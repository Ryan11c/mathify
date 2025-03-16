from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import SignUp, EditProfileForm, PasswordChangingForm, ProfilePageForm
from myApp.models import Profile, Category
from django.contrib.auth import login, authenticate


class CreateProfilePageView(CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/create_user_profile.html'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cat_menu'] = Category.objects.all()
        return context


class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    fields = ['bio', 'profile_pic']
    success_url = reverse_lazy('edit_profile')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cat_menu'] = Category.objects.all()
        return context


class UserRegisterView(generic.CreateView):
    form_class = SignUp
    template_name = 'registration/register.html'
    success_url = reverse_lazy('home') 
    #log in the user when they successfully register
    def form_valid(self, form):
        self.object = form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
        return redirect(self.get_success_url())
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cat_menu'] = Category.objects.all()
        return context


class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')
    def get_object(self):
        return self.request.user
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cat_menu'] = Category.objects.all()
        return context
    

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    template_name='registration/change_password.html'
    success_url = reverse_lazy('edit_profile')


