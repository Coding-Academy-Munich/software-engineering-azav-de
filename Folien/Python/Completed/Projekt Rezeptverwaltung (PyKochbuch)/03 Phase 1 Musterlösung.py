# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Phase 1: Musterlösung</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
#
# <div style="text-align:center;">Coding-Akademie München</div>
# <br/>


# %% [markdown]
#
# # Phase 1: Musterlösung
#
# Hier finden Sie die vollständige Implementierung für Phase 1. Versuchen Sie,
# die Aufgaben zuerst selbst zu lösen, bevor Sie hier nachschauen.

# %% [markdown]
#
# ## `unit.py`
#
# Das Enum definiert die Maßeinheiten mit ihren Abkürzungen. Die Konvertierung
# nutzt ein Dictionary mit Tupeln als Schlüssel.

# %% [markdown]
#
# ```python
# from __future__ import annotations
#
# from enum import Enum
#
#
# class Unit(Enum):
#     GRAM = "g"
#     KILOGRAM = "kg"
#     MILLILITER = "ml"
#     LITER = "l"
#     PIECE = "pc"
#     TABLESPOON = "tbsp"
#     TEASPOON = "tsp"
#
#
# CONVERSIONS: dict[tuple[Unit, Unit], float] = {
#     (Unit.GRAM, Unit.KILOGRAM): 0.001,
#     (Unit.KILOGRAM, Unit.GRAM): 1000,
#     (Unit.MILLILITER, Unit.LITER): 0.001,
#     (Unit.LITER, Unit.MILLILITER): 1000,
# }
#
#
# def units_are_compatible(a: Unit, b: Unit) -> bool:
#     return a == b or (a, b) in CONVERSIONS
#
#
# def convert(amount: float, from_unit: Unit, to_unit: Unit) -> float:
#     if from_unit == to_unit:
#         return amount
#     factor = CONVERSIONS.get((from_unit, to_unit))
#     if factor is None:
#         raise ValueError(f"Cannot convert {from_unit.value} to {to_unit.value}")
#     return amount * factor
# ```

# %% [markdown]
#
# ## `ingredient.py`
#
# Die frozen Dataclass nutzt `object.__setattr__` in `__post_init__`, um den
# Namen trotz `frozen=True` zu normalisieren.

# %% [markdown]
#
# ```python
# from __future__ import annotations
#
# from dataclasses import dataclass
#
# from pykochbuch.unit import Unit
#
#
# @dataclass(frozen=True)
# class Ingredient:
#     name: str
#     amount: float
#     unit: Unit
#
#     def __post_init__(self) -> None:
#         normalized = self.name.strip().lower()
#         if not normalized:
#             raise ValueError("Ingredient name must not be empty")
#         object.__setattr__(self, "name", normalized)
#         if self.amount <= 0:
#             raise ValueError("Ingredient amount must be positive")
#
#     def scale(self, factor: float) -> Ingredient:
#         return Ingredient(name=self.name, amount=self.amount * factor, unit=self.unit)
#
#     def __str__(self) -> str:
#         return f"{self.amount:g}{self.unit.value} {self.name}"
# ```

# %% [markdown]
#
# ## `recipe.py`
#
# Das Recipe nutzt `tuple` und `frozenset` für unveränderliche Sammlungen.
# Die `scale`-Methode erzeugt immer ein neues Objekt.

# %% [markdown]
#
# ```python
# from __future__ import annotations
#
# from dataclasses import dataclass, field
#
# from pykochbuch.ingredient import Ingredient
#
#
# @dataclass
# class Recipe:
#     title: str
#     description: str = ""
#     servings: int = 4
#     prep_time_minutes: int = 0
#     ingredients: tuple[Ingredient, ...] = ()
#     instructions: tuple[str, ...] = ()
#     tags: frozenset[str] = field(default_factory=frozenset)
#
#     def __post_init__(self) -> None:
#         if not self.title.strip():
#             raise ValueError("Recipe title must not be empty")
#         if self.servings <= 0:
#             raise ValueError("Servings must be greater than zero")
#         if self.prep_time_minutes < 0:
#             raise ValueError("Prep time must be non-negative")
#         if not self.ingredients:
#             raise ValueError("Recipe must have at least one ingredient")
#         if not self.instructions:
#             raise ValueError("Recipe must have at least one instruction")
#
#     def scale(self, factor: float) -> Recipe:
#         return Recipe(
#             title=self.title,
#             description=self.description,
#             servings=max(1, round(self.servings * factor)),
#             prep_time_minutes=self.prep_time_minutes,
#             ingredients=tuple(i.scale(factor) for i in self.ingredients),
#             instructions=self.instructions,
#             tags=self.tags,
#         )
#
#     def scale_to_servings(self, n: int) -> Recipe:
#         if n <= 0:
#             raise ValueError("Target servings must be greater than zero")
#         return self.scale(n / self.servings)
# ```

# %% [markdown]
#
# ## `recipe_book.py`
#
# Das RecipeBook speichert Rezepte in einem Dictionary mit dem Titel in
# Kleinbuchstaben als Schlüssel.

# %% [markdown]
#
# ```python
# from __future__ import annotations
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
# ```

# %% [markdown]
#
# ## Beispieltests
#
# Die folgenden Tests zeigen, wie Ihre Tests aussehen könnten. Schreiben Sie
# weitere Tests für alle Validierungsregeln und Randfälle.
#
# ### `unit_test.py`

# %% [markdown]
#
# ```python
# import pytest
# from pykochbuch.unit import Unit, convert, units_are_compatible
#
#
# def test_gram_to_kilogram():
#     assert convert(1000, Unit.GRAM, Unit.KILOGRAM) == pytest.approx(1.0)
#
#
# def test_same_unit_returns_unchanged():
#     assert convert(500, Unit.GRAM, Unit.GRAM) == pytest.approx(500)
#
#
# def test_incompatible_units_raise():
#     with pytest.raises(ValueError):
#         convert(100, Unit.GRAM, Unit.LITER)
#
#
# def test_compatible_units():
#     assert units_are_compatible(Unit.GRAM, Unit.KILOGRAM)
#     assert units_are_compatible(Unit.GRAM, Unit.GRAM)
#     assert not units_are_compatible(Unit.GRAM, Unit.LITER)
# ```

# %% [markdown]
#
# ### `ingredient_test.py`

# %% [markdown]
#
# ```python
# import pytest
# from pykochbuch.ingredient import Ingredient
# from pykochbuch.unit import Unit
#
#
# def test_creation_normalizes_name():
#     ing = Ingredient("  Mehl  ", 500, Unit.GRAM)
#     assert ing.name == "mehl"
#     assert ing.amount == 500
#     assert ing.unit == Unit.GRAM
#
#
# def test_rejects_empty_name():
#     with pytest.raises(ValueError):
#         Ingredient("", 100, Unit.GRAM)
#
#
# def test_rejects_whitespace_only_name():
#     with pytest.raises(ValueError):
#         Ingredient("   ", 100, Unit.GRAM)
#
#
# def test_rejects_negative_amount():
#     with pytest.raises(ValueError):
#         Ingredient("Mehl", -1, Unit.GRAM)
#
#
# def test_rejects_zero_amount():
#     with pytest.raises(ValueError):
#         Ingredient("Mehl", 0, Unit.GRAM)
#
#
# @pytest.mark.parametrize("factor,expected", [(2, 1000), (0.5, 250), (1, 500)])
# def test_scaling(factor, expected):
#     ing = Ingredient("Mehl", 500, Unit.GRAM)
#     scaled = ing.scale(factor)
#     assert scaled.amount == pytest.approx(expected)
#     assert scaled.name == "mehl"
#     assert scaled.unit == Unit.GRAM
# ```
