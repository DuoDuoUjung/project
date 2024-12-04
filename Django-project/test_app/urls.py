from django.urls import path
from . import views

urlpatterns = [
    path('ans/', views.ans_view, name='ans'),
    path('test/', views.test_view, name='test'),
]