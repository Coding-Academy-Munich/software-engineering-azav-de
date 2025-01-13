from shopping_list_pytest.shopping_list import ShoppingListItem

def test_default_value_for_amount():
    unit = ShoppingListItem("eggs")
    assert unit.amount == "1"