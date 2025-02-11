from src.product import Product


def test_product_init(first_product, second_product):
    assert first_product.name == "Samsung Galaxy C23 Ultra"
    assert first_product.description == "256GB, Серый цвет, 200MP камера"
    assert first_product.price == 180000.0
    assert first_product.quantity == 5

    assert second_product.name == "Iphone 15"
    assert second_product.description == "512GB, Gray space"
    assert second_product.price == 210000.0
    assert second_product.quantity == 8


def test_price_getter_setter(capsys):
    """Проверка геттера и сеттера для цены."""
    product = Product("Laptop", "A high-performance laptop", 1000.0, 10)

    # Проверяем начальную цену
    assert product.price == 1000.0

    # Изменяем цену на допустимое значение
    product.price = 2000.0
    assert product.price == 2000.0

    # Попытка установить недопустимую цену
    product.price = -500.0  # Выводится предупреждение
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-1] == "Цена не должна быть нулевая или отрицательная"
    assert product.price == 2000.0  # Цена не изменилась


def test_new_product():
    """Проверка метода new_product."""
    product_data = {
        "name": "Smartphone",
        "description": "A flagship smartphone",
        "price": 120000.0,
        "quantity": 5,
    }

    product = Product.new_product(product_data)

    assert product.name == "Smartphone"
    assert product.description == "A flagship smartphone"
    assert product.price == 120000.0
    assert product.quantity == 5


def test_product_str(first_product):
    """Проверка строкового представления продукта"""
    assert str(first_product) == "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_product_addition(sample_products):
    """Проверка сложения стоимости товаров"""
    product1, product2 = sample_products
    total = product1 + product2
    assert total == 1400
