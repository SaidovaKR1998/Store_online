class Product:
    """Класс для представления товара."""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Инициализация товара.

        :param name: Название товара.
        :param description: Описание товара.
        :param price: Цена товара (с копейками).
        :param quantity: Количество товара в наличии.
        """
        self.name = name
        self.description = description
        self._price = price  # Приватный атрибут
        self.quantity = quantity

        if price <= 0:
            raise ValueError("Цена должна быть положительной.")
        if quantity < 0:
            raise ValueError("Количество не может быть отрицательным.")

    @classmethod
    def new_product(cls, product_data: dict):
        """
        Класс-метод для создания нового продукта из словаря.

        :param product_data: Словарь с данными продукта.
        :return: Объект класса Product.
        """
        return cls(
            name=product_data['name'],
            description=product_data['description'],
            price=product_data['price'],
            quantity=product_data['quantity']
        )

    @property
    def price(self):
        """Геттер для цены."""
        return self._price

    @price.setter
    def price(self, new_price):
        """Сеттер для цены с проверкой."""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self._price = new_price

