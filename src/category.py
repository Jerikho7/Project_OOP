from src.product import Product


class Category:
    """Класс описывающий категорию продуктов"""
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self):
        """Строковое представление категории"""
        total_quantity = 0
        for product in self.__products:
            total_quantity += product.quantity
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    @property
    def products(self):
        """
        Геттер для приватного списка __products.
        Возвращает строку с информацией о продуктах в заданном формате.
        """
        return "".join(
            f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
            for product in self.__products
        )

    def add_product(self, product):
        """
        Добавляет продукт в приватный список __products и увеличивает счетчик продуктов.
        Аргумент:
        product (Product): объект класса Product.
        """
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise ValueError("Only instances of Product can be added.")

    @property
    def products_in_list(self):
        return self.__products
