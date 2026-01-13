# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Mengen</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
# ## Mengen
#
# - Mengen sind eine Sammlung von Elementen ohne Reihenfolge
# - Jedes Element kommt in einer Menge nur einmal vor
# - Sie können Elemente zu Mengen hinzufügen und entfernen
# - Sie können Mengen mit anderen Mengen vereinigen, schneiden oder die
#   Differenz bilden

# %%

# %%

# %% [markdown]
#
# ### Hinzufügen und Entfernen von Elementen
#
# - `s.add(x)` fügt ein Element `x` zur Menge `s` hinzu
# - `s.remove(x)` entfernt das Element `x` aus der Menge `s`
# - `s.discard(x)` entfernt das Element `x` aus der Menge `s`, falls es
#   vorhanden ist

# %%
numbers

# %%

# %%
numbers

# %%

# %%
numbers

# %%
numbers

# %%

# %%
numbers

# %%

# %%

# %%

# %% [markdown]
#
# ### Test auf Mitgliedschaft
#
# - `x in s` testet, ob das Element `x` in der Menge `s` enthalten ist
# - `x not in s` testet, ob das Element `x` nicht in der Menge `s` enthalten ist

# %%
numbers = {3, 5, 9}

# %%

# %%

# %% [markdown]
#
# ### Vereinigung, Schnittmenge und Differenz
#
# - Vereinigung (alle Elemente, die in mindestens einer Menge enthalten sind):
#   - `s.union(t)`
#   - `s | t`
# - Schnittmenge (alle Elemente, die in beiden Mengen enthalten sind):
#   - `s.intersection(t)`
#   - `s & t`
# - Differenz (alle Elemente, die in der ersten Menge, aber nicht in der zweiten
#   enthalten sind):
#   - `s.difference(t)`
#   - `s - t`

# %%
numbers = {3, 4, 5, 9}

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
# ### Teilmengen
#
# - `s` ist Teilmenge von `t`, wenn jedes Element von `s` auch in `t` enthalten
#   ist
#   - `s <= t` testet, ob `s` eine Teilmenge von `t` ist
# - `s` ist echte Teilmenge von `t`, wenn jedes Element von `s` auch in `t`
#   enthalten ist, aber mindestens ein Element in `t` nicht in `s` enthalten ist
#   - `s < t` testet, ob `s` eine echte Teilmenge von `t` ist

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
# ## Vorbereitung für den Workshop

# %%
philosophy = (
    "Half a bee , philosophically , must ipso facto half not be . "
    "But can it be an entire bee , if half of it is not a bee , "
    "due to some ancient injury ."
)
philosophy

# %%

# %%

# %%

# %%

# %%

# %% [markdown]
# ### Mini-Workshop
#
# Schreiben Sie eine Funktion `count_unique_words(text: str)`, die die Anzahl der in
# einem Text vorkommenden Wörter (ohne Wiederholungen und Satzzeichen) zählt. Testen Sie
# die Funktion mit dem in `dickens` gespeicherten String.
#
# ```python
# >>> count_unique_words(dickens)
# 8
# >>>
# ```


# %%

# %%
dickens = "It was the best of times , it was the worst of times"

# %%
assert count_unique_words(dickens) == 7

# %%
assert count_unique_words(philosophy) == 22

# %%
