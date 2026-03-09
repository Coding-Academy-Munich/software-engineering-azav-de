# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Phase 2: Musterlösung</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
#
# <div style="text-align:center;">Coding-Akademie München</div>
# <br/>


# %% [markdown]
#
# # Phase 2: Musterlösung

# %% [markdown]
#
# ## Erweiterte `recipe_book.py`
#
# Die Suchmethoden verwenden List Comprehensions. Die kombinierte Suche nutzt
# Mengen-Schnittmenge (`&`), um Ergebnisse zu kombinieren.

# %% [markdown]
#
# ```python
# from __future__ import annotations
#
# import re
#
# from pykochbuch.recipe import Recipe
#
#
# class RecipeBook:
#     def __init__(self) -> None:
#         self._recipes: dict[str, Recipe] = {}
#
#     def add_recipe(self, recipe: Recipe) -> None:
#         key = recipe.title.lower()
#         if key in self._recipes:
#             raise ValueError(f"Recipe '{recipe.title}' already exists")
#         self._recipes[key] = recipe
#
#     def remove_recipe(self, title: str) -> None:
#         key = title.lower()
#         if key not in self._recipes:
#             raise KeyError(f"Recipe '{title}' not found")
#         del self._recipes[key]
#
#     def get_recipe(self, title: str) -> Recipe:
#         key = title.lower()
#         if key not in self._recipes:
#             raise KeyError(f"Recipe '{title}' not found")
#         return self._recipes[key]
#
#     @property
#     def recipes(self) -> list[Recipe]:
#         return list(self._recipes.values())
#
#     def search_by_title(self, query: str) -> list[Recipe]:
#         pattern = re.compile(query, re.IGNORECASE)
#         return [r for r in self._recipes.values() if pattern.search(r.title)]
#
#     def search_by_ingredient(self, name: str) -> list[Recipe]:
#         name_lower = name.lower()
#         return [
#             r
#             for r in self._recipes.values()
#             if any(i.name == name_lower for i in r.ingredients)
#         ]
#
#     def search_by_tag(self, tag: str) -> list[Recipe]:
#         return [r for r in self._recipes.values() if tag in r.tags]
#
#     def filter_by_max_time(self, minutes: int) -> list[Recipe]:
#         return [
#             r for r in self._recipes.values() if r.prep_time_minutes <= minutes
#         ]
#
#     def search(
#         self,
#         title: str | None = None,
#         ingredient: str | None = None,
#         tag: str | None = None,
#         max_time: int | None = None,
#     ) -> list[Recipe]:
#         results: set[str] | None = None
#
#         def intersect(recipes: list[Recipe]) -> None:
#             nonlocal results
#             keys = {r.title.lower() for r in recipes}
#             if results is None:
#                 results = keys
#             else:
#                 results &= keys
#
#         if title is not None:
#             intersect(self.search_by_title(title))
#         if ingredient is not None:
#             intersect(self.search_by_ingredient(ingredient))
#         if tag is not None:
#             intersect(self.search_by_tag(tag))
#         if max_time is not None:
#             intersect(self.filter_by_max_time(max_time))
#
#         if results is None:
#             return self.recipes
#
#         return [self._recipes[key] for key in results]
# ```

# %% [markdown]
#
# ## `shopping_list.py`
#
# Die Einkaufsliste speichert Zutaten in einem Dictionary. Beim Hinzufügen
# werden kompatible Einheiten konvertiert und Mengen addiert.

# %% [markdown]
#
# ```python
# from __future__ import annotations
#
# from pykochbuch.ingredient import Ingredient
# from pykochbuch.recipe import Recipe
# from pykochbuch.unit import convert, units_are_compatible
#
#
# class ShoppingList:
#     def __init__(self) -> None:
#         self._items: dict[str, Ingredient] = {}
#
#     def add_recipe(self, recipe: Recipe) -> None:
#         for ingredient in recipe.ingredients:
#             key = ingredient.name
#             if key in self._items:
#                 existing = self._items[key]
#                 if not units_are_compatible(existing.unit, ingredient.unit):
#                     raise ValueError(
#                         f"Cannot merge '{key}': incompatible units "
#                         f"{existing.unit.value} and {ingredient.unit.value}"
#                     )
#                 converted_amount = convert(
#                     ingredient.amount, ingredient.unit, existing.unit
#                 )
#                 self._items[key] = Ingredient(
#                     name=key,
#                     amount=existing.amount + converted_amount,
#                     unit=existing.unit,
#                 )
#             else:
#                 self._items[key] = ingredient
#
#     @property
#     def items(self) -> list[Ingredient]:
#         return list(self._items.values())
#
#     def __str__(self) -> str:
#         if not self._items:
#             return "Shopping list is empty"
#         lines = ["Shopping List:", "-------------"]
#         for item in self._items.values():
#             lines.append(f"  {item}")
#         return "\n".join(lines)
#
#     @classmethod
#     def from_recipes(cls, recipes: list[Recipe]) -> ShoppingList:
#         shopping_list = cls()
#         for recipe in recipes:
#             shopping_list.add_recipe(recipe)
#         return shopping_list
# ```

# %% [markdown]
#
# ## Beispieltests
#
# ### `shopping_list_test.py`

# %% [markdown]
#
# ```python
# import pytest
# from pykochbuch.ingredient import Ingredient
# from pykochbuch.recipe import Recipe
# from pykochbuch.shopping_list import ShoppingList
# from pykochbuch.unit import Unit
#
#
# @pytest.fixture
# def pancakes():
#     return Recipe(
#         title="Pancakes",
#         servings=4,
#         ingredients=(
#             Ingredient("flour", 250, Unit.GRAM),
#             Ingredient("milk", 500, Unit.MILLILITER),
#             Ingredient("eggs", 2, Unit.PIECE),
#         ),
#         instructions=("Mix", "Cook"),
#     )
#
#
# @pytest.fixture
# def cake():
#     return Recipe(
#         title="Cake",
#         servings=8,
#         ingredients=(
#             Ingredient("flour", 300, Unit.GRAM),
#             Ingredient("sugar", 200, Unit.GRAM),
#             Ingredient("eggs", 3, Unit.PIECE),
#         ),
#         instructions=("Mix", "Bake"),
#     )
#
#
# def test_merge_same_unit(pancakes, cake):
#     sl = ShoppingList.from_recipes([pancakes, cake])
#     items_by_name = {i.name: i for i in sl.items}
#     assert items_by_name["flour"].amount == pytest.approx(550)
#     assert items_by_name["eggs"].amount == 5
#
#
# def test_merge_compatible_units(pancakes):
#     bread = Recipe(
#         title="Bread",
#         servings=1,
#         ingredients=(Ingredient("flour", 1, Unit.KILOGRAM),),
#         instructions=("Bake",),
#     )
#     sl = ShoppingList.from_recipes([pancakes, bread])
#     items_by_name = {i.name: i for i in sl.items}
#     assert items_by_name["flour"].amount == pytest.approx(1250)
#
#
# def test_incompatible_units_raises():
#     r1 = Recipe(
#         title="A",
#         ingredients=(Ingredient("stuff", 100, Unit.GRAM),),
#         instructions=("Do",),
#     )
#     r2 = Recipe(
#         title="B",
#         ingredients=(Ingredient("stuff", 200, Unit.MILLILITER),),
#         instructions=("Do",),
#     )
#     sl = ShoppingList()
#     sl.add_recipe(r1)
#     with pytest.raises(ValueError, match="incompatible"):
#         sl.add_recipe(r2)
#
#
# def test_empty_list():
#     sl = ShoppingList.from_recipes([])
#     assert sl.items == []
# ```
