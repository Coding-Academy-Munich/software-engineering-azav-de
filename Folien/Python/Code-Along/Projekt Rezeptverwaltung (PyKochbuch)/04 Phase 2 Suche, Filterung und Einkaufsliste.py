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
