# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Truthiness</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# ## Truthiness
#
# Die `if`-Anweisung kann als Argument beliebige Python-Werte bekommen,
# nicht nur Boolesche Werte.
#
# Folgende Werte gelten als *falsch*
#
# - `None` und `False`
# - `0` und `0.0` (und Null-Werte von anderen Zahlentypen)
# - Leere Strings, Listen und andere Collections: `""`, `[]`, ...
# - Manche Werte von benutzerdefinierten Datentypen
#
#  Alle anderen Werte gelten als wahr.

# %%
def check(value):
    if value:
        print(f"{value!r} is truthy.")
    else:
        print(f"{value!r} is falsy.")

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
#
# Wie wird das verwendet?

# %%

# %%

# %%


# %% [markdown]
#
# ## Mini-Workshop: Truthiness
#
# Für welche Werte von `x` ist `len(x) - 1` falsy?


# %% [markdown]
# *Antwort:* 

# %% [markdown]
#
# Geben Sie zwei Beispielwerte mit verschiedenem Typ an.

# %%

# %%


# %% [markdown]
#
# Gibt es einen String `s`, für den `s[0]` falsy ist?

# %% [markdown]
# *Antwort:* 
