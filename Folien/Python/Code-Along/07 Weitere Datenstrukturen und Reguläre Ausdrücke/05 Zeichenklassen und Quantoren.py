# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Zeichenklassen und Quantoren</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %%
import re

# %% [markdown]
# # Zeichenklassen
#
# - Bisher haben unsere Muster exakten Text gesucht, z.B. `"wood"`
# - **Zeichenklassen** beschreiben **Kategorien** von Zeichen
# - Damit können wir z.B. "beliebige Ziffer" oder "beliebiger Buchstabe" suchen
# - Python bietet vordefinierte Zeichenklassen mit Backslash-Notation

# %% [markdown]
# ## `\d` -- Ziffern
#
# - `\d` steht für eine beliebige **Ziffer** (0-9)
# - `\D` steht für ein beliebiges Zeichen, das **keine Ziffer** ist

# %%
text = "Bestellung 42, Artikel 7, Preis 99 Euro"

# %%

# %%

# %% [markdown]
# ## `\w` -- Wortzeichen
#
# - `\w` steht für **Buchstaben**, **Ziffern** und **Unterstrich**
# - `\W` steht für alles, was **kein** Wortzeichen ist (Leerzeichen,
#   Satzzeichen etc.)

# %%
text = "Hello, World! 123"

# %%

# %%

# %% [markdown]
# ## `\s` -- Leerzeichen
#
# - `\s` steht für **Whitespace** (Leerzeichen, Tabulator, Zeilenumbruch)
# - `\S` steht für alles, was **kein** Whitespace ist

# %%
text = "Hallo Welt\tTab\nNeue Zeile"

# %%

# %%

# %% [markdown]
# ## Übersicht: Vordefinierte Zeichenklassen
#
# | Klasse | Beschreibung | Gegenteil |
# |--------|-------------|-----------|
# | `\d` | Ziffer (0-9) | `\D` |
# | `\w` | Wortzeichen (Buchstabe, Ziffer, `_`) | `\W` |
# | `\s` | Whitespace (Leerzeichen, Tab, Newline) | `\S` |

# %% [markdown]
# # Eigene Zeichenklassen
#
# - Mit eckigen Klammern `[...]` definieren wir eigene Zeichenklassen
# - `[abc]` steht für `a`, `b` oder `c`
# - `[a-z]` steht für jeden Kleinbuchstaben
# - `[A-Za-z]` steht für jeden Buchstaben
# - `[0-9]` ist äquivalent zu `\d`

# %%
text = "Hello World 123"

# %%

# %%

# %%

# %%

# %% [markdown]
# ## Negierte Zeichenklassen
#
# - `[^...]` steht für jedes Zeichen, das **nicht** in der Klasse ist
# - `[^aeiou]` steht für jedes Zeichen, das kein Vokal ist
# - `[^0-9]` ist äquivalent zu `\D`

# %%

# %%

# %% [markdown]
# # Der Punkt `.`
#
# - Der Punkt `.` steht für **ein beliebiges Zeichen** (außer Zeilenumbruch)
# - Sehr nützlich als "Platzhalter"
# - Vorsicht: `.` ist sehr allgemein und kann zu unerwarteten Treffern führen

# %%
tongue_twister = (
    "How much wood would a woodchuck chuck, if a woodchuck could chuck wood?"
)

# %%

# %%

# %% [markdown]
# # Quantoren
#
# - Quantoren bestimmen, **wie oft** ein Muster wiederholt werden soll
# - Sie stehen direkt nach dem Zeichen oder der Zeichenklasse
#
# | Quantor | Bedeutung |
# |---------|-----------|
# | `*` | Null oder mehr Wiederholungen |
# | `+` | Eine oder mehr Wiederholungen |
# | `?` | Null oder eine Wiederholung (optional) |
# | `{n}` | Genau n Wiederholungen |
# | `{n,m}` | Zwischen n und m Wiederholungen |
# | `{n,}` | Mindestens n Wiederholungen |

# %% [markdown]
# ## `+` -- Eine oder mehr Wiederholungen
#
# - `\d+` findet eine oder mehr Ziffern (also eine ganze Zahl)
# - `\w+` findet ein ganzes Wort

# %%
text = "abc 42 def 7 ghi 123"

# %%

# %%

# %% [markdown]
# ## `*` -- Null oder mehr Wiederholungen
#
# - `\d*` findet null oder mehr Ziffern
# - Nützlich wenn ein Teil des Musters optional ist

# %%

# %% [markdown]
# ## `?` -- Null oder eine Wiederholung (optional)
#
# - Macht das vorherige Zeichen **optional**
# - Nützlich für Varianten wie "color" / "colour"

# %%

# %%

# %% [markdown]
# ## `{n}`, `{n,m}`, `{n,}` -- Genaue Anzahl
#
# - `{n}` -- genau n Wiederholungen
# - `{n,m}` -- zwischen n und m Wiederholungen
# - `{n,}` -- mindestens n Wiederholungen
#
# (`\b` markiert eine Wortgrenze -- wir werden das in der nächsten Lektion
# genauer erklären)

# %%
tongue_twister = (
    "How much wood would a woodchuck chuck, if a woodchuck could chuck wood?"
)

# %%

# %%

# %%

# %% [markdown]
# ## Kombinationen von Klassen und Quantoren
#
# - Die Stärke von Regex liegt in der Kombination:
#   - `\d{3,}` -- Zahlen mit mindestens 3 Ziffern
#   - `[aeiou]{2}` -- zwei aufeinanderfolgende Vokale
#   - `[A-Z][a-z]+` -- ein Großbuchstabe gefolgt von Kleinbuchstaben

# %%

# %%

# %%

# %% [markdown]
# ## Mini-Workshop: Muster-Detektiv
#
# Schreiben Sie zwei Funktionen:
#
# 1. `find_numbers(text: str) -> list` -- gibt alle Zahlen (Folgen von Ziffern)
#    als Liste von Strings zurück
# 2. `find_words(text: str) -> list` -- gibt alle Wörter (Folgen von
#    Wortzeichen) als Liste von Strings zurück
#
# ```python
# >>> find_numbers("Bestellung 42: 3 Artikel, 99 Euro")
# ['42', '3', '99']
# >>> find_words("Hallo, Welt! 123")
# ['Hallo', 'Welt', '123']
# ```

# %% [markdown]
# ### Hinweise
#
# - Verwenden Sie `re.findall()` mit den passenden Zeichenklassen und Quantoren
# - Zahlen: eine oder mehr Ziffern (`\d+`)
# - Wörter: eine oder mehr Wortzeichen (`\w+`)

# %%

# %%
assert find_numbers("Bestellung 42: 3 Artikel, 99 Euro") == ["42", "3", "99"]
assert find_numbers("Keine Zahlen hier") == []
assert find_numbers("100 200 300") == ["100", "200", "300"]

# %%

# %%
assert find_words("Hallo, Welt! 123") == ["Hallo", "Welt", "123"]
assert find_words("...") == []

# %% [markdown]
# ## Mini-Workshop: Datumsfinder
#
# Schreiben Sie eine Funktion `find_dates(text: str) -> list`, die alle
# Datumsangaben im Format `JJJJ-MM-TT` (z.B. `2024-01-15`) aus einem
# Text extrahiert.
#
# ```python
# >>> find_dates("Termine: 2024-01-15 und 2024-03-20, nicht aber 15.01.2024")
# ['2024-01-15', '2024-03-20']
# ```

# %% [markdown]
# ### Hinweise
#
# - Das Muster besteht aus: 4 Ziffern, Bindestrich, 2 Ziffern, Bindestrich,
#   2 Ziffern
# - Verwenden Sie `\d{4}` für genau 4 Ziffern usw.

# %%

# %%
assert find_dates("Termine: 2024-01-15 und 2024-03-20, nicht aber 15.01.2024") == [
    "2024-01-15",
    "2024-03-20",
]
assert find_dates("Kein Datum hier") == []
assert find_dates("Start: 2023-12-31, Ende: 2024-06-01") == [
    "2023-12-31",
    "2024-06-01",
]
