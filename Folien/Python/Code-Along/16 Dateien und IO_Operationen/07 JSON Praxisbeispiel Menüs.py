# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>JSON Praxisbeispiel: Menüs</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# # JSON Praxisbeispiel: Menüs

# %% [markdown]
#
# ## Praxisbeispiel: Menüs
#
# - Die Datei `menu-config.json` enthält eine Menü-Konfiguration
# - Verschachtelte Struktur: Menüs enthalten Menüeinträge und Separatoren
# - Jedes Objekt hat ein `_type`-Feld
# - Das gleiche Format wird vom Beispielprojekt `JsonMenuApp` verwendet

# %%
import json
from pprint import pprint

# %%
with open("menu-config.json", encoding="utf-8") as file:
    menu_data = json.load(file)


# %%

# %% [markdown]
#
# Wir definieren Klassen für Menüs, Menüeinträge und Separatoren:

# %%
class MenuItem:
    def __init__(self, name, action, shortcut=None):
        self.name = name
        self.action = action
        self.shortcut = shortcut

    def __repr__(self):
        if self.shortcut:
            return f"MenuItem({self.name!r}, {self.action!r}, {self.shortcut!r})"
        return f"MenuItem({self.name!r}, {self.action!r})"


# %%
class Separator:
    def __repr__(self):
        return "Separator()"


# %%
class Menu:
    def __init__(self, name, items):
        self.name = name
        self.items = items

    def __repr__(self):
        return f"Menu({self.name!r}, {self.items!r})"


# %% [markdown]
#
# Der `object_hook` prüft das `_type`-Feld und erzeugt das passende Objekt:
#
# - `object_hook` wird bottom-up aufgerufen
# - Menüeinträge und Separatoren werden zuerst erzeugt
# - Wenn das Menü verarbeitet wird, enthält `d["items"]` bereits Objekte

# %%
def menu_hook(d):
    type_val = d.get("_type")
    if type_val == "menuitem":
        return MenuItem(d["name"], d["action"], d.get("shortcut"))
    if type_val == "separator":
        return Separator()
    if type_val == "menu":
        return Menu(d["name"], d["items"])
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
with open("menu-config.json", encoding="utf-8") as file:
    file_contents = file.read()

# %%

# %% [markdown]
#
# ## Vollständiges Beispiel: JSON Menu App
#
# Im Ordner `examples/JsonMenuApp` finden Sie eine vollständige Anwendung:
#
# - Text-Editor (tkinter) mit Menüleiste aus JSON konfiguriert
# - Zeigt alle besprochenen Patterns in einer echten Anwendung
# - Menüeinträge, Separatoren und Tastaturkürzel aus der JSON-Datei
# - Ändern Sie `data/menu-config.json` um die Menüs anzupassen

# %% [markdown]
#
# **Ausprobieren:**
#
# ```bash
# cd examples/JsonMenuApp
# uv sync
# uv run json-menu-app
# ```
