from src.product import Product


class LawnGrass(Product):
    """Класс для представления газонной травы."""

    def __init__(self, name: str, description: str, price: float, quantity: int,
                 country: str, germination_period: str, color: str):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        """Сложение только с объектами того же класса."""
        if not isinstance(other, LawnGrass):
            raise TypeError("Можно складывать только объекты класса LawnGrass")
        return super().__add__(other)

    def __repr__(self):
        attrs = ', '.join([f"{key}={value!r}" for key, value in self.__dict__.items()])
        return f"{self.__class__.__name__}({attrs})"
