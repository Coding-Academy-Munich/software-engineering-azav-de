# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Komprehensionen: Elegantere Iteration</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# # Eleganter: Listen-Komprehension

# %%
result = []
for item in [1, 2, 3, 4]:
    result.append(item + 1)
result

# %%
my_list = [item + 1 for item in [1, 2, 3, 4]]
my_list

# %%
result = []
for n in [1, 2, 3, 4]:
    result.append(f"Item {n}")
result

# %%
[f"Item {n}" for n in [1, 2, 3, 4]]

# %% [markdown]
#
#  ## Mini-Workshop
#
# Schreiben Sie die folgenden Ausdrücke als Listen-Komprehensionen:

# %%
result = []
for item in [1, 2, 3, 4, 5, 6]:
    if item % 2 == 0:
        result.append(item)
result

# %%
[item for item in [1, 2, 3, 4, 5, 6] if item % 2 == 0]

# %%
result = []
for item in ["abc", "def", "asd", "qwe", "bab"]:
    if item[0] == "a":
        result.append(item)
result

# %%
[item for item in ["abc", "def", "asd", "qwe"] if item[0] == "a"]


# %% [markdown]
# # Quadratzahlen mit Listen-Komprehension
#
# Erzeugen Sie eine neue Liste mit den Quadraten von `numbers`. Verwenden Sie
# dazu eine Listen-Komprehension

# %%
numbers = [1, 7, 4, 87, 23]

# %%
[n * n for n in numbers]


# %% [markdown]
#
# Schreiben Sie eine Funktion `quadriere(zahlen)`, die jedes Element einer Liste
# quadriert, mit Listen-Komprehension.

# %%
def quadriere(zahlen):
    return [n * n for n in zahlen]


# %%
quadriere(numbers)


# %%
result = []
for list_1 in [[1, 2], ["a", "b", "c"]]:
    for item in list_1:
        result.append(f"Item {item} in {list_1}")
result


# %%
[f"Item {item} in {list_1}" for list_1 in [[1, 2], ["a", "b", "c"]] for item in list_1]


# %% [markdown]
#
# ## Mini-Workshop: Tupledatenbank
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
def filter_city(data, city):
    return [(first, last) for first, last, _, c in data if c == city]


# %%
filter_city(data, "Musterstadt")


# %% [markdown]
# # Filtern mit Listen-Komprehension
#
# Erzeugen Sie eine neue Liste, die alle Zahlen in `numbers` enthält, die größer
# als 10 sind. Verwenden Sie dazu Listen-Komprehension.

# %%
[n for n in numbers if n > 10]


# %% [markdown]
# Schreiben Sie die Funktion `zahlen_größer_als_10(zahlen)` mit
# Listen-Komprehension.

# %%
def zahlen_größer_als_10(zahlen):
    return [n for n in zahlen if n > 10]


# %%
assert zahlen_größer_als_10(numbers) == [87, 23]
