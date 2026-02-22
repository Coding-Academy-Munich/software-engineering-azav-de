# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>DB-API Integration (Teil 2)</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# # Best Practices für DB-API
#
# - Verbindungen zentral konfigurieren
# - Context Manager für Transaktionssicherheit
# - Fehlerbehandlung in Repositories
# - Trennung der Verantwortlichkeiten

# %%
import sqlite3
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
# ## Verbindungs-Factory
#
# - Zentrale Funktion für die Konfiguration der Verbindung
# - Alle Verbindungen erhalten konsistente Einstellungen
# - z.B. `PRAGMA foreign_keys` für SQLite

# %%
def create_connection(db_path: str = ":memory:") -> sqlite3.Connection:
    con = sqlite3.connect(db_path)
    con.execute("PRAGMA foreign_keys = ON")
    return con

# %%
con = create_connection()
con.execute("PRAGMA foreign_keys").fetchone()


# %% [markdown]
#
# ## Connections als Context Manager
#
# - `with con:` startet eine Transaktion
# - Bei Erfolg: automatischer Commit
# - Bei Ausnahme: automatischer Rollback
# - **Wichtig:** Die Verbindung wird dabei **nicht** geschlossen!

# %%
con = create_connection()
con.execute(
    """CREATE TABLE habits(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        description TEXT DEFAULT ''
    )"""
)
con.commit()

# %% [markdown]
#
# ## Erfolgreiche Transaktion

# %%
with con:
    con.execute(
        "INSERT INTO habits(name, description) VALUES (?, ?)",
        ("Exercise", "Daily workout"),
    )

# %%
con.execute("SELECT * FROM habits").fetchall()

# %% [markdown]
#
# ## Fehlgeschlagene Transaktion
#
# - Der zweite `INSERT` schlägt fehl (doppelte ID)
# - Der erste `INSERT` wird automatisch zurückgerollt

# %%
try:
    with con:
        con.execute(
            "INSERT INTO habits(id, name) VALUES (?, ?)", (100, "Read")
        )
        con.execute(
            "INSERT INTO habits(id, name) VALUES (?, ?)", (100, "Duplicate!")
        )
except sqlite3.IntegrityError as e:
    print(f"Error: {e}")

# %%
con.execute("SELECT * FROM habits WHERE id = 100").fetchone() is None


# %% [markdown]
#
# ## Repository mit Context Manager
#
# - Repository-Methoden verwenden `with self.con:`
# - Jede Operation ist transaktionssicher

# %%
class HabitRepository:
    def __init__(self, connection: sqlite3.Connection):
        self.con = connection

    def create_table(self):
        with self.con:
            self.con.execute(
                """CREATE TABLE IF NOT EXISTS habits(
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    description TEXT DEFAULT ''
                )"""
            )

    def add(self, habit: Habit) -> Habit:
        with self.con:
            cursor = self.con.execute(
                "INSERT INTO habits(name, description) VALUES (?, ?)",
                (habit.name, habit.description),
            )
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
        with self.con:
            self.con.execute("DELETE FROM habits WHERE id = ?", (habit_id,))


# %%
con = create_connection()
repo = HabitRepository(con)
repo.create_table()

# %%
repo.add(Habit(0, "Exercise", "Daily workout"))
repo.add(Habit(0, "Read", "Read before bed"))
repo.get_all()


# %% [markdown]
#
# ## Fehlerbehandlung in Repositories
#
# - Was kann schiefgehen?
#   - Constraint-Verletzungen (z.B. doppelte Einträge)
#   - Fehlende Daten (z.B. `get_by_id` findet nichts)
# - DB-spezifische Fehler im Repository behandeln
# - Eigene Ausnahmen für die Anwendung definieren

# %%
class HabitNotFoundError(Exception):
    def __init__(self, habit_id: int):
        super().__init__(f"Habit with id {habit_id} not found")
        self.habit_id = habit_id

# %% [markdown]
#
# ## Variante: Ausnahme statt `None`
#
# - `get_by_id` wirft `HabitNotFoundError` statt `None` zurückzugeben
# - Aufrufer muss nicht auf `None` prüfen
# - Fehler werden explizit behandelt

# %%
def get_by_id_strict(repo: HabitRepository, habit_id: int) -> Habit:
    habit = repo.get_by_id(habit_id)
    if habit is None:
        raise HabitNotFoundError(habit_id)
    return habit

# %%
get_by_id_strict(repo, 1)

# %%
try:
    get_by_id_strict(repo, 99)
except HabitNotFoundError as e:
    print(e)


# %% [markdown]
#
# ## Trennung der Verantwortlichkeiten
#
# - **Domänenobjekte:** Datenstruktur (Dataclasses)
# - **Repositories:** Datenbankzugriff
# - **Anwendungslogik:** Abläufe mit Repositories
#
# ```
# Anwendungslogik
#       ↓
# Repositories
#       ↓
#   Datenbank
# ```

# %% [markdown]
#
# ## Warum `habit_id` statt `habit`?
#
# - In reinem Python würde man `habit: Habit` speichern (Objektreferenz)
# - Mit Datenbanken verwenden wir stattdessen `habit_id: int` (Fremdschlüssel)
#
# **Gründe:**
#
# - Entspricht der Datenbankstruktur (Fremdschlüssel sind IDs)
# - Einfache Umwandlung zwischen Datenbankzeilen und Objekten
# - Repositories bleiben unabhängig voneinander
# - Anwendungslogik verbindet die Daten bei Bedarf

# %% [markdown]
#
# ## IDs vs. Objektreferenzen
#
# | | Ohne ORM (DB-API) | Mit ORM (z.B. SQLAlchemy) |
# |---|---|---|
# | **Referenzen** | IDs (`habit_id: int`) | Objekte (`habit: Habit`) |
# | **Laden** | Explizit über Repository | Automatisch (Lazy Loading) |
# | **Koordination** | Anwendungslogik | ORM übernimmt |
#
# Unsere Repositories verwenden IDs — Standard ohne ORM.
#
# ORMs wie SQLAlchemy machen Objektreferenzen praktikabel.

# %% [markdown]
#
# ## Beispiel: Anwendungslogik
#
# - Funktion `log_today` orchestriert Repositories
# - Enthält kein SQL, arbeitet nur mit Domänenobjekten

# %%
class EntryRepository:
    def __init__(self, connection: sqlite3.Connection):
        self.con = connection

    def create_table(self):
        with self.con:
            self.con.execute(
                """CREATE TABLE IF NOT EXISTS entries(
                    id INTEGER PRIMARY KEY,
                    habit_id INTEGER NOT NULL,
                    date TEXT NOT NULL,
                    completed INTEGER DEFAULT 1
                )"""
            )

    def log_entry(self, entry: HabitEntry) -> HabitEntry:
        with self.con:
            cursor = self.con.execute(
                "INSERT INTO entries(habit_id, date, completed) VALUES (?, ?, ?)",
                (entry.habit_id, entry.date, int(entry.completed)),
            )
        return HabitEntry(
            cursor.lastrowid, entry.habit_id, entry.date, entry.completed
        )

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


# %%
def log_today(
    habit_repo: HabitRepository,
    entry_repo: EntryRepository,
    habit_name: str,
    date: str,
):
    for habit in habit_repo.get_all():
        if habit.name == habit_name:
            return entry_repo.log_entry(HabitEntry(0, habit.id, date))
    raise HabitNotFoundError(-1)

# %%
entry_repo = EntryRepository(con)
entry_repo.create_table()

# %%
log_today(repo, entry_repo, "Exercise", "2026-02-20")

# %%
entry_repo.get_entries_for_habit(1)


# %% [markdown]
#
# ## Alles zusammen: Habit Tracker
#
# - Komplette Mini-Anwendung
# - Sauberer Aufbau: Connection → Repositories → Logik

# %%
con = create_connection()

# %%
habit_repo = HabitRepository(con)
habit_repo.create_table()
entry_repo = EntryRepository(con)
entry_repo.create_table()

# %%
exercise = habit_repo.add(Habit(0, "Exercise", "Daily workout"))
reading = habit_repo.add(Habit(0, "Read", "Read before bed"))
meditation = habit_repo.add(Habit(0, "Meditate", "Morning meditation"))

# %%
for date in ["2026-02-17", "2026-02-18", "2026-02-19", "2026-02-20"]:
    entry_repo.log_entry(HabitEntry(0, exercise.id, date))

# %%
entry_repo.log_entry(HabitEntry(0, reading.id, "2026-02-17"))
entry_repo.log_entry(HabitEntry(0, reading.id, "2026-02-19"))
entry_repo.log_entry(HabitEntry(0, meditation.id, "2026-02-20"))

# %%
for habit in habit_repo.get_all():
    count = entry_repo.get_completion_count(habit.id)
    total = len(entry_repo.get_entries_for_habit(habit.id))
    print(f"{habit.name}: {count}/{total} completed")


# %% [markdown]
#
# ## Wie das beim Testen hilft
#
# - Repository bekommt Verbindung → `:memory:`-DB für Tests
# - Funktionen bekommen Repositories → Testdaten leicht einzurichten
# - Kein externer Zustand nötig

# %%
def test_add_and_get_habit():
    con = create_connection()
    repo = HabitRepository(con)
    repo.create_table()

    habit = repo.add(Habit(0, "Test Habit", "For testing"))

    assert habit.id == 1
    assert habit.name == "Test Habit"

    retrieved = repo.get_by_id(1)
    assert retrieved is not None
    assert retrieved.name == "Test Habit"

    con.close()
    print("Test passed!")

# %%
test_add_and_get_habit()

# %%
def test_delete_habit():
    con = create_connection()
    repo = HabitRepository(con)
    repo.create_table()

    habit = repo.add(Habit(0, "To Delete"))
    repo.delete(habit.id)

    assert repo.get_by_id(habit.id) is None
    assert repo.get_all() == []

    con.close()
    print("Test passed!")

# %%
test_delete_habit()


# %% [markdown]
#
# ## Best Practices: Checkliste
#
# - Dataclasses für Domänenobjekte verwenden
# - Alles SQL in Repository-Klassen sammeln
# - Verbindungen als Konstruktor-Parameter übergeben
# - Context Manager für Transaktionssicherheit nutzen
# - Fehler behandeln und in Anwendungsausnahmen umwandeln
# - Geschäftslogik frei von SQL halten
