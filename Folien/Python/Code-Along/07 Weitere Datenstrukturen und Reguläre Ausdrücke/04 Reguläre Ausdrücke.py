# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Reguläre Ausdrücke</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
# # Finden von Text in Strings
#
# - Wir kennen bereits String-Methoden zum Suchen und Ersetzen von Text
# - `str.index()` und `str.find()` finden die Position eines Teilstrings
# - `str.replace()` ersetzt alle Vorkommen eines Teilstrings
# - Aber diese Methoden haben Grenzen...

# %%
tongue_twister = (
    "How much wood would a woodchuck chuck, if a woodchuck could chuck wood?"
)

# %%

# %%

# %% [markdown]
# ## Grenzen von String-Methoden
#
# - `find()` findet nur das erste Vorkommen
# - `replace()` ersetzt **alle** Vorkommen -- keine Kontrolle
# - Wir können keine **Muster** suchen (z.B. "beliebiges 4-Buchstaben-Wort")
# - Wir können keine **Teile** eines Treffers extrahieren
# - Wir können nicht zwischen "wood" als eigenständigem Wort und "wood" in
#   "woodchuck" unterscheiden

# %% [markdown]
# ## Was sind Reguläre Ausdrücke?
#
# - Eine kleine Sprache zum Beschreiben von **Textmustern**
# - Verfügbar in fast jeder Programmiersprache
# - Python bietet das Modul `re` in der Standardbibliothek
# - Damit können wir:
#   - Muster in Texten **finden**
#   - Teile von Treffern **extrahieren**
#   - Text nach Mustern **ersetzen**

# %%
import re

# %% [markdown]
# # Suchen mit `re.search()`
#
# - `re.search(pattern, string)` sucht das Muster im String
# - Gibt ein **Match-Objekt** zurück, wenn das Muster gefunden wird
# - Gibt `None` zurück, wenn das Muster nicht gefunden wird

# %%
result = re.search("wood", tongue_twister)

# %%

# %% [markdown]
# ## Match-Objekte
#
# - `.group()` gibt den gefundenen Text zurück
# - `.start()` gibt die Startposition zurück
# - `.end()` gibt die Endposition zurück (exklusiv)
# - `.span()` gibt ein Tupel `(start, end)` zurück

# %%

# %%

# %%

# %%

# %% [markdown]
# ## Kein Treffer
#
# - Wenn das Muster nicht gefunden wird, gibt `re.search()` `None` zurück
# - Prüfen Sie immer auf `None`, bevor Sie das Match-Objekt verwenden!

# %%

# %%

# %%
result = re.search("coffee", tongue_twister)
if result is not None:
    print(f"Gefunden an Position {result.start()}")
else:
    print("Nicht gefunden")

# %% [markdown]
# # Alle Treffer finden mit `re.findall()`
#
# - `re.findall(pattern, string)` findet **alle** Vorkommen des Musters
# - Gibt eine **Liste von Strings** zurück
# - Nützlich, wenn wir alle Treffer auf einmal brauchen

# %%
tongue_twister = (
    "How much wood would a woodchuck chuck, if a woodchuck could chuck wood?"
)

# %%

# %%

# %%

# %% [markdown]
# ## Alle Treffer mit Position: `re.finditer()`
#
# - `re.finditer(pattern, string)` gibt einen Iterator über Match-Objekte zurück
# - Nützlich, wenn wir sowohl den Text als auch die Position jedes Treffers
#   brauchen

# %%

# %% [markdown]
# # Raw Strings
#
# - In regulären Ausdrücken hat der Backslash `\` eine besondere Bedeutung
# - Aber auch in Python-Strings hat `\` eine besondere Bedeutung!
# - `"\n"` ist ein Zeilenumbruch, `"\t"` ist ein Tabulator
# - Problem: Wie schreiben wir `\d` (Ziffer) oder `\b` (Wortgrenze) in Regex?

# %%

# %%

# %% [markdown]
# ## Die Lösung: Raw Strings mit `r"..."`
#
# - Mit dem Präfix `r` vor einem String wird der Backslash **nicht** als
#   Escape-Zeichen interpretiert
# - `r"\n"` ist ein String mit zwei Zeichen: `\` und `n`
# - **Best Practice:** Verwenden Sie immer Raw Strings für Regex-Muster!

# %%

# %%

# %%

# %% [markdown]
# ## Vergleich: Normaler String vs. Raw String
#
# | Ausdruck | Ergebnis | Länge |
# |----------|----------|-------|
# | `"\n"` | Zeilenumbruch | 1 |
# | `r"\n"` | `\n` (zwei Zeichen) | 2 |
# | `"\\n"` | `\n` (zwei Zeichen) | 2 |
# | `r"\d"` | `\d` (zwei Zeichen) | 2 |

# %% [markdown]
# ## Mini-Workshop: Textsuche
#
# Schreiben Sie eine Funktion `count_occurrences(text: str, pattern: str) -> int`,
# die zählt, wie oft `pattern` in `text` vorkommt.
#
# ```python
# >>> count_occurrences("abcabc", "abc")
# 2
# >>> count_occurrences("hello world", "xyz")
# 0
# ```

# %% [markdown]
# ### Hinweise
#
# - Verwenden Sie `re.findall()`, um alle Treffer zu finden
# - Die Länge der zurückgegebenen Liste ist die Anzahl der Treffer

# %%

# %%
assert count_occurrences("abcabc", "abc") == 2
assert count_occurrences("hello world", "xyz") == 0
assert count_occurrences(tongue_twister, "wood") == 4
assert count_occurrences(tongue_twister, "chuck") == 4

# %% [markdown]
# ## Mini-Workshop: Wortfinder
#
# Schreiben Sie eine Funktion
# `find_word_positions(text: str, word: str) -> list`,
# die eine Liste von Tupeln `(start, end)` zurückgibt, die die Positionen
# aller Vorkommen von `word` in `text` angeben.
#
# ```python
# >>> find_word_positions("abcabc", "abc")
# [(0, 3), (3, 6)]
# ```

# %% [markdown]
# ### Hinweise
#
# - Verwenden Sie `re.finditer()`, um alle Treffer mit Position zu erhalten
# - Jeder Treffer hat eine `.span()`-Methode, die `(start, end)` zurückgibt

# %%

# %%
assert find_word_positions("abcabc", "abc") == [(0, 3), (3, 6)]
assert find_word_positions("hello", "xyz") == []
assert find_word_positions(tongue_twister, "wood") == [(9, 13), (22, 26), (44, 48), (66, 70)]
