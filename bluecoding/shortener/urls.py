from django.urls import path
from .views import ShortenURLView

app_name = 'shortener'

urlpatterns = [
    path('', ShortenURLView.as_view(), name='shortener'),
]



