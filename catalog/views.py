from django.shortcuts import render
from .models import Product, Category


def index(request):
    """Главная страница - показывает последние 5 продуктов."""
    latest_products = Product.objects.order_by('-created_at')[:5]
    categories = Category.objects.all()

    context = {
        'latest_products': latest_products,
        'categories': categories,
    }
    return render(request, 'catalog/index.html', context)


def book_list(request):
    """Страница со списком всех продуктов."""
    products = Product.objects.all()
    categories = Category.objects.all()

    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'catalog/book_list.html', context)