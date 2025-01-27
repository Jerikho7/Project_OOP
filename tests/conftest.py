import pytest

from src.product import Product
from src.category import Category
from src.product_types import Smartphone, LawnGrass


@pytest.fixture
def first_product():
    return Product(
        name="Samsung Galaxy C23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5
    )


@pytest.fixture
def second_product():
    return Product(
        name="Iphone 15",
        description="512GB, Gray space",
        price=210000.0,
        quantity=8
    )


@pytest.fixture
def category_data():
    return Category(
        name="Телевизоры",
        description="Современный телевизор, который позволяет наслаждаться просмотром, "
                    "станет вашим другом и помощником",
        products=[
            Product.new_product(
                {"name": '55" QLED 4K', "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}
            )
        ]
    )


@pytest.fixture
def count_category_product(first_product, second_product):
    return Category(
        name="Смартфоны",
        description="Смартфоны последних поколений, различных брендов",
        products=[first_product, second_product]
    )


@pytest.fixture
def new_product():
    """Новый продукт  для gроверка добавления продукта в категорию"""
    return Product.new_product({
        "name": "Haier 65 Smart TV S3",
        "description": "4K Ultra HD, экран формата 16:9, частота обновления составляет 60 Гц",
        "price": 70000.0,
        "quantity": 5,
    })


@pytest.fixture
def sample_products():
    """Фикстура для создания тестовых продуктов"""
    product1 = Product("Laptop", "A powerful laptop", 100, 10)  # 100 * 10 = 1000
    product2 = Product("Mouse", "Wireless mouse", 200, 2)  # 200 * 2 = 400
    return product1, product2



@pytest.fixture
def first_smartphone():
    return Smartphone(
        name="iPhone 13",
        description="Флагман Apple",
        price=100000.0,
        quantity=5,
        efficiency="A15 Bionic",
        model="iPhone 13",
        memory=256,
        color="Синий"
    )


@pytest.fixture
def lawngrass():
    """Данные для теста lawngrass"""
    return LawnGrass(
        name="Lawngrass",
        description="Lawngrass small size",
        price=1500.0,
        quantity=5,
        country="Russia",
        germination_period="2 month",
        color="Зелёный"
    )