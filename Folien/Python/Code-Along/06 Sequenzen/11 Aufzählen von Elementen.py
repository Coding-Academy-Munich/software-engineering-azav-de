# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Aufzählen von Elementen</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# # Aufzählen von Elementen
#
# In manchen Fällen ist es hilfreich, bei der Iteration über eine Liste
# sowohl den Index des aktuellen Elements, als auch das Element selber
# zur Verfügung zu haben.
#
# Ein Beispiel dafür ist die bereits besprochene `find()` Funktion.

# %% [markdown]
#
# ## Nochmal Finden von Elementen
#
# Bei unserer bisherigen Version von `find` muss die Liste zweimal durchlaufen
# werden:
#
# - Einmal um zu testen, ob das gesuchte Element in der Liste vorkommt
# - Einmal um den Index zu finden.
#
# Schöner wäre es, wenn wir das in einem Durchlauf erledigen könnten.

# %% [markdown]
#
# Die Funktion `enumerate()` nimmt eine Liste als Argument und liefert
# ein Iterable bestehend aus Paaren `(index, element)` zurück:

# %%
my_list = ["a", "b", "c", "d", "e"]

# %%

# %%

# %%

# %%

# %%

# %%
my_list = ["a", "b", "c", "d", "a"]

# %%

# %%

# %%

# %%
assert find("a", my_list) == 0
assert find("d", my_list) == 3
assert find("x", my_list) is None

# %% [markdown]
#
# ## Workshop: Nummerierte Aufzählung
#
# Schreiben Sie eine Funktion `print_enumerated(items: list[string])`, die eine Liste von Strings bekommt und diese als
# nummerierte Aufzählung auf dem Bildschirm ausgibt:
#
# ```python
# print_enumerated(["Gehe Einkaufen", "Koche Mittagessen", "Wasche ab"])
# ```
#
# sollte folgendes ausgeben:
#
# ```
# 1: Gehe Einkaufen
# 2: Koche Mittagessen
# 3: Wasche ab
# ```

# %%

# %% [markdown]
#
# ## Workshop: Finden des letzten Elements
#
# Schreiben Sie eine Funktion `find_last(element, a_list: list)`, die den Index des
# *letzten* Vorkommens von `element` in `a_list` zurückgibt, oder `None` falls das
# Element nicht in der Liste vorkommt.


# %% [markdown]
#
# ### Mögliches Vorgehen
#
# - Laufe durch alle Elemente der Liste
# - Wenn das aktuelle Element gleich dem gesuchten Element ist, speichere den Index
# - Nachdem alle Elemente durchlaufen wurden: Gib den gespeicherten Index zurück
# - (Oder None, wenn kein Index gefunden wurde)

# %%

# %%
values = [1, 3, 2, 3, 1, 1]

# %%
assert find_last(1, values) == 5
assert find_last(2, values) == 2
assert find_last(3, values) == 3
assert find_last(4, values) is None
