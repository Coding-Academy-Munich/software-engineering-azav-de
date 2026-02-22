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
rows = con.execute("SELECT * FROM habits").fetchall()
rows

# %% [markdown]
#
# - Was bedeutet `habit[0]`? Was ist `habit[2]`?

# %%
habit = rows[0]
habit[0]

# %%
habit[2]

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
@dataclass
class Habit:
    id: int
    name: str
    description: str = ""

# %%
@dataclass
class HabitEntry:
    id: int
    habit_id: int
    date: str
    completed: bool = True

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
habit = Habit(*row)
habit

# %%
habit.name

# %%
habit.description

# %% [markdown]
#
# ## Alle Zeilen umwandeln

# %%
habits = [Habit(*row) for row in con.execute("SELECT * FROM habits").fetchall()]
habits

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
# - Habit löschen

# %% [markdown]
#
# ## Konstruktor: Verbindung speichern

# %% [markdown]
#
# ## Tabelle anlegen

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

    def add(self, habit: Habit) -> Habit:
        cursor = self.con.execute(
            "INSERT INTO habits(name, description) VALUES (?, ?)",
            (habit.name, habit.description),
        )
        self.con.commit()
        return Habit(cursor.lastrowid, habit.name, habit.description)

# %% [markdown]
#
# ## Habit abfragen

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

    def add(self, habit: Habit) -> Habit:
        cursor = self.con.execute(
            "INSERT INTO habits(name, description) VALUES (?, ?)",
            (habit.name, habit.description),
        )
        self.con.commit()
        return Habit(cursor.lastrowid, habit.name, habit.description)

    def get_by_id(self, habit_id: int) -> Habit | None:
        row = self.con.execute(
            "SELECT * FROM habits WHERE id = ?", (habit_id,)
        ).fetchone()
        if row is None:
            return None
        return Habit(*row)

# %% [markdown]
#
# ## Alle Habits und Löschen

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

    def add(self, habit: Habit) -> Habit:
        cursor = self.con.execute(
            "INSERT INTO habits(name, description) VALUES (?, ?)",
            (habit.name, habit.description),
        )
        self.con.commit()
        return Habit(cursor.lastrowid, habit.name, habit.description)

    def get_by_id(self, habit_id: int) -> Habit | None:
        row = self.con.execute(
            "SELECT * FROM habits WHERE id = ?", (habit_id,)
        ).fetchone()
        if row is None:
            return None
        return Habit(*row)

    def get_all(self) -> list[Habit]:
        rows = self.con.execute("SELECT * FROM habits").fetchall()
        return [Habit(*row) for row in rows]

    def delete(self, habit_id: int):
        self.con.execute("DELETE FROM habits WHERE id = ?", (habit_id,))
        self.con.commit()


# %% [markdown]
#
# ## HabitRepository verwenden

# %%
con = sqlite3.connect(":memory:")
repo = HabitRepository(con)
repo.create_table()

# %%
exercise = repo.add(Habit(0, "Exercise", "Daily workout for 30 minutes"))
exercise

# %%
reading = repo.add(Habit(0, "Read", "Read for 20 minutes before bed"))
reading

# %%
meditation = repo.add(Habit(0, "Meditate", "Morning meditation for 10 minutes"))
meditation

# %%
repo.get_by_id(1)

# %%
repo.get_by_id(99) is None

# %%
repo.get_all()

# %%
repo.delete(2)
repo.get_all()


# %% [markdown]
#
# ## EntryRepository
#
# - Zweites Repository für die `entries`-Tabelle
# - Gleiches Muster für eine zweite Entität
# - Zeigt: Das Pattern skaliert

# %%
class EntryRepository:
    def __init__(self, connection: sqlite3.Connection):
        self.con = connection

    def create_table(self):
        self.con.execute(
            """CREATE TABLE IF NOT EXISTS entries(
                id INTEGER PRIMARY KEY,
                habit_id INTEGER NOT NULL,
                date TEXT NOT NULL,
                completed INTEGER DEFAULT 1
            )"""
        )
        self.con.commit()

    def log_entry(self, entry: HabitEntry) -> HabitEntry:
        cursor = self.con.execute(
            "INSERT INTO entries(habit_id, date, completed) VALUES (?, ?, ?)",
            (entry.habit_id, entry.date, int(entry.completed)),
        )
        self.con.commit()
        return HabitEntry(cursor.lastrowid, entry.habit_id, entry.date, entry.completed)

    def get_entries_for_habit(self, habit_id: int) -> list[HabitEntry]:
        rows = self.con.execute(
            "SELECT * FROM entries WHERE habit_id = ?", (habit_id,)
        ).fetchall()
        return [HabitEntry(r[0], r[1], r[2], bool(r[3])) for r in rows]

    def get_completion_count(self, habit_id: int) -> int:
        row = self.con.execute(
            "SELECT COUNT(*) FROM entries WHERE habit_id = ? AND completed = 1",
            (habit_id,),
        ).fetchone()
        return row[0]


# %% [markdown]
#
# ## EntryRepository verwenden

# %%
entry_repo = EntryRepository(con)
entry_repo.create_table()

# %%
exercise = repo.add(Habit(0, "Exercise", "Daily workout for 30 minutes"))
exercise

# %%
entry_repo.log_entry(HabitEntry(0, exercise.id, "2026-02-17"))
entry_repo.log_entry(HabitEntry(0, exercise.id, "2026-02-18"))
entry_repo.log_entry(HabitEntry(0, exercise.id, "2026-02-19", completed=False))

# %%
entry_repo.get_entries_for_habit(exercise.id)

# %%
entry_repo.get_completion_count(exercise.id)


# %% [markdown]
#
# ## Repositories zusammen verwenden
#
# - Der aufrufende Code enthält kein SQL
# - Liest sich wie eine Beschreibung der Geschäftslogik

# %%
con2 = sqlite3.connect(":memory:")
habit_repo = HabitRepository(con2)
habit_repo.create_table()
entry_repo2 = EntryRepository(con2)
entry_repo2.create_table()

# %%
exercise = habit_repo.add(Habit(0, "Exercise", "Daily workout"))
reading = habit_repo.add(Habit(0, "Read", "Read before bed"))
meditation = habit_repo.add(Habit(0, "Meditate", "Morning meditation"))

# %%
for date in ["2026-02-17", "2026-02-18", "2026-02-19"]:
    entry_repo2.log_entry(HabitEntry(0, exercise.id, date))

# %%
entry_repo2.log_entry(HabitEntry(0, reading.id, "2026-02-17"))
entry_repo2.log_entry(HabitEntry(0, reading.id, "2026-02-19"))

# %%
for habit in habit_repo.get_all():
    count = entry_repo2.get_completion_count(habit.id)
    print(f"{habit.name}: {count} completions")


# %% [markdown]
#
# ## Zusammenfassung: Vorher vs. Nachher
#
# | Vorher | Nachher |
# |--------|---------|
# | `habit[2]` | `habit.description` |
# | SQL überall | SQL nur in Repositories |
# | Schwer zu testen | Connection austauschbar |
# | Rohe Tupel | Objekte mit Attributen |
