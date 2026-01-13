# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Eigenschaften von Tupeln</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# # Eigenschaften von Tupeln
#
# - Tupel können beliebige Python-Werte speichern
# - Elemente in einem Tupel haben eine feste Reihenfolge
# - Auf Elemente eines Tupels kann mit einem Index zugegriffen werden
# - `for`-Schleifen können über die Elemente von Tupeln iterieren (Iterables)
# - Tupel können *nicht* modifiziert werden
#
# Oft werden Tupel zum Speichern *heterogener* Daten verwendet.

# %% [markdown]
#
# ## Modifizierbarkeit von Tupeln

# %%

# %%

# %%

# %%


# %% [markdown]
#
# ## Mini-Workshop: Bücher
#
# Wir wollen Tupel verwenden, um Bücher zu repräsentieren. Jedes Buch wird
# durch ein Tupel dargestellt, das den Autor (als String),
# den Titel (als String) und die Seitenzahl (als ganze Zahl) enthält.
#
# Stellen Sie das Buch "1984" von George Orwell mit 328 Seiten in dieser Form
# dar und speichern Sie es in einer Variable "orwell".


# %%

# %% [markdown]
#
# Bilden Sie eine Liste aus dem genannten Buch "1984", sowie
#
# - Catch-22 von Joseph Heller (453 Seiten)
# - Fahrenheit 451 von Ray Bradbury (256 Seiten)
#
# und weisen Sie die Liste an eine Variablen `books` zu.

# %%

# %% [markdown]
#
# Schreiben Sie Funktionen `title(book) -> str`, `author(book) -> str` und
# `pages(book) -> int`, die den Titel, Autor und die Zahl der Seiten in einem Buch
# zurückgeben.
#
# Testen Sie die Funktionen mit dem Buch "1984".

# %%

# %%

# %%

# %%

# %%

# %%

# %% [markdown]
#
# Schreiben Sie eine Funktion `get_short_books(books)`, die eine Liste von Büchern als
# Argument bekommt und eine Liste derjenigen Bücher zurückgibt, die weniger als 300
# Seiten haben:
#
# ```python
# >>> get_short_books(books)
# [('Fahrenheit 451', 'Ray Bradbury', 256)]
# ```

# %%

# %%
assert get_short_books(books) == [("Fahrenheit 451", "Ray Bradbury", 256)]
