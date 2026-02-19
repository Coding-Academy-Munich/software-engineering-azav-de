# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>DB-API Live (Teil 2)</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# ## Zugriff auf Ergebnisse
#
# - `cursor.fetchall()` — alle Ergebnisse als Liste
# - `cursor.fetchone()` — ein einzelnes Ergebnis (oder `None`)
# - `cursor.fetchmany(n)` — die nächsten `n` Ergebnisse
# - Direkte Iteration über den Cursor

# %%
import sqlite3

# %%
DB = ":memory:"

# %%
MOVIES = [
    (1, "Inception", 2010),
    (2, "The Matrix", 1999),
    (3, "Pulp Fiction", 1994),
    (4, "The Shawshank Redemption", 1994),
    (5, "Interstellar", 2014),
    (6, "Back to the Future", 1985),
]

# %%
con = sqlite3.connect(DB)

# %%
cur = con.cursor()
cur.execute("CREATE TABLE movies(id INTEGER PRIMARY KEY, title TEXT, year INTEGER)")
cur.executemany("INSERT INTO movies VALUES(?, ?, ?)", MOVIES)
con.commit()

# %% [markdown]
#
# ### `fetchall()`

# %%
cur.execute("SELECT * FROM movies ORDER BY year")

# %%

# %% [markdown]
#
# ### Cursor-Ergebnisse werden verbraucht
#
# Was passiert, wenn wir `fetchall()` ein zweites Mal aufrufen?

# %%

# %% [markdown]
#
# ### `fetchone()`

# %%
cur.execute("SELECT * FROM movies ORDER BY year")

# %%

# %%

# %%

# %%

# %% [markdown]
#
# ### `fetchmany()`

# %%
cur.execute("SELECT * FROM movies ORDER BY year")

# %%

# %% [markdown]
#
# ### Shortcut-Methoden auf der Connection
#
# - Man kann `execute()` direkt auf der Connection aufrufen
# - Gibt einen Cursor zurück

# %%

# %%

# %%

# %%

# %% [markdown]
#
# ## Mehrere Verbindungen und Cursors
#
# - Mehrere Verbindungen zur selben Datenbank möglich
# - Mehrere Cursors auf einer Verbindung möglich
#   - Aber: Gleichzeitig aktive Transaktionen führen zu Timeouts
# - Cursors auf derselben Verbindung sind **nicht** isoliert

# %%
con.close()

# %% [markdown]
#
# Für mehrere Verbindungen brauchen wir eine dateibasierte Datenbank.
# Bei `:memory:` erzeugt jede Verbindung eine eigene Datenbank.

# %%
import tempfile

# %%
FD, DB = tempfile.mkstemp(suffix=".db")

# %%
con = sqlite3.connect(DB)

# %%
cur = con.cursor()
cur.execute("CREATE TABLE movies(id INTEGER PRIMARY KEY, title TEXT, year INTEGER)")
cur.executemany("INSERT INTO movies VALUES(?, ?, ?)", MOVIES)

# %%
con2 = sqlite3.connect(DB)

# %% [markdown]
#
# ### Primärschlüssel-Constraint
#
# Die Tabelle hat einen `PRIMARY KEY` — doppelte IDs sind nicht erlaubt:

# %%
try:
    cur.execute("INSERT INTO movies VALUES(1, 'Duplicate Movie', 2020)")
except sqlite3.IntegrityError as e:
    print(f"Error: {e}")

# %% [markdown]
#
# ### Sichtbarkeit von Transaktionen
#
# Vor dem Commit sieht die zweite Verbindung die Daten nicht:

# %%

# %% [markdown]
#
# Nach dem Commit sind die Daten sichtbar:

# %%

# %%

# %%

# %%
con = sqlite3.connect(DB)

# %% [markdown]
#
# ### Zwei Cursors, eine Verbindung
#
# Cursors auf derselben Verbindung teilen sich den Zustand:

# %%

# %%

# %%

# %%

# %% [markdown]
#
# `cur1` sieht die von `cur2` eingefügten Daten sofort:

# %%

# %%

# %% [markdown]
#
# ## Metadaten mit `sqlite_master`
#
# - `sqlite_master` enthält Informationen über alle Tabellen und Indizes
# - Andere Datenbanken: `INFORMATION_SCHEMA` (PostgreSQL, MySQL)

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
# ## Mini-Workshop: Restaurant-Speisekarte
#
# 1. Erstellen Sie eine In-Memory-Datenbank mit einer Tabelle `dishes`
#    (Spalten: `id` INTEGER, `name` TEXT, `price` REAL, `category` TEXT)
# 2. Fügen Sie mindestens 5 Gerichte mit `executemany()` ein
# 3. Verwenden Sie `fetchall()`, um alle Gerichte abzurufen
# 4. Verwenden Sie `fetchone()`, um das erste Gericht abzurufen
# 5. Verwenden Sie `fetchmany(3)`, um drei Gerichte abzurufen
# 6. Verwenden Sie `con.execute()`, um Gerichte unter 10.00 zu finden
# 7. Prüfen Sie mit `sqlite_master`, ob die Tabelle existiert

# %%
import sqlite3

# %%
DISHES = [
    (1, "Margherita Pizza", 8.50, "Main"),
    (2, "Caesar Salad", 6.90, "Starter"),
    (3, "Chocolate Cake", 5.50, "Dessert"),
    (4, "Grilled Salmon", 14.90, "Main"),
    (5, "Tomato Soup", 4.90, "Starter"),
    (6, "Ice Cream", 3.50, "Dessert"),
]

# %%

# %%

# %%

# %%
cur.execute("SELECT * FROM dishes ORDER BY price")

# %%

# %%
cur.execute("SELECT * FROM dishes ORDER BY price")

# %%

# %%

# %%

# %%
