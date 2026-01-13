# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Fortgeschrittene Komprehensionen</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# ## Komplexere Iteration
#
# - Komplexere Iteration:
#   - Beliebige Kombinationen von `for`-Schleifen und `if`-Anweisungen
#   - Beispiel: Geschachtelte Schleifen

# %%
result = []
for list_1 in [[1, 2], ["a", "b", "c"]]:
    for item in list_1:
        result.append(f"Item {item} in {list_1}")
result


# %%


# %% [markdown]
#
# Beispiel: `for`-Schleifen mit `if`-Anweisung

# %%
values = [1, ['a', 'b'], 3, 4, ['c', 'd', 'e']]

# %%

# %%

# %% [markdown]
#
# ### Hinweis
#
# - `else`- und `elif`-Anweisungen sind nicht vorgesehen
# - Es ist besser, komplexe Komprehensionen zu vermeiden

# %% [markdown]
#
# ## Destrukturierung
#
# Wenn die Elemente in der Liste selber Tupel oder Listen sind und alle die
# gleiche Struktur haben, können Sie die Elemente auch destrukturieren:

# %%
# (Model, Production-Start, Production-End)
cars = [
    ("Chevrolet Corvette C1", 1953, 1962),
    ("Ford Mustang (First Generation)", 1964, 1973),
    ("Volkswagen Beetle (Type 1 - Original)", 1938, 2003),
    ("Porsche 911 (993 Generation - last air-cooled)", 1994, 1998),
    ("Honda Civic (EK - Sixth Generation)", 1995, 2000),
    ("Toyota Camry (XV20)", 1996, 2001),
    ("BMW 3 Series (E30)", 1982, 1991),
    ("Mercedes-Benz S-Class (W126)", 1979, 1991),
]

# %%

# %%

# %%

# %% [markdown]
#
# ## Workshop: Tupledatenbank
#
# Wir haben eine Tupeldatenbank mit den folgenden Einträgen:
#
# ```python
# data = [
#     ("Max", "Mustermann", 1999, "Musterstadt"),
#     ("John", "Doe", 1995, "New York"),
#     ("Jane", "Doe", 1996, "New York"),
#     ("Erika", "Mustermann", 2002, "Musterstadt"),
#     ("Franziska", "Musterfrau", 2001, "Musterstadt"),
#     ("Max", "Mustermann", 1972, "Musterstadt"),
#     ("Max", "Power", 1972, "Springfield"),
#     ("Peter", "Pan", 1953, "Nimmerland"),
# ]
# ```
#
# Schreiben Sie eine Funktion `filter_city(data, city)`, die eine Liste
# aller Personen zurückgibt, die in der Stadt `city` leben. Verwenden Sie
# dazu eine list comprehension. Die Liste soll dabei aus Tupeln der Form `(Vorname, Nachname)` bestehen.
#

# %%
data = [
    ("Max", "Mustermann", 1999, "Musterstadt"),
    ("John", "Doe", 1995, "New York"),
    ("Jane", "Doe", 1996, "New York"),
    ("Erika", "Mustermann", 2002, "Musterstadt"),
    ("Franziska", "Musterfrau", 2001, "Musterstadt"),
    ("Max", "Mustermann", 1972, "Musterstadt"),
    ("Max", "Power", 1972, "Springfield"),
    ("Peter", "Pan", 1953, "Nimmerland"),
]

# %%

# %%

# %% [markdown]
#
# - Schreiben Sie eine Funktion `filter_year(data, years)`, die eine Liste oder
#   Range von Jahren bekommt und alle Personen zurückgibt, die in einem der
#   Jahre aus `years` geboren wurde.
# - Verwenden Sie dazu eine list comprehension.
# - Die Liste soll dabei aus Tupeln der Form `(Vorname, Nachname)` bestehen.

# %%

# %%
