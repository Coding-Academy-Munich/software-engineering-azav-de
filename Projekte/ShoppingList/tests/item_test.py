from shopping_list import ShoppingListItem


def test_default_args():
    item = ShoppingListItem("Coffee", 1.99)
    assert item.amount == 1
