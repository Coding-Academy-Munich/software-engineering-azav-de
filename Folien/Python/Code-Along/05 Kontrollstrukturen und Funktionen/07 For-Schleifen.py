# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>For-Schleifen</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
# ## Iteration über Listen
#
# In Python kann man mit der `for`-Schleife über Listen iterieren.
#
# Die `for`-Schleife entspricht dem range-based for aus C++,
# `for-in`/`for-of` aus JavaScript oder der `for-each`-Schleife
# aus Java, nicht der klassischen `for`-Schleife
# aus C, C++ oder Java.

# %%
number_list = [0, 1, 2, 3, 4]
number_list

# %%

# %% [markdown]
# ## Syntax der `for`-Schleife
#
# ```python
# for <Element-var> in <Liste>:
#     <Rumpf>
# ```

# %% [markdown]
# ### Workshop
#
# Schreiben Sie eine Funktion `print_all(items: list)`, die die Elemente der
# Liste `items` auf dem Bildschirm ausgibt, jeweils ein Element pro Zeile:
#
# ```python
# >>> print_all([1, 2, 3])
# 1
# 2
# 3
# >>>
# ```
# Was passiert, wenn Sie die Funktion mit einem String als Argument aufrufen,
# z.B. `print_all("abc")`


# %%

# %%

# %%

# %% [markdown]
#
# ## Workshop: Einkaufsliste
#
# Definieren Sie Variablen
# - `meine_einkaufsliste`, die eine Liste mit den Strings `Tee` und `Kaffee`
#   enthält,
# - `eine_andere_einkaufsliste`, die ebenfalls eine Liste mit den Strings
#   `Tee` und `Kaffee` enthält.

# %%

# %% [markdown]
#
# Definieren Sie eine Funktion `drucke_einkaufsliste(einkaufsliste)`, die die
# als Argument übergebene Einkaufsliste ausdruckt:
#
# ```
# Einkaufsliste:
#   Tee
#   Kaffee
# ```

# %%

# %% [markdown]
#
# Testen Sie die Funktion `drucke_einkaufsliste(einkaufsliste)` mit beiden
# Einkaufslisten.

# %%

# %%

# %% [markdown]
#
# Definieren Sie eine Funktion `kaufe(produkt, einkaufsliste)`, das `produkt`
# zu  `einkaufsliste` hinzufügt.

# %%

# %% [markdown]
# Fügen Sie `Butter` und `Brot` zur Einkaufsliste `meine_einkaufsliste` hinzu.

# %%

# %% [markdown]
# Drucken Sie beide Einkaufslisten nochmal aus.

# %%

# %%

# %% [markdown]
# Was passiert, wenn Sie `Butter` und `Brot` nochmals zur Einkaufsliste
# `meine_einkaufsliste` hinzufügen?

# %%
