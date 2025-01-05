
def test_category_init(category_data):
    assert category_data.name == "Телевизоры"
    assert (
            category_data.description
            == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
    assert category_data.products == [
        {"name": '55" QLED 4K', "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}
    ]

    assert category_data.category_count == 1
    assert category_data.product_count == 1
