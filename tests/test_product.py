import pytest
from products.product import Product


def test_product_initialization():
    """Проверяет корректность инициализации товара."""
    product = Product("Телефон", "Смартфон", 599.99, 10)

    assert product.name == "Телефон"
    assert product.description == "Смартфон"
    assert product.price == 599.99
    assert product.quantity == 10


def test_product_invalid_price():
    """Проверяет, что цена не может быть отрицательной."""
    with pytest.raises(ValueError):
        Product("Телефон", "Смартфон", -100.0, 10)


def test_product_invalid_quantity():
    """Проверяет, что количество не может быть отрицательным."""
    with pytest.raises(ValueError):
        Product("Телефон", "Смартфон", 599.99, -5)
