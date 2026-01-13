# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Tupel</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
# ## Tupel
#
# Tupel sind ähnlich zu Listen, allerdings sind Tupel nach ihrer Konstruktion
# unveränderlich. Funktionen und Methoden für Listen, die die Liste nicht
# destruktiv modifizieren sind in der Regel auch auf Tupel anwendbar.

# %% [markdown]
#
# ## Tupel-Literale
#
# - Elemente durch Kommata getrennt: `1, 2, 3, 4`
# - In vielen Fällen müssen Tupel eingeklammert werden: `(1, 2, 3)`

# %%

# %%

# %%

# %%

# %% [markdown]
#
# ### Leeres Tupel

# %%

# %%

# %% [markdown]
#
# ### Singleton-Tupel

# %%

# %%

# %%

# %%

# %% [markdown]
#
# ### Heterogenes Tupel

# %%

# %%

# %% [markdown]
#
# ## Operationen auf Tupeln
#
# - Viele der Operationen auf Listen lassen sich auf Tupel anwenden.
# - Die Operationen, die Listen verändern sind nicht anwendbar.

# %% [markdown]
#
# ### Konstruktion von Tupeln

# %%
values = (1, 2, 3)
values

# %%

# %% [markdown]
#
# ### Konkatenation von Tupeln

# %%
values = (1, 2, 3)

# %%

# %%

# %%

# %%

# %% [markdown]
#
# ### Tupel und Indizes

# %%
values = (1, 2, 3)

# %%

# %%

# %% [markdown]
#
# ### Funktionen und Methoden

# %%
values = (1, 2, 3, 1, 2, 1, 2)

# %%

# %%

# %% [markdown]
#
# ### Schleifen über Tupel

# %%

# %% [markdown]
#
# ### Illegale Operationen

# %%
values = (1, 2, 3)

# %%

# %%


# %% [markdown]
# ### Mini-Workshop: Funktionen mit mehreren Rückgabewerten
#
# Schreiben Sie eine Funktion `min_max(numbers)`, die das Minimum und das
# Maximum aus einer Liste von Zahlen zurückgibt.
# ```python
# >>> min_max([5, 3, 1, 7, 2])
# (1, 7)
# ```


# %%

# %%
assert min_max([5, 3, 1, 7, 2]) == (1, 7)


# %% [markdown]
#
# ## Mini-Workshop: Zufällige Tupel
#
# Die folgenden Anweisungen erzeugen ein Tupel von Zufallszahlen mit
# zufälliger Länge:


# %%
import random

# %%
random.seed(2022)
my_tuple = random.choices(range(1000), k=random.randint(5_000, 15_000))

# %% [markdown]
#
# Wie viele Elemente enthält `my_tuple`?

# %%

# %% [markdown]
#
# Kommt die Zahl 1 in `my_tuple` vor?
# Falls ja, bei welchem Index ist ihr erstes Vorkommen?

# %%

# %%

# %% [markdown]
#
# Drucken Sie eine Tabelle, die angibt, wie oft jede der Zahlen 0 bis 9
# in `my_tuple` vorkommt.

# %%


# %%
