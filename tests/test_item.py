from src.item import Item


def test_calculate_total_price():
    item = Item("TestItem", 400, 5)
    assert item.calculate_total_price() == 2000


def test_apply_discount():
    item = Item("TestItem", 400, 3)
    Item.pay_rate = 0.5
    item.apply_discount()
    assert item.price == 400 * Item.pay_rate
