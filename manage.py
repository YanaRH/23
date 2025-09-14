from catalog.models import Category, Product

# Создание категорий
cat1 = Category.objects.create(name='Электроника', description='Электронные устройства')
cat2 = Category.objects.create(name='Книги', description='Различные книги')

# Создание продуктов
prod1 = Product.objects.create(name='Смартфон', description='Современный смартфон', category=cat1, price=25000)
prod2 = Product.objects.create(name='Ноутбук', description='Мощный ноутбук', category=cat1, price=55000)

# Получить все категории
print(Category.objects.all())

# Получить все продукты
print(Product.objects.all())

# Найти продукты в категории "Электроника"
print(Product.objects.filter(category=cat1))

# Обновить цену продукта
prod1.price = 26000
prod1.save()

# Удалить продукт
prod2.delete()
