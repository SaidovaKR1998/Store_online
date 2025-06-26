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
        self.products = products

        # Увеличиваем счетчики при создании категории
        Category.category_count += 1
        Category.product_count += len(products)
