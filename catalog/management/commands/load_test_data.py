import json
import os
from django.core.management.base import BaseCommand
from catalog.models import Category, Product

class Command(BaseCommand):
    help = 'Загружает тестовые данные из фикстур'

    def handle(self, *args, **options):
        self.stdout.write('Удаляем старые данные...')
        Product.objects.all().delete()
        Category.objects.all().delete()

        fixtures_dir = os.path.join('catalog', 'fixtures')

        categories_path = os.path.join(fixtures_dir, 'categories.json')
        products_path = os.path.join(fixtures_dir, 'products.json')

        self.stdout.write('Загружаем категории...')
        with open(categories_path, 'r', encoding='utf-8') as f:
            categories = json.load(f)
            for item in categories:
                Category.objects.create(**item['fields'])

        self.stdout.write('Загружаем продукты...')
        with open(products_path, 'r', encoding='utf-8') as f:
            products = json.load(f)
            for item in products:
                category = Category.objects.get(pk=item['fields']['category'])
                Product.objects.create(
                    name=item['fields']['name'],
                    description=item['fields']['description'],
                    category=category,
                    price=item['fields']['price']
                )

        self.stdout.write(self.style.SUCCESS('Тестовые данные успешно загружены!'))

