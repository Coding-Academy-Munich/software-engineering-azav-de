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
# ## Was ist eine Transaktion?
#
# - Eine Transaktion fasst mehrere Datenbankoperationen zu einer logischen Einheit
#   zusammen
# - Entweder werden alle Operationen ausgeführt oder keine
# - Beispiel: Banküberweisung
#   - Konto A wird belastet, Konto B wird gutgeschrieben
#   - Beide Operationen müssen gemeinsam gelingen oder gemeinsam fehlschlagen
#   - Ohne Transaktionen: Ein Absturz zwischen den beiden Operationen könnte
#     dazu führen, dass Geld "verschwindet"

# %% [markdown]
#
# ## Commit und Rollback
#
# - **Commit**: Macht alle Änderungen der aktuellen Transaktion dauerhaft
# - **Rollback**: Macht alle Änderungen der aktuellen Transaktion rückgängig
# - Typisches Muster:
#   - Operationen ausführen
#   - Bei Erfolg: Commit
#   - Bei Fehler: Rollback
# - Viele Datenbanken öffnen Transaktionen automatisch
#   - Änderungen sind für andere erst nach einem Commit sichtbar

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

# %% [markdown]
#
# Mit dem Cursor können wir SQL-Anweisungen ausführen, um z.B. Tabellen zu
# erstellen oder Daten einzufügen.

# %%
cur.execute("SELECT 'hello, world'")

# %%
for row in cur.execute("SELECT 'hello, world'"):
    print(row)

# %% [markdown]
#
# ### Tabellen erstellen und Daten einfügen

# %%
cur.execute("CREATE TABLE students(id INTEGER PRIMARY KEY, name TEXT)")

# %%
con.commit()

# %% [markdown]
#
# Wir fügen Zeilen mit `execute()` und Parametersubstitution (`?`) ein:

# %%
cur.execute("INSERT INTO students VALUES(?, ?)", (123, "Joe Random"))

# %%
cur.execute("INSERT INTO students VALUES(?, ?)", (234, "Jane Doe"))

# %%
con.commit()

# %%
for row in cur.execute("SELECT id, name FROM students ORDER BY name"):
    print(row)

# %% [markdown]
#
# Mit `executemany()` können wir mehrere Zeilen auf einmal einfügen. Beachten
# Sie den zweiten Eintrag — wir werden ihn später verwenden, um SQL-Injection
# zu demonstrieren:

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
# Bevorzuge `execute()` und `executemany()` mit Parametersubstitution statt manuell
# erstellten SQL-Abfragen. Der folgende Code ist anfällig für einen
# SQL-Injection-Angriff:


# %% [markdown]
#
# Wir setzen die Tabelle zurück, um den Angriff zu demonstrieren:

# %%
cur.executescript("DROP TABLE IF EXISTS students")
cur.execute("CREATE TABLE students(id INTEGER PRIMARY KEY, name TEXT)")
cur.execute("INSERT INTO students VALUES(?, ?)", (123, "Joe Random"))
cur.execute("INSERT INTO students VALUES(?, ?)", (234, "Jane Doe"))
con.commit()

# %% [markdown]
#
# Dieser Code verwendet String-Formatierung statt Parametersubstitution:

# %%
try:
    for s in STUDENTS:
        cur.executescript(f"INSERT INTO students VALUES({s[0]}, '{s[1]}')")
except sqlite3.OperationalError as e:
    print(f"Error: {e}")

# %% [markdown]
#
# Bobby Tables hat die Tabelle gelöscht!

# %%
try:
    cur.execute("SELECT * FROM students")
except sqlite3.OperationalError as e:
    print(f"Error: {e}")

# %% [markdown]
#
# Wir stellen die Tabelle wieder her:

# %%
cur.execute("CREATE TABLE students(id INTEGER PRIMARY KEY, name TEXT)")
cur.execute("INSERT INTO students VALUES(?, ?)", (123, "Joe Random"))
cur.execute("INSERT INTO students VALUES(?, ?)", (234, "Jane Doe"))
cur.executemany("INSERT INTO students VALUES(?, ?)", STUDENTS)
con.commit()

# %%
for row in cur.execute("SELECT * FROM students ORDER BY id"):
    print(row)

# %% [markdown]
#
# ### `executescript()`: Mehrere Anweisungen ausführen

# %%
SCRIPT = """
    BEGIN;
    CREATE TABLE teachers(id INTEGER PRIMARY KEY, name TEXT);
    CREATE TABLE courses(course_id INTEGER PRIMARY KEY, title TEXT, grade_points REAL);
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

# %% [markdown]
#
# ## Workshop: Bücherdatenbank
#
# Erstellen Sie ein Python-Programm, das folgende Schritte ausführt:
#
# 1. Erzeugen Sie eine Verbindung zu einer In-Memory-Datenbank
# 2. Erstellen Sie eine Tabelle `books` mit den Spalten `id` (INTEGER) und
#    `title` (TEXT)
# 3. Fügen Sie ein Buch mit `execute()` und Parametersubstitution ein
# 4. Fügen Sie mehrere Bücher mit `executemany()` ein
# 5. Geben Sie alle Bücher aus
# 6. Schließen Sie die Verbindung

# %%
import sqlite3

# %%
con = sqlite3.connect(":memory:")

# %%
cur = con.cursor()

# %%
cur.execute("CREATE TABLE books(id INTEGER PRIMARY KEY, title TEXT)")

# %%
cur.execute("INSERT INTO books VALUES(?, ?)", (1, "The Hitchhiker's Guide to the Galaxy"))

# %%
MORE_BOOKS = [
    (2, "1984"),
    (3, "Brave New World"),
    (4, "Fahrenheit 451"),
]

# %%
cur.executemany("INSERT INTO books VALUES(?, ?)", MORE_BOOKS)

# %%
con.commit()

# %%
for row in cur.execute("SELECT * FROM books ORDER BY id"):
    print(row)

# %%
con.close()
