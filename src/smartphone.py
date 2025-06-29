from src.product import Product


class Smartphone(Product):
    """Класс для представления смартфонов."""

    def __init__(self, name: str, description: str, price: float, quantity: int,
                 efficiency: float, model: str, memory: int, color: str):
        """
        Инициализация смартфона.

        :param efficiency: Производительность
        :param model: Модель
        :param memory: Объем памяти (ГБ)
        :param color: Цвет
        """
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        """Сложение только с объектами того же класса."""
        if not isinstance(other, Smartphone):
            raise TypeError("Можно складывать только объекты класса Smartphone")
        return super().__add__(other)
