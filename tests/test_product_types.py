def test_smartphone_init(first_smartphone):
    assert first_smartphone.name == "iPhone 13"
    assert first_smartphone.description == "Флагман Apple"
    assert first_smartphone.price == 100000.0
    assert first_smartphone.quantity == 5
    assert first_smartphone.efficiency == "A15 Bionic"
    assert first_smartphone.model == "iPhone 13"
    assert first_smartphone.memory == 256
    assert first_smartphone.color == "Синий"


def test_lawngrass_init(lawngrass):
    assert lawngrass.name == "Lawngrass"
    assert lawngrass.description == "Lawngrass small size"
    assert lawngrass.price == 1500.0
    assert lawngrass.quantity == 5
    assert lawngrass.country == "Russia"
    assert lawngrass.germination_period == "2 month"
    assert lawngrass.color == "Зелёный"
