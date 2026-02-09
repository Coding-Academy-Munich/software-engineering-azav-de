# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Python DB-API (Teil 2)</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# ## Zugriff auf Ergebnisse
#
# - `cursor.fetchall()` für alle Ergebnisse
# - `cursor.fetchone()` für einzelne Ergebnisse
# - `cursor.fetchmany()` für eine bestimmte Anzahl an Ergebnissen
# - Iteration über einen Ergebnis-Cursor

# %%
import sqlite3

# %%
DB = ":memory:"

# %%
STUDENTS = [
    (1, "Jack Bradley"),
    (2, "Robert'); DROP TABLE students; --"),
    (845, "Samantha Jones"),
    (210, "Jill McGee"),
    (62, "Doug Caisson"),
]

# %%
con = sqlite3.connect(DB)

# %%
cur = con.cursor()

# %% [markdown]
#
# Wir erstellen die Tabelle `students` mit einigen Daten:

# %%
cur.execute("CREATE TABLE IF NOT EXISTS students(id INTEGER, name TEXT)")
cur.executemany("INSERT INTO students VALUES(?, ?)", STUDENTS)

# %%
cur.execute("SELECT * FROM students ORDER BY id")

# %%

# %% [markdown]
#
# Ein Cursor kann nur einmal verwendet werden, um Ergebnisse zu bekommen:

# %%

# %%
cur = cur.execute("SELECT * FROM students ORDER BY id")

# %%

# %%

# %%

# %%

# %%
cur = cur.execute("SELECT * FROM students ORDER BY id")

# %%

# %% [markdown]
#
# ### Shortcut-Methoden
#
# - Um das explizite Erzeugen von Cursor-Instanzen zu umgehen, kann man
#   die Shortcut-Methoden auf dem Connection-Objekt verwenden:

# %%

# %%

# %%

# %%

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
import tempfile

# %%
FD, DB = tempfile.mkstemp(suffix=".db")

# %%
con = sqlite3.connect(DB)

# %%
cur = con.cursor()

# %%
cur.execute("CREATE TABLE IF NOT EXISTS students(id INTEGER, name TEXT)")
cur.executemany("INSERT INTO students VALUES(?, ?)", STUDENTS)

# %%
con2 = sqlite3.connect(DB)

# %%
cur.execute("INSERT INTO students VALUES(2, 'Deborah Winter')")

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%
con = sqlite3.connect(DB)

# %%

# %%

# %%

# %%

# %%

# %%

# %% [markdown]
#
# ## Zugriff auf Metadaten
#
# - Erfolgt typischerweise mit DB-spezifischen Tabellen:

# %%

# %%

# %%

# %%

# %%

# %%

# %%
import os

# %%
try:
    os.unlink(DB)
except PermissionError as e:
    print(f"Could not delete the database file: {e}")
