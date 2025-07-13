from src.product import Product
from src.smartphone import Smartphone
from src.lawn_grass import LawnGrass
from src.category import Category

if __name__ == '__main__':
    # Демонстрация работы миксина
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)

    # Создание объектов наследников
    smartphone = Smartphone(
        "Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14,
        85.5, "Note 11 Pro", 128, "Blue"
    )

    lawn_grass = LawnGrass(
        "Газонная трава Premium", "Мягкая трава", 1500.0, 50,
        "Россия", "14 дней", "Зеленый"
    )

    # Демонстрация работы категорий
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, smartphone]
    )

    category2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром",
        [Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)]
    )

    # Вывод информации
    print("\nИнформация о категориях:")
    print(f"Всего категорий: {Category.category_count}")
    print(f"Всего продуктов: {Category.product_count}")

    print("\nПродукты в категории 'Смартфоны':")
    print(category1.products)

    print("\nДемонстрация сложения продуктов:")
    try:
        total = product1 + lawn_grass
    except TypeError as e:
        print(f"Ошибка: {e}")

    # Демонстрация repr
    print("\nПредставление объектов:")
    print(repr(product1))
    print(repr(smartphone))
    print(repr(lawn_grass))
