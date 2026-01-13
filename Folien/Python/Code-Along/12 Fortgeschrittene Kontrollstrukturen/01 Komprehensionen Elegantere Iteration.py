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

# %% [markdown]
#
# ### Transformation
#
# - Eine Liste wird in eine neue Liste umgewandelt.
# - Dabei wird jedes Element der Liste bearbeitet.

# %%

# %% [markdown]
#
# ### Filterung
#
# - Eine Liste wird in eine neue Liste umgewandelt.
# - Dabei werden nur bestimmte Elemente der Liste ausgewählt.
# - Die anderen Elemente werden verworfen.

# %%

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

# %%
result = []
for n in [1, 2, 3, 4]:
    result.append(f"Item {n}")
result

# %%

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

# %%
result = []
for item in ["abc", "def", "asd", "qwe", "bab"]:
    if item[0] == "a":
        result.append(item)
result

# %%

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

# %% [markdown]
#
# Schreiben Sie eine Funktion `quadriere(zahlen)`, die jedes Element einer Liste
# quadriert, mit Listen-Komprehension.

# %%

# %%

# %% [markdown]
# ### Filtern mit Listen-Komprehension
#
# Erzeugen Sie eine neue Liste, die alle Zahlen in `numbers` enthält, die größer
# als 10 sind. Verwenden Sie dazu Listen-Komprehension.

# %%
numbers = [1, 7, 4, 87, 23]

# %%


# %% [markdown]
#
# Schreiben Sie die Funktion `zahlen_größer_als_10(zahlen)` mit
# Listen-Komprehension.

# %%

# %%
