import pytest
from io import StringIO
from unittest.mock import patch
from src.product import Product


def test_product_creation_logging(capsys):
    """Тестируем логирование при создании продукта"""
    product = Product("Телефон", "Смартфон", 599.99, 10)
    captured = capsys.readouterr()
    assert "Создан объект Product с параметрами:" in captured.out
    assert "name=Телефон" in captured.out
    assert "description=Смартфон" in captured.out


def test_product_repr():
    """Тестируем repr продукта"""
    product = Product("Телефон", "Смартфон", 599.99, 10)
    assert repr(product) == ("Product(name='Телефон', description='Смартфон', "
                            "_Product__price=599.99, quantity=10)")


def test_product_zero_quantity():
    """Тест создания продукта с нулевым количеством."""
    with pytest.raises(ValueError) as excinfo:
        Product("Test", "Description", 100.0, 0)
    assert "Товар с нулевым количеством не может быть добавлен" in str(excinfo.value)


def test_product_negative_quantity():
    """Тест создания продукта с отрицательным количеством."""
    with pytest.raises(ValueError) as excinfo:
        Product("Test", "Description", 100.0, -1)
    assert "Количество не может быть отрицательным" in str(excinfo.value)


def test_product_negative_price():
    """Тест создания продукта с отрицательной ценой."""
    with pytest.raises(ValueError) as excinfo:
        Product("Test", "Description", -100.0, 1)
    assert "Цена должна быть положительной" in str(excinfo.value)