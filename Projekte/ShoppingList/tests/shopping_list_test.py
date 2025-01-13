from shopping_list import ShoppingList, ShoppingListItem
import pytest


@pytest.fixture
def shopping_list():
    return ShoppingList.from_item_values([("Tea", 2.5), ("Coffee", 7.0, 2)])


def test_from_item_values():
    sl = ShoppingList.from_item_values([("Tea", 2.5), ("Coffee", 7.0, 2)])
    assert isinstance(sl, ShoppingList)
    assert sl.items == [
        ShoppingListItem("Tea", 2.5),
        ShoppingListItem("Coffee", 7.0, 2),
    ]


def test_str(shopping_list):
    assert str(shopping_list) == (
        "Shopping List\n"
        "  1 x Tea à 2.5 = 2.5\n"
        "  2 x Coffee à 7.0 = 14.0\n"
        "Total: 16.5"
    )


def test_len(shopping_list):
    assert len(shopping_list) == 2


def test_getitem_with_int_index(shopping_list):
    assert shopping_list[0] == ShoppingListItem("Tea", 2.5)


def test_getitem_with_string_index(shopping_list):
    assert shopping_list["Tea"] == [ShoppingListItem("Tea", 2.5)]
    assert shopping_list["Water"] == []


def test_find_product(shopping_list):
    assert shopping_list.find_by_product_name("Tea") == [ShoppingListItem("Tea", 2.5)]
    assert shopping_list.find_by_product_name("Water") == []


def test_add_item():
    sl = ShoppingList()
    sl.add_item(ShoppingListItem("Butter", 2.5, 2))
    assert sl == ShoppingList([ShoppingListItem("Butter", 2.5, 2)])
