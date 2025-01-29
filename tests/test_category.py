

def test_category_init(category_data):
    assert category_data.name == "Телевизоры"
    assert (
            category_data.description
            == "Современный телевизор, который позволяет наслаждаться просмотром, "
               "станет вашим другом и помощником"
    )
    expected_product = "55\" QLED 4K, 123000.0 руб. Остаток: 7 шт.\n"

    assert category_data.products == expected_product

    assert category_data.category_count == 1
    assert category_data.product_count == 1


def test_count_category_product(count_category_product):
    assert count_category_product.category_count == 2
    assert count_category_product.product_count == 3


def test_products_property(count_category_product):
    """Проверка корректности вывода строки"""
    assert count_category_product.products == (
        "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n")


def test_add_product(category_data, new_product):
    """Проверка добавления продукта в категорию"""
    assert len(category_data.products_in_list) == 1
    category_data.add_product(new_product)
    assert len(category_data.products_in_list) == 2


def test_category_str(category_data):
    """Проверка строкового представления категории"""
    expected_str = "Телевизоры, количество продуктов: 7 шт."
    assert str(category_data) == expected_str
