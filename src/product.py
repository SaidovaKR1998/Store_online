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
        if price <= 0:
            raise ValueError("Цена должна быть положительной.")
        if quantity < 0:
            raise ValueError("Количество не может быть отрицательным.")

        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
