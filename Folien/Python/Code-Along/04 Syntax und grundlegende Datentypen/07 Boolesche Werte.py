# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Boolesche Werte</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
# # Vergleiche, Boolesche Werte

# %% [markdown]
# Gleichheit von Werten wird mit `==` getestet:

# %%

# %%

# %% [markdown]
# Das Ergebnis eines Vergleichs ist ein Boolescher Wert (Wahrheitswert)
#
# - `True`
# - `False`

# %%

# %% [markdown]
# ## Gleichheit von Zahlen

# %%

# %% [markdown]
# ### Vorsicht: Rundungsfehler!

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %% [markdown]
# ## Ungleichheit von Zahlen
#
# Der Operator `!=` testet, ob zwei Zahlen verschieden sind

# %%

# %%

# %% [markdown]
# ## Vergleich von Zahlen

# %%

# %%

# %%

# %%

# %%

# %% [markdown]
# ## Vergleichsoperatoren auf anderen Typen
#
# Die Vergleichsoperatoren lassen sich auch auf viele andere Typen anwenden
# (genaueres später).

# %% [markdown]
#
# ### Der Wert `None`
#
# `None` ist ein Wert, der von Python verwendet wird, um das Fehlen eines
# sinnvollen Wertes anzuzeigen. Jupyter druckt `None` nicht als Wert einer Zelle
# aus:


# %%

# %%

# %%

# %%

# %%

# %% [markdown]
#
# Um auf `None` zu testen wird oft der Operator `is` verwendet.

# %%

# %% [markdown]
#
# `is` testet Objektidentität und ist im Allgemeinen nicht mit `==`
# austauschbar.

# %% [markdown]
# ## Mini-Workshop: Vergleiche
#
# Ist $2^{16}$ größer als $32\,000\,\,/\,\,2$?

# %%

# %% [markdown]
# Ist $72$ ohne Rest durch $3$ teilbar?

# %%

# %% [markdown]
# Gegeben die folgenden Variablendefinitionen:

# %%
var1 = 2**2**4
var2 = 3**12
var3 = 100 * 200 * 300
var4 = 4**3**2

# %% [markdown]
#
# Ist das Maximum von `var1` und `var2` größer als das Minimum von `var3` und `var4`?

# %%
