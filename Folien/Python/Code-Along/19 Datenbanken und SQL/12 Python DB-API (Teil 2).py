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
cur.execute("CREATE TABLE IF NOT EXISTS students(id INTEGER PRIMARY KEY, name TEXT)")
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

# %% [markdown]
#
# Mit `fetchone()` können wir die Ergebnisse einzeln abrufen. Nach dem letzten
# Ergebnis gibt `fetchone()` `None` zurück:

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
cur.execute("CREATE TABLE IF NOT EXISTS students(id INTEGER PRIMARY KEY, name TEXT)")
cur.executemany("INSERT INTO students VALUES(?, ?)", STUDENTS)

# %%
con2 = sqlite3.connect(DB)

# %% [markdown]
#
# Da die Tabelle einen Primärschlüssel hat, können wir keine weitere Zeile mit
# `id` 2 einfügen:

# %%
try:
    cur.execute("INSERT INTO students VALUES(2, 'Deborah Winter')")
except sqlite3.IntegrityError as e:
    print(f"Error: {e}")

# %%

# %% [markdown]
#
# Nach dem Commit von `con` kann `con2` die eingefügten Daten sehen:

# %%

# %%

# %%

# %%

# %%

# %% [markdown]
#
# Die zweite Verbindung sieht die gleichen Daten:

# %%

# %%

# %%
con = sqlite3.connect(DB)

# %% [markdown]
#
# Wir erzeugen zwei Cursors auf der gleichen Verbindung und beobachten, dass
# sie nicht voneinander isoliert sind:

# %%

# %%

# %%

# %%

# %%

# %% [markdown]
#
# `cur1` sieht die von `cur2` eingefügten Daten, da beide Cursors zur gleichen
# Verbindung gehören:

# %%

# %%

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

# %%

# %%

# %%
cur.execute("SELECT * FROM products ORDER BY price")

# %%

# %%
cur.execute("SELECT * FROM products ORDER BY price")

# %%

# %%

# %%

# %%
