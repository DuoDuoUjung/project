from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('main/', views.main_view, name='main'),
    path('profile/', views.profile_view, name='profile'),
    path('register/', views.register_view, name='register'),
]