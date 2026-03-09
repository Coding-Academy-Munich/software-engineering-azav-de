# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Phase 3: JSON-Persistenz</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
#
# <div style="text-align:center;">Coding-Akademie München</div>
# <br/>


# %% [markdown]
#
# # Phase 3: JSON-Persistenz

# %% [markdown]
#
# ## Ziel
#
# In dieser Phase lernen Sie, Rezepte als JSON-Dateien zu speichern und zu laden.
# Sie implementieren Serialisierungs-Methoden und einen `JsonStore`, der Rezepte
# in einer Datei verwaltet.

# %% [markdown]
#
# ## So sieht das Ergebnis aus
#
# ```python
# from pathlib import Path
# from pykochbuch.storage import JsonStore
#
# # Rezepte in Datei speichern
# store = JsonStore(Path("rezepte.json"))
# store.save_recipe(pfannkuchen)
# store.save_recipe(pasta)
#
# # Später wieder laden
# alle = store.get_all_recipes()
# gefunden = store.get_recipe("Pfannkuchen")
#
# # Die JSON-Datei sieht so aus:
# # [
# #   {
# #     "title": "Pfannkuchen",
# #     "servings": 4,
# #     "ingredients": [
# #       {"name": "mehl", "amount": 500, "unit": "g"},
# #       ...
# #     ],
# #     ...
# #   }
# # ]
# ```

# %% [markdown]
#
# ## Vorbereitung
#
# **Aufgabe V1:** Wandeln Sie ein verschachteltes Python-Dictionary in einen
# JSON-String um und zurück. Verwenden Sie `json.dumps()` und `json.loads()`:
#
# ```python
# import json
#
# daten = {"name": "Mehl", "menge": 500, "einheit": "g"}
# json_string = json.dumps(daten)  # → String
# zurueck = json.loads(json_string)  # → Dictionary
# ```
#
# Probieren Sie auch `json.dumps(daten, indent=2)` für lesbare Ausgabe.
#
# > **Kursreferenz:** „JSON" (in Abschnitt 16 Dateien und IO_Operationen)
#
# **Aufgabe V2:** Schreiben Sie einen String in eine Datei und lesen Sie ihn
# wieder zurück. Verwenden Sie `open()` mit `"w"` zum Schreiben und `"r"` zum
# Lesen:
#
# ```python
# with open("test.txt", "w") as f:
#     f.write("Hallo Welt")
#
# with open("test.txt", "r") as f:
#     inhalt = f.read()
# ```
#
# > **Kursreferenz:** „Dateien" (in Abschnitt 16)
#
# **Aufgabe V3:** Erstellen Sie ein `Path`-Objekt und prüfen Sie, ob eine Datei
# existiert:
#
# ```python
# from pathlib import Path
#
# pfad = Path("test.txt")
# pfad.exists()  # True oder False
# ```
#
# > **Kursreferenz:** „Pathlib" (in Abschnitt 16)
#
# **Aufgabe V4:** Schreiben Sie eine Funktion, die ein Dictionary in eine
# JSON-Datei speichert, und eine Funktion, die es wieder lädt. Verwenden Sie
# `json.dump()` (ohne „s") und `json.load()` (ohne „s") direkt mit
# Datei-Objekten:
#
# ```python
# import json
#
# def save_to_json(data, path):
#     with open(path, "w") as f:
#         json.dump(data, f, indent=2)
#
# def load_from_json(path):
#     with open(path) as f:
#         return json.load(f)
# ```
#
# > **Kursreferenz:** „JSON" und „JSON mit eigenen Objekten" (in Abschnitt 16)

# %% [markdown]
#
# ## Aufgaben
#
# ### Schritt 1: Serialisierung (`to_dict` / `from_dict`)
#
# Erstellen Sie eine neue Datei `src/pykochbuch/storage.py`. Implementieren Sie
# zwei Hilfsfunktionen:
#
# - `_recipe_to_dict(recipe)` — wandelt ein `Recipe` in ein Dictionary um, das
#   JSON-kompatibel ist:
#   - Ingredients werden zu Listen von Dicts `{"name": ..., "amount": ..., "unit": ...}`
#   - Enum-Werte werden als Strings gespeichert (`unit.value`)
#   - `frozenset` wird zu einer sortierten Liste
#   - `tuple` wird zu einer Liste
# - `_dict_to_recipe(data)` — wandelt ein Dictionary zurück in ein `Recipe`:
#   - Strings werden zurück in `Unit`-Enums konvertiert (`Unit(string)`)
#   - Listen werden zu Tupeln und Frozensets
#
# Testen Sie mit einem Round-Trip: `_dict_to_recipe(_recipe_to_dict(recipe))`
# sollte ein gleichwertiges Rezept ergeben.
#
# > **Kursreferenz:** „JSON mit eigenen Objekten" (in Abschnitt 16 Dateien und
# > IO_Operationen)
#
# ### Schritt 2: `JsonStore`
#
# Implementieren Sie eine Klasse `JsonStore`, die alle Rezepte in einer einzigen
# JSON-Datei speichert (als Liste von Dictionaries):
#
# - `__init__(self, path: Path)` — speichert den Dateipfad
# - `save_recipe(recipe)` — lädt die bestehenden Daten, fügt das neue Rezept
#   hinzu, speichert alles zurück. `ValueError` bei Duplikat.
# - `get_recipe(title)` — lädt die Datei, sucht nach Titel. `KeyError` wenn
#   nicht gefunden.
# - `get_all_recipes()` — lädt und konvertiert alle Rezepte
# - `delete_recipe(title)` — entfernt ein Rezept. `KeyError` wenn nicht
#   gefunden.
# - `search_by_title(query)` — Regex-Suche wie im RecipeBook
#
# Beachten Sie: Wenn die Datei noch nicht existiert, soll `get_all_recipes()`
# eine leere Liste zurückgeben (keine Exception).
#
# > **Kursreferenz:** „Dateien" und „Pathlib" (in Abschnitt 16),
# > „Fehlerbehandlung" (in Abschnitt 10 Fehlerbehandlung)
#
# ### Schritt 3: Tests
#
# Erstellen Sie `tests/storage_test.py`. Verwenden Sie die `tmp_path`-Fixture
# von pytest — sie stellt ein temporäres Verzeichnis bereit, das nach dem Test
# automatisch aufgeräumt wird:
#
# ```python
# def test_save_and_load(tmp_path):
#     store = JsonStore(tmp_path / "recipes.json")
#     store.save_recipe(some_recipe)
#     result = store.get_recipe("Recipe Title")
#     assert result.title == "Recipe Title"
# ```
#
# Testen Sie:
# - Speichern und Laden (Round-Trip: alle Felder erhalten?)
# - Leere Datei / nicht existierende Datei
# - Duplikate und nicht gefundene Rezepte
# - Mehrere Rezepte speichern und laden
#
# > **Kursreferenz:** „Pytest" (in Abschnitt 18 Unit-Tests und Test Frameworks)

# %% [markdown]
#
# ## Prüfe dein Ergebnis
#
# - [ ] `uv run pytest` läuft ohne Fehler
# - [ ] Ein Rezept kann gespeichert und wieder geladen werden, wobei alle Felder
#       erhalten bleiben (Titel, Zutaten, Einheiten, Tags, Anweisungen)
# - [ ] `get_all_recipes()` gibt eine leere Liste zurück, wenn die Datei nicht
#       existiert
# - [ ] Doppeltes Speichern wirft `ValueError`
# - [ ] `get_recipe("Unbekannt")` wirft `KeyError`
# - [ ] `delete_recipe()` entfernt das Rezept aus der Datei
# - [ ] Die erzeugte JSON-Datei ist menschenlesbar (eingerückt)
# - [ ] Sie haben mindestens 35 Tests (insgesamt)

# %% [markdown]
# *Antwort:* 
