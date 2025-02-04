

class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

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
        """Магический метод сложения для расчета полной стоимости товаров на складе"""
        if isinstance(other, Product):
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError("Сложение возможно только между объектами класса Product")

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
