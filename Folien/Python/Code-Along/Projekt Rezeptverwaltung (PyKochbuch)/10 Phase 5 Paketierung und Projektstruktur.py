# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Phase 5: Paketierung und Projektstruktur</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
#
# <div style="text-align:center;">Coding-Akademie München</div>
# <br/>


# %% [markdown]
#
# # Phase 5: Paketierung und Projektstruktur

# %% [markdown]
#
# ## Ziel
#
# In dieser Phase strukturieren Sie Ihr Projekt als sauberes Python-Paket mit
# einer klaren Modulstruktur. Sie überprüfen, dass alle bestehenden Tests nach
# der Umstrukturierung weiterhin bestehen.

# %% [markdown]
#
# ## So sieht das Ergebnis aus
#
# Nach der Umstrukturierung sieht Ihr Projekt so aus:
#
# ```
# pykochbuch/
#   src/
#     pykochbuch/
#       __init__.py
#       models/
#         __init__.py
#         ingredient.py
#         recipe.py
#         unit.py
#       storage/
#         __init__.py
#         base.py          # RecipeStore ABC
#         json_store.py
#         sqlite_store.py
#         memory_store.py
#         serialization.py # to_dict / from_dict
#       recipe_book.py
#       shopping_list.py
#   tests/
#     ingredient_test.py
#     recipe_test.py
#     recipe_book_test.py
#     shopping_list_test.py
#     storage_test.py
#     unit_test.py
#   pyproject.toml
# ```
#
# Die Imports ändern sich entsprechend:
#
# ```python
# # Vorher:
# from pykochbuch.ingredient import Ingredient
# from pykochbuch.storage import JsonStore
#
# # Nachher:
# from pykochbuch.models.ingredient import Ingredient
# from pykochbuch.storage.json_store import JsonStore
# ```

# %% [markdown]
#
# ## Vorbereitung
#
# **Aufgabe V1:** Erstellen Sie ein Mini-Paket mit Unterpaketen, um die Konzepte
# zu üben. Erstellen Sie diese Struktur:
#
# ```
# meinpaket/
#   __init__.py
#   werkzeuge/
#     __init__.py
#     rechner.py      # enthält: def addiere(a, b): return a + b
# ```
#
# Importieren Sie dann `addiere` auf verschiedene Weisen:
#
# ```python
# from meinpaket.werkzeuge.rechner import addiere
# from meinpaket.werkzeuge import rechner
# ```
#
# > **Kursreferenz:** „Module und Packages" und „Packages" (in Abschnitt 14
# > Module und Packages)
#
# **Aufgabe V2:** Machen Sie sich mit Re-Exports in `__init__.py` vertraut.
# Fügen Sie in `meinpaket/werkzeuge/__init__.py` hinzu:
#
# ```python
# from meinpaket.werkzeuge.rechner import addiere
# ```
#
# Dann können Sie kürzer importieren:
#
# ```python
# from meinpaket.werkzeuge import addiere
# ```
#
# > **Kursreferenz:** „Packages" (in Abschnitt 14)

# %% [markdown]
#
# ## Aufgaben
#
# ### Schritt 1: Unterpaket `models/` erstellen
#
# Erstellen Sie das Verzeichnis `src/pykochbuch/models/` mit einer
# `__init__.py`-Datei. Verschieben Sie diese Dateien dorthin:
#
# - `ingredient.py` → `models/ingredient.py`
# - `recipe.py` → `models/recipe.py`
# - `unit.py` → `models/unit.py`
#
# Aktualisieren Sie die Imports **innerhalb** dieser Dateien (z.B. importiert
# `ingredient.py` aus `pykochbuch.models.unit` statt `pykochbuch.unit`).
#
# > **Kursreferenz:** „Packages" und „Importieren von Modulen" (in Abschnitt 14
# > Module und Packages)
#
# ### Schritt 2: Unterpaket `storage/` erstellen
#
# Erstellen Sie `src/pykochbuch/storage/` und teilen Sie die bisherige
# `storage.py` auf:
#
# - `base.py` — die abstrakte Klasse `RecipeStore`
# - `serialization.py` — `_recipe_to_dict` und `_dict_to_recipe`
# - `json_store.py` — die Klasse `JsonStore`
# - `sqlite_store.py` — die Klasse `SqliteStore`
# - `memory_store.py` — die Klasse `InMemoryStore`
# - `__init__.py` — Re-Exports für bequemere Imports
#
# Jede Datei importiert nur das, was sie tatsächlich braucht.
#
# > **Kursreferenz:** „Benutzerdefinierte Module" (in Abschnitt 14)
#
# ### Schritt 3: Imports in allen Dateien aktualisieren
#
# Aktualisieren Sie die Imports in:
#
# - `recipe_book.py` (importiert aus `pykochbuch.models.recipe`)
# - `shopping_list.py` (importiert aus `pykochbuch.models.*`)
# - Alle Testdateien
#
# **Tipp:** Führen Sie nach jeder Änderung `uv run pytest` aus, um
# sicherzustellen, dass nichts kaputt gegangen ist. Ändern Sie nicht alles auf
# einmal.
#
# ### Schritt 4: Re-Exports in `__init__.py`
#
# Fügen Sie in `src/pykochbuch/models/__init__.py` Re-Exports hinzu, damit
# die häufigsten Klassen bequem importiert werden können:
#
# ```python
# from pykochbuch.models.ingredient import Ingredient
# from pykochbuch.models.recipe import Recipe
# from pykochbuch.models.unit import Unit
# ```
#
# Ähnlich in `src/pykochbuch/storage/__init__.py`:
#
# ```python
# from pykochbuch.storage.base import RecipeStore
# from pykochbuch.storage.json_store import JsonStore
# from pykochbuch.storage.sqlite_store import SqliteStore
# from pykochbuch.storage.memory_store import InMemoryStore
# ```
#
# ### Schritt 5: `pyproject.toml` überprüfen
#
# Stellen Sie sicher, dass Ihre `pyproject.toml` korrekt konfiguriert ist:
#
# ```toml
# [project]
# name = "pykochbuch"
# version = "0.1.0"
# description = "A recipe manager"
# requires-python = ">=3.12"
# dependencies = []
#
# [dependency-groups]
# dev = ["pytest>=8"]
# ```
#
# Testen Sie, dass `uv run pytest` alle Tests findet und ausführt.
#
# > **Kursreferenz:** „Der uv Package Manager" (in Abschnitt 14)

# %% [markdown]
#
# ## Prüfe dein Ergebnis
#
# - [ ] `uv run pytest` läuft ohne Fehler — **alle** bisherigen Tests bestehen
# - [ ] Die Verzeichnisstruktur hat `models/` und `storage/` Unterpakete
# - [ ] Jede `__init__.py` enthält sinnvolle Re-Exports
# - [ ] Keine Datei enthält Imports aus dem alten Pfad (z.B.
#       `from pykochbuch.ingredient import ...`)
# - [ ] `storage.py` existiert nicht mehr (aufgeteilt in `storage/`)
# - [ ] `from pykochbuch.models import Ingredient, Recipe, Unit` funktioniert
# - [ ] `from pykochbuch.storage import JsonStore, SqliteStore` funktioniert

# %% [markdown]
# *Antwort:* 
