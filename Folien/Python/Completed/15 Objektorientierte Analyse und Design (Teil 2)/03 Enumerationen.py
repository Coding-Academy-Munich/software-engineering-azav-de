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
class Status(Enum):
    NEW = auto()
    IN_PROGRESS = auto()
    DONE = auto()


# %% [markdown]
# ### Verwendung der Aufzählung
#
# - Auf Mitglieder wird über den Klassennamen zugegriffen.
# - Jedes Mitglied ist eine eindeutige Instanz.
# - `name` und `value` Attribute geben den Namen und den zugewiesenen Wert des
#   Mitglieds zurück.

# %%
current_status = Status.IN_PROGRESS
print(current_status)

# %% [markdown]
#
# Enums sind Singletons

# %%
assert Status.IN_PROGRESS is Status.IN_PROGRESS

# %% [markdown]
#
# Zugriff auf Name und Wert

# %%
print(f"Name: {current_status.name}, Value: {current_status.value}")

# %% [markdown]
#
# Iteration über alle Mitglieder

# %%
for member in Status:
    print(repr(member))


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
process_task_enum(Status.NEW)


# %%
# process_task_enum("new")

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
class LogLevel(StrEnum):
    DEBUG = "debug"
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"


# %% [markdown]
#
# Instanzen von `StrEnum` können wie Strings verwendet werden.

# %%
def log_message(level: LogLevel, message: str):
    print(f"[{level.upper()}]: {message}")


# %%
log_message(LogLevel.INFO, "User logged in.")

# %% [markdown]
#
# - `StrEnum`-Instanzen bieten aber auch alle Methoden und Eigenschaften von
#   Enums.

# %%
LogLevel.INFO == "info"

# %%
LogLevel.INFO is not LogLevel.WARNING

# %%
LogLevel.INFO.name

# %%
LogLevel.INFO.value

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
from enum import Enum, auto


# %%
class TrafficLight(Enum):
    RED = auto()
    GREEN = auto()
    YELLOW = auto()


# %%
def next_state(current_state: TrafficLight) -> TrafficLight:
    if current_state is TrafficLight.RED:
        return TrafficLight.GREEN
    elif current_state is TrafficLight.GREEN:
        return TrafficLight.YELLOW
    else:  # current_state is TrafficLight.YELLOW
        return TrafficLight.RED


# %%
assert next_state(TrafficLight.RED) is TrafficLight.GREEN
assert next_state(TrafficLight.GREEN) is TrafficLight.YELLOW
assert next_state(TrafficLight.YELLOW) is TrafficLight.RED

print("Traffic light tests passed!")


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
from enum import StrEnum


# %%
class Environment(StrEnum):
    DEVELOPMENT = "development"
    STAGING = "staging"
    PRODUCTION = "production"


# %%
def get_database_url(env: Environment) -> str:
    # Der env-Parameter kann wie ein String verwendet werden
    return f"db://user:pass@host_{env}:5432/{env}_db"


# %%
# Tests
dev_url = get_database_url(Environment.DEVELOPMENT)
assert dev_url == "db://user:pass@host_development:5432/development_db"
print(f"Development URL: {dev_url}")

prod_url = get_database_url(Environment.PRODUCTION)
assert prod_url == "db://user:pass@host_production:5432/production_db"
print(f"Production URL: {prod_url}")

# Vergleiche funktionieren wie erwartet
assert Environment.STAGING == "staging"

print("\nConfiguration settings tests passed!")
