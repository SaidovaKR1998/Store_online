import pytest
from src.category import Category
from src.product import Product


def test_category_initialization():
    """Проверяет корректность инициализации категории."""
    product1 = Product("Телефон", "Смартфон", 599.99, 10)
    product2 = Product("Ноутбук", "Игровой", 1299.99, 5)
    category = Category("Электроника", "Техника", [product1, product2])

    assert category.name == "Электроника"
    assert category.description == "Техника"
    # Проверяем наличие продуктов в строке
    assert "Телефон" in category.products
    assert "Ноутбук" in category.products


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


def test_middle_price_with_products():
    """Тест расчета средней цены с товарами."""
    product1 = Product("Product1", "Desc1", 100.0, 10)
    product2 = Product("Product2", "Desc2", 200.0, 5)
    category = Category("Test", "Test desc", [product1, product2])

    assert category.middle_price() == 150.0


def test_middle_price_empty_category():
    """Тест расчета средней цены без товаров."""
    category = Category("Empty", "Empty desc", [])
    assert category.middle_price() == 0


def test_middle_price_single_product():
    """Тест расчета средней цены с одним товаром."""
    product = Product("Product", "Desc", 100.0, 10)
    category = Category("Single", "Single desc", [product])
    assert category.middle_price() == 100.0