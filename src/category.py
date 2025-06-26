from itertools import product

from src.product import Product


class Category:
    """Класс для представления категории товаров."""

    category_count = 0  # Атрибут класса: общее количество категорий
    product_count = 0  # Атрибут класса: общее количество товаров

    def __init__(self, name: str, description: str, products: list):
        """
        Инициализация категории.

        :param name: Название категории.
        :param description: Описание категории.
        :param products: Список товаров (объектов класса Product).
        """
        self.name = name
        self.description = description
        self.__products = products  # Приватный атрибут

        # Увеличиваем счетчики при создании категории
        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: Product):
        """
        Метод для добавления товара в категорию.

        :param product: Объект класса Product.
        """
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        """Геттер для списка товаров."""
        return "\n".join(
            [f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
             for product in self.__products]
        )