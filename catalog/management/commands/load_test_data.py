import json
import os
from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Загружает тестовые данные из фикстур'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Начинаем загрузку тестовых данных...'))

        # Удаляем старые данные
        self.stdout.write('Удаляем старые данные...')
        Product.objects.all().delete()
        Category.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Старые данные удалены.'))

        fixtures_dir = os.path.join('fixtures')
        categories_path = os.path.join(fixtures_dir, 'categories.json')
        products_path = os.path.join(fixtures_dir, 'products.json')

        # Загружаем категории
        self.stdout.write('Загружаем категории...')
        with open(categories_path, 'r', encoding='utf-8') as f:
            categories = json.load(f)
            for item in categories:
                Category.objects.create(**item['fields'])
        self.stdout.write(self.style.SUCCESS(f'Загружено категорий: {len(categories)}'))

        # Загружаем продукты
        self.stdout.write('Загружаем продукты...')
        with open(products_path, 'r', encoding='utf-8') as f:
            products = json.load(f)
            for item in products:
                category = Category.objects.get(pk=item['fields']['category'])
                Product.objects.create(
                    name=item['fields']['name'],
                    description=item['fields']['description'],
                    image=item['fields'].get('image'),
                    category=category,
                    price=item['fields']['price'],
                    created_at=item['fields'].get('created_at'),
                    updated_at=item['fields'].get('updated_at'),
                )
        self.stdout.write(self.style.SUCCESS(f'Загружено продуктов: {len(products)}'))

        self.stdout.write(self.style.SUCCESS('Все тестовые данные успешно загружены!'))
