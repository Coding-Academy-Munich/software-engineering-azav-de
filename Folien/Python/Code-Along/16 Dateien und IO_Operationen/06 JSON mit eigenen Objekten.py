# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>JSON mit eigenen Objekten</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# # JSON mit eigenen Objekten

# %% [markdown]
#
# ## Das Problem
#
# - `json.dumps()` kann nur Python-Grundtypen serialisieren:
#   - `dict`, `list`, `str`, `int`, `float`, `bool`, `None`
# - Was passiert, wenn wir eigene Objekte in JSON speichern wollen?

# %%
import json
from pprint import pprint


# %%
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


# %%

# %%

# %%
try:
    json.dumps(p)
except TypeError as e:
    print(f"Error: {e}")

# %% [markdown]
#
# ## Objekte in JSON serialisieren
#
# - Strategie: Objekt in ein Dictionary umwandeln
# - `json.dumps()` kann Dictionaries problemlos serialisieren
# - Wir schreiben eine Funktion, die ein Objekt in ein Dict umwandelt

# %%

# %%

# %%

# %% [markdown]
#
# ## Der `default`-Parameter
#
# - `json.dumps()` hat einen `default`-Parameter
# - Eine Funktion, die für nicht-serialisierbare Objekte aufgerufen wird
# - Bekommt das Objekt und muss etwas JSON-serialisierbares zurückgeben
# - Typischerweise ein Dictionary

# %%

# %%

# %%
points = [Point(1, 2), Point(3, 4), Point(5, 6)]

# %%

# %% [markdown]
#
# ## Objekte aus JSON erzeugen
#
# - `json.loads()` erzeugt aus JSON-Objekten Python-Dictionaries
# - Wir wollen aber unsere eigenen Objekte zurückbekommen
# - Dafür gibt es den `object_hook`-Parameter
# - Eine Funktion, die für jedes geparste JSON-Objekt (Dict) aufgerufen wird
# - Der Rückgabewert ersetzt das Dictionary

# %%

# %%
json_string = json.dumps(points, default=point_serializer)

# %%

# %%

# %% [markdown]
#
# ## Typ-Erkennung mit `_type`
#
# - Problem: Wenn mehrere Objekttypen ähnliche Felder haben
# - Lösung: Ein `_type`-Feld beim Serialisieren hinzufügen
# - Beim Deserialisieren prüfen wir `_type` um den richtigen Typ zu wählen
# - Das ist ein gängiges Muster in JSON-APIs

# %%

# %%

# %%

# %%

# %%

# %% [markdown]
#
# ## Praxisbeispiel: Menüs
#
# - Die Datei `simple-menu.json` enthält Menü-Daten
# - Verschachtelte Struktur: Menüs enthalten Menüeinträge
# - Das `_type`-Feld ist bereits vorhanden

# %%
with open("simple-menu.json", encoding="utf-8") as file:
    menu_data = json.load(file)


# %%

# %% [markdown]
#
# Wir definieren Klassen für Menüs und Menüeinträge:

# %%
class MenuItem:
    def __init__(self, name, onclick):
        self.name = name
        self.onclick = onclick

    def __repr__(self):
        return f"MenuItem({self.name!r}, {self.onclick!r})"


# %%
class Menu:
    def __init__(self, id, name, items):
        self.id = id
        self.name = name
        self.items = items

    def __repr__(self):
        return f"Menu({self.id!r}, {self.name!r}, {self.items!r})"


# %% [markdown]
#
# Der `object_hook` prüft das `_type`-Feld und erzeugt das passende Objekt:

# %%
def menu_hook(d):
    if d.get("_type") == "menu":
        items = [MenuItem(m["name"], m["onclick"]) for m in d["menuitems"]]
        return Menu(d["id"], d["name"], items)
    return d


# %%

# %%

# %% [markdown]
#
# Der Serializer wandelt die Objekte zurück in Dictionaries:

# %%

# %%

# %% [markdown]
#
# Überprüfung: Stimmt die Serialisierung mit der Originaldatei überein?

# %%
with open("simple-menu.json", encoding="utf-8") as file:
    file_contents = file.read()

# %%


# %% [markdown]
#
# ## Mini-Workshop: Rezepte mit Objekten
#
# Die Datei `recipes.json` enthält Kochrezepte im JSON-Format als Liste von
# Objekten mit den Attributen `title`, `ingredients`, `instructions` und `tips`.

# %% [markdown]
#
# Wir verwenden folgende Klasse:

# %%
class Recipe:
    def __init__(self, title, ingredients, instructions, tips=None):
        self.title = title
        self.ingredients = ingredients
        self.instructions = instructions
        self.tips = tips if tips is not None else []

    def __repr__(self):
        return f"Recipe({self.title!r})"


# %% [markdown]
#
# Schreiben Sie Funktionen `recipe_hook` und `recipe_serializer` zum
# Deserialisieren und Serialisieren von `Recipe`-Instanzen.
#
# Lesen Sie die Datei `recipes.json` mit `object_hook` ein.
#
# Überprüfen Sie, dass die Serialisierung mit dem Dateiinhalt übereinstimmt.
#
# *Hinweis:* Verwenden Sie `ensure_ascii=False` bei `json.dumps()`.
#
# Geben Sie den Titel jedes Rezepts aus.

# %%

# %%

# %%

# %%

# %%
with open("recipes.json", "r", encoding="utf-8") as file:
    recipe_str = file.read()

# %%

# %%
