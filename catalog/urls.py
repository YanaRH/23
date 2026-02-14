from django.urls import path
from . import views

app_name = 'catalog'  # Добавьте эту строку

urlpatterns = [
    path('', views.index, name='index'),
]