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
numbers = {3, 5, 4, 9, 4, 1, 5, 4, 3}
numbers

# %%
type(numbers)

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
numbers.add(2)

# %%
numbers

# %%
numbers.add(5)

# %%
numbers

# %%
numbers

# %%
numbers.remove(5)

# %%
numbers

# %%
# numbers.remove(5)

# %%
numbers.discard(5)

# %%
numbers

# %% [markdown]
#
# ### Test auf Mitgliedschaft
#
# - `x in s` testet, ob das Element `x` in der Menge `s` enthalten ist
# - `x not in s` testet, ob das Element `x` nicht in der Menge `s` enthalten ist

# %%
numbers = {3, 5, 9}

# %%
3 in numbers

# %%
2 not in numbers

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
numbers.union({42})

# %%
numbers

# %%
numbers | {42}

# %%
numbers

# %%
numbers.intersection({2, 3, 4})

# %%
numbers & {2, 3, 4}

# %%
numbers.difference({2, 3, 4})

# %%
numbers - {2, 3, 4}

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
{2, 3} <= {1, 2, 3, 4}

# %%
{2, 3} < {1, 2, 3, 4}

# %%
{2, 5} <= {1, 2}

# %%
{2, 5} <= {2, 5}

# %%
{2, 5} < {2, 5}

# %%
type({})  # Empty dictionary!

# %%
set()

# %%
type(set())

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
words = philosophy.lower().split()
words[10:20]

# %%
len(words)

# %%
word_set = set(words)

# %%
len(word_set)

# %%
word_set - {".", ","}

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
def count_unique_words(text: str):
    word_set = set(text.lower().split()) - {",", "."}
    return len(word_set)


# %%
dickens = "It was the best of times , it was the worst of times"

# %%
assert count_unique_words(dickens) == 7

# %%
assert count_unique_words(philosophy) == 22

# %%
