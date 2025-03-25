# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Iterations-Muster (Teil 3)</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
# # Filtern von Listen

# %%
ergebnis = []
for item in [1, 2, 3, 4, 5, 6]:
    if item % 2 == 0:
        ergebnis.append(item)
ergebnis

# %%
ergebnis = []
for item in ["abc", "def", "asd", "qwe", "bab"]:
    if "ab" in item:
        ergebnis.append(item)
ergebnis

# %% [markdown]
# # Mini-Workshop: Filtern von Listen
#
# Gegeben sei die folgende Liste mit Zahlen:

# %%
zahlen = [1, 183, 7, 4, 87, 10, 23, -12, 493, 11]

# %% [markdown]
# Erzeugen Sie eine neue Liste, die alle Zahlen in `numbers` enthält,
# die größer als 10 sind.

# %%
ergebnis = []
for n in zahlen:
    if n > 10:
        ergebnis.append(n)
ergebnis


# %% [markdown]
#
# Schreiben Sie eine Funktion `zahlen_größer_als_10(zahlen)`, die eine neue
# Liste zurückgibt, die die Zahlen aus `zahlen` enthält, die größer als 10 sind.

# %%
def zahlen_größer_als_10(zahlen):
    result = []
    for n in zahlen:
        if n > 10:
            result.append(n)
    return result


# %%
assert zahlen_größer_als_10(zahlen) == [183, 87, 23, 493, 11]
