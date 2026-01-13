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

# %%

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

# %% [markdown]
# Testen Sie die Funktion für geeignete Argumente.

# %%

# %%

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

# %%

# %%

# %%

# %%

