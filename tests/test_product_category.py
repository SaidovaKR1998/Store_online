# test_product_category.py
import unittest
from unittest.mock import patch
from io import StringIO
from product import Product
from category import Category

class TestProductCategory(unittest.TestCase):
    def setUp(self):
        # Создаем тестовые данные
        self.product_data = {
            'name': 'Телефон',
            'description': 'Смартфон',
            'price': 50000.0,
            'quantity': 10
        }
        self.product = Product.new_product(self.product_data)
        self.product2 = Product('Ноутбук', 'Игровой ноутбук', 100000.0, 5)
        self.category = Category(
            'Электроника',
            'Технические устройства',
            [self.product]
        )

    def test_product_creation(self):
        self.assertEqual(self.product.name, 'Телефон')
        self.assertEqual(self.product.price, 50000.0)
        self.assertEqual(self.product.quantity, 10)

    def test_category_private_products(self):
        with self.assertRaises(AttributeError):
            print(self.category.__products)

    def test_add_product_to_category(self):
        initial_count = Category.product_count
        self.category.add_product(self.product2)
        self.assertEqual(Category.product_count, initial_count + 1)

    def test_add_invalid_product_type(self):
        with self.assertRaises(TypeError):
            self.category.add_product("Не продукт")

    def test_products_property(self):
        expected_output = "Телефон, 50000.0 руб. Остаток: 10 шт."
        self.assertIn(expected_output, self.category.products)

    def test_product_price_setter(self):
        # Проверяем, что нельзя установить отрицательную цену
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.product.price = -100
            self.assertIn("Цена не должна быть нулевая или отрицательная", fake_out.getvalue())
        self.assertEqual(self.product.price, 50000.0)  # Цена не изменилась

        # Проверяем, что цена действительно приватная
        with self.assertRaises(AttributeError):
            print(self.product.__price)

        # Проверяем корректное изменение цены
        self.product.price = 45000.0
        self.assertEqual(self.product.price, 45000.0)

    def test_new_product_classmethod(self):
        product = Product.new_product({
            'name': 'Планшет',
            'description': 'Графический планшет',
            'price': 30000.0,
            'quantity': 7
        })
        self.assertIsInstance(product, Product)
        self.assertEqual(product.name, 'Планшет')

    # Новые тесты для проверки добавленной функциональности

    def test_product_str_representation(self):
        """Тестируем строковое представление продукта"""
        expected_str = "Телефон, 50000.0 руб. Остаток: 10 шт."
        self.assertEqual(str(self.product), expected_str)

    def test_category_str_representation(self):
        """Тестируем строковое представление категории"""
        # Добавляем второй продукт в категорию
        self.category.add_product(self.product2)
        expected_str = "Электроника, количество продуктов: 15 шт."  # 10 + 5
        self.assertEqual(str(self.category), expected_str)

    def test_product_addition(self):
        """Тестируем сложение продуктов"""
        # 50000 * 10 + 100000 * 5 = 500000 + 500000 = 1000000
        total = self.product + self.product2
        self.assertEqual(total, 1000000.0)

    def test_product_addition_with_invalid_type(self):
        """Тестируем сложение продукта с неверным типом"""
        with self.assertRaises(TypeError):
            result = self.product + "не продукт"

    def test_category_products_property_optimization(self):
        """Тестируем оптимизированный геттер products"""
        # Добавляем второй продукт
        self.category.add_product(self.product2)
        output = self.category.products
        self.assertIn("Телефон, 50000.0 руб. Остаток: 10 шт.", output)
        self.assertIn("Ноутбук, 100000.0 руб. Остаток: 5 шт.", output)
        self.assertEqual(output.count('\n'), 1)  # Проверяем, что одна строка разделена

if __name__ == '__main__':
    unittest.main()
