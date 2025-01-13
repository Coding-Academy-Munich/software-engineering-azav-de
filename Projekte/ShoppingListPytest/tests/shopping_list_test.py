import pytest

from shopping_list_pytest.shopping_list import ShoppingList, ShoppingListItem


@pytest.fixture
def items():
    return [ShoppingListItem("Tea", "50 tea bags"), ShoppingListItem("Coffee", "500g")]


@pytest.fixture
def shopping_list(items):
    return ShoppingList(items)


def test_shopping_list_from_item_values(items):
    sl = ShoppingList.from_item_values([("Tea", "50 tea bags"), ("Coffee", "500g")])
    assert sl.items == items


def test_shopping_list_to_string(shopping_list):
    assert str(ShoppingList()).strip() == "Shopping List"
    assert str(shopping_list).strip() == 'Shopping List\n  Tea (50 tea bags)\n  Coffee (500g)'


def test_shopping_list_len(shopping_list):
    assert len(ShoppingList()) == 0
    assert len(shopping_list) == 2


def test_shopping_list_getitem_for_numerical_index(shopping_list):
    assert shopping_list[0] == ShoppingListItem("Tea", "50 tea bags")
    assert shopping_list[1] == ShoppingListItem("Coffee", "500g")

    with pytest.raises(IndexError):
        shopping_list[2]  # noqa


def test_shopping_list_getitem_for_string_index(shopping_list):
    assert shopping_list["Tea"] == ShoppingListItem("Tea", "50 tea bags")
    assert shopping_list["Water"] is None


def test_shopping_list_add_item_for_new_item(shopping_list):
    shopping_list.add_item(ShoppingListItem("Milk", "500g"))
    assert shopping_list.items == [
        ShoppingListItem("Tea", "50 tea bags"),
        ShoppingListItem("Coffee", "500g"),
        ShoppingListItem("Milk", "500g"),
    ]


def test_shopping_list_add_item_for_existing_item(shopping_list):
    with pytest.raises(ValueError):
        shopping_list.add_item(ShoppingListItem("Tea", "100g"))
