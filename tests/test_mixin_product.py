from src.product import Product
from src.product_types import Smartphone, LawnGrass


def test_mixin_product(capsys):
    Product("Товар", "Описание товара", 150.0, 5)
    message = capsys.readouterr()
    assert message.out.strip() == "Product (Товар, Описание товара, 150.0, 5)"

    Smartphone("Телефон", "Описание телефона", 150000.0, 8, "A15 Bionic", "Последняя модель", 256, "Синий")
    message = capsys.readouterr()
    assert message.out.strip() == "Smartphone (Телефон, Описание телефона, 150000.0, 8)"

    LawnGrass("Lawngrass", "Lawngrass small size", 1500.0, 5, "Russia", "2 month", "Зелёный")
    message = capsys.readouterr()
    assert message.out.strip() == "LawnGrass (Lawngrass, Lawngrass small size, 1500.0, 5)"
