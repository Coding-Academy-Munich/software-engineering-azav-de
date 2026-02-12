# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Gruppen, Ersetzen und Fortgeschrittenes</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %%
import re

# %%
tongue_twister = (
    "How much wood would a woodchuck chuck, if a woodchuck could chuck wood?"
)


# %% [markdown]
# # Anker
#
# - Anker prüfen die **Position** im String, nicht ein bestimmtes Zeichen
# - `^` -- Anfang des Strings
# - `$` -- Ende des Strings
# - Nützlich um sicherzustellen, dass das Muster an einer bestimmten Stelle steht

# %%

# %%

# %%

# %% [markdown]
# ## Wortgrenzen: `\b`
#
# - `\b` steht für die Grenze zwischen einem Wortzeichen (`\w`) und einem
#   Nicht-Wortzeichen (`\W`)
# - Damit können wir **ganze Wörter** suchen, nicht nur Teilstrings
# - Vergleich: `"wood"` findet auch "wood" in "woodchuck"

# %%

# %%

# %% [markdown]
# - Ohne `\b`: findet "wood" 4 Mal (auch in "woodchuck")
# - Mit `\b`: findet "wood" nur 2 Mal (nur eigenständige Wörter)
# - Wortgrenzen sind sehr nützlich, um präzise Muster zu erstellen

# %% [markdown]
# # Ersetzen mit `re.sub()`
#
# - `re.sub(pattern, replacement, string)` ersetzt alle Treffer des Musters
# - Viel mächtiger als `str.replace()`, weil wir Muster verwenden können

# %%

# %%

# %% [markdown]
# ## Ersetzen mit Funktionen
#
# - Das Ersetzungsargument kann auch eine **Funktion** sein
# - Die Funktion erhält das Match-Objekt als Argument
# - Das ermöglicht dynamische Ersetzungen

# %%
def annotate(match):
    return f"{match.group()}[{match.start()}-{match.end()}]"

# %%

# %% [markdown]
# - Besonders nützlich mit **Lambda-Funktionen** für kurze Ersetzungen

# %%

# %%

# %% [markdown]
# # Gruppen
#
# - Runde Klammern `(...)` erstellen **Capture Groups** (Erfassungsgruppen)
# - Gruppen erlauben es, **Teile** eines Treffers zu extrahieren
# - `.group(0)` gibt den gesamten Treffer zurück
# - `.group(1)` gibt die erste Gruppe zurück, `.group(2)` die zweite, usw.

# %%
text = "Meine Email ist joe@example.com und deine ist alice@test.org"

# %%
match = re.search(r"(\w+)@(\w+\.\w+)", text)

# %%

# %%

# %%

# %% [markdown]
# ## Gruppen in `re.findall()`
#
# - Wenn das Muster Gruppen enthält, gibt `re.findall()` eine Liste von
#   **Tupeln** zurück
# - Jedes Tupel enthält die Inhalte der Gruppen

# %%
text = "Meine Email ist joe@example.com und deine ist alice@test.org"

# %%

# %% [markdown]
# ## Gruppenreferenzen in `re.sub()`
#
# - In der Ersetzung können wir auf Gruppen verweisen:
#   - `\1` für die erste Gruppe, `\2` für die zweite, usw.
# - Damit können wir Teile des Treffers im Ergebnis wiederverwenden

# %%
text = "Kontakt: joe@example.com oder alice@test.org"

# %%

# %%
tongue_twister = (
    "How much wood would a woodchuck chuck, if a woodchuck could chuck wood?"
)

# %%

# %% [markdown]
# # Muster kompilieren: `re.compile()`
#
# - Wenn wir das gleiche Muster mehrmals verwenden, können wir es **kompilieren**
# - `re.compile(pattern)` gibt ein kompiliertes Pattern-Objekt zurück
# - Das Pattern-Objekt hat dieselben Methoden wie das `re`-Modul:
#   `search()`, `findall()`, `sub()`, etc.

# %%
wood_rx = re.compile(r"\bwood\b")

# %%

# %%

# %%

# %% [markdown]
# # `match()`, `search()` und `fullmatch()`
#
# - Python bietet drei Varianten zum Suchen:
#   - `search()`: Findet den Treffer **irgendwo** im String
#   - `match()`: Sucht nur am **Anfang** des Strings
#   - `fullmatch()`: Der **gesamte** String muss zum Muster passen

# %%
email_rx = re.compile(r"[\w.+-]+@[\w.+-]+")

# %%

# %%

# %%

# %%

# %%

# %% [markdown]
# ## Übersicht
#
# | Methode | Sucht wo? | Beispiel |
# |---------|-----------|----------|
# | `search()` | Überall im String | `"Email: joe@ex.com"` -- findet `joe@ex.com` |
# | `match()` | Nur am Anfang | `"joe@ex.com ..."` -- findet `joe@ex.com` |
# | `fullmatch()` | Gesamter String | `"joe@ex.com"` -- findet `joe@ex.com` |

# %% [markdown]
# # Flags
#
# - Flags verändern das Verhalten des Musterabgleichs
# - `re.IGNORECASE` (oder `re.I`): Groß-/Kleinschreibung wird ignoriert

# %%

# %%

# %% [markdown]
# ## Flags mit `re.compile()`
#
# - Flags können auch bei `re.compile()` angegeben werden

# %%
email_rx = re.compile(r"[\w.+-]+@[\w.+-]+", re.IGNORECASE)

# %%

# %% [markdown]
# ## Mini-Workshop: E-Mail-Prüfung
#
# Schreiben Sie eine Funktion `is_valid_email(text: str) -> bool`, die prüft,
# ob `text` eine gültig aussehende E-Mail-Adresse ist.
#
# Eine gültige E-Mail hat das Format:
# - Benutzername: Buchstaben, Ziffern, Punkte, Bindestriche, Pluszeichen
# - Dann ein `@`
# - Dann eine Domain mit mindestens einem Punkt
#
# ```python
# >>> is_valid_email("joe@example.com")
# True
# >>> is_valid_email("nicht eine email")
# False
# ```

# %% [markdown]
# ### Hinweise
#
# - Verwenden Sie `re.fullmatch()`, da der gesamte String eine E-Mail sein soll
# - Der Benutzername-Teil: `[\w.+-]+`
# - Die Domain: `[\w-]+\.[\w.-]+` (mindestens ein Punkt)
# - Prüfen Sie, ob das Ergebnis `None` ist oder nicht

# %%

# %%
assert is_valid_email("joe@example.com")
assert is_valid_email("alice.smith@test.org")
assert is_valid_email("user+tag@domain.co.uk")
assert not is_valid_email("nicht eine email")
assert not is_valid_email("@example.com")
assert not is_valid_email("joe@")
assert not is_valid_email("joe@example")
assert not is_valid_email("")

# %% [markdown]
# ## Mini-Workshop: Textbereinigung
#
# Schreiben Sie zwei Funktionen:
#
# 1. `clean_whitespace(text: str) -> str` -- ersetzt mehrfache Leerzeichen durch
#    ein einzelnes Leerzeichen und entfernt Leerzeichen am Anfang und Ende
# 2. `censor_numbers(text: str) -> str` -- ersetzt alle Zahlen (Folgen von
#    Ziffern) durch `"***"`
#
# ```python
# >>> clean_whitespace("  Hallo   Welt  ")
# 'Hallo Welt'
# >>> censor_numbers("Ruf an: 0123-456789")
# 'Ruf an: ***-***'
# ```

# %% [markdown]
# ### Hinweise
#
# - Für `clean_whitespace`: Verwenden Sie `\s+` als Muster und ersetzen Sie
#   durch ein einzelnes Leerzeichen, dann `.strip()` aufrufen
# - Für `censor_numbers`: Verwenden Sie `\d+` als Muster und ersetzen Sie
#   durch `"***"`

# %%

# %%
assert clean_whitespace("  Hallo   Welt  ") == "Hallo Welt"
assert clean_whitespace("keine  extra   spaces") == "keine extra spaces"
assert clean_whitespace("   ") == ""

# %%

# %%
assert censor_numbers("Ruf an: 0123-456789") == "Ruf an: ***-***"
assert censor_numbers("Konto 12345, PIN 9876") == "Konto ***, PIN ***"
assert censor_numbers("Keine Zahlen") == "Keine Zahlen"
