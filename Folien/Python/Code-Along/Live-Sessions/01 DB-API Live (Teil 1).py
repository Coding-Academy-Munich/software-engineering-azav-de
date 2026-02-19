# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>DB-API Live (Teil 1)</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# # Datenbanken in Python: DB-API 2.0
#
# - Python bietet ein einheitliches Interface für SQL-Datenbanken
# - Definiert in [PEP-249](https://peps.python.org/pep-0249/)
# - Wir nutzen `sqlite3` — in Python eingebaut
# - Andere Datenbanken (PostgreSQL, MySQL) funktionieren sehr ähnlich

# %% [markdown]
#
# ## Die zwei wichtigsten Objekte
#
# - **Connection** — die Verbindung zur Datenbank
# - **Cursor** — führt SQL aus und liefert Ergebnisse
# - Analogie: Connection = Telefonleitung, Cursor = das Gespräch

# %% [markdown]
#
# ## Was ist eine Transaktion?
#
# - Mehrere Datenbankoperationen werden als Einheit zusammengefasst
# - Entweder gelingen alle — oder keine wird übernommen
# - Beispiel: Online-Bestellung
#   - Bestellung wird angelegt, Zahlung belastet, Lagerbestand reduziert
#   - Alle drei Schritte müssen gemeinsam gelingen oder gemeinsam fehlschlagen
#   - Ohne Transaktionen: Ein Fehler mittendrin könnte zu bezahlten, aber nie
#     versendeten Bestellungen führen

# %% [markdown]
#
# ## Commit und Rollback
#
# - **Commit**: Alle Änderungen der Transaktion werden dauerhaft gespeichert
# - **Rollback**: Alle Änderungen der Transaktion werden verworfen
# - Ablauf:
#   - Operationen durchführen
#   - Erfolgreich → Commit
#   - Fehler → Rollback
# - Änderungen sind für andere erst nach einem Commit sichtbar

# %% [markdown]
#
# ## Verbindung erzeugen
#
# - `sqlite3.connect()` erzeugt eine `Connection`
# - `":memory:"` für eine temporäre In-Memory-Datenbank
# - Alternativ: Dateipfad für persistente Datenbank, z.B. `"movies.db"`

# %%
import sqlite3

# %%
DB = ":memory:"

# %%

# %%

# %%

# %% [markdown]
#
# ## Cursor erzeugen
#
# - Die meisten Operationen laufen über den Cursor
# - Commit und Rollback erfolgen auf der Connection

# %%

# %% [markdown]
#
# ## SQL ausführen
#
# - `cursor.execute()` — eine SQL-Anweisung ausführen
#   - Parameter werden mit `?` als Platzhalter übergeben
# - `cursor.executemany()` — gleiche Anweisung mit vielen Datensätzen
# - `cursor.executescript()` — mehrere SQL-Anweisungen auf einmal

# %%

# %%

# %% [markdown]
#
# ### Tabelle erstellen

# %%

# %%

# %% [markdown]
#
# ### Daten einfügen mit Parametern
#
# Immer `?`-Platzhalter verwenden, nie String-Formatierung:

# %%

# %%

# %%

# %%

# %% [markdown]
#
# ### Mehrere Zeilen einfügen mit `executemany()`
#
# Beachten Sie den zweiten Eintrag — wir verwenden ihn später, um SQL-Injection
# zu demonstrieren:

# %%
MOVIES = [
    (3, "Pulp Fiction", 1994),
    (4, "', 2000); DROP TABLE movies; --", 2000),
    (5, "The Shawshank Redemption", 1994),
    (6, "Interstellar", 2014),
    (7, "Back to the Future", 1985),
]

# %%

# %%

# %%

# %% [markdown]
#
# ### SQL-Injection vermeiden
#
# Was passiert, wenn wir SQL-Strings mit f-Strings zusammenbauen?
#
# Film Nr. 4 hat einen verdächtigen Titel...

# %% [markdown]
#
# Wir setzen die Tabelle zurück, um den Angriff zu demonstrieren:

# %%
cur.executescript("DROP TABLE IF EXISTS movies")
cur.execute("CREATE TABLE movies(id INTEGER PRIMARY KEY, title TEXT, year INTEGER)")
cur.execute("INSERT INTO movies VALUES(?, ?, ?)", (1, "Inception", 2010))
cur.execute("INSERT INTO movies VALUES(?, ?, ?)", (2, "The Matrix", 1999))
con.commit()

# %% [markdown]
#
# Dieser Code verwendet String-Formatierung statt Parametersubstitution:

# %%
try:
    for m in MOVIES:
        cur.executescript(f"INSERT INTO movies VALUES({m[0]}, '{m[1]}', {m[2]})")
except sqlite3.OperationalError as e:
    print(f"Error: {e}")

# %% [markdown]
#
# Die Tabelle wurde gelöscht!

# %%
try:
    cur.execute("SELECT * FROM movies")
except sqlite3.OperationalError as e:
    print(f"Error: {e}")

# %% [markdown]
#
# Wir stellen die Tabelle wieder her:

# %%
cur.execute("CREATE TABLE movies(id INTEGER PRIMARY KEY, title TEXT, year INTEGER)")
cur.execute("INSERT INTO movies VALUES(?, ?, ?)", (1, "Inception", 2010))
cur.execute("INSERT INTO movies VALUES(?, ?, ?)", (2, "The Matrix", 1999))
cur.executemany("INSERT INTO movies VALUES(?, ?, ?)", MOVIES)
con.commit()

# %%

# %% [markdown]
#
# ### `executescript()`: Mehrere Anweisungen ausführen

# %%

# %%

# %%

# %% [markdown]
#
# ## Verbindung schließen

# %%

# %% [markdown]
#
# ## Workshop: Videospiel-Sammlung
#
# Erstellen Sie ein Programm, das folgende Schritte ausführt:
#
# 1. Erzeugen Sie eine Verbindung zu einer In-Memory-Datenbank
# 2. Erstellen Sie eine Tabelle `games` mit den Spalten `id` (INTEGER),
#    `title` (TEXT) und `platform` (TEXT)
# 3. Fügen Sie ein Spiel mit `execute()` und `?`-Parametern ein
# 4. Fügen Sie mehrere Spiele mit `executemany()` ein
# 5. Geben Sie alle Spiele sortiert nach Titel aus
# 6. Schließen Sie die Verbindung

# %%
import sqlite3

# %%

# %%

# %%

# %%

# %%
MORE_GAMES = [
    (2, "The Legend of Zelda", "Nintendo Switch"),
    (3, "God of War", "PlayStation"),
    (4, "Minecraft", "PC"),
]

# %%

# %%

# %%

# %%
