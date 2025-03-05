# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Python von der Kommandozeile nutzen</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# # Python auf der Kommandozeile nutzen
# ## Interaktive und Skript-Ausführung von Python

# %% [markdown]
#
# ## Interaktives Python: Die REPL
#
# Starte interaktives Python mit:
#
# ```bash
# python
# ```
#
# Der Prompt `>>>` zeigt an, dass Python bereit ist und Sie Anweisungen eingeben können.

# %% [markdown]
#
# Probieren Sie einfache Anweisungen aus:
#
# ```python
# >>> 2 + 2
# 4
# >>> "Hallo" + " Welt"
# 'Hallo Welt'
# ```
#
# Beenden mit `exit()` oder `Strg+D`.

# %% [markdown]
#
# ## Skripte aus Dateien ausführen
#
# Erstelle `hallo.py`:
#
# ```python
# print("Hallo aus dem Skript!")
# ```
#
# Skript ausführen:
#
# ```bash
# python hallo.py
# ```


# %% [markdown]
#
# ## Python-Module mit `python -m` ausführen
#
# Python ermöglicht direkten Aufruf interner Module mit `-m`:
#
# ```bash
# python -m calendar
# python -m calendar 2024 5
# ```

# %% [markdown]
#
# ## Workshop: Python auf der Kommandozeile nutzen
#
# - Geben Sie folgende Ausdrücke interaktiv ein:
#   - `2+3`
#   - `"Hallo " * 3`
# - Führen Sie die Turtle-Grafikskripte aus verschiedenen Verzeichnissen aus. Wann können Sie die `-m` Option verwenden?
# - Führen Sie die folgenden internen Module aus:
#   - `calendar` (ohne Argumente, mit Jahr, mit Jahr und Monat)
#   - `this` (ohne Argumente)
