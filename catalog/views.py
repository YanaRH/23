from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Добро пожаловать в каталог!")

def book_list(request):
    # Пример view для списка книг (замените на свою логику)
    return render(request, 'catalog/book_list.html')