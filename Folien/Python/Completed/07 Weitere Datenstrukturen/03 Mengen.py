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

# %%
numbers = {3, 5, 4, 9, 4, 1, 5, 4, 3}
numbers

# %%
type(numbers)

# %%
numbers.add(3)

# %%
numbers

# %%
numbers.union({42})

# %%
numbers

# %%
numbers | {42}

# %%
numbers

# %%
numbers & {2, 3, 4}

# %%
numbers - {2, 3, 4}

# %%
numbers.add(5)

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

# %%
3 in numbers

# %%
2 not in numbers

# %%
{2, 3} <= {1, 2, 3, 4}

# %%
{2, 5} <= {1, 2}

# %%
type({})  # Empty dictionary!

# %%
set()

# %%
type(set())

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
# Schreiben Sie eine Funktion `count_unique_words(text: str)`, die die Anzahle der in
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
