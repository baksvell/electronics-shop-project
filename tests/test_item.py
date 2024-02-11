from src.item import Item


def test_calculate_total_price():
    item = Item("TestItem", 400, 5)
    assert item.calculate_total_price() == 2000


def test_apply_discount():
    item = Item("TestItem", 400, 3)
    Item.pay_rate = 0.5
    item.apply_discount()
    assert item.price == 400 * Item.pay_rate


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_get_name():
    item = Item("TestItem", 4, 5)
    assert item.name == "TestItem"

def test_set_name():
    item = Item("TestItem", 4, 5)
    item.name = "Test"
    assert item.name == "Test"
    item.name = "TestItem_set"
    assert item.name == "TestItem_s"


def test_instantiate_from_csv():
    Item.instantiate_from_csv('items.csv')
    assert len(Item.all) == 5


def test_repr():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Велосипед", 100000, 200)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"
    assert repr(item2) == "Item('Велосипед', 100000, 200)"


def test_str():
    item2 = Item("Велосипед", 100000, 200)
    assert str(item2) == 'Велосипед'