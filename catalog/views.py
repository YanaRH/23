from django.shortcuts import render

def index(request):
    # Отображает главную страницу
    return render(request, 'catalog/index.html')

def book_list(request):
    # Отображает страницу контактов или списка книг (замените на свою логику)
    return render(request, 'catalog/book_list.html')