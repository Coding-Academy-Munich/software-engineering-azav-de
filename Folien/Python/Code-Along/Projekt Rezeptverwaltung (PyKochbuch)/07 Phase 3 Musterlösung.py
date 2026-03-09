# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Phase 3: Musterlösung</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
#
# <div style="text-align:center;">Coding-Akademie München</div>
# <br/>


# %% [markdown]
#
# # Phase 3: Musterlösung

# %% [markdown]
#
# ## `storage.py` (Serialisierung und `JsonStore`)
#
# Die Datei enthält die Hilfsfunktionen für die Serialisierung und die
# `JsonStore`-Klasse.

# %% [markdown]
#
# ```python
# from __future__ import annotations
#
# import json
# import re
# from pathlib import Path
#
# from pykochbuch.ingredient import Ingredient
# from pykochbuch.recipe import Recipe
# from pykochbuch.unit import Unit
#
#
# def _recipe_to_dict(recipe: Recipe) -> dict:
#     return {
#         "title": recipe.title,
#         "description": recipe.description,
#         "servings": recipe.servings,
#         "prep_time_minutes": recipe.prep_time_minutes,
#         "ingredients": [
#             {"name": i.name, "amount": i.amount, "unit": i.unit.value}
#             for i in recipe.ingredients
#         ],
#         "instructions": list(recipe.instructions),
#         "tags": sorted(recipe.tags),
#     }
#
#
# def _dict_to_recipe(data: dict) -> Recipe:
#     return Recipe(
#         title=data["title"],
#         description=data.get("description", ""),
#         servings=data["servings"],
#         prep_time_minutes=data.get("prep_time_minutes", 0),
#         ingredients=tuple(
#             Ingredient(
#                 name=i["name"],
#                 amount=i["amount"],
#                 unit=Unit(i["unit"]),
#             )
#             for i in data["ingredients"]
#         ),
#         instructions=tuple(data["instructions"]),
#         tags=frozenset(data.get("tags", [])),
#     )
#
#
# class JsonStore:
#     def __init__(self, path: Path) -> None:
#         self._path = path
#
#     def _load_all(self) -> list[dict]:
#         if not self._path.exists():
#             return []
#         with open(self._path, encoding="utf-8") as f:
#             return json.load(f)
#
#     def _save_all(self, data: list[dict]) -> None:
#         with open(self._path, "w", encoding="utf-8") as f:
#             json.dump(data, f, indent=2, ensure_ascii=False)
#
#     def save_recipe(self, recipe: Recipe) -> None:
#         data = self._load_all()
#         for entry in data:
#             if entry["title"].lower() == recipe.title.lower():
#                 raise ValueError(f"Recipe '{recipe.title}' already exists")
#         data.append(_recipe_to_dict(recipe))
#         self._save_all(data)
#
#     def get_recipe(self, title: str) -> Recipe:
#         data = self._load_all()
#         for entry in data:
#             if entry["title"].lower() == title.lower():
#                 return _dict_to_recipe(entry)
#         raise KeyError(f"Recipe '{title}' not found")
#
#     def get_all_recipes(self) -> list[Recipe]:
#         return [_dict_to_recipe(entry) for entry in self._load_all()]
#
#     def delete_recipe(self, title: str) -> None:
#         data = self._load_all()
#         new_data = [e for e in data if e["title"].lower() != title.lower()]
#         if len(new_data) == len(data):
#             raise KeyError(f"Recipe '{title}' not found")
#         self._save_all(new_data)
#
#     def search_by_title(self, query: str) -> list[Recipe]:
#         pattern = re.compile(query, re.IGNORECASE)
#         return [
#             _dict_to_recipe(entry)
#             for entry in self._load_all()
#             if pattern.search(entry["title"])
#         ]
# ```

# %% [markdown]
#
# ## Beispieltests
#
# ### `storage_test.py`

# %% [markdown]
#
# ```python
# import pytest
# from pykochbuch.ingredient import Ingredient
# from pykochbuch.recipe import Recipe
# from pykochbuch.storage import JsonStore
# from pykochbuch.unit import Unit
#
#
# @pytest.fixture
# def pancakes():
#     return Recipe(
#         title="Pancakes",
#         description="Classic pancakes",
#         servings=4,
#         prep_time_minutes=20,
#         ingredients=(
#             Ingredient("flour", 250, Unit.GRAM),
#             Ingredient("milk", 500, Unit.MILLILITER),
#             Ingredient("eggs", 2, Unit.PIECE),
#         ),
#         instructions=("Mix ingredients", "Cook on pan"),
#         tags=frozenset({"breakfast", "quick"}),
#     )
#
#
# def test_save_and_load_round_trip(tmp_path, pancakes):
#     store = JsonStore(tmp_path / "recipes.json")
#     store.save_recipe(pancakes)
#     result = store.get_recipe("Pancakes")
#     assert result.title == "Pancakes"
#     assert result.servings == 4
#     assert len(result.ingredients) == 3
#     assert result.tags == frozenset({"breakfast", "quick"})
#
#
# def test_get_all_empty_file(tmp_path):
#     store = JsonStore(tmp_path / "recipes.json")
#     assert store.get_all_recipes() == []
#
#
# def test_duplicate_raises(tmp_path, pancakes):
#     store = JsonStore(tmp_path / "recipes.json")
#     store.save_recipe(pancakes)
#     with pytest.raises(ValueError, match="already exists"):
#         store.save_recipe(pancakes)
#
#
# def test_get_nonexistent_raises(tmp_path):
#     store = JsonStore(tmp_path / "recipes.json")
#     with pytest.raises(KeyError):
#         store.get_recipe("Unknown")
#
#
# def test_delete_recipe(tmp_path, pancakes):
#     store = JsonStore(tmp_path / "recipes.json")
#     store.save_recipe(pancakes)
#     store.delete_recipe("Pancakes")
#     assert store.get_all_recipes() == []
#
#
# def test_ingredient_amounts_survive_round_trip(tmp_path, pancakes):
#     store = JsonStore(tmp_path / "recipes.json")
#     store.save_recipe(pancakes)
#     result = store.get_recipe("Pancakes")
#     by_name = {i.name: i for i in result.ingredients}
#     assert by_name["flour"].amount == pytest.approx(250)
#     assert by_name["flour"].unit == Unit.GRAM
# ```
