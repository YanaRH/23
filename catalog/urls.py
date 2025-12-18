from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Главная страница приложения
    path('books/', views.book_list, name='book_list'),  # Список книг
]