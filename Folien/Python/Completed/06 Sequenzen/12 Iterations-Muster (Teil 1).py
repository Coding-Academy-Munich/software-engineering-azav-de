# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Iterations-Muster (Teil 1)</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# # Iterations-Muster
#
# Iteration wird oft auf eine relativ "schematische" Art verwendet. Wir betrachten im
# Folgenden verschieden derartige "Muster", wie Iteration eingesetzt wird.

# %% [markdown]
#
#  ## Aggregation von Listenelementen

# %%
def summe(zahlen):
    ergebnis = 0
    for n in zahlen:
        ergebnis += n
    return ergebnis


# %%
summe([1, 2, 3])


# %% [markdown]
# ## Mini-Workshop: Mittelwert einer Liste
#
# Der Mittelwert einer Liste mit $n$ Elementen $[x_0, \dots, x_{n-1}]$ ist
# definiert als
#
# $$\frac{x_0 + \dots + x_{n-1}}{n}$$
#
# Schreiben Sie eine Funktion `mittelwert(zahlen: list)`, die den Mittelwert einer
# Liste berechnet.

# %%
def mittelwert(zahlen: list):
    if zahlen:
        ergebnis = 0
        for zahl in zahlen:
            ergebnis += zahl
        return ergebnis / len(zahlen)
    return 0


# %% [markdown]
# Testen Sie die Funktion für geeignete Argumente.

# %%
assert mittelwert([1, 2, 3]) == 2.0

# %%
assert mittelwert([]) == 0


# %% [markdown]
# ### Bonus-Aufgabe
#
# Der Mittelwert der Elemente einer Liste $[x_0, \dots, x_{n-1}]$ kann iterativ
# folgendermaßen berechnet werden:
#
# - Der Mittelwert $m$ der leeren Liste ist (per Definition für diese Lösung) 0
# - Wenn wir das $n$-te Element $x_n$ hinzufügen, so wird der neue
#   Mittelwert berechnet als
#
# $$m \leftarrow m + \frac{x_n - m}{n+1}$$
#
# Schreiben Sie eine Funktion `iterativer_mittelwert(numbers: list)`, die den
# Mittelwert einer Liste iterativ berechnet.

# %%
def iterativer_mittelwert(zahlen):
    ergebnis = 0
    for pos, value in enumerate(zahlen, 1):
        ergebnis += (value - ergebnis) / pos
    return ergebnis


# %%
assert iterativer_mittelwert([]) == 0.0

# %%
assert iterativer_mittelwert([1]) == 1.0

# %%
assert iterativer_mittelwert([1, 2, 3]) == 2.0

# %%
assert iterativer_mittelwert(range(11)) == 5.0

