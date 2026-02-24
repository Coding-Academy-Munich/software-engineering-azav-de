# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>DB-API Integration (Teil 1)</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# # Von Funktionen zu Klassen
#
# - Bisher: Funktionen mit SQL-Strings und Tupel als Ergebnis
# - Probleme:
#   - Was bedeutet `row[0]`? Was ist `row[2]`?
#   - Kein Autocomplete, leicht zu verwechseln
#   - SQL ist über das Programm verstreut
# - Ziel: Saubere Integration von DB-API in Python-Anwendungen

# %% [markdown]
#
# ## Das Problem mit rohen Tupeln
#
# - Ergebnis einer Abfrage: Liste von Tupeln
# - Bedeutung der Felder nur aus der Abfrage ersichtlich
# - Fehleranfällig bei Änderungen

# %%
import sqlite3

# %%
con = sqlite3.connect(":memory:")
con.execute(
    "CREATE TABLE habits(id INTEGER PRIMARY KEY, name TEXT, description TEXT)"
)
con.execute(
    "INSERT INTO habits VALUES (1, 'Exercise', 'Daily workout for 30 minutes')"
)
con.execute(
    "INSERT INTO habits VALUES (2, 'Read', 'Read for 20 minutes before bed')"
)
con.execute(
    "INSERT INTO habits VALUES (3, 'Meditate', 'Morning meditation for 10 minutes')"
)
con.commit()

# %%

# %%

# %% [markdown]
#
# - Was bedeutet `habit[0]`? Was ist `habit[2]`?

# %%
habit = rows[0]

# %%

# %%

# %% [markdown]
#
# - Ohne Dokumentation: Was ist was?
# - Bei Schemaänderungen müssen alle Indizes angepasst werden

# %% [markdown]
#
# ## Dataclasses als Domänenobjekte
#
# - Dataclasses geben den Daten Struktur und Namen
# - Autocomplete in der IDE
# - Klare, lesbare Attribute statt Indizes

# %%
from dataclasses import dataclass

# %%

# %% [markdown]
#
# ## DB-Zeilen in Objekte umwandeln
#
# - `Habit(*row)` entpackt ein Tupel in die Dataclass
# - Jetzt: `habit.name` statt `habit[1]`

# %%
row = con.execute("SELECT * FROM habits WHERE id = 1").fetchone()
row

# %%

# %%

# %%

# %%

# %% [markdown]
#
# ## Alle Zeilen umwandeln

# %%

# %%

# %%
con.close()


# %% [markdown]
#
# ## Das Problem mit verstreutem SQL
#
# - Gleiche Abfragen an mehreren Stellen im Programm
# - Bei Tabellenänderungen: alle Stellen finden und anpassen
# - Schwer zu testen
# - Vermischung von Geschäftslogik und Datenbankzugriff

# %% [markdown]
#
# ## Das Repository Pattern
#
# - Eine Klasse für alle DB-Operationen einer Entität
# - Geschäftslogik verwendet das Repository, schreibt nie SQL direkt
# - Repository wandelt zwischen DB-Zeilen und Domänenobjekten um
#
# ```
# Anwendung → HabitRepository → Datenbank
# ```

# %% [markdown]
#
# ## Vorteile des Repository Patterns
#
# - SQL ist an einer Stelle gesammelt
# - Einfach zu ändern, wenn sich das Schema ändert
# - Geschäftslogik bleibt sauber
# - Leicht testbar: Connection austauschen genügt

# %% [markdown]
#
# ## HabitRepository: Schritt für Schritt
#
# - Verbindung als Konstruktor-Parameter
# - Tabelle anlegen
# - Habit hinzufügen
# - Habit abfragen
# - Alle Habits abfragen
# - Habit aktualisieren
# - Habit löschen

# %% [markdown]
#
# ## Konstruktor: Verbindung speichern

# %%
class HabitRepository:
    pass

# %% [markdown]
#
# ## Tabelle anlegen

# %%
class HabitRepository:
    def __init__(self, connection: sqlite3.Connection):
        self.con = connection

# %% [markdown]
#
# ## Habit hinzufügen
#
# - `INSERT` und letzte eingefügte ID abfragen
# - Neues `Habit`-Objekt mit generierter ID zurückgeben

# %%
class HabitRepository:
    def __init__(self, connection: sqlite3.Connection):
        self.con = connection

    def create_table(self):
        self.con.execute(
            """CREATE TABLE IF NOT EXISTS habits(
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                description TEXT DEFAULT ''
            )"""
        )
        self.con.commit()

# %% [markdown]
#
# ## Repository verwenden: Tabelle anlegen

# %%
con = sqlite3.connect(":memory:")


# %%

# %%

# %% [markdown]
#
# ## Einfügen von Gewohnheiten

# %%

# %%

# %%

# %%

# %%

# %%

# %% [markdown]
#
# ## Repository: Habit abfragen

# %%
class HabitRepository:
    def __init__(self, connection: sqlite3.Connection):
        self.con = connection

    def create_table(self):
        self.con.execute(
            """CREATE TABLE IF NOT EXISTS habits(
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                description TEXT DEFAULT ''
            )"""
        )
        self.con.commit()

    def add(self, name: str, description: str = "") -> Habit:
        cursor = self.con.execute(
            "INSERT INTO habits(name, description) VALUES (?, ?)",
            (name, description),
        )
        self.con.commit()
        return Habit(cursor.lastrowid, name, description)

# %% [markdown]
#
# ## Repository: Alle Habits, Aktualisieren und Löschen

# %%
class HabitRepository:
    def __init__(self, connection: sqlite3.Connection):
        self.con = connection

    def create_table(self):
        self.con.execute(
            """CREATE TABLE IF NOT EXISTS habits(
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                description TEXT DEFAULT ''
            )"""
        )
        self.con.commit()

    def add(self, name: str, description: str = "") -> Habit:
        cursor = self.con.execute(
            "INSERT INTO habits(name, description) VALUES (?, ?)",
            (name, description),
        )
        self.con.commit()
        return Habit(cursor.lastrowid, name, description)

    def get_by_id(self, habit_id: int) -> Habit | None:
        row = self.con.execute(
            "SELECT * FROM habits WHERE id = ?", (habit_id,)
        ).fetchone()
        if row is None:
            return None
        return Habit(*row)

# %% [markdown]
#
# ## `HabitRepository` verwenden

# %%
con = sqlite3.connect(":memory:")
repo = HabitRepository(con)
repo.create_table()

# %%
exercise = repo.add("Exercise", "Daily workout for 30 minutes")
reading = repo.add("Read", "Read for 20 minutes before bed")
meditation = repo.add("Meditate", "Morning meditation for 10 minutes")

# %% [markdown]
#
# ## Abfragen von Gewohnheiten

# %%

# %%

# %%

# %% [markdown]
#
# ## Update

# %%

# %%

# %%

# %%

# %%

# %%

# %% [markdown]
#
# ## Delete

# %%
repo.get_all()


# %%

# %%

# %% [markdown]
#
# ## Anwendungslogik mit dem `HabitTracker`
#
# - Klasse `HabitTracker` kapselt das Repository
# - Aufrufer muss nicht wissen, dass eine Datenbank im Hintergrund arbeitet
# - Saubere Trennung: Geschäftslogik vs. Datenbankzugriff

# %%
class HabitTracker:
    pass

# %% [markdown]
#
# ## `HabitTracker` erweitern
#
# - `rename_habit`: Habit abfragen, ändern, aktualisieren
# - `remove_habit`: Delegiert an Repository

# %%
class HabitTracker:
    def __init__(self, habit_repo: HabitRepository):
        self.habits = habit_repo

    def add_habit(self, name: str, description: str = "") -> Habit:
        return self.habits.add(name, description)

    def show_habits(self):
        for habit in self.habits.get_all():
            print(f"- {habit.name}: {habit.description}")

# %% [markdown]
#
# ## HabitTracker verwenden

# %%
con = sqlite3.connect(":memory:")
repo = HabitRepository(con)
repo.create_table()
tracker = HabitTracker(repo)

# %%
tracker.add_habit("Exercise", "Daily workout")
tracker.add_habit("Read", "Read before bed")
tracker.show_habits()

# %%

# %%

# %%

# %%


# %% [markdown]
#
# ## Zusammenfassung: Vorher vs. Nachher
#
# | Vorher              | Nachher                 |
# |---------------------|-------------------------|
# | `habit[2]`          | `habit.description`     |
# | SQL überall         | SQL nur in Repositories |
# | Schwer zu testen    | Connection austauschbar |
# | Rohe Tupel          | Objekte mit Attributen  |
# | Logik direkt mit DB | Logik über HabitTracker |
