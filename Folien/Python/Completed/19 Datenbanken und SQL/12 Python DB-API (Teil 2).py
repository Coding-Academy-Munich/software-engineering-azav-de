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


# %% [markdown]
#
# Wir stellen eine Verbindung zu einer In-Memory-Datenbank her und erzeugen
# eine Tabelle `students` mit einigen Daten:

# %%
con = sqlite3.connect(DB)

# %%
cur = con.cursor()

# %%
cur.execute("CREATE TABLE students(id INTEGER PRIMARY KEY, name TEXT)")
cur.executemany("INSERT INTO students VALUES(?, ?)", STUDENTS)
con.commit()

# %% [markdown]
#
# ## Erhalten aller Ergebnis-Zeilen mit `fetchall()`
#
# - Mit `fetchall()` können wir alle Zeilen eines Ergebnisses auf einmal
#   abrufen.
# - Das Ergebnis ist eine Liste von Tupeln, wobei jedes Tupel eine Zeile der
#   Ergebnismenge darstellt.

# %%
cur.execute("SELECT * FROM students ORDER BY id")

# %%
cur.fetchall()

# %% [markdown]
#
# Ein Cursor kann (pro Abfrage) nur einmal verwendet werden, um Ergebnisse zu
# bekommen:

# %%
cur.fetchall()

# %% [markdown]
#
# ## Erhalten eines einzelnen Ergebnisses mit `fetchone()`
#
# - Mit `fetchone()` können wir die Ergebnisse einzeln abrufen.
# - Nach dem letzten Ergebnis gibt `fetchone()` `None` zurück:

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

# %% [markdown]
#
# ## Erhalten von mehreren Ergebnissen mit `fetchmany()`
#
# - Mit `fetchmany(size)` können wir eine bestimmte Anzahl von Ergebnissen
#   abrufen.
# - Nach dem letzten Ergebnis gibt `fetchmany()` eine leere Liste zurück:

# %%
cur = cur.execute("SELECT * FROM students ORDER BY id")

# %%
cur.fetchmany(3)

# %% [markdown]
#
# ## Cursor und Iteration
#
# - Ein Cursor ist auch ein Iterator
# - Das bedeutet, dass wir über die Ergebnisse eines Cursors iterieren können,
#   ohne explizit `fetchone()` oder `fetchmany()` aufzurufen.

# %%
cur = cur.execute("SELECT * FROM students ORDER BY id")

# %%
for row in cur:
    print(row)

# %%
list(cur)


# %% [markdown]
#
# ### Shortcut-Methoden
#
# - Um das explizite Erzeugen von Cursor-Instanzen zu umgehen, kann man
#   Shortcut-Methoden auf dem Connection-Objekt verwenden:

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
# ## Mehrere Cursors und Verbindungen
#
# - Bisher haben wir einen einzelnen Cursor auf einer einzelnen Verbindung
#   verwendet
# - Wir können aber auch mehrere Cursors auf einer Verbindung oder mehrere
#   Verbindungen zur gleichen Datenbank verwenden
# - Diese beiden Fälle verhalten sich unterschiedlich

# %%
con.close()

# %% [markdown]
#
# ### Mehrere Cursors (gleiche Verbindung)
#
# - Eine Verbindung kann mehrere Cursors haben
# - Alle Cursors teilen sich den Zustand der Verbindung
# - Änderungen über einen Cursor sind sofort für andere Cursors sichtbar
#   (auch ohne Commit)

# %%
con = sqlite3.connect(":memory:")
cur = con.cursor()
cur.execute("CREATE TABLE students(id INTEGER PRIMARY KEY, name TEXT)")
cur.executemany("INSERT INTO students VALUES(?, ?)", STUDENTS)
con.commit()

# %% [markdown]
#
# Wir erzeugen zwei Cursors auf der gleichen Verbindung:

# %%
cur1 = con.cursor()
cur2 = con.cursor()

# %% [markdown]
#
# `cur2` fügt eine neue Zeile ein:

# %%
cur2.execute("INSERT INTO students VALUES(?, ?)", (1001, "Kay Garcia"))

# %% [markdown]
#
# `cur1` sieht die von `cur2` eingefügte Zeile sofort — obwohl wir noch kein
# Commit gemacht haben:

# %%
cur1.execute("SELECT * FROM students ORDER BY id").fetchall()

# %%
con.commit()
con.close()

# %% [markdown]
#
# ### Mehrere Verbindungen (gleiche Datenbank)
#
# - Jede Verbindung hat ihre eigene Transaktion
# - Änderungen einer Verbindung sind für andere erst nach einem Commit sichtbar
# - Bei `:memory:` erzeugt jede Verbindung eine eigene, unabhängige Datenbank
# - Daher verwenden wir für dieses Beispiel eine dateibasierte Datenbank

# %%
import tempfile

# %%
FD, DB = tempfile.mkstemp(suffix=".db")

# %% [markdown]
#
# Wir erzeugen eine Verbindung, erstellen eine Tabelle und fügen Daten ein:

# %%
con = sqlite3.connect(DB)
cur = con.cursor()
cur.execute("CREATE TABLE students(id INTEGER PRIMARY KEY, name TEXT)")
cur.executemany("INSERT INTO students VALUES(?, ?)", STUDENTS)
con.commit()

# %% [markdown]
#
# Wir öffnen eine zweite Verbindung zur gleichen Datenbank.
# Sie kann die bereits committeten Daten sehen:

# %%
con2 = sqlite3.connect(DB)

# %%
con2.execute("SELECT * FROM students ORDER BY id").fetchall()

# %% [markdown]
#
# Jetzt fügen wir über `con` eine neue Zeile ein, **ohne** zu committen:

# %%
con.execute("INSERT INTO students VALUES(?, ?)", (1001, "Kay Garcia"))

# %% [markdown]
#
# `con2` kann die neue Zeile **nicht** sehen, da `con` noch nicht committet hat:

# %%
con2.execute("SELECT * FROM students ORDER BY id").fetchall()

# %% [markdown]
#
# Nach dem Commit von `con` kann `con2` die neue Zeile sehen:

# %%
con.commit()

# %%
con2.execute("SELECT * FROM students ORDER BY id").fetchall()

# %%
con2.close()

# %% [markdown]
#
# ## Zugriff auf Metadaten
#
# - Erfolgt typischerweise mit DB-spezifischen Tabellen
# - In SQLite enthält `sqlite_master` Informationen über alle Tabellen und
#   Indizes
# - Andere Datenbanken haben ähnliche Mechanismen (z.B. `INFORMATION_SCHEMA`
#   in PostgreSQL/MySQL)

# %%
cursor = con.execute("SELECT name FROM sqlite_master")
cursor

# %%
cursor.fetchone()

# %%
cursor = con.execute("SELECT name FROM sqlite_master WHERE name='foo'")
cursor.fetchone() is None

# %%
con.execute("CREATE TABLE projects(proj_id INTEGER PRIMARY KEY, name TEXT, budget REAL)")

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
# ## Workshop: Produkte abfragen
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
cur.execute("CREATE TABLE products(id INTEGER PRIMARY KEY, name TEXT, price REAL)")
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
