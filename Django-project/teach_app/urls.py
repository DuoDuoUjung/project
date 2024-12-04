from django.urls import path
from . import views

urlpatterns = [
    path('teach/', views.teach_view, name='teach'),
]