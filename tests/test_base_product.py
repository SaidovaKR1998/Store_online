import pytest
from abc import ABC
from src.base_product import BaseProduct
from src.product import Product
from src.smartphone import Smartphone
from src.lawn_grass import LawnGrass


def test_base_product_is_abstract():
    with pytest.raises(TypeError):
        BaseProduct("Test", "Test", 100, 1)


def test_base_product_methods():
    assert issubclass(BaseProduct, ABC)
    assert hasattr(BaseProduct, '__init__')
    assert hasattr(BaseProduct, '__str__')
    assert hasattr(BaseProduct, '__repr__')
    assert hasattr(BaseProduct, 'price')
    assert hasattr(BaseProduct.price, 'fget')
    assert hasattr(BaseProduct.price, 'fset')
    assert hasattr(BaseProduct, 'new_product')
    assert hasattr(BaseProduct, '__add__')


def test_product_inherits_base_product():
    assert issubclass(Product, BaseProduct)


def test_smartphone_inherits_base_product():
    assert issubclass(Smartphone, BaseProduct)


def test_lawn_grass_inherits_base_product():
    assert issubclass(LawnGrass, BaseProduct)
