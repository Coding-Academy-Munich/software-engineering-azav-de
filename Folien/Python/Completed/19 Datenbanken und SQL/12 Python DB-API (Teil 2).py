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
cur.fetchall()

# %% [markdown]
#
# Ein Cursor kann nur einmal verwendet werden, um Ergebnisse zu bekommen:

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
cursor = con.execute("SELECT * FROM students ORDER BY id")

# %%
cursor

# %%
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

# %% [markdown]
#
# Wir verwenden jetzt eine dateibasierte Datenbank, denn bei `:memory:` erzeugt
# jede Verbindung eine eigene, unabhängige Datenbank.

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

# %% [markdown]
#
# Da die Tabelle keinen Primärschlüssel hat, können wir eine weitere Zeile mit
# `id` 2 einfügen:

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

# %% [markdown]
#
# `cur1` sieht die von `cur2` eingefügten Daten, da beide Cursors zur gleichen
# Verbindung gehören:

# %%
cur1.execute("SELECT * FROM students").fetchall()

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
con.execute("CREATE TABLE projects(proj_id INTEGER, name TEXT, budget REAL)")

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
# ## Mini-Workshop: Produkte abfragen
#
# 1. Erstellen Sie eine In-Memory-Datenbank mit einer Tabelle `products`
#    (Spalten: `id` INTEGER, `name` TEXT, `price` REAL)
# 2. Fügen Sie mindestens 5 Produkte mit `executemany()` ein
# 3. Verwenden Sie `fetchall()`, um alle Produkte abzurufen
# 4. Verwenden Sie `fetchone()`, um das erste Produkt abzurufen
# 5. Verwenden Sie `fetchmany(2)`, um zwei Produkte abzurufen
# 6. Verwenden Sie `con.execute()` (Shortcut-Methode) für eine Abfrage
# 7. Prüfen Sie mit `sqlite_master`, ob die Tabelle `products` existiert

# %%
import sqlite3

# %%
PRODUCTS = [
    (1, "Laptop", 999.99),
    (2, "Mouse", 29.99),
    (3, "Keyboard", 59.99),
    (4, "Monitor", 349.99),
    (5, "Headphones", 79.99),
]

# %%
con = sqlite3.connect(":memory:")
cur = con.cursor()
cur.execute("CREATE TABLE products(id INTEGER, name TEXT, price REAL)")
cur.executemany("INSERT INTO products VALUES(?, ?, ?)", PRODUCTS)
con.commit()

# %%
cur.execute("SELECT * FROM products ORDER BY price")

# %%
cur.fetchall()

# %%
cur.execute("SELECT * FROM products ORDER BY price")

# %%
cur.fetchone()

# %%
cur.execute("SELECT * FROM products ORDER BY price")

# %%
cur.fetchmany(2)

# %%
con.execute("SELECT * FROM products WHERE price > 100").fetchall()

# %%
con.execute("SELECT name FROM sqlite_master").fetchone()

# %%
con.close()
