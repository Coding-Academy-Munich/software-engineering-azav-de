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

# %% [markdown]
#
# ## Tracking von Gewohnheiten

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


# %% [markdown]
#
# ## Verbindungs-Factory
#
# - Zentrale Funktion für die Konfiguration der Verbindung
# - Alle Verbindungen erhalten konsistente Einstellungen
# - z.B. `PRAGMA foreign_keys` für SQLite um Fremdschlüssel zu aktivieren

# %%

# %%
con = sqlite3.connect(":memory:")
con.execute("PRAGMA foreign_keys").fetchone()
con.close()

# %%


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
        con.execute("INSERT INTO habits(id, name) VALUES (?, ?)", (100, "Read"))
        con.execute("INSERT INTO habits(id, name) VALUES (?, ?)", (100, "Duplicate!"))
except sqlite3.IntegrityError as e:
    print(f"Error: {e}")

# %%
con.execute("SELECT * FROM habits WHERE id = 100").fetchone() is None


# %% [markdown]
#
# ## Repository mit Context Manager
#
# - Repository-Methoden verwenden `with self.con:`
# - Jede schreibende Operation ist transaktionssicher
# - Lesende Operationen brauchen keine Transaktion

# %%
class HabitRepository:
    pass


# %%
con = create_connection()
repo = HabitRepository(con)
repo.create_table()

# %%
repo.add("Exercise", "Daily workout")
repo.add("Read", "Read before bed")
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
# - `get_by_id_strict` wirft `HabitNotFoundError` statt `None` zurückzugeben
# - Aufrufer muss nicht auf `None` prüfen
# - Fehler werden explizit behandelt

# %%

# %%

# %%


# %% [markdown]
#
# ## EntryRepository
#
# - Zweites Repository für die `entries`-Tabelle
# - Gleiches Muster für eine zweite Entität
# - Zeigt: Das Pattern skaliert

# %%
class EntryRepository:
    pass


# %% [markdown]
#
# ## EntryRepository: Abfragen
#
# - `completed` wird als `INTEGER` gespeichert
# - Deshalb `bool(r[3])` statt `HabitEntry(*r)`

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

    def log_entry(self, habit_id: int, date: str, completed: bool = True) -> HabitEntry:
        with self.con:
            cursor = self.con.execute(
                "INSERT INTO entries(habit_id, date, completed) VALUES (?, ?, ?)",
                (habit_id, date, int(completed)),
            )
        return HabitEntry(cursor.lastrowid, habit_id, date, completed)


# %% [markdown]
#
# ## `EntryRepository` verwenden

# %%
entry_repo = EntryRepository(con)
entry_repo.create_table()

# %%
exercise = repo.add("Exercise", "Daily workout for 30 minutes")

# %% [markdown]
#
# ### Einträge protokollieren

# %%

# %%

# %%

# %% [markdown]
#
# ### Informationen abfragen

# %%

# %%


# %% [markdown]
#
# ## Trennung der Verantwortlichkeiten
#
# - **Domänenobjekte:** Datenstruktur (Dataclasses)
# - **Repositories:** Datenbankzugriff
# - **Anwendungslogik:** Abläufe mit Repositories
#
# ```
# Anwendungslogik (HabitTracker)
#       ↓
# Repositories (HabitRepository, EntryRepository)
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
# ## HabitTracker mit Entries
#
# - Erweitert den HabitTracker aus Teil 1
# - Nimmt beide Repositories als Konstruktor-Parameter
# - Enthält kein SQL, arbeitet nur mit Repositories

# %%
class HabitTracker:
    pass


# %% [markdown]
#
# ## `HabitTracker` verwenden

# %%
con = create_connection()
habit_repo = HabitRepository(con)
habit_repo.create_table()
entry_repo = EntryRepository(con)
entry_repo.create_table()

# %%
tracker = HabitTracker(habit_repo, entry_repo)

# %%
exercise = tracker.add_habit("Exercise", "Daily workout")
reading = tracker.add_habit("Read", "Read before bed")
meditation = tracker.add_habit("Meditate", "Morning meditation")

# %%
for date in ["2026-02-17", "2026-02-18", "2026-02-19", "2026-02-20"]:
    tracker.log_entry("Exercise", date)

# %%
tracker.log_entry("Read", "2026-02-17")
tracker.log_entry("Read", "2026-02-19")
tracker.log_entry("Meditate", "2026-02-20")

# %%
tracker.show_progress()

# %%
tracker.get_progress()


# %% [markdown]
#
# ## Wie das beim Testen hilft
#
# - Datenbanken sind eine Quelle von Nichtdeterminismus in Tests
# - `:memory:`-DB = ein Fake (vereinfachte echte Implementierung)
# - Jeder Test erstellt seine eigene DB → vollständige Isolation
# - DI: `HabitTracker` bekommt Repositories → testbar ohne SQL

# %% [markdown]
#
# ## Repository testen

# %%
def setup_test_db() -> tuple[HabitRepository, EntryRepository]:
    con = create_connection(":memory:")
    habit_repo = HabitRepository(con)
    habit_repo.create_table()
    entry_repo = EntryRepository(con)
    entry_repo.create_table()
    return habit_repo, entry_repo


# %%
def test_add_habit():
    repo, _ = setup_test_db()
    habit = repo.add("Test Habit", "For testing")

    assert habit.id == 1
    assert habit.name == "Test Habit"


# %%
test_add_habit()


# %%
def test_get_nonexistent_habit():
    repo, _ = setup_test_db()

    assert repo.get_by_id(999) is None


# %%
test_get_nonexistent_habit()


# %% [markdown]
#
# ## Anwendungslogik testen
#
# - `HabitTracker` enthält kein SQL
# - Gleicher Test-Aufbau: Repos mit `:memory:`-DB injizieren
# - Geschäftslogik unabhängig von Datenbankdetails testen

# %%
def setup_habit_tracker() -> HabitTracker:
    habit_repo, entry_repo = setup_test_db()
    return HabitTracker(habit_repo, entry_repo)


# %%
def test_habit_tracking():
    tracker = setup_habit_tracker()

    tracker.add_habit("Exercise")
    tracker.log_entry("Exercise", "2026-02-17")
    tracker.log_entry("Exercise", "2026-02-18")

    progress = tracker.get_progress()
    assert progress == [("Exercise", 2, 2)]


# %%
test_habit_tracking()


# %%
def test_log_entry_unknown_habit():
    tracker = setup_habit_tracker()

    try:
        tracker.log_entry("Nonexistent", "2026-02-17")
        assert False, "Should have raised HabitNotFoundError"
    except HabitNotFoundError:
        pass


# %%
test_log_entry_unknown_habit()


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
# - Anwendungsklassen (z.B. HabitTracker) kapseln die Repositories
