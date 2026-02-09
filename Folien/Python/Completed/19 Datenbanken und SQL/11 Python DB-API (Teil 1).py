# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Python DB-API (Teil 1)</b>
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
# Wir verwenden eine In-Memory-Datenbank für die Beispiele.
#
# Wenn Sie die Daten dauerhaft speichern möchten, können Sie stattdessen einen
# Dateipfad als Wert für `DB` verwenden, z.B. `DB = "students.db"`.

# %%
import sqlite3

# %%
DB = ":memory:"

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

# %% [markdown]
#
# ### Tabellen erstellen und Daten einfügen

# %%
cur.execute("CREATE TABLE students(id INTEGER, name TEXT)")

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
# ### SQL-Injection vermeiden
#
# Bevorzuge `executemany()` mit Argumentensubstitution statt manuell erstellten
# SQL-Abfragen. Der folgende Code ist anfällig für einen SQL-Injection-Angriff:


# %%
# for s in STUDENTS:
#     cur.executescript(f"INSERT INTO students VALUES({s[0]}, '{s[1]}')")


# %%
for row in cur.execute("SELECT * FROM students ORDER BY id"):
    print(row)

# %% [markdown]
#
# ### `executescript()`: Mehrere Anweisungen ausführen

# %%
SCRIPT = """
    BEGIN;
    CREATE TABLE teachers(id INTEGER, name TEXT);
    CREATE TABLE courses(course_id INTEGER, title TEXT, grade_points REAL);
    CREATE TABLE teaches(teacher_id INTEGER, course_id INTEGER);
    CREATE TABLE enrolments(student_id INTEGER, course_id INTEGER);
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
