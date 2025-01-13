from dataclasses import dataclass, field  # noqa
from typing import Sequence


@dataclass
class ShoppingListItem:
    product: str
    price: float
    amount: int = 1

    def total_price(self):
        """Return the total price of an item.

        >>> ShoppingListItem("Tea", 2.5).total_price()
        2.5
        >>> ShoppingListItem("Tea", 2.5, 2).total_price()
        5.0
        """
        return self.price * self.amount


@dataclass
class ShoppingList:
    items: list[ShoppingListItem] = field(default_factory=list)

    @staticmethod
    def from_item_values(
        item_values: Sequence[tuple[str, float] | tuple[str, float, int]]
    ):
        """Create a shopping list from item values.

        Each item value in `item_values` is a tuple of product name, price per item,
        and optional amount.
        >>> ShoppingList.from_item_values([("Tea", 2.5), ("Coffee", 7.0, 2)])
        ShoppingList(items=[ShoppingListItem(product='Tea', price=2.5, amount=1),\
                            ShoppingListItem(product='Coffee', price=7.0, amount=2)])
        """
        items = [ShoppingListItem(*values) for values in item_values]
        return ShoppingList(items)

    def __str__(self):
        """Convert a shopping list into a string.

        >>> print(ShoppingList().from_item_values([("Tea", 2.5), ("Coffee", 7.0, 2)]))
        Shopping List
          1 x Tea à 2.5 = 2.5
          2 x Coffee à 7.0 = 14.0
        Total: 16.5
        """
        result = f"Shopping List\n"
        for item in self.items:
            result += (
                f"  {item.amount} x {item.product} à {item.price}"
                f" = {item.total_price()}\n"
            )
        result += f"Total: {self.total_price()}"
        return result

    def __len__(self):
        """Return the number of items in a shopping list.

        >>> len(ShoppingList())
        0
        >>> len(ShoppingList.from_item_values([("Tea", 2.5), ("Coffee", 7.0, 2)]))
        2
        """
        return len(self.items)

    def __getitem__(self, n):
        """Return an item, either by index or product name.

        >>> sl = ShoppingList.from_item_values(
        ...          [("Tea", 2.5), ("Coffee", 7.0, 2), ("Tea", 3.5)])
        >>> sl[0]
        ShoppingListItem(product='Tea', price=2.5, amount=1)
        >>> sl["Tea"]
        [ShoppingListItem(product='Tea', price=2.5, amount=1),
         ShoppingListItem(product='Tea', price=3.5, amount=1)]
        >>> sl["Coffee"]
        [ShoppingListItem(product='Coffee', price=7.0, amount=2)]
        >>> sl["Water"]
        []
        """

        if isinstance(n, str):
            return self.find_by_product_name(n)
        return self.items[n]

    def find_by_product_name(self, product: str):
        """Find items given their product name.

        >>> sl = ShoppingList.from_item_values(
        ...          [("Tea", 2.5), ("Coffee", 7.0, 2), ("Tea", 3.5)])
        >>> sl.find_by_product_name("Tea")
        [ShoppingListItem(product='Tea', price=2.5, amount=1),
         ShoppingListItem(product='Tea', price=3.5, amount=1)]
        >>> sl.find_by_product_name("Coffee")
        [ShoppingListItem(product='Coffee', price=7.0, amount=2)]
        """
        return [item for item in self.items if item.product == product]

    def add_item(self, item: ShoppingListItem):
        """Add an item to a shopping list.

        If an item with the same product name and price already exists, the amount
        is increased instead of adding a new item.

        >>> sl = ShoppingList()
        >>> sl.add_item(ShoppingListItem("Tea", 2.5))
        >>> sl.add_item(ShoppingListItem("Coffee", 7.0, 2))
        >>> sl.add_item(ShoppingListItem("Tea", 3.5))
        >>> sl.add_item(ShoppingListItem("Tea", 2.5))
        >>> sl
        ShoppingList(items=[ShoppingListItem(product='Tea', price=2.5, amount=2),
                            ShoppingListItem(product='Coffee', price=7.0, amount=2),
                            ShoppingListItem(product='Tea', price=3.5, amount=1)])
        """
        for existing_product in self.items:
            if (
                existing_product.product == item.product
                and existing_product.price == item.price
            ):
                existing_product.amount += item.amount
                return
        self.items.append(item)

    def total_price(self):
        """Return the total price of a shopping list.

        >>> ShoppingList().total_price()
        0
        >>> ShoppingList.from_item_values([("Tea", 2.5), ("Coffee", 7.0, 2)]).total_price()
        16.5
        """
        return round(sum(item.total_price() for item in self.items), 2)
