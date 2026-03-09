# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Phase 4: Datenbank und abstrakte Schnittstelle</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
#
# <div style="text-align:center;">Coding-Akademie München</div>
# <br/>


# %% [markdown]
#
# # Phase 4: Datenbank und abstrakte Schnittstelle

# %% [markdown]
#
# ## Ziel
#
# In dieser Phase migrieren Sie die Datenspeicherung von JSON zu SQLite und
# erstellen eine gemeinsame abstrakte Schnittstelle (`RecipeStore`), die beide
# Backends (JSON und SQLite) unter einer einheitlichen API vereint.

# %% [markdown]
#
# ## So sieht das Ergebnis aus
#
# ```python
# from pykochbuch.storage import SqliteStore, JsonStore
#
# # Beide Stores haben dieselbe Schnittstelle
# sqlite_store = SqliteStore(":memory:")
# json_store = JsonStore(Path("rezepte.json"))
#
# # Genau dieselben Methoden funktionieren mit beiden
# for store in [sqlite_store, json_store]:
#     store.save_recipe(pfannkuchen)
#     store.get_recipe("Pfannkuchen")
#     store.get_all_recipes()
#     store.delete_recipe("Pfannkuchen")
# ```

# %% [markdown]
#
# ## Vorbereitung
#
# **Aufgabe V1:** Erstellen Sie eine SQLite-Datenbank im Speicher und führen Sie
# einfache SQL-Befehle aus:
#
# ```python
# import sqlite3
#
# conn = sqlite3.connect(":memory:")
# cursor = conn.cursor()
# cursor.execute("CREATE TABLE personen (name TEXT, alter_ INTEGER)")
# cursor.execute("INSERT INTO personen VALUES (?, ?)", ("Anna", 30))
# conn.commit()
#
# cursor.execute("SELECT * FROM personen")
# print(cursor.fetchall())  # [("Anna", 30)]
# ```
#
# Üben Sie `INSERT`, `SELECT`, `UPDATE` und `DELETE`.
#
# > **Kursreferenz:** „Tabellen erstellen (CREATE TABLE)", „Daten einfügen
# > (INSERT)", „Daten abfragen (SELECT)" (in Abschnitt 19 Datenbanken und SQL)
#
# **Aufgabe V2:** Erstellen Sie zwei verknüpfte Tabellen und verwenden Sie einen
# `FOREIGN KEY`:
#
# ```python
# cursor.execute("""
#     CREATE TABLE kurse (id INTEGER PRIMARY KEY, name TEXT)
# """)
# cursor.execute("""
#     CREATE TABLE teilnehmer (
#         id INTEGER PRIMARY KEY,
#         kurs_id INTEGER,
#         name TEXT,
#         FOREIGN KEY (kurs_id) REFERENCES kurse(id)
#     )
# """)
# ```
#
# Fügen Sie Daten in beide Tabellen ein und lesen Sie sie mit einem `JOIN` aus.
#
# > **Kursreferenz:** „Python DB-API (Teil 1)" und „Python DB-API (Teil 2)"
# > (in Abschnitt 19)
#
# **Aufgabe V3:** Schreiben Sie eine abstrakte Klasse mit einer abstrakten
# Methode:
#
# ```python
# from abc import ABC, abstractmethod
#
# class Tier(ABC):
#     @abstractmethod
#     def laut(self) -> str: ...
#
# class Hund(Tier):
#     def laut(self) -> str:
#         return "Wau!"
# ```
#
# Versuchen Sie, `Tier()` direkt zu instanziieren — was passiert?
#
# > **Kursreferenz:** „Abstrakte Klassen" (in Abschnitt 11 Vererbung und
# > Polymorphie)

# %% [markdown]
#
# ## Aufgaben
#
# ### Schritt 1: Datenbankschema entwerfen
#
# Entwerfen Sie das Schema für die SQLite-Datenbank. Sie brauchen vier Tabellen:
#
# - `recipes` — id, title (UNIQUE), description, servings, prep_time_minutes
# - `ingredients` — id, recipe_id (FOREIGN KEY), name, amount, unit
# - `instructions` — id, recipe_id (FOREIGN KEY), step_number, instruction
# - `recipe_tags` — recipe_id + tag als zusammengesetzter Primärschlüssel
#
# Überlegen Sie, warum Zutaten, Anweisungen und Tags jeweils eigene Tabellen
# brauchen (Stichwort: 1:n-Beziehung).
#
# > **Kursreferenz:** „Relationale Datenbanken (Teil 1)" bis „(Teil 3)" (in
# > Abschnitt 19 Datenbanken und SQL)
#
# ### Schritt 2: `SqliteStore` implementieren
#
# Erweitern Sie `storage.py` um eine Klasse `SqliteStore`:
#
# - `__init__(self, db_path)` — Verbindung herstellen, Tabellen anlegen
#   (`CREATE TABLE IF NOT EXISTS`)
# - `save_recipe(recipe)` — Rezept in alle vier Tabellen einfügen. Verwenden
#   Sie `cursor.lastrowid`, um die ID des eingefügten Rezepts zu erhalten.
#   `ValueError` bei Duplikat (fangen Sie `sqlite3.IntegrityError` ab).
# - `get_recipe(title)` — Rezept mit Zutaten, Anweisungen und Tags aus allen
#   Tabellen laden
# - `get_all_recipes()` — alle Rezepte laden
# - `delete_recipe(title)` — Rezept und alle zugehörigen Daten löschen
# - `search_by_title(query)` — Regex-Suche
#
# Denken Sie an `conn.commit()` nach Schreiboperationen.
#
# > **Kursreferenz:** „Python DB-API (Teil 1)" und „Python DB-API (Teil 2)"
# > (in Abschnitt 19)
#
# ### Schritt 3: Abstrakte Schnittstelle `RecipeStore`
#
# Erstellen Sie eine abstrakte Basisklasse `RecipeStore`:
#
# ```python
# class RecipeStore(ABC):
#     def save_recipe(self, recipe: Recipe) -> None: ...
#     def get_recipe(self, title: str) -> Recipe: ...
#     def get_all_recipes(self) -> list[Recipe]: ...
#     def delete_recipe(self, title: str) -> None: ...
#     def search_by_title(self, query: str) -> list[Recipe]: ...
# ```
#
# Lassen Sie `JsonStore` und `SqliteStore` von `RecipeStore` erben. Erstellen
# Sie außerdem einen `InMemoryStore`, der intern ein `RecipeBook` verwendet.
#
# > **Kursreferenz:** „Abstrakte Klassen" und „Vererbung" (in Abschnitt 11
# > Vererbung und Polymorphie)
#
# ### Schritt 4: Tests
#
# Verwenden Sie eine **parametrisierte Fixture**, um dieselben Tests mit allen
# drei Store-Implementierungen auszuführen:
#
# ```python
# @pytest.fixture(params=["memory", "json", "sqlite"])
# def store(request, tmp_path):
#     if request.param == "memory":
#         return InMemoryStore()
#     elif request.param == "json":
#         return JsonStore(tmp_path / "recipes.json")
#     return SqliteStore(":memory:")
# ```
#
# Jeder Test, der `store` als Parameter hat, wird automatisch dreimal
# ausgeführt — einmal pro Backend.
#
# Testen Sie:
# - Speichern und Laden (Round-Trip mit allen Feldern)
# - Duplikate und nicht gefundene Rezepte
# - Löschen
# - Suche
# - Rezepte ohne Tags
#
# > **Kursreferenz:** „Pytest" (in Abschnitt 18 Unit-Tests und Test Frameworks)

# %% [markdown]
#
# ## Prüfe dein Ergebnis
#
# - [ ] `uv run pytest` läuft ohne Fehler
# - [ ] Alle Store-Tests laufen mit allen drei Backends (memory, json, sqlite)
# - [ ] Ein Rezept mit Zutaten, Anweisungen und Tags überlebt den Round-Trip
#       durch die Datenbank
# - [ ] `SqliteStore(":memory:")` funktioniert (In-Memory-Datenbank)
# - [ ] `InMemoryStore`, `JsonStore` und `SqliteStore` erben alle von
#       `RecipeStore`
# - [ ] Duplikates Speichern wirft `ValueError` (auch bei SQLite)
# - [ ] Löschen eines Rezepts entfernt auch Zutaten, Anweisungen und Tags
# - [ ] Sie haben mindestens 45 Tests (insgesamt)

# %% [markdown]
# *Antwort:* 
# ## Hinweise
#
# ### Zu Schritt 1: Datenbankschema
#
# Zutaten, Anweisungen und Tags sind jeweils 1:n-Beziehungen: Ein Rezept hat
# **mehrere** Zutaten, aber jede Zutat gehört zu **einem** Rezept. In einer
# relationalen Datenbank modelliert man das mit separaten Tabellen und
# `FOREIGN KEY`-Verweisen.
#
# Für die Tabellenerstellung:
#
# ```python
# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS recipes (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         title TEXT UNIQUE NOT NULL,
#         description TEXT NOT NULL DEFAULT '',
#         servings INTEGER NOT NULL,
#         prep_time_minutes INTEGER NOT NULL DEFAULT 0
#     )
# """)
# ```
#
# `AUTOINCREMENT` erzeugt automatisch eine eindeutige ID.
# `UNIQUE` bei `title` verhindert Duplikate auf Datenbankebene.
#
# ### Zu Schritt 2: `SqliteStore`
#
# Beim **Einfügen** eines Rezepts müssen Sie in alle vier Tabellen schreiben.
# Holen Sie sich nach dem `INSERT` in `recipes` die erzeugte ID:
#
# ```python
# cursor.execute(
#     "INSERT INTO recipes (title, description, servings, prep_time_minutes) "
#     "VALUES (?, ?, ?, ?)",
#     (recipe.title, recipe.description, recipe.servings, recipe.prep_time_minutes),
# )
# recipe_id = cursor.lastrowid
# ```
#
# Dann für jede Zutat, Anweisung und jeden Tag einen weiteren `INSERT` mit
# dieser `recipe_id`.
#
# Verwenden Sie `?`-Platzhalter für Parameter — **niemals** f-Strings oder
# String-Verkettung in SQL-Befehlen (SQL-Injection-Gefahr).
#
# Beim **Laden** brauchen Sie mehrere Abfragen: erst das Rezept, dann die
# Zutaten, Anweisungen und Tags. Erstellen Sie eine Hilfsmethode
# `_load_recipe_by_row`, die eine Zeile aus der `recipes`-Tabelle nimmt und das
# vollständige `Recipe`-Objekt zusammenbaut.
#
# Für **Duplikat-Erkennung**: `sqlite3.IntegrityError` wird geworfen, wenn das
# `UNIQUE`-Constraint auf `title` verletzt wird:
#
# ```python
# try:
#     cursor.execute("INSERT INTO recipes ...")
# except sqlite3.IntegrityError:
#     raise ValueError(f"Recipe '{recipe.title}' already exists")
# ```
#
# ### Zu Schritt 3: Abstrakte Schnittstelle
#
# Markieren Sie alle Methoden in `RecipeStore` mit `@abstractmethod`:
#
# ```python
# from abc import ABC, abstractmethod
#
# class RecipeStore(ABC):
#     @abstractmethod
#     def save_recipe(self, recipe: Recipe) -> None: ...
#
#     @abstractmethod
#     def get_recipe(self, title: str) -> Recipe: ...
#     # ...
# ```
#
# Der `InMemoryStore` ist der einfachste — er delegiert alles an ein
# `RecipeBook`:
#
# ```python
# class InMemoryStore(RecipeStore):
#     def __init__(self):
#         self._book = RecipeBook()
#
#     def save_recipe(self, recipe):
#         self._book.add_recipe(recipe)
#     # ...
# ```
#
# ### Zu Schritt 4: Parametrisierte Fixtures
#
# Die parametrisierte Fixture erstellt für jeden Testtag automatisch drei
# Store-Instanzen. Das `request`-Objekt enthält den aktuellen Parameter:
#
# ```python
# @pytest.fixture(params=["memory", "json", "sqlite"])
# def store(request, tmp_path):
#     if request.param == "memory":
#         return InMemoryStore()
#     elif request.param == "json":
#         return JsonStore(tmp_path / "recipes.json")
#     return SqliteStore(":memory:")
# ```
#
# Wenn Sie `uv run pytest -v` ausführen, sehen Sie jeden Test dreimal mit dem
# jeweiligen Backend im Namen.
