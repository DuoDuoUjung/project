from django.urls import path
from . import views

urlpatterns = [
    path('flask-service/', views.proxy_to_flask, name='flask_service'),
]
