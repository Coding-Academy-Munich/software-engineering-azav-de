# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Pickling</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# ## Motivation
#
# - Bisher: Textdateien für einfache Daten
# - Problem: Wie speichert man komplexe Python-Objekte?
# - Listen, Dictionaries, eigene Klassen...
# - Lösung: **Pickling** (Serialisierung)

# %% [markdown]
#
# ## Was ist Pickling?
#
# - Umwandlung von Python-Objekten in Bytes
# - Diese Bytes können gespeichert oder übertragen werden
# - Später: Bytes zurück in Python-Objekte umwandeln
# - Name kommt von "einlegen" (wie Gurken!)

# %% [markdown]
#
# ## Pickle vs. JSON
#
# | Pickle | JSON |
# |--------|------|
# | Python-spezifisch | Universell lesbar |
# | Alle Python-Typen | Nur Basis-Typen |
# | Binärformat | Textformat |
# | Schnell | Langsamer |
# | **Sicherheitsrisiko!** | Sicher |

# %% [markdown]
#
# ## Das `pickle` Modul
#
# - `pickle.dumps(obj)`: Objekt → Bytes (im Speicher)
# - `pickle.loads(bytes)`: Bytes → Objekt (im Speicher)
# - `pickle.dump(obj, file)`: Objekt → Datei
# - `pickle.load(file)`: Datei → Objekt

# %%
import pickle
from pprint import pprint

# %% [markdown]
#
# ## Beispiel: Dictionary serialisieren
#
# - Wir erstellen ein verschachteltes Dictionary
# - Mit Listen als Werte

# %%
my_list = [1, 2, 3, 4]
my_other_list = [3, 4, 5]
my_dict = {1: my_list, 2: my_other_list, 3: "a string", 4: ["some list"]}

# %%

# %% [markdown]
#
# ## Serialisieren mit `dumps()`
#
# - `dumps()` erzeugt einen Bytes-String
# - Das ist das "eingelegte" Objekt

# %%

# %% [markdown]
#
# ## Deserialisieren mit `loads()`
#
# - `loads()` wandelt Bytes zurück in ein Objekt
# - Das neue Objekt ist eine **Kopie** des Originals

# %%

# %%

# %% [markdown]
#
# ## Gleichheit vs. Identität
#
# - Das wiederhergestellte Objekt ist **gleich** (`==`)
# - Aber **nicht identisch** (`is`)
# - Es ist eine unabhängige Kopie

# %%

# %%
my_dict is restored_pickle

# %% [markdown]
#
# ## Pickle erhält Referenzen
#
# - Pickle kann zirkuläre Referenzen speichern!
# - Objekte, die sich gegenseitig referenzieren
# - Das kann JSON nicht

# %% [markdown]
#
# ## Beispiel: Zirkuläre Referenzen
#
# - Wir lassen zwei Listen sich gegenseitig referenzieren
# - Pickle kann das problemlos speichern

# %%
my_list.append(my_other_list)
my_other_list.append(my_list)

# %%
pprint(my_list)


# %%
pprint(my_dict)

# %%
my_pickle = pickle.dumps(my_dict)
restored_pickle = pickle.loads(my_pickle)

# %%
pprint(restored_pickle)

# %% [markdown]
#
# ## Vorsicht bei Vergleichen!
#
# - Zirkuläre Strukturen können nicht mit `==` verglichen werden
# - Das führt zu einer Endlosschleife!

# %%
# Don't try this...
# my_dict == restored_pickle

# %% [markdown]
#
# ## Pickle in Dateien speichern
#
# - `pickle.dump(obj, file)`: In Datei schreiben
# - `pickle.load(file)`: Aus Datei lesen
# - **Wichtig**: Datei im Binärmodus öffnen (`"wb"`, `"rb"`)

# %%
data = {"name": "Alice", "scores": [95, 87, 92], "active": True}

# %%

# %%

# %%

# %% [markdown]
#
# ## Sicherheitswarnung!
#
# - **Niemals** Pickle-Daten aus unbekannten Quellen laden!
# - Pickle kann beliebigen Code ausführen
# - Angreifer können schadhaften Code einschleusen
# - Für externe Daten: JSON oder andere sichere Formate

# %% [markdown]
#
# ## Wann Pickle verwenden?
#
# - **Ja**: Eigene Daten zwischenspeichern
# - **Ja**: Daten zwischen eigenen Programmen austauschen
# - **Ja**: Komplexe Python-Objekte (ML-Modelle, etc.)
# - **Nein**: Daten von Benutzern oder dem Internet
# - **Nein**: Langzeit-Speicherung (Format kann sich ändern)

# %% [markdown]
#
# ## Zusammenfassung
#
# - Pickle serialisiert Python-Objekte in Bytes
# - Kann komplexe Strukturen speichern (auch zirkuläre)
# - Schnell und einfach für Python-zu-Python
# - **Aber**: Sicherheitsrisiko bei fremden Daten!
# - Alternativen: JSON, YAML, Protocol Buffers
