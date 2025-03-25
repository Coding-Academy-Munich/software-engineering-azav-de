# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Iterations-Muster (Teil 2)</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# # Transformation von Listen

# %%
result = []
for item in [1, 2, 3, 4]:
    result.append(item + 1)
result

# %%
result = []
for n in [1, 2, 3, 4]:
    result.append(f"Item {n}")
result

# %% [markdown]
# ## Mini-Workshop: Quadratzahlen
#
# Gegeben sei die folgende Liste mit Zahlen.

# %%
zahlen = [1, 7, 4, 87, 23]

# %% [markdown]
# Erzeugen Sie eine neue Liste, die die Quadrate der Zahlen in `numbers` enthält.

# %%
ergebnis = []
for n in zahlen:
    ergebnis.append(n * n)
ergebnis


# %% [markdown]
# Schreiben Sie eine Funktion `quadriere(zahlen)`, die eine neue Liste mit den
# Quadraten der Zahlen in `zahlen` zurückgibt.

# %%
def quadriere(zahlen):
    ergebnis = []
    for n in zahlen:
        ergebnis.append(n * n)
    return ergebnis


# %%
assert quadriere(zahlen) == [1, 49, 16, 7569, 529]
