# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Kontrollstrukturen (Teil 2)</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# ## Einseitiges `if`

# %%

# %%

# %%

# %% [markdown]
#
#  ## Mehrere Zweige
#
#  - Wir wollen ein Spiel schreiben, in dem der Spieler eine Zahl zwischen 1 und
#    100 erraten muss.
#  - Nachdem er geraten hat, bekommt er die Information, ob seine Zahl zu hoch,
#    zu niedrig oder richtig war angezeigt.
#  - Später wollen wir dem Spieler mehrere Versuche erlauben.

# %%

# %%

# %%

# %%

# %% [markdown]
#
#  ## Struktur einer `if`-Anweisung (vollständig):
#
# ```python
# if {Bedingung 1}:
#     Rumpf, der ausgeführt wird, wenn {Bedingung 1} wahr ist
# elif {Bedingung 2}:
#     Rumpf, der ausgeführt wird, wenn {Bedingung 2} wahr ist
# ...
# else:
#     Rumpf, der ausgeführt wird, wenn keine der Bedingungen wahr ist
# ```
# - Nur das `if` und der erste Rumpf sind notwendig
# - Falls ein `elif` oder ein `else` vorhanden ist, so darf der entsprechende
#   Rumpf nicht leer sein

# %% [markdown]
# ## Mini-Workshop: Positiv / Negativ
#
# Schreiben Sie eine Funktion `drucke_ist_positiv(zahl)`, die
#
# - `{zahl} ist positiv.` auf dem Bildschirm ausgibt, falls `zahl > 0` ist,
# - `{zahl} ist Null.` auf dem Bildschirm ausgibt, falls `zahl == 0` ist,
# - `{zahl} ist negativ.` auf dem Bildschirm ausgibt, falls `zahl < 0` ist.

# %%

# %% [markdown]
# Testen Sie `drucke_ist_positiv(zahl)` mit den Werten -3, 0 und 2.

# %%
