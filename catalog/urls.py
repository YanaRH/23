
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contacts/', views.book_list, name='book_list'),  # Или 'books/' если это список книг
]