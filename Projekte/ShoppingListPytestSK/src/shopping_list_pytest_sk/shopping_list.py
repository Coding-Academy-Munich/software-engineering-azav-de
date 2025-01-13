from dataclasses import dataclass, field  # noqa
from typing import Sequence


@dataclass
class ShoppingListItem:
    product: str
    amount: str = field(default="1")


@dataclass
class ShoppingList:
    items: list[ShoppingListItem] = field(default_factory=list)

    @staticmethod
    def from_item_values(item_values: Sequence[tuple[str, str]]):
        """Create a shopping list from item values.

        Each item value in `item_values` is a tuple of product name and amount."""
        items = [ShoppingListItem(product, amount) for product, amount in item_values]
        return ShoppingList(items)

    def __str__(self):
        """Convert a shopping list into a string."""
        result = "Shopping List\n"
        for item in self.items:
            result += f"  {item.product} ({item.amount})\n"
        return result

    def __len__(self):
        """Return the number of items in a shopping list."""
        return len(self.items)

    def __getitem__(self, n):
        """Return an item, either by index or product name."""
        if isinstance(n, str):
            return self.find_by_product_name(n)
        return self.items[n]

    def find_by_product_name(self, product_name: str):
        """Find an item given its product name."""
        for item in self.items:
            if item.product == product_name:
                return item
        return None

    def add_item(self, item: ShoppingListItem):
        """Add an item to a shopping list if it is not already in the list.

        Raises an error of type ValueError if an item with the same product name
        is already contained in the shopping list."""
        if self.find_by_product_name(item.product):
            raise ValueError(f"Shopping list already contains {item.product}.")
        self.items.append(item)
