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

# %%
test_add_and_get_habit()

# %%

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
