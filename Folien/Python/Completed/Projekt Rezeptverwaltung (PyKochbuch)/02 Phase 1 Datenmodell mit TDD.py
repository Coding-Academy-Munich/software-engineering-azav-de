# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Phase 1: Datenmodell mit TDD</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
#
# <div style="text-align:center;">Coding-Akademie München</div>
# <br/>


# %% [markdown]
#
# # Phase 1: Datenmodell mit TDD

# %% [markdown]
#
# ## Ziel
#
# In dieser Phase implementieren Sie die Grundbausteine der Rezeptverwaltung:
#
# - Ein `Unit`-Enum für Maßeinheiten
# - Eine `Ingredient`-Klasse (frozen Dataclass) mit Validierung
# - Eine `Recipe`-Klasse (Dataclass) mit Skalierungsfunktion
# - Eine `RecipeBook`-Klasse zum Verwalten mehrerer Rezepte
#
# Sie arbeiten dabei testgetrieben (TDD): Schreiben Sie **zuerst den Test**, dann
# die Implementierung.

# %% [markdown]
#
# ## So sieht das Ergebnis aus
#
# Wenn Phase 1 fertig ist, können Sie Folgendes tun:
#
# ```python
# from pykochbuch.unit import Unit
# from pykochbuch.ingredient import Ingredient
# from pykochbuch.recipe import Recipe
# from pykochbuch.recipe_book import RecipeBook
#
# # Zutaten erstellen
# mehl = Ingredient("Mehl", 500, Unit.GRAM)
# eier = Ingredient("Eier", 3, Unit.PIECE)
#
# # Rezept erstellen
# pfannkuchen = Recipe(
#     title="Pfannkuchen",
#     servings=4,
#     ingredients=(mehl, eier),
#     instructions=("Zutaten verrühren", "In der Pfanne braten"),
#     tags=frozenset({"schnell", "vegetarisch"}),
# )
#
# # Portionen skalieren
# fuer_8 = pfannkuchen.scale_to_servings(8)
# # → 1000g Mehl, 6 Eier
#
# # Rezeptbuch verwalten
# buch = RecipeBook()
# buch.add_recipe(pfannkuchen)
# ```

# %% [markdown]
#
# ## Vorbereitung
#
# Bevor Sie mit den Klassen beginnen, üben Sie die grundlegenden Konzepte mit
# diesen kleinen Aufgaben. Sie können sie in einem separaten Notebook lösen.
#
# **Aufgabe V1:** Schreiben Sie eine Funktion `format_ingredient`, die einen
# Namen (str), eine Menge (float) und eine Einheit (str) als Parameter nimmt und
# einen formatierten String zurückgibt, z.B. `"500g mehl"`. Der Name soll dabei
# in Kleinbuchstaben umgewandelt werden.
#
# > **Kursreferenz:** „Funktionen" (in Abschnitt 05 Kontrollstrukturen und
# > Funktionen), „String-Interpolation"
#
# **Aufgabe V2:** Schreiben Sie eine Funktion `scale_amounts`, die eine Liste
# von Zahlen und einen Faktor nimmt und eine neue Liste mit den skalierten Werten
# zurückgibt. Beispiel: `scale_amounts([500, 3, 200], 2)` → `[1000, 6, 400]`.
#
# > **Kursreferenz:** „Listen" und „For-Schleifen" (in Abschnitt 05)
#
# **Aufgabe V3:** Schreiben Sie eine Funktion `validate_positive`, die eine Zahl
# nimmt und einen `ValueError` auslöst, wenn die Zahl nicht positiv ist.
# Testen Sie die Funktion mit verschiedenen Eingaben.
#
# > **Kursreferenz:** „Kontrollstrukturen" (in Abschnitt 05),
# > „Ausnahmen (Exceptions)" (in Abschnitt 10 Fehlerbehandlung)
#
# **Aufgabe V4:** Erstellen Sie ein Dictionary, das Maßeinheiten-Abkürzungen
# auf ihre vollen Namen abbildet: `{"g": "Gramm", "kg": "Kilogramm", ...}`.
# Schreiben Sie eine Funktion, die zu einer Abkürzung den vollen Namen
# zurückgibt.
#
# > **Kursreferenz:** „Dictionaries" (in Abschnitt 07 Weitere Datenstrukturen
# > und Reguläre Ausdrücke)

# %% [markdown]
#
# ## Aufgaben
#
# ### Schritt 1: Projekt aufsetzen
#
# Erstellen Sie das Projekt wie in der Übersicht beschrieben (`uv init --lib`,
# `uv add --dev pytest`). Erstellen Sie die leeren Dateien:
#
# - `src/pykochbuch/unit.py`
# - `src/pykochbuch/ingredient.py`
# - `src/pykochbuch/recipe.py`
# - `src/pykochbuch/recipe_book.py`
# - `tests/unit_test.py`
# - `tests/ingredient_test.py`
# - `tests/recipe_test.py`
# - `tests/recipe_book_test.py`
#
# > **Kursreferenz:** „Der uv Package Manager" (in Abschnitt 14 Module und
# > Packages)
#
# ### Schritt 2: `Unit`-Enum
#
# Erstellen Sie ein Enum `Unit` mit 7 Maßeinheiten: Gramm, Kilogramm,
# Milliliter, Liter, Stück, Esslöffel, Teelöffel. Jeder Wert hat eine
# Abkürzung als String (z.B. `"g"`, `"kg"`).
#
# Implementieren Sie außerdem zwei Hilfsfunktionen:
#
# - `units_are_compatible(a, b)` — prüft, ob zwei Einheiten ineinander
#   umgerechnet werden können (z.B. g ↔ kg, ml ↔ l)
# - `convert(amount, from_unit, to_unit)` — rechnet einen Betrag um
#
# > **Kursreferenz:** „Enumerationen" (in Abschnitt 15 Objektorientierte Analyse
# > und Design (Teil 2))
#
# ### Schritt 3: `Ingredient`
#
# Erstellen Sie eine **frozen** Dataclass `Ingredient` mit den Feldern `name`
# (str), `amount` (float) und `unit` (Unit).
#
# Validierung in `__post_init__`:
#
# - `name` darf nicht leer sein (Whitespace entfernen und prüfen)
# - `amount` muss positiv sein
# - `name` soll normalisiert werden (Whitespace entfernen, Kleinbuchstaben)
#
# Fügen Sie eine `scale(factor)`-Methode hinzu, die ein neues `Ingredient` mit
# skaliertem `amount` zurückgibt.
#
# > **Kursreferenz:** „Dataclasses", „Unveränderliche Dataclasses",
# > „Initialisierung von Dataclasses" (in Abschnitt 09 Objektmodell und Magic
# > Methods)
#
# ### Schritt 4: `Recipe`
#
# Erstellen Sie eine Dataclass `Recipe` mit: `title`, `description`, `servings`,
# `prep_time_minutes`, `ingredients` (Tuple von Ingredients), `instructions`
# (Tuple von Strings) und `tags` (Frozenset von Strings).
#
# Validierung:
#
# - `title` darf nicht leer sein
# - `servings` muss größer als 0 sein
# - Es muss mindestens eine Zutat und eine Anweisung geben
#
# Methoden:
#
# - `scale(factor)` — gibt ein neues Recipe mit skalierten Zutaten zurück
# - `scale_to_servings(n)` — berechnet den Faktor und ruft `scale()` auf
#
# > **Kursreferenz:** „Dataclasses" (in Abschnitt 09),
# > „Tupel" (in Abschnitt 06 Sequenzen)
#
# ### Schritt 5: `RecipeBook`
#
# Erstellen Sie eine Klasse `RecipeBook`, die Rezepte in einem Dictionary
# verwaltet (Titel als Schlüssel).
#
# Methoden:
#
# - `add_recipe(recipe)` — fügt ein Rezept hinzu; `ValueError` bei Duplikat
# - `remove_recipe(title)` — entfernt ein Rezept; `KeyError` wenn nicht gefunden
# - `get_recipe(title)` — gibt ein einzelnes Rezept zurück
# - `recipes` (Property) — gibt alle Rezepte als Liste zurück
#
# > **Kursreferenz:** „Klassen" und „Methoden" (in Abschnitt 08 Klassen, Objekte
# > und Methoden), „Properties" (in Abschnitt 09), „Dictionaries" (in Abschnitt
# > 07)
#
# ### Schritt 6: Tests schreiben
#
# Schreiben Sie Tests für jede Klasse. Nutzen Sie TDD: Schreiben Sie den Test
# **vor** der Implementierung und prüfen Sie, dass der Test zuerst fehlschlägt
# (rot), dann nach der Implementierung besteht (grün).
#
# Testen Sie insbesondere:
#
# - Validierung (ungültige Eingaben lösen die richtigen Exceptions aus)
# - Skalierung (Rechenlogik korrekt?)
# - Einheitenkonvertierung
# - Hinzufügen/Entfernen im RecipeBook
#
# > **Kursreferenz:** „Pytest" und „Test-Driven-Development" (in Abschnitt 18
# > Unit-Tests und Test Frameworks)

# %% [markdown]
#
# ## Prüfe dein Ergebnis
#
# - [ ] `uv run pytest` läuft ohne Fehler
# - [ ] `Ingredient("Mehl", 500, Unit.GRAM)` erzeugt ein Ingredient mit
#       `name == "mehl"` (normalisiert)
# - [ ] `Ingredient("", 100, Unit.GRAM)` wirft `ValueError`
# - [ ] `Ingredient("Mehl", -1, Unit.GRAM)` wirft `ValueError`
# - [ ] Ein Rezept mit 4 Portionen, skaliert auf 8 Portionen, verdoppelt alle
#       Zutatenmengen
# - [ ] `RecipeBook.add_recipe()` mit doppeltem Titel wirft `ValueError`
# - [ ] `RecipeBook.remove_recipe()` mit unbekanntem Titel wirft `KeyError`
# - [ ] `convert(1000, Unit.GRAM, Unit.KILOGRAM)` ergibt `1.0`
# - [ ] Sie haben mindestens 15 Tests

# %% [markdown]
# *Antwort:* 
# ## Hinweise
#
# ### Zu Vorbereitung V1
#
# Verwenden Sie einen f-String und die String-Methode `.lower()`:
#
# ```python
# def format_ingredient(name: str, amount: float, unit: str) -> str:
#     return f"{amount:g}{unit} {name.lower()}"
# ```
#
# Die Format-Angabe `:g` entfernt unnötige Nachkommastellen (z.B. `500.0` →
# `500`).
#
# ### Zu Vorbereitung V3
#
# So lösen Sie einen `ValueError` aus:
#
# ```python
# def validate_positive(value: float) -> None:
#     if value <= 0:
#         raise ValueError(f"Wert muss positiv sein, ist aber {value}")
# ```
#
# ### Zu Schritt 2: `Unit`-Enum
#
# Definieren Sie das Enum so:
#
# ```python
# from enum import Enum
#
# class Unit(Enum):
#     GRAM = "g"
#     KILOGRAM = "kg"
#     # ... weitere Einheiten
# ```
#
# Für die Konvertierung speichern Sie die Umrechnungsfaktoren in einem Dictionary
# mit Tupeln als Schlüssel — genau wie in Vorbereitung V4, nur mit
# `(Unit, Unit)`-Tupeln statt Strings:
#
# ```python
# CONVERSIONS = {
#     (Unit.GRAM, Unit.KILOGRAM): 0.001,
#     (Unit.KILOGRAM, Unit.GRAM): 1000,
#     # ...
# }
# ```
#
# `units_are_compatible` prüft, ob `a == b` oder ob `(a, b)` im Dictionary
# vorhanden ist. Die `in`-Prüfung für Dictionaries funktioniert genauso wie bei
# Listen.
#
# ### Zu Schritt 3: `Ingredient`
#
# Bei einer `frozen` Dataclass können Sie Felder nicht direkt in `__post_init__`
# zuweisen — Python verhindert das, weil das Objekt unveränderlich sein soll.
# Verwenden Sie stattdessen diesen Trick:
#
# ```python
# object.__setattr__(self, "name", normalized_name)
# ```
#
# Die String-Methode `.strip()` entfernt Leerzeichen am Anfang und Ende,
# `.lower()` wandelt in Kleinbuchstaben um. Sie können beides verketten:
# `self.name.strip().lower()`.
#
# Für `scale()`: Da `Ingredient` frozen ist, können Sie `self.amount` nicht
# ändern. Erstellen Sie stattdessen ein **neues** Ingredient-Objekt mit dem
# skalierten Wert.
#
# ### Zu Schritt 4: `Recipe`
#
# Verwenden Sie `tuple` statt `list` für `ingredients` und `instructions`, und
# `frozenset` statt `set` für `tags`. So verhindern Sie versehentliche
# Änderungen nach der Erstellung.
#
# Für `tags` brauchen Sie `field(default_factory=frozenset)` als Defaultwert,
# da `frozenset()` ein veränderbares Defaultargument wäre.
#
# Die `scale`-Methode erstellt ein **neues** Recipe-Objekt. Verwenden Sie einen
# Generator-Ausdruck, um alle Zutaten zu skalieren:
#
# ```python
# ingredients=tuple(i.scale(factor) for i in self.ingredients)
# ```
#
# Für `scale_to_servings`: Der Faktor berechnet sich als
# `gewünschte_portionen / aktuelle_portionen`.
#
# ### Zu Schritt 5: `RecipeBook`
#
# Verwenden Sie ein Dictionary mit dem Titel in Kleinbuchstaben als Schlüssel.
# So vermeiden Sie Duplikate unabhängig von Groß-/Kleinschreibung:
#
# ```python
# def add_recipe(self, recipe: Recipe) -> None:
#     key = recipe.title.lower()
#     if key in self._recipes:
#         raise ValueError(...)
#     self._recipes[key] = recipe
# ```
#
# Für die `recipes`-Property: Geben Sie `list(self._recipes.values())` zurück.
# Eine Property definieren Sie mit dem `@property`-Dekorator.
#
# ### Zu Schritt 6: Tests
#
# Nützliche pytest-Features für diese Phase:
#
# - `pytest.raises(ValueError)` — prüft, dass eine Exception geworfen wird.
#   Verwenden Sie es als Kontextmanager mit `with`:
#   ```python
#   with pytest.raises(ValueError):
#       Ingredient("", 100, Unit.GRAM)
#   ```
# - `pytest.approx(expected)` — vergleicht Floats mit Toleranz, nützlich bei
#   Skalierungsberechnungen
# - `@pytest.mark.parametrize` — führt einen Test mit verschiedenen Eingaben aus:
#   ```python
#   @pytest.mark.parametrize("factor,expected", [(2, 1000), (0.5, 250)])
#   def test_ingredient_scaling(factor, expected):
#       ing = Ingredient("Mehl", 500, Unit.GRAM)
#       scaled = ing.scale(factor)
#       assert scaled.amount == pytest.approx(expected)
#   ```
