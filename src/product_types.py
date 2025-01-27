from product import Product


class Smartphone(Product):
    """Класс, представляющий смартфон"""
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency  # Производительность
        self.model = model            # Модель
        self.memory = memory          # Объем памяти
        self.color = color            # Цвет

    def __str__(self):
        return (f"Смартфон {self.model} ({self.color}), {self.memory} ГБ, "
                f"производительность: {self.efficiency}, {self.price} руб., Остаток: {self.quantity} шт.")


class LawnGrass(Product):
    """Класс, представляющий газонную траву"""
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country                   # Страна-производитель
        self.germination_period = germination_period  # Срок прорастания
        self.color = color                        # Цвет травы

    def __str__(self):
        return (f"Газонная трава ({self.color}), страна: {self.country}, "
                f"срок прорастания: {self.germination_period} дней, {self.price} руб., Остаток: {self.quantity} шт.")
