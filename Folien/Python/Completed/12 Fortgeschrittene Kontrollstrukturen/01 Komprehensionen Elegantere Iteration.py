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
# ## Wiederholung: Iteration mit Schleifen
#
# Wir hatten drei grundlegende Arten von `for`-Schleifen identifiziert:
#
# ### Aggregation
#
# Eine Liste wird in eine einzelne Zahl zusammengefasst.

# %%
result = 0
for n in [1, 2, 3]:
    result += n
result

# %% [markdown]
#
# ### Transformation
#
# - Eine Liste wird in eine neue Liste umgewandelt.
# - Dabei wird jedes Element der Liste bearbeitet.

# %%
result = []
for item in [1, 2, 3, 4]:
    result.append(item + 1)
result

# %% [markdown]
#
# ### Filterung
#
# - Eine Liste wird in eine neue Liste umgewandelt.
# - Dabei werden nur bestimmte Elemente der Liste ausgewählt.
# - Die anderen Elemente werden verworfen.

# %%
result = []
for item in [1, 2, 3, 4]:
    if item % 2 == 0:
        result.append(item)
result

# %% [markdown]
#
# ## Eleganter: Listen-Komprehension
#
# - Kompakte Syntax für die Transformation und Filterung von Listen
# - Beide Operationen können zusammengefasst werden

# %% [markdown]
#
# ### Transformation

# %%
result = []
for item in [1, 2, 3, 4]:
    result.append(item + 1)
result

# %%
[item + 1 for item in [1, 2, 3, 4]]

# %% [markdown]
#
# ### Filterung

# %%
result = []
for item in [1, 2, 3, 4]:
    if item % 2 == 0:
        result.append(item)
result

# %%
[item for item in [1, 2, 3, 4] if item % 2 == 0]

# %% [markdown]
#
# ### Kombination von Transformation und Filterung

# %%
result = []
for item in [1, 2, 3, 4]:
    if item % 2 == 0:
        result.append(item + 1)
result

# %%
[item + 1 for item in [1, 2, 3, 4] if item % 2 == 0]

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
#
# ## Workshop: Listen-Komprehension
#
# ### Quadratzahlen mit Listen-Komprehension
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

# %% [markdown]
# ### Filtern mit Listen-Komprehension
#
# Erzeugen Sie eine neue Liste, die alle Zahlen in `numbers` enthält, die größer
# als 10 sind. Verwenden Sie dazu Listen-Komprehension.

# %%
numbers = [1, 7, 4, 87, 23]

# %%
[n for n in numbers if n > 10]


# %% [markdown]
#
# Schreiben Sie die Funktion `zahlen_größer_als_10(zahlen)` mit
# Listen-Komprehension.

# %%
def zahlen_größer_als_10(zahlen):
    return [n for n in zahlen if n > 10]


# %%
assert zahlen_größer_als_10(numbers) == [87, 23]
