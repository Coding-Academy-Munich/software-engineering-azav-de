# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Python DB-API</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# # Datenbanken in Python: DB-API 2.0
#
# - Python hat ein standardisiertes API für SQL-Datenbanken
# - Die Spezifikation ist in [PEP-249](https://peps.python.org/pep-0249/)
# - Wir verwenden beispielhaft das `sqlite3` Modul
#   - Dieses Modul ist in der Standard-Installation von Python enthalten
#   - Es bietet einen Modus, in dem die Datenbank nur im Arbeitsspeicher gehalten wird
#   - Andere SQL-Datenbanken funktionieren ähnlich, haben aber gewisse Variationen


# %% [markdown]
#
# ## Grundlegende Konzepte
#
# - Datenbanken werden über eine *Verbindung* *("Connection")* angesprochen
# - Zum Ausführen von Anweisungen (und Zugriff auf die Ergebnisse) benötigen
#   wir einen *Cursor*
# - Weitere Klassen, wie `Row` oder `Blob` dienen zum Umgang mit Ergebnissen.

# %% [markdown]
#
# ## Erzeugen einer Verbindung
#
# - Eine `Connection`-Instanz wird mit `sqlite3.connect()` erzeugt
# - Argumente zu `connect()` beschreiben die Konfiguration der Datenbank
# - Mit `":memory:"` wird eine In-Memory-Datenbank erzeugt
# - Connections verwalten Transaktionen, falls die Datenbank das unterstützt:
#   - `connection.commit()` existiert immer, macht möglicherweise nichts
#   - `connection.rollback()` existiert nur, falls die DB Transaktionen unterstützt

# %% [markdown]
#
# Wir erstellen eine temporäre Datei für eine sqlite3-Datenbank, damit die Daten
# erhalten bleiben, wenn wir eine Verbindung trennen und wiederherstellen.
#
# Wenn dies Probleme verursacht, können Sie entweder
#
# - den Pfad, unter dem die Datenbank gespeichert werden soll in der Variable
#   `DB` speichern oder
# - die Variable `DB` auf den speziellen Namen `:memory:` setzen, um eine
#   In-Memory-Datenbank zu erstellen. In diesem Fall sollten Sie die Befehle
#   nicht ausführen, die die die Datenbankverbindung trennen und wieder
#   herstellen.

# %%
import tempfile

# %%
DB = ":memory:"
print(f"Database path: {DB}")

# %%
import sqlite3

# %%
con = sqlite3.connect(DB)
con

# %%
con.commit()

# %%
con.rollback()

# %% [markdown]
#
# ## Erzeugen eines Cursors
#
# - Die meisten Operationen im DB-API werden nicht auf der Connection ausgeführt,
#   sondern auf einem Cursor:
# - Commit und Rollback erfolgen direkt auf der Connection

# %%
cur = con.cursor()
cur

# %% [markdown]
#
# ## Ausführen von SQL-Anweisungen
#
# - `cursor.execute()` führt eine (parametrisierte) SQL-Anweisung aus
#   - Je nach Wert von `connection.isolation_level` wird eine Transaktion eröffnet
#   - Parameter werden korrekt "maskiert" um SQL-Injektionen zu vermeiden
#   - [`sqlite3.paramstyle`](https://peps.python.org/pep-0249/#paramstyle)
#     bestimmt, wie Parameter im Query-String gekennzeichnet werden
# - `cursor.executemany()`
#   - Wie `.execute()` aber mit einem Iterator von Parametern
# - `cursor.executescript()` führt mehrere SQL-Anweisungen aus
#   - Transaktionen müssen manuell verwaltet werden

# %%
con.isolation_level

# %%
sqlite3.paramstyle

# %%
cur.execute("SELECT 'hello, world'")

# %%
for cursor in cur.execute("SELECT 'hello, world'"):
    print(cursor)

# %%
# cur.execute("DROP TABLE students")

# %%
cur.execute("CREATE TABLE students(id, name)")

# %%
con.commit()

# %%
cur.execute("INSERT INTO students VALUES(?, ?)", (123, "Joe Random"))

# %%
cur.execute("INSERT INTO students VALUES(?, ?)", (234, "Jane Doe"))

# %%
con.commit()

# %%
for row in cur.execute("SELECT id, name FROM students ORDER BY name"):
    print(row)

# %%
STUDENTS = [
    (1, "Jack Bradley"),
    # https://xkcd.com/327/
    (2, "Robert'); DROP TABLE students; --"),
    (845, "Samantha Jones"),
    (210, "Jill McGee"),
    (62, "Doug Caisson"),
]

# %%
cur.executemany("INSERT INTO students VALUES(?, ?)", STUDENTS)

# %%
con.commit()

# %% [markdown]
#
# Bevorzuge `executemany()` mit Argumentensubstitution statt manuell erstellten
# SQL-Abfragen . Der folgende Code ist anfällig für einen SQL-Injection-Angriff:


# %%
# for s in STUDENTS:
#     cur.executescript(f"INSERT INTO students VALUES({s[0]}, '{s[1]}')")


# %%
for row in cur.execute("SELECT * FROM students ORDER BY id"):
    print(row)

# %%
SCRIPT = """
    BEGIN;
    CREATE TABLE teachers(id, name);
    CREATE TABLE courses(course_id, title, grade_points);
    CREATE TABLE teaches(teacher_id, course_id);
    CREATE TABLE enrolments(student_id, course_id);
    COMMIT;
"""

# %%
cur.executescript(SCRIPT)

# %%
for row in cur.execute("SELECT * from sqlite_master"):
    print(row)

# %% [markdown]
#
# ## Schließen von Verbindungen
#
# Wenn eine Verbindung nicht mehr benötigt wird, kann sie mit `close()` geschlossen
# werden:

# %%
con.close()

# %% [markdown]
#
# ## Zugriff auf Ergebnisse
#
# - `cursor.fetchall()` für alle Ergebnisse
# - `cursor.fetchone()` für einzelne Ergebnisse
# - `cursor.fetchmany()` für eine bestimmte Anzahl an Ergebnissen
# - Iteration über einen Ergebnis-Cursor

# %%
con = sqlite3.connect(DB)


# %%
cur = con.cursor()

# %% [markdown]
#
# - Ensure that we have the `students` table with some data:

# %%
cur.execute("CREATE TABLE IF NOT EXISTS students(id, name)")
cur.executemany("INSERT INTO students VALUES(?, ?)", STUDENTS)

# %%
cur.execute("SELECT * FROM students ORDER BY id")

# %%
cur.fetchall()

# %% [markdown]
#
# Ein Cursor kan nur einmal verwendet werden, um Ergebnisse zu bekommen:

# %%
cur.fetchall()

# %%
cur = cur.execute("SELECT * FROM students ORDER BY id")

# %%
cur.fetchone()

# %%
cur.fetchone()

# %%
cur.fetchall()

# %%
cur.fetchone() is None

# %%
cur = cur.execute("SELECT * FROM students ORDER BY id")

# %%
cur.fetchmany(3)

# %% [markdown]
#
# ### Shortcut-Methoden
#
# - Um das explizite Erzeugen von Cursor-Instanzen zu umgehen, kann man
#   die Shortcut-Methoden auf dem Connection-Objekt verwenden:

# %%
print(cursor)

# %%
# Required to work around a bug in nbclient...
if not isinstance(cursor, tuple):
    cursor.fetchall()

# %%
# res = con.executemany(
#     "INSERT INTO students VALUES (?, ?)",
#     [(42, "Douglas Adams"), (63, "Andrea A. Graves")],
# )

# %%
# Might throw an error (or not)
# res.fetchall()

# %%
cursor = con.execute("SELECT * FROM students ORDER BY id")

# %%
# Required to work around a bug in nbclient...
if not isinstance(cursor, tuple):
    cursor.fetchall()

# %%
con.commit()

# %% [markdown]
#
# ## Mehrere Verbindungen
#
# - Mehrere Verbindungen zur gleichen Datenbank sind möglich
# - Mehrere Cursors zur gleichen Verbindung sind möglich
#   - Aber: In beiden Fällen führen mehrere gleichzeitig aktive
#     Transaktionen zu Timeouts
# - Cursors zur gleichen Verbindung sind nicht isoliert
# - Wie isoliert Threads voneinander sind, wird durch
#   [`connection.threadsafety`](https://peps.python.org/pep-0249/#threadsafety)
#   beschrieben.

# %%
con.close()

# %%
FD, DB = tempfile.mkstemp(suffix=".db")

# %%
con = sqlite3.connect(DB)

# %%
cur = con.cursor()

# %%
cur.execute("CREATE TABLE IF NOT EXISTS students(id, name)")
cur.executemany("INSERT INTO students VALUES(?, ?)", STUDENTS)

# %%
con2 = sqlite3.connect(DB)

# %%
cur.execute("INSERT INTO students VALUES(2, 'Deborah Winter')")

# %%
con.commit()

# %%
res2 = con2.execute("SELECT * FROM students ORDER BY id")

# %%
con2.commit()

# %%
res1 = con.execute("SELECT * FROM students ORDER BY id")

# %%
con.commit()

# %%
res1.fetchall()

# %%
res2.fetchall()

# %%
con.close()
con2.close()

# %%
con = sqlite3.connect(DB)

# %%
cur1 = con.cursor()

# %%
cur2 = con.cursor()

# %%
cur1.execute("SELECT * FROM students")

# %%
cur1.fetchall()

# %%
cur2.executemany(
    "INSERT INTO students VALUES (?, ?)", [(1, "Kay Garcia"), (2, "Amanda Goodson")]
)

# %%
con.commit()

# %% [markdown]
#
# ## Zugriff auf Metadaten
#
# - Erfolgt typischerweise mit DB-spezifischen Tabellen:

# %%
cursor = con.execute("SELECT name FROM sqlite_master")
cursor

# %%
cursor.fetchone()

# %%
cursor = con.execute("SELECT name FROM sqlite_master WHERE name='foo'")
cursor.fetchone() is None

# %%
con.execute("CREATE TABLE projects(proj_id, name, budget)")

# %%
list(con.execute("SELECT * FROM sqlite_master"))

# %%
con.close()

# %%
import os

# %%
try:
    os.unlink(DB)
except PermissionError as e:
    print(f"Could not delete the database file: {e}")

# %% [markdown]
#
# ## Mini-Workshop: Mitarbeiter-Datenbank
#
# Sie wollen Daten für die Mitarbeiter einer Firma in einer SQLite Datenbank
# speichern. Jeder Mitarbeiter wird dabei durch folgende Daten beschrieben:
#
# - Personalnummer
# - Name
# - Abteilungs-Nummer
# - Wochenarbeitszeit in Stunden
#
# Jede Abteilung wird repräsentiert durch folgende Daten:
#
# - Abteilungs-Nummer
# - Name der Abteilung
#
# Schreiben Sie folgende Funktionen:
#
# - `create_employee_db(...)`, die die Tabellen erzeugt
# - `create_department(...)`, die eine neue Abteilung in die Datenbank einfügt.
# - `create_employee(...)`, die einen neuen Mitarbeiter in die Datenbank einfügt.
# - `create_employee(...)`, die mehrere neue Mitarbeiter in die Datenbank einfügt.
# - `get_employee_data(db, id)`, die die Daten für den Mitarbeiter mit
#    Personalnummer `id` zurückgibt. (Falls Sie SQL Joins kennen, können Sie statt
#    der Abteilungs-Nummer den Namen der Abteilung zurückgeben.)
# - `find_part_time_employees(...)`, die die Personalnummern alle Mitarbeiter
#    zurückgibt, die weniger als 30 Stunden pro Woche arbeiten.
# - `print_employees_in_department(con: sqlite3.Connection, name: str)`,
#    die die Daten aller Mitarbeiter in
#    der Abteilung mit Namen `name` ausdruckt. (Falls sie SQL-Joins nicht kennen,
#    können Sie auch die Abteilungs-Nummer an die Funktion übergeben.)

# %%
import sqlite3

# %%
con = sqlite3.connect(":memory:")


# %%
def create_employee_db(con: sqlite3.Connection):
    return con.executescript(
        """
        BEGIN;
        CREATE TABLE employees(id, name, dep_id, hours);
        CREATE TABLE departments(id, name);
        COMMIT;
        """
    )


# %%
create_employee_db(con)


# %%
def create_department(con: sqlite3.Connection, id_: int, name: str):
    con.execute("INSERT INTO departments VALUES (?, ?)", (id_, name))
    con.commit()


# %%
create_department(con, 1, "Marketing")
create_department(con, 2, "R&D")
create_department(con, 3, "Accounting")

# %%
assert con.execute("SELECT * FROM departments ORDER BY id").fetchall() == [
    (1, "Marketing"),
    (2, "R&D"),
    (3, "Accounting"),
]


# %%
def create_employee(
    con: sqlite3.Connection, id_: int, name: str, dep_id: int, hours: int
):
    con.execute("INSERT INTO employees VALUES (?, ?, ?, ?)", (id_, name, dep_id, hours))
    con.commit()


# %%
create_employee(con, 1, "Geraldine E. Stegner", 1, 40)

# %%
assert con.execute("SELECT * FROM employees").fetchall() == [
    (1, "Geraldine E. Stegner", 1, 40)
]

# %%
from typing import Sequence


# %%
def create_employees(con: sqlite3.Connection, data: Sequence):
    con.executemany("INSERT INTO employees VALUES (?, ?, ?, ?)", data)
    con.commit()


# %%
EMPLOYEES = [
    (2, "Tammy T. Selby", 2, 42),
    (3, "Pam Adams", 3, 24),
    (4, "Bobby A. Skaggs", 1, 38),
    (5, "Sandra A. Finley", 2, 26),
]

# %%
create_employees(con, EMPLOYEES)

# %%
assert con.execute("SELECT * FROM employees").fetchall() == [
    (1, "Geraldine E. Stegner", 1, 40),
    *EMPLOYEES,
]


# %%
def get_employee_data(con: sqlite3.Connection, id_: int):
    return con.execute(
        """
        SELECT e.id, e.name, d.name, e.hours
        FROM employees AS e
        JOIN departments AS d
        ON e.dep_id = d.id
        WHERE e.id = ?
        """,
        (id_,),
    ).fetchone()


# %%
assert get_employee_data(con, 1) == (1, "Geraldine E. Stegner", "Marketing", 40)

# %%
assert get_employee_data(con, 10) is None


# %%
def get_employee_data_no_join(con: sqlite3.Connection, id_: int):
    return con.execute(
        """
        SELECT id, name, dep_id, hours
        FROM employees AS e
        WHERE id = ?
        """,
        (id_,),
    ).fetchone()


# %%
assert get_employee_data_no_join(con, 1) == (1, "Geraldine E. Stegner", 1, 40)

# %%
assert get_employee_data_no_join(con, 10) is None


# %%
def get_part_time_employees(con: sqlite3.Connection):
    return [
        id_
        for (id_,) in con.execute(
            "SELECT id FROM employees WHERE hours < 30"
        ).fetchall()
    ]


# %%
assert get_part_time_employees(con) == [3, 5]


# %%
def print_employees_in_department(con: sqlite3.Connection, name: str):
    employees = con.execute(
        """
        SELECT e.id, e.name, d.name, e.hours
        FROM employees AS e
        JOIN departments AS d
        ON e.dep_id = d.id
        WHERE d.name = ?
        """,
        (name,),
    )
    for id_, name, dep, hours in employees:
        print(f"{name}: id = {id_}, dep = {dep}, hours = {hours}")


# %%
print_employees_in_department(con, "Marketing")

# %% [markdown]
#
# Ausgabe:
# ```
# Geraldine E. Stegner: id = 1, dep = Marketing, hours = 40
# Bobby A. Skaggs: id = 4, dep = Marketing, hours = 38
# ```

# %%
