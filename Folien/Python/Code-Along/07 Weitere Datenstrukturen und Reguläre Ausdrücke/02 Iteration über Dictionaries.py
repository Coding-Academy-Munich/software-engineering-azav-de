# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Iteration über Dictionaries</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# ## Iteration über Schlüssel

# %%
translations = {"snake": "Schlange", "bat": "Fledermaus", "horse": "Pferd"}

# %%

# %%

# %% [markdown]
#
# ## Iteration über Werte

# %%
translations = {"snake": "Schlange", "bat": "Fledermaus", "horse": "Pferd"}

# %%

# %% [markdown]
#
# ## Iteration über Key-Value-Paare

# %%
translations = {"snake": "Schlange", "bat": "Fledermaus", "horse": "Pferd"}

# %%

# %%

# %% [markdown]
#
# ## Mini-Workshop: Drucken von Lagerbeständen
#
# Wir schreiben die Software für ein Hochregallager, in dem der Lagerbestand in einem
# Dictionary verwaltet wird.
#
# Die Keys im Dictionary sind die Plätze im Lager, die Werte das am jeweiligen Platz
# gespeicherte Produkt.
#
# Schreiben Sie die folgenden Funktionen:
#
# - `print_inventory(warehouse)`, die alle im Lager vorhandenen Produkte ausdruckt
# - `print_locations(warehouse)`, die alle Plätze im Lager ausdruckt
# - `print_assignments(warehouse)`, die für jedes Produkt ausgibt, in welchem
#    Platz es gespeichert ist.


# %% [markdown]
#
# ```python
# >>> my_warehouse = {(0, 0): "plugs", (1, 0): "cables", (0, 1): "circuit boards"}
# ```
#
# ```python
# >>> print_inventory(my_warehouse)
# plugs
# cables
# circuit boards
# ```
#
# ```python
# >>> print_locations(my_warehouse)
# (0, 0)
# (1, 0)
# (0, 1)
# ```
#
# ```python
# >>> print_assignments(my_warehouse)
# plugs          -> (0, 0)
# cables         -> (1, 0)
# circuit boards -> (0, 1)
# ```


# %%
my_warehouse = {(0, 0): "plugs", (1, 0): "cables", (0, 1): "circuit boards"}

# %%

# %%
print_inventory(my_warehouse)

# %%

# %%
print_locations(my_warehouse)

# %%

# %%
print_assignments(my_warehouse)
