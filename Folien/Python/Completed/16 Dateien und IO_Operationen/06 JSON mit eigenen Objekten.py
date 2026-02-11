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
p = Point(3, 4)

# %%
p

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
def point_to_dict(p):
    return {"x": p.x, "y": p.y}


# %%
point_to_dict(p)

# %%
json.dumps(point_to_dict(p))

# %% [markdown]
#
# ## Der `default`-Parameter
#
# - `json.dumps()` hat einen `default`-Parameter
# - Eine Funktion, die für nicht-serialisierbare Objekte aufgerufen wird
# - Bekommt das Objekt und muss etwas JSON-serialisierbares zurückgeben
# - Typischerweise ein Dictionary

# %%
def point_serializer(obj):
    if isinstance(obj, Point):
        return {"x": obj.x, "y": obj.y}
    raise TypeError(f"Object of type {type(obj)} is not JSON serializable")


# %%
json.dumps(p, default=point_serializer)

# %%
points = [Point(1, 2), Point(3, 4), Point(5, 6)]

# %%
print(json.dumps(points, default=point_serializer, indent=2))

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
def point_hook(d):
    if "x" in d and "y" in d:
        return Point(d["x"], d["y"])
    return d


# %%
json_string = json.dumps(points, default=point_serializer)

# %%
json_string

# %%
json.loads(json_string, object_hook=point_hook)

# %% [markdown]
#
# ## Typ-Erkennung mit `_type`
#
# - Problem: Wenn mehrere Objekttypen ähnliche Felder haben
# - Lösung: Ein `_type`-Feld beim Serialisieren hinzufügen
# - Beim Deserialisieren prüfen wir `_type` um den richtigen Typ zu wählen
# - Das ist ein gängiges Muster in JSON-APIs

# %%
def point_serializer_v2(obj):
    if isinstance(obj, Point):
        return {"_type": "point", "x": obj.x, "y": obj.y}
    raise TypeError(f"Object of type {type(obj)} is not JSON serializable")


# %%
def point_hook_v2(d):
    if d.get("_type") == "point":
        return Point(d["x"], d["y"])
    return d


# %%
json_string = json.dumps(points, default=point_serializer_v2)

# %%
json_string

# %%
json.loads(json_string, object_hook=point_hook_v2)

# %% [markdown]
#
# ## Mehrere Typen und verschachtelte Objekte
#
# - Wir erweitern unser Beispiel um eine `Line`-Klasse
# - Eine Linie verbindet zwei Punkte
# - Dies zeigt verschachtelte Objekt-Serialisierung

# %%
class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __repr__(self):
        return f"Line({self.start!r}, {self.end!r})"


# %%
line = Line(Point(1, 2), Point(3, 4))

# %%
line

# %% [markdown]
#
# Ein Serializer für mehrere geometrische Typen:

# %%
def geo_serializer(obj):
    if isinstance(obj, Point):
        return {"_type": "point", "x": obj.x, "y": obj.y}
    if isinstance(obj, Line):
        return {"_type": "line", "start": obj.start, "end": obj.end}
    raise TypeError(f"Object of type {type(obj)} is not JSON serializable")


# %%
print(json.dumps(line, default=geo_serializer, indent=2))

# %%
geo_objects = [Point(1, 2), line, Point(5, 6)]

# %%
print(json.dumps(geo_objects, default=geo_serializer, indent=2))

# %% [markdown]
#
# Der `object_hook` wird bottom-up aufgerufen:
# - Zuerst werden die verschachtelten Objekte (Points) deserialisiert
# - Dann das umschließende Objekt (Line)

# %%
def geo_hook(d):
    type_val = d.get("_type")
    if type_val == "point":
        return Point(d["x"], d["y"])
    if type_val == "line":
        return Line(d["start"], d["end"])
    return d


# %%
geo_json = json.dumps(geo_objects, default=geo_serializer)

# %%
json.loads(geo_json, object_hook=geo_hook)

# %% [markdown]
#
# ## Warum `_type` wichtig ist
#
# - Was passiert, wenn wir Objekte und normale Dictionaries mischen?
# - Das `_type`-Feld unterscheidet zwischen getypten Objekten und einfachen Daten

# %%
mixed_data = [
    Point(1, 2),
    Line(Point(3, 4), Point(5, 6)),
    {"x": 10, "y": 20},
    {"start": "Hello", "end": "Goodbye"},
]

# %%
mixed_json = json.dumps(mixed_data, default=geo_serializer, indent=2)

# %%
print(mixed_json)

# %%
json.loads(mixed_json, object_hook=geo_hook)


# %% [markdown]
#
# - Objekte mit `_type` werden korrekt zu ihren Klassen konvertiert
# - Dictionaries ohne `_type` bleiben Dictionaries
# - So vermeiden wir falsche Konvertierungen

# %% [markdown]
#
# ## Mini-Workshop: Rezepte mit Objekten
#
# Die Datei `typed-recipes.json` enthält Kochrezepte im JSON-Format als Liste von
# Objekten mit den Attributen `_type`, `title`, `ingredients`, `instructions`
# und `tips`.
#
# *Hinweis:* Zum Testen können Sie `typed-recipes-short.json` verwenden, die nur
# 2 einfache Rezepte enthält.

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
# Verwenden Sie das `_type`-Feld zur Erkennung von Rezept-Objekten.
#
# Lesen Sie die Datei `typed-recipes.json` mit `object_hook` ein.
#
# Überprüfen Sie, dass die Serialisierung mit dem Dateiinhalt übereinstimmt.
#
# *Hinweis:* Verwenden Sie `ensure_ascii=False` bei `json.dumps()`.
#
# Geben Sie den Titel jedes Rezepts aus.

# %%
def recipe_hook(d):
    if d.get("_type") == "recipe":
        return Recipe(
            d["title"], d["ingredients"], d["instructions"], d.get("tips", [])
        )
    return d


# %%
def recipe_serializer(obj):
    if isinstance(obj, Recipe):
        return {
            "_type": "recipe",
            "title": obj.title,
            "ingredients": obj.ingredients,
            "instructions": obj.instructions,
            "tips": obj.tips,
        }
    raise TypeError(f"Object of type {type(obj)} is not JSON serializable")


# %%
with open("typed-recipes.json", "r", encoding="utf-8") as file:
    recipes = json.load(file, object_hook=recipe_hook)

# %%
recipes

# %%
with open("typed-recipes.json", "r", encoding="utf-8") as file:
    recipe_str = file.read()

# %%
json.dumps(recipes, default=recipe_serializer, indent=2, ensure_ascii=False) == recipe_str

# %%
for recipe in recipes:
    print(recipe.title)
