# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Phase 2: Suche, Filterung und Einkaufsliste</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
#
# <div style="text-align:center;">Coding-Akademie München</div>
# <br/>


# %% [markdown]
#
# # Phase 2: Suche, Filterung und Einkaufsliste

# %% [markdown]
#
# ## Ziel
#
# In dieser Phase erweitern Sie das `RecipeBook` um Such- und Filterfunktionen
# und implementieren eine `ShoppingList`, die Zutaten aus mehreren Rezepten
# zusammenfasst.

# %% [markdown]
#
# ## So sieht das Ergebnis aus
#
# ```python
# from pykochbuch.recipe_book import RecipeBook
# from pykochbuch.shopping_list import ShoppingList
#
# # Suche nach Titel (mit Regex)
# ergebnisse = buch.search_by_title("Pfann")  # findet "Pfannkuchen"
# ergebnisse = buch.search_by_title("^C")     # findet alle mit "C" am Anfang
#
# # Suche nach Zutat
# mit_mehl = buch.search_by_ingredient("mehl")
#
# # Suche nach Tag
# schnelle = buch.search_by_tag("schnell")
#
# # Filter nach Zeit
# unter_30_min = buch.filter_by_max_time(30)
#
# # Einkaufsliste aus mehreren Rezepten
# einkauf = ShoppingList.from_recipes([pfannkuchen, kuchen])
# print(einkauf)
# # Shopping List:
# # -------------
# #   550g mehl
# #   500ml milch
# #   5pc eier
# #   200g zucker
# ```

# %% [markdown]
#
# ## Vorbereitung
#
# **Aufgabe V1:** Schreiben Sie eine Funktion `filter_short_strings`, die eine
# Liste von Strings und eine maximale Länge nimmt und nur die Strings zurückgibt,
# die kürzer oder gleich lang sind. Verwenden Sie eine List Comprehension.
#
# Beispiel: `filter_short_strings(["hi", "hello", "hey"], 3)` → `["hi", "hey"]`
#
# > **Kursreferenz:** „Komprehensionen: Elegantere Iteration" (in Abschnitt 12
# > Fortgeschrittene Kontrollstrukturen)
#
# **Aufgabe V2:** Testen Sie reguläre Ausdrücke: Importieren Sie `re` und
# verwenden Sie `re.search(pattern, text)`, um in einem String zu suchen.
# Probieren Sie folgende Muster auf den String `"Spaghetti Bolognese"`:
#
# - `"Spaghetti"` — exakte Teilsuche
# - `"spaghetti"` mit `re.IGNORECASE` — Groß-/Kleinschreibung ignorieren
# - `"^S"` — beginnt mit "S"
# - `"e$"` — endet mit "e"
#
# > **Kursreferenz:** „Reguläre Ausdrücke" (in Abschnitt 07 Weitere
# > Datenstrukturen und Reguläre Ausdrücke)
#
# **Aufgabe V3:** Erstellen Sie zwei Sets: `tags_a = {"schnell", "vegetarisch"}`
# und `tags_b = {"schnell", "dessert"}`. Finden Sie heraus, wie Sie prüfen, ob
# ein Element in einem Set enthalten ist (`"schnell" in tags_a`), und wie
# Schnittmenge (`&`) und Vereinigung (`|`) funktionieren.
#
# > **Kursreferenz:** „Mengen" (in Abschnitt 07)
#
# **Aufgabe V4:** Schreiben Sie eine Funktion `merge_amounts`, die ein Dictionary
# `{"mehl": 250, "eier": 2}` und ein zweites Dictionary
# `{"mehl": 300, "zucker": 200}` nimmt und ein neues Dictionary zurückgibt,
# in dem gleiche Schlüssel summiert werden:
# `{"mehl": 550, "eier": 2, "zucker": 200}`.
#
# > **Kursreferenz:** „Dictionaries" und „Iteration über Dictionaries" (in
# > Abschnitt 07)

# %% [markdown]
#
# ## Aufgaben
#
# ### Schritt 1: Suchmethoden im `RecipeBook`
#
# Erweitern Sie Ihr `RecipeBook` um diese Methoden:
#
# - `search_by_title(query)` — verwendet `re.search` mit `re.IGNORECASE`, um
#   Rezepte zu finden, deren Titel zum Muster passt (Teilübereinstimmung genügt)
# - `search_by_ingredient(name)` — findet alle Rezepte, die eine bestimmte Zutat
#   enthalten
# - `search_by_tag(tag)` — findet alle Rezepte mit einem bestimmten Tag
# - `filter_by_max_time(minutes)` — gibt Rezepte zurück, deren
#   `prep_time_minutes` kleiner oder gleich dem Wert ist
#
# Jede Methode gibt eine `list[Recipe]` zurück.
#
# > **Kursreferenz:** „Reguläre Ausdrücke" und „Zeichenklassen und Quantoren"
# > (in Abschnitt 07), „Komprehensionen: Elegantere Iteration" (in Abschnitt
# > 12)
#
# ### Schritt 2: Kombinierte Suche
#
# Implementieren Sie eine `search()`-Methode, die alle Filter optional
# kombiniert:
#
# ```python
# def search(self, title=None, ingredient=None, tag=None, max_time=None):
#     ...
# ```
#
# Wenn mehrere Kriterien angegeben sind, sollen nur Rezepte zurückgegeben werden,
# die **alle** Kriterien erfüllen (Schnittmenge). Wenn kein Kriterium angegeben
# ist, werden alle Rezepte zurückgegeben.
#
# > **Kursreferenz:** „Mengen" (in Abschnitt 07)
#
# ### Schritt 3: `ShoppingList`
#
# Erstellen Sie eine neue Datei `src/pykochbuch/shopping_list.py` und eine
# Klasse `ShoppingList`:
#
# - `add_recipe(recipe)` — fügt alle Zutaten eines Rezepts hinzu. Wenn eine
#   Zutat mit gleichem Namen bereits existiert:
#   - Gleiche oder kompatible Einheit: Mengen addieren (ggf. konvertieren)
#   - Inkompatible Einheiten (z.B. Gramm + Milliliter): `ValueError` auslösen
# - `items` (Property) — gibt alle Zutaten als Liste zurück
# - `from_recipes(recipes)` (Classmethod) — erzeugt eine ShoppingList aus
#   mehreren Rezepten
# - `__str__` — gibt eine formatierte Einkaufsliste als String zurück
#
# Nutzen Sie die Funktionen `units_are_compatible` und `convert` aus `unit.py`.
#
# > **Kursreferenz:** „Dictionaries" (in Abschnitt 07), „Klassen" und „Methoden"
# > (in Abschnitt 08 Klassen, Objekte und Methoden)
#
# ### Schritt 4: Tests
#
# Erstellen Sie Testdateien: `tests/recipe_book_test.py` (erweitern) und
# `tests/shopping_list_test.py` (neu).
#
# Nutzen Sie **Fixtures**, um Testdaten zu erstellen. Erstellen Sie eine Fixture,
# die mehrere Rezepte erzeugt und ins RecipeBook einfügt.
#
# Testen Sie:
# - Titelsuche mit verschiedenen Mustern (Teilmatch, Groß-/Kleinschreibung, Regex)
# - Suche nach Zutaten und Tags
# - Zeitfilter mit Grenzwerten
# - Zusammenführung von Zutaten in der Einkaufsliste (gleiche Einheit, kompatible
#   Einheiten, inkompatible Einheiten)
# - Leere Fälle (leeres RecipeBook, keine Treffer, leere Einkaufsliste)
#
# > **Kursreferenz:** „Pytest" (in Abschnitt 18 Unit-Tests und Test Frameworks)

# %% [markdown]
#
# ## Prüfe dein Ergebnis
#
# - [ ] `uv run pytest` läuft ohne Fehler
# - [ ] `search_by_title("pfann")` findet „Pfannkuchen" (Groß-/Kleinschreibung
#       wird ignoriert)
# - [ ] `search_by_title("^C")` findet alle Rezepte, die mit „C" beginnen
# - [ ] `search_by_ingredient("mehl")` findet alle Rezepte mit Mehl
# - [ ] `search_by_tag("schnell")` findet die richtigen Rezepte
# - [ ] `filter_by_max_time(15)` gibt nur schnelle Rezepte zurück
# - [ ] `ShoppingList.from_recipes(...)` fasst gleiche Zutaten zusammen
#       (z.B. 250g Mehl + 300g Mehl = 550g Mehl)
# - [ ] Mehl in g + Mehl in kg wird korrekt konvertiert und addiert
# - [ ] Mehl in g + Mehl in ml wirft `ValueError`
# - [ ] Sie haben mindestens 25 Tests (insgesamt)

# %% [markdown]
# *Antwort:* 
# ## Hinweise
#
# ### Zu Vorbereitung V1
#
# Eine List Comprehension mit Bedingung sieht so aus:
#
# ```python
# def filter_short_strings(strings: list[str], max_len: int) -> list[str]:
#     return [s for s in strings if len(s) <= max_len]
# ```
#
# Dieses Muster — eine Liste filtern und nur bestimmte Elemente behalten —
# werden Sie in den Suchmethoden häufig verwenden.
#
# ### Zu Vorbereitung V4
#
# Iterieren Sie über das zweite Dictionary und prüfen Sie für jeden Schlüssel,
# ob er bereits im Ergebnis vorhanden ist:
#
# ```python
# def merge_amounts(a: dict, b: dict) -> dict:
#     result = dict(a)  # Kopie von a
#     for key, value in b.items():
#         if key in result:
#             result[key] = result[key] + value
#         else:
#             result[key] = value
#     return result
# ```
#
# Die Methode `dict.get(key, default)` ist eine kürzere Alternative zu
# `if key in dict`.
#
# ### Zu Schritt 1: Suchmethoden
#
# Alle Suchmethoden verwenden List Comprehensions. Hier das Muster für die
# Titelsuche mit Regex:
#
# ```python
# import re
#
# def search_by_title(self, query: str) -> list[Recipe]:
#     pattern = re.compile(query, re.IGNORECASE)
#     return [r for r in self._recipes.values() if pattern.search(r.title)]
# ```
#
# `re.compile` erstellt ein Muster-Objekt, `pattern.search(text)` prüft, ob
# das Muster irgendwo im Text vorkommt.
#
# Für `search_by_ingredient`: Prüfen Sie mit `any()`, ob mindestens eine Zutat
# den gesuchten Namen hat:
#
# ```python
# any(i.name == name_lower for i in r.ingredients)
# ```
#
# Für `search_by_tag`: Tags ist ein `frozenset`, Mitgliedschaft prüfen Sie mit
# `tag in r.tags`.
#
# ### Zu Schritt 2: Kombinierte Suche
#
# Verwenden Sie ein Set, um die Schnittmenge der Ergebnisse zu berechnen.
# Beginnen Sie mit `None` und schneiden Sie nach und nach die Ergebnisse jeder
# Suchmethode zu:
#
# ```python
# results = None  # None bedeutet: noch kein Filter angewendet
#
# if title is not None:
#     keys = {r.title.lower() for r in self.search_by_title(title)}
#     results = keys if results is None else results & keys
# # ... weitere Filter analog
# ```
#
# Am Ende: Wenn `results` immer noch `None` ist, wurde kein Filter angewendet →
# alle Rezepte zurückgeben.
#
# ### Zu Schritt 3: `ShoppingList`
#
# Speichern Sie die Zutaten intern in einem Dictionary mit dem Zutatennamen als
# Schlüssel:
#
# ```python
# self._items: dict[str, Ingredient] = {}
# ```
#
# In `add_recipe`: Für jede Zutat prüfen, ob der Name bereits im Dictionary ist.
# Falls ja: kompatible Einheiten prüfen, konvertieren, Mengen addieren, neues
# Ingredient-Objekt erstellen. Falls nein: einfach einspeichern.
#
# Für die `from_recipes`-Classmethod:
#
# ```python
# @classmethod
# def from_recipes(cls, recipes: list[Recipe]) -> "ShoppingList":
#     shopping_list = cls()
#     for recipe in recipes:
#         shopping_list.add_recipe(recipe)
#     return shopping_list
# ```
#
# ### Zu Schritt 4: Tests mit Fixtures
#
# Fixtures erstellen Testdaten, die in mehreren Tests wiederverwendet werden:
#
# ```python
# @pytest.fixture
# def pancakes():
#     return Recipe(
#         title="Pancakes",
#         servings=4,
#         ingredients=(
#             Ingredient("flour", 250, Unit.GRAM),
#             Ingredient("milk", 500, Unit.MILLILITER),
#         ),
#         instructions=("Mix", "Cook"),
#         tags=frozenset({"breakfast", "quick"}),
#     )
#
# @pytest.fixture
# def book(pancakes, pasta, salad):
#     book = RecipeBook()
#     book.add_recipe(pancakes)
#     book.add_recipe(pasta)
#     book.add_recipe(salad)
#     return book
# ```
#
# Fixtures können andere Fixtures als Parameter verwenden — pytest löst die
# Abhängigkeiten automatisch auf.
