#from . import views
from django.urls import path
from .views import UserRegisterView, UserEditView, PasswordsChangeView, EditProfilePageView, CreateProfilePageView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit-profile/', UserEditView.as_view(), name='edit_profile'),
    #path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change_password.html'), name='edit_profile'),
    path('password/', PasswordsChangeView.as_view()),
    path('<int:pk>/edit-profile-page/', EditProfilePageView.as_view(), name='edit_profile_page'),
    path('create-profile-page/', CreateProfilePageView.as_view(), name='create_profile'),
] 