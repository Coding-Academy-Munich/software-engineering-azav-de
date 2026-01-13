# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Enumerationen</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# ## Motivation
#
# - Oft müssen wir einen Zustand repräsentieren, der einen von mehreren
#   vordefinierten Werten annehmen kann.
# - Ein häufiger, aber fehleranfälliger Ansatz ist die Verwendung von "Magic
#   Strings" oder Zahlen.
#
# **Beispiel:** Eine Funktion, die den Status einer Aufgabe verarbeitet.

# %%
def process_task(status: str):
    if status == "new":
        print("Starting a new task.")
    elif status == "in_progress":
        print("Task is currently in progress.")
    elif status == "done":
        print("Task completed.")
    else:
        print(f"Unknown status: {status}")


# %%
process_task("new")

# %%
process_task("in progress")  # Typo!

# %%
process_task("Done")         # Upper/lower case mismatch


# %% [markdown]
#
# ### Probleme mit diesem Ansatz
#
# - **Tippfehler:** Falsch geschriebene Strings führen zu stillem Versagen oder
#   unerwartetem Verhalten.
# - **Keine "Single Source of Truth":** Die gültigen Werte sind im Code
#   verstreut.
# - **Schlechte Lesbarkeit:** Man muss den Code lesen, um alle möglichen
#   Zustände zu finden.
# - **Keine Typsicherheit:** Jede beliebige Zeichenkette kann an die Funktion
#   übergeben werden.

# %% [markdown]
#
# ## Aufzählungen (Enumerationen, `Enum`)
#
# - Eine Aufzählung ist ein Satz von symbolischen Namen (Mitgliedern), die an
#   eindeutige, konstante Werte gebunden sind.
# - Das `enum`-Modul stellt die `Enum`-Basisklasse zur Verfügung.
# - Sie lösen die Probleme von "Magic Strings", indem sie eine robuste,
#   typsichere Alternative bieten.

# %% [markdown]
#
# **Vorteile:**
# - **Lesbarkeit:** Code wird selbsterklärend.
# - **Wartbarkeit:** Zustände sind an einem Ort zentralisiert.
# - **Sicherheit:** Verhindert die Verwendung ungültiger Werte. Moderne IDEs
#   bieten Autovervollständigung.

# %% [markdown]
# ### Definition einer einfachen Aufzählung

# %%
from enum import Enum, auto

# %% [markdown]
#
# - Wir definieren eine Aufzählung für den Task-Status.
# - `auto()` weist automatisch einen ganzzahligen Wert zu.

# %%

# %% [markdown]
# ### Verwendung der Aufzählung
#
# - Auf Mitglieder wird über den Klassennamen zugegriffen.
# - Jedes Mitglied ist eine eindeutige Instanz.
# - `name` und `value` Attribute geben den Namen und den zugewiesenen Wert des
#   Mitglieds zurück.

# %%

# %% [markdown]
#
# Enums sind Singletons

# %%

# %% [markdown]
#
# Zugriff auf Name und Wert

# %%

# %% [markdown]
#
# Iteration über alle Mitglieder

# %%

# %% [markdown]
# ### Überarbeitete Funktion
#
# Wir können unsere Funktion nun so umschreiben, dass sie Typsicherheit mit
# `Status` bietet.

# %%
def process_task_enum(status: Status):
    if status is Status.NEW:
        print("Starting a new task.")
    elif status is Status.IN_PROGRESS:
        print("Task is currently in progress.")
    elif status is Status.DONE:
        print("Task completed.")
    # else may not be needed, as Status is exhaustive

# %%


# %%

# %% [markdown]
#
# ## String-Enumerationen (`StrEnum`)
#
# - Manchmal ist es nützlich, wenn ein Enum-Mitglied sich auch wie ein String
#   verhält.
# - Anwendungsfälle: JSON-Serialisierung, Speicherung in Datenbanken,
#   Konfigurationsdateien.
# - `StrEnum` erbt von `str` und `Enum`.
# - Die Mitglieder sind sowohl Enum-Mitglieder als auch Strings.
# - Verfügbar seit Python 3.11.

# %% [markdown]
# ### Beispiel: `StrEnum` für Loglevel
#
# - Die Werte der Mitglieder müssen Strings sein.

# %%
from enum import StrEnum

# %%

# %% [markdown]
#
# Instanzen von `StrEnum` können wie Strings verwendet werden.

# %%

# %%

# %% [markdown]
#
# - `StrEnum`-Instanzen bieten aber auch alle Methoden und Eigenschaften von
#   Enums.

# %%

# %%

# %%

# %%

# %% [markdown]
#
# ## Workshop 1: Ampelsteuerung
#
# In diesem Workshop implementieren Sie eine Ampelsteuerung mit einer
# Aufzählung.
#
# - Erstellen Sie eine `Enum`-Klasse namens `TrafficLight` mit den Zuständen
#   `RED`, `GREEN` und `YELLOW`.
# - Schreiben Sie eine Funktion `next_state(current_state: TrafficLight) ->
#   TrafficLight`, die den nächsten Zustand im Zyklus zurückgibt.
# - Der Zyklus ist: `RED` -> `GREEN` -> `YELLOW` -> `RED`.
# - Testen Sie Ihre Funktion für alle Zustände.

# %%

# %%

# %% [markdown]
# ## Workshop 2: Konfigurationseinstellungen
#
# In diesem Workshop verwenden Sie `StrEnum`, um Konfigurationen für
# verschiedene Umgebungen zu verwalten.
#
# - Erstellen Sie eine `StrEnum` namens `Environment` mit den Mitgliedern
#   `DEVELOPMENT`, `STAGING` und `PRODUCTION`. Die Werte sollen die
#   kleingeschriebenen Namen sein (z.B. `"development"`).
# - Schreiben Sie eine Funktion `get_database_url(env: Environment) -> str`, die
#   je nach Umgebung eine andere Dummy-Datenbank-URL zurückgibt.
# - Testen Sie Ihre Funktion. Zeigen Sie, dass Sie das `Environment`-Mitglied
#   direkt in einen f-String einfügen können.

# %%
