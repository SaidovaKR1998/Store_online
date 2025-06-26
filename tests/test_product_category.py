# test_product_category.py
import unittest

from src.category import Category
from src.product import Product


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
        new_product = Product('Ноутбук', 'Игровой ноутбук', 100000.0, 5)
        initial_count = Category.product_count
        self.category.add_product(new_product)
        self.assertEqual(Category.product_count, initial_count + 1)

    def test_products_property(self):
        expected_output = "Телефон, 50000.0 руб. Остаток: 10 шт."
        self.assertIn(expected_output, self.category.products)

    def test_product_price_setter(self):
        # Проверяем, что нельзя установить отрицательную цену
        import io
        from contextlib import redirect_stdout

        with io.StringIO() as buf, redirect_stdout(buf):
            self.product.price = -100
            output = buf.getvalue()
            self.assertIn("Цена не должна быть нулевая или отрицательная", output)
        self.assertEqual(self.product.price, 50000.0)  # Цена не изменилась

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

if __name__ == '__main__':
    unittest.main()
