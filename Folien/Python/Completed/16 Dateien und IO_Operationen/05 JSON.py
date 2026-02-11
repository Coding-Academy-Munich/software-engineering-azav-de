# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>JSON</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# # JSON
#
# Python bietet ein eingebautes Paket `json` an, mit dem JSON-Daten in
# Python-Datenstrukturen übersetzt werden können.

# %%
import json
from pprint import pprint

# %% [markdown]
#
# ## JSON aus Strings
#
# Zur Illustration laden wir die JSON-Datei in einen String und wandeln den String
# in Python-Objekte um. Normalerweise führen wir die Umwandlung direkt von der
# Datei aus durch, ohne vorher einen Python-String zu erzeugen.

# %%
with open("simple-menu.json") as file:
    json_data = file.read()

# %%
print(json_data)

# %%
type(json_data)

# %% [markdown]
#
# Die Funktion `json.loads()` wandelt einen String im JSON-Format in Python-Objekte
# um. Dabei werden die JSON-Datentypen wie folgt nach Python übersetzt:
#
# | JSON Typ | Python Typ      |
# |----------|-----------------|
# | `object`  | `dict`          |
# | `array`  | `list`, `tuple` |
# | `string` | `str`           |
# | `number` | `int`, `float`  |
# | `true`   | `True`          |
# | `false`  | `False`         |
# | `null`   | `None`          |

# %%
data = json.loads(json_data)

# %%
type(data)

# %%
pprint(data)

# %%
json_dump = json.dumps(data)

# %%
type(json_dump)

# %%
print(json_dump)

# %%
print(json.dumps(data, indent=4))

# %% [markdown]
#
# Meistens verwendet man die Funktion `json.load()` um die JSON-Daten direkt aus einer
# Datei zu laden:

# %%
with open("simple-menu.json", encoding="utf-8") as file:
    json_data = json.load(file)

# %%
pprint(json_data)

# %% [markdown]
#
# ## Mini-Workshop: Kochrezepte
#
# In der Datei `recipes.json` sind Kochrezepte im JSON-Format gespeichert.
#
# Die Rezepte sind in einer Liste zusammengefasst.
#
# Jedes Rezept ist dabei ein JSON Objekt, das folgende Attribute enthält:
# - `title` (String)
# - `ingredients` (Liste von Strings): die Zutaten
# - `instructions` (Liste von Strings): Anweisungen zum Kochen; jedes Element gibt
#   einen Schritt des Kochablaufs an
# - `tips` (Liste von Strings): Weitere Hinweise
#
# *Hinweis:* Zum Testen können Sie `recipes-short.json` verwenden, die nur
# 2 einfache Rezepte enthält.
#
# Lesen Sie diese Datei ein und geben Sie die Liste der Rezepte in folgendem
# Format aus:
#
# ```
# # Title
#
# ## Ingredients
# - Zutat 1
# - Zutat 2
# - ...
#
# ## Instructions
# 1. Anweisung 1
# 2. Anweisung 2
# 3. ...
#
# ## Tips
# - Tip 1
# - Tip 2
# - ...
# ```

# %%
with open("recipes.json", "r", encoding="utf-8") as file:
    recipes = json.load(file)

# %%
pprint(recipes)

# %%
for recipe in recipes:
    print(f"# {recipe['title']}\n")
    print("## Ingredients\n")
    for ingredient in recipe["ingredients"]:
        print(f"- {ingredient}")
    print("\n## Instructions\n")
    for n, instruction in enumerate(recipe["instructions"], 1):
        print(f"{n}. {instruction}")
    print("\n## Tips\n")
    for tip in recipe["tips"]:
        print(f"- {tip}")
    print("\n")

# %%
