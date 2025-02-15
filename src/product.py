from abc import ABC, abstractmethod

from src.mixin_product import MixinProduct


class BaseProduct(ABC):

    @abstractmethod
    def __init__(self):
        pass


class Product(MixinProduct, BaseProduct):
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        if self.quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        super().__init__()

    @property
    def price(self):
        """
        Геттер для получения значения цены.
        """
        return self.__price

    @price.setter
    def price(self, value):
        """
        Сеттер для установки значения цены с проверкой.
        Если значение цены меньше или равно нулю, выводится предупреждение.
        """
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value

    def __str__(self):
        """Строковое представление продукта"""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Сложение стоимости товаров одного типа"""
        if type(self) is not type(other):
            raise TypeError("Сложение возможно только между товарами одного типа")
        return self.__price * self.quantity + other.__price * other.quantity

    @classmethod
    def new_product(cls, product_data):
        """
        Создает новый экземпляр Product на основе данных словаря.
        Аргументы:
            product_data (dict): словарь с данными о продукте.
                Ожидаются ключи: "name", "description", "price", "quantity".
        Возвращает:
                Product: экземпляр класса Product.
        """
        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"],
        )
