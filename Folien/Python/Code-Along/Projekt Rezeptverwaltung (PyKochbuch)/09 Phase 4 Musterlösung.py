# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Phase 4: Musterlösung</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
#
# <div style="text-align:center;">Coding-Akademie München</div>
# <br/>


# %% [markdown]
#
# # Phase 4: Musterlösung

# %% [markdown]
#
# ## Vollständige `storage.py`
#
# Diese Datei enthält die abstrakte Schnittstelle `RecipeStore` und alle drei
# Implementierungen: `InMemoryStore`, `JsonStore` und `SqliteStore`.

# %% [markdown]
#
# ```python
# from __future__ import annotations
#
# import json
# import re
# import sqlite3
# from abc import ABC, abstractmethod
# from pathlib import Path
#
# from pykochbuch.ingredient import Ingredient
# from pykochbuch.recipe import Recipe
# from pykochbuch.recipe_book import RecipeBook
# from pykochbuch.unit import Unit
#
#
# class RecipeStore(ABC):
#     @abstractmethod
#     def save_recipe(self, recipe: Recipe) -> None: ...
#
#     @abstractmethod
#     def get_recipe(self, title: str) -> Recipe: ...
#
#     @abstractmethod
#     def get_all_recipes(self) -> list[Recipe]: ...
#
#     @abstractmethod
#     def delete_recipe(self, title: str) -> None: ...
#
#     @abstractmethod
#     def search_by_title(self, query: str) -> list[Recipe]: ...
#
#
# class InMemoryStore(RecipeStore):
#     def __init__(self) -> None:
#         self._book = RecipeBook()
#
#     def save_recipe(self, recipe: Recipe) -> None:
#         self._book.add_recipe(recipe)
#
#     def get_recipe(self, title: str) -> Recipe:
#         return self._book.get_recipe(title)
#
#     def get_all_recipes(self) -> list[Recipe]:
#         return self._book.recipes
#
#     def delete_recipe(self, title: str) -> None:
#         self._book.remove_recipe(title)
#
#     def search_by_title(self, query: str) -> list[Recipe]:
#         return self._book.search_by_title(query)
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
# class JsonStore(RecipeStore):
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
#
#
# class SqliteStore(RecipeStore):
#     def __init__(self, db_path: str | Path) -> None:
#         self.connection = sqlite3.connect(str(db_path))
#         self._create_tables()
#
#     def _create_tables(self) -> None:
#         cursor = self.connection.cursor()
#         cursor.execute(
#             """CREATE TABLE IF NOT EXISTS recipes (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 title TEXT UNIQUE NOT NULL,
#                 description TEXT NOT NULL DEFAULT '',
#                 servings INTEGER NOT NULL,
#                 prep_time_minutes INTEGER NOT NULL DEFAULT 0
#             )"""
#         )
#         cursor.execute(
#             """CREATE TABLE IF NOT EXISTS ingredients (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 recipe_id INTEGER NOT NULL,
#                 name TEXT NOT NULL,
#                 amount REAL NOT NULL,
#                 unit TEXT NOT NULL,
#                 FOREIGN KEY (recipe_id) REFERENCES recipes(id)
#             )"""
#         )
#         cursor.execute(
#             """CREATE TABLE IF NOT EXISTS instructions (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 recipe_id INTEGER NOT NULL,
#                 step_number INTEGER NOT NULL,
#                 instruction TEXT NOT NULL,
#                 FOREIGN KEY (recipe_id) REFERENCES recipes(id)
#             )"""
#         )
#         cursor.execute(
#             """CREATE TABLE IF NOT EXISTS recipe_tags (
#                 recipe_id INTEGER NOT NULL,
#                 tag TEXT NOT NULL,
#                 PRIMARY KEY (recipe_id, tag),
#                 FOREIGN KEY (recipe_id) REFERENCES recipes(id)
#             )"""
#         )
#         self.connection.commit()
#
#     def save_recipe(self, recipe: Recipe) -> None:
#         cursor = self.connection.cursor()
#         try:
#             cursor.execute(
#                 "INSERT INTO recipes (title, description, servings, prep_time_minutes) "
#                 "VALUES (?, ?, ?, ?)",
#                 (recipe.title, recipe.description, recipe.servings,
#                  recipe.prep_time_minutes),
#             )
#         except sqlite3.IntegrityError:
#             raise ValueError(f"Recipe '{recipe.title}' already exists")
#         recipe_id = cursor.lastrowid
#         for ingredient in recipe.ingredients:
#             cursor.execute(
#                 "INSERT INTO ingredients (recipe_id, name, amount, unit) "
#                 "VALUES (?, ?, ?, ?)",
#                 (recipe_id, ingredient.name, ingredient.amount,
#                  ingredient.unit.value),
#             )
#         for step_number, instruction in enumerate(recipe.instructions):
#             cursor.execute(
#                 "INSERT INTO instructions (recipe_id, step_number, instruction) "
#                 "VALUES (?, ?, ?)",
#                 (recipe_id, step_number, instruction),
#             )
#         for tag in recipe.tags:
#             cursor.execute(
#                 "INSERT INTO recipe_tags (recipe_id, tag) VALUES (?, ?)",
#                 (recipe_id, tag),
#             )
#         self.connection.commit()
#
#     def _load_recipe_by_row(self, row: tuple) -> Recipe:
#         recipe_id, title, description, servings, prep_time_minutes = row
#         cursor = self.connection.cursor()
#         cursor.execute(
#             "SELECT name, amount, unit FROM ingredients WHERE recipe_id = ?",
#             (recipe_id,),
#         )
#         ingredients = tuple(
#             Ingredient(name=name, amount=amount, unit=Unit(unit))
#             for name, amount, unit in cursor.fetchall()
#         )
#         cursor.execute(
#             "SELECT instruction FROM instructions WHERE recipe_id = ? "
#             "ORDER BY step_number",
#             (recipe_id,),
#         )
#         instructions = tuple(row[0] for row in cursor.fetchall())
#         cursor.execute(
#             "SELECT tag FROM recipe_tags WHERE recipe_id = ?", (recipe_id,)
#         )
#         tags = frozenset(row[0] for row in cursor.fetchall())
#         return Recipe(
#             title=title,
#             description=description,
#             servings=servings,
#             prep_time_minutes=prep_time_minutes,
#             ingredients=ingredients,
#             instructions=instructions,
#             tags=tags,
#         )
#
#     def get_recipe(self, title: str) -> Recipe:
#         cursor = self.connection.cursor()
#         cursor.execute(
#             "SELECT id, title, description, servings, prep_time_minutes "
#             "FROM recipes WHERE LOWER(title) = LOWER(?)",
#             (title,),
#         )
#         row = cursor.fetchone()
#         if row is None:
#             raise KeyError(f"Recipe '{title}' not found")
#         return self._load_recipe_by_row(row)
#
#     def get_all_recipes(self) -> list[Recipe]:
#         cursor = self.connection.cursor()
#         cursor.execute(
#             "SELECT id, title, description, servings, prep_time_minutes "
#             "FROM recipes"
#         )
#         return [self._load_recipe_by_row(row) for row in cursor.fetchall()]
#
#     def delete_recipe(self, title: str) -> None:
#         cursor = self.connection.cursor()
#         cursor.execute(
#             "SELECT id FROM recipes WHERE LOWER(title) = LOWER(?)", (title,)
#         )
#         row = cursor.fetchone()
#         if row is None:
#             raise KeyError(f"Recipe '{title}' not found")
#         recipe_id = row[0]
#         cursor.execute("DELETE FROM recipe_tags WHERE recipe_id = ?",
#                         (recipe_id,))
#         cursor.execute("DELETE FROM instructions WHERE recipe_id = ?",
#                         (recipe_id,))
#         cursor.execute("DELETE FROM ingredients WHERE recipe_id = ?",
#                         (recipe_id,))
#         cursor.execute("DELETE FROM recipes WHERE id = ?", (recipe_id,))
#         self.connection.commit()
#
#     def search_by_title(self, query: str) -> list[Recipe]:
#         pattern = re.compile(query, re.IGNORECASE)
#         all_recipes = self.get_all_recipes()
#         return [r for r in all_recipes if pattern.search(r.title)]
# ```

# %% [markdown]
#
# ## Beispieltests mit parametrisierter Fixture
#
# ### `storage_test.py`

# %% [markdown]
#
# ```python
# import pytest
# from pykochbuch.ingredient import Ingredient
# from pykochbuch.recipe import Recipe
# from pykochbuch.storage import InMemoryStore, JsonStore, SqliteStore
# from pykochbuch.unit import Unit
#
#
# @pytest.fixture(params=["memory", "json", "sqlite"])
# def store(request, tmp_path):
#     if request.param == "memory":
#         return InMemoryStore()
#     elif request.param == "json":
#         return JsonStore(tmp_path / "recipes.json")
#     return SqliteStore(":memory:")
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
# def test_save_and_get_round_trip(store, pancakes):
#     store.save_recipe(pancakes)
#     result = store.get_recipe("Pancakes")
#     assert result.title == "Pancakes"
#     assert result.servings == 4
#     assert len(result.ingredients) == 3
#     assert result.tags == frozenset({"breakfast", "quick"})
#
#
# def test_get_all_empty(store):
#     assert store.get_all_recipes() == []
#
#
# def test_duplicate_raises(store, pancakes):
#     store.save_recipe(pancakes)
#     with pytest.raises(ValueError, match="already exists"):
#         store.save_recipe(pancakes)
#
#
# def test_delete_recipe(store, pancakes):
#     store.save_recipe(pancakes)
#     store.delete_recipe("Pancakes")
#     assert store.get_all_recipes() == []
#
#
# def test_delete_nonexistent_raises(store):
#     with pytest.raises(KeyError):
#         store.delete_recipe("Unknown")
#
#
# def test_recipe_without_tags(store):
#     recipe = Recipe(
#         title="Simple Soup",
#         servings=2,
#         ingredients=(Ingredient("water", 1, Unit.LITER),),
#         instructions=("Boil water",),
#     )
#     store.save_recipe(recipe)
#     result = store.get_recipe("Simple Soup")
#     assert result.tags == frozenset()
# ```
