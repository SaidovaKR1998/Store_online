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

    def add_product(self, product):
        """
        Метод для добавления товара в категорию.

        :param product: Объект класса Product.
        :raises TypeError: Если передается объект не класса Product.
        """
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product")

        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        """Геттер для списка товаров."""
        return "\n".join(str(product) for product in self.__products)

    def __str__(self):
        """Строковое представление категории."""
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."
