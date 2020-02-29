from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    # path('about/register/', views.register),
    # path('login/register/', views.register),
]