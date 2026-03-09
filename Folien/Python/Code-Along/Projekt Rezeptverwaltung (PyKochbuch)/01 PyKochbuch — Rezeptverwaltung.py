# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>PyKochbuch — Rezeptverwaltung</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
#
# <div style="text-align:center;">Coding-Akademie München</div>
# <br/>


# %% [markdown]
#
# # PyKochbuch — Rezeptverwaltung

# %% [markdown]
#
# ## Was bauen wir?
#
# In diesem Projekt entwickeln Sie **PyKochbuch**, eine Rezeptverwaltung in Python.
# Die Anwendung ermöglicht es, Rezepte zu erstellen, nach ihnen zu suchen,
# Portionen zu skalieren und Einkaufslisten zu generieren.
#
# Sie bauen das Projekt schrittweise in 5 Phasen auf — vom einfachen Datenmodell
# bis zur Datenbank-Anbindung.

# %% [markdown]
#
# ## Funktionen
#
# - Rezepte mit Zutaten, Zubereitungsschritten und Tags erstellen
# - Portionen hoch- und runterskalieren
# - Rezepte suchen (nach Titel, Zutat oder Tag)
# - Rezepte nach maximaler Zubereitungszeit filtern
# - Einkaufslisten aus mehreren Rezepten generieren (gleiche Zutaten werden
#   automatisch zusammengefasst)
# - Rezepte als JSON-Dateien speichern und laden
# - Rezepte in einer SQLite-Datenbank verwalten

# %% [markdown]
#
# ## Domänenmodell
#
# Das folgende Diagramm zeigt die Klassen, die Sie im Laufe des Projekts
# implementieren werden:
#
# ```
# Unit (Enum)
#   GRAM, KILOGRAM, MILLILITER, LITER, PIECE, TABLESPOON, TEASPOON
#
# Ingredient (frozen dataclass)
#   - name: str
#   - amount: float
#   - unit: Unit
#   + scale(factor) → Ingredient
#
# Recipe (dataclass)
#   - title: str
#   - servings: int
#   - ingredients: tuple[Ingredient, ...]
#   - instructions: tuple[str, ...]
#   - tags: frozenset[str]
#   + scale(factor) → Recipe
#   + scale_to_servings(n) → Recipe
#
# RecipeBook
#   + add_recipe(recipe)
#   + remove_recipe(title)
#   + search_by_title(query)
#   + search_by_ingredient(name)
#   + search_by_tag(tag)
#   + filter_by_max_time(minutes)
#
# ShoppingList
#   + from_recipes(recipes) → ShoppingList
#   + add_recipe(recipe)
#   + items: list[Ingredient]
#
# RecipeStore (ABC)
#   + save_recipe(recipe)
#   + get_recipe(title) → Recipe
#   + get_all_recipes() → list[Recipe]
#   + delete_recipe(title)
#   ├── InMemoryStore
#   ├── JsonStore
#   └── SqliteStore
# ```

# %% [markdown]
#
# ## Phasenübersicht
#
# | Phase | Thema | Neue Konzepte |
# |-------|-------|---------------|
# | 1 | Datenmodell mit TDD | Enums, Dataclasses, `__post_init__`, pytest |
# | 2 | Suche und Filterung | Regex, Comprehensions, Sets, Einkaufsliste |
# | 3 | JSON-Persistenz | Dateien, pathlib, JSON-Serialisierung |
# | 4 | Datenbank | SQLite, DB-API, abstrakte Klassen, Vererbung |
# | 5 | Paketierung | Module, Pakete, uv, Projektstruktur |
#
# Jede Phase baut auf der vorherigen auf. Arbeiten Sie die Phasen der Reihe nach
# durch.

# %% [markdown]
#
# ## Projekt-Setup
#
# Erstellen Sie das Projekt mit `uv`:
#
# ```bash
# uv init --lib pykochbuch
# cd pykochbuch
# uv add --dev pytest
# ```
#
# Ihre Projektstruktur sollte so aussehen:
#
# ```
# pykochbuch/
#   src/
#     pykochbuch/
#       __init__.py
#   tests/
#   pyproject.toml
# ```
#
# Neue Dateien legen Sie in `src/pykochbuch/` an, Tests in `tests/`.
#
# Führen Sie Tests mit folgendem Befehl aus:
#
# ```bash
# uv run pytest
# ```
