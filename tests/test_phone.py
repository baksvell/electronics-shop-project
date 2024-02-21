from src.item import Item
from src.phone import Phone

phone1 = Phone("iPhone 14", 120_000, 5, 2)

item1 = Item("Смартфон", 10000, 20)


def test__init__():
    assert phone1.name == "iPhone 14"
    assert phone1.price == 120_000
    assert phone1.quantity == 5
    assert phone1.number_of_sim == 2


def test__repr__():
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"


def test__str__():
    assert str(phone1) == "iPhone 14"


def test__add__():
    assert item1 + phone1 == 25
    assert phone1 + item1 == 25
    assert phone1 + 15 is None
