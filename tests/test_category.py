import pytest
from products.category import Category
from products.product import Product


def test_category_initialization():
    """Проверяет корректность инициализации категории."""
    product1 = Product("Телефон", "Смартфон", 599.99, 10)
    product2 = Product("Ноутбук", "Игровой", 1299.99, 5)
    category = Category("Электроника", "Техника", [product1, product2])

    assert category.name == "Электроника"
    assert category.description == "Техника"
    assert len(category.products) == 2


def test_category_count():
    """Проверяет подсчет количества категорий."""
    initial_count = Category.category_count
    product = Product("Телефон", "Смартфон", 599.99, 10)
    category = Category("Тест", "Тест", [product])

    assert Category.category_count == initial_count + 1


def test_product_count():
    """Проверяет подсчет количества товаров."""
    initial_count = Category.product_count
    product1 = Product("Телефон", "Смартфон", 599.99, 10)
    product2 = Product("Ноутбук", "Игровой", 1299.99, 5)
    category = Category("Тест", "Тест", [product1, product2])

    assert Category.product_count == initial_count + 2
