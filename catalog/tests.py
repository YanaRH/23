from django.test import TestCase
from catalog.models import Category, Product


class CategoryModelTest(TestCase):
    """Тесты для модели Category"""

    def test_category_creation(self):
        """Тест создания категории"""
        category = Category.objects.create(
            name='Электроника',
            description='Электронные устройства'
        )
        self.assertEqual(category.name, 'Электроника')
        self.assertEqual(category.description, 'Электронные устройства')
        self.assertEqual(str(category), 'Электроника')

    def test_category_str(self):
        """Тест метода __str__"""
        category = Category.objects.create(name='Книги')
        self.assertEqual(str(category), 'Книги')

    def test_category_verbose_name(self):
        """Тест verbose_name"""
        self.assertEqual(Category._meta.verbose_name, 'Категория')
        self.assertEqual(Category._meta.verbose_name_plural, 'Категории')


class ProductModelTest(TestCase):
    """Тесты для модели Product"""

    def setUp(self):
        """Создаем тестовые данные"""
        self.category = Category.objects.create(
            name='Электроника',
            description='Электронные устройства'
        )

    def test_product_creation(self):
        """Тест создания продукта"""
        product = Product.objects.create(
            name='Смартфон',
            description='Современный смартфон',
            category=self.category,
            price=25000.00
        )
        self.assertEqual(product.name, 'Смартфон')
        self.assertEqual(product.price, 25000.00)
        self.assertEqual(product.category, self.category)

    def test_product_str(self):
        """Тест метода __str__"""
        product = Product.objects.create(
            name='Ноутбук',
            description='Мощный ноутбук',
            category=self.category,
            price=55000.00
        )
        self.assertEqual(str(product), 'Ноутбук')

    def test_product_verbose_name(self):
        """Тест verbose_name"""
        self.assertEqual(Product._meta.verbose_name, 'Продукт')
        self.assertEqual(Product._meta.verbose_name_plural, 'Продукты')

    def test_product_foreign_key(self):
        """Тест связи ForeignKey"""
        product = Product.objects.create(
            name='Планшет',
            description='Планшетный компьютер',
            category=self.category,
            price=30000.00
        )
        # Проверяем, что связь работает
        self.assertEqual(product.category.name, 'Электроника')

    def test_product_ordering(self):
        """Тест сортировки"""
        Product.objects.create(
            name='Z-Товар',
            description='Товар с Z',
            category=self.category,
            price=1000.00
        )
        Product.objects.create(
            name='A-Товар',
            description='Товар с A',
            category=self.category,
            price=2000.00
        )

        products = Product.objects.all()
        self.assertEqual(products[0].name, 'A-Товар')
        self.assertEqual(products[1].name, 'Z-Товар')