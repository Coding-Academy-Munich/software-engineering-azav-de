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

# %%

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

# %%

# %%

# %%

# %%

# %%

# %%

# %% [markdown]
#
# Meistens verwendet man die Funktion `json.load()` um die JSON-Daten direkt aus einer
# Datei zu laden:

# %%

# %%

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

# %%

# %%

# %%
