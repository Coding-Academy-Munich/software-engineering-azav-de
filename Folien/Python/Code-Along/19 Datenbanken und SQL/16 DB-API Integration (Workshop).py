# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>DB-API Integration (Workshop)</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# ## Workshop: Bankkonto-System
#
# Implementieren Sie ein einfaches Bankkonto-System mit dem Repository Pattern.
#
# Ein Konto hat folgende Daten:
#
# - Konto-ID
# - Inhaber (Name)
# - Kontostand
#
# Verwenden Sie:
# - Eine `Account`-Dataclass als Domänenobjekt
# - Ein `AccountRepository` für alle Datenbankoperationen
# - Funktionen für Einzahlung, Abhebung und Überweisung

# %%
import sqlite3
from dataclasses import dataclass

# %% [markdown]
#
# ### Schritt 1: `Account`-Dataclass
#
# Definieren Sie eine Dataclass `Account` mit:
# - `id: int`
# - `owner: str`
# - `balance: float` (Standardwert `0.0`)

# %%

# %%
assert Account(1, "Alice", 100.0).owner == "Alice"
assert Account(2, "Bob").balance == 0.0

# %% [markdown]
#
# ### Schritt 2: `AccountRepository`
#
# Implementieren Sie `AccountRepository` mit:
# - `__init__(self, connection)` - Verbindung speichern
# - `create_table(self)` - Tabelle `accounts` anlegen
# - `add(self, account) -> Account` - Konto einfügen, mit generierter ID zurückgeben
# - `get_by_id(self, account_id) -> Account | None` - Konto abfragen
# - `get_all(self) -> list[Account]` - Alle Konten abfragen
# - `update(self, account)` - Kontostand aktualisieren

# %% [markdown]
#
# *Hinweise:*
# - Verwenden Sie `with self.con:` für Transaktionssicherheit
# - Die Tabelle sollte die Spalten `id`, `owner` und `balance` haben
# - Bei `add()`: Verwenden Sie `cursor.lastrowid` für die generierte ID
# - Bei `update()`: Aktualisieren Sie `owner` und `balance` anhand der `id`

# %%

# %%
con = sqlite3.connect(":memory:")
repo = AccountRepository(con)
repo.create_table()

# %%
alice = repo.add(Account(0, "Alice", 1000.0))
bob = repo.add(Account(0, "Bob", 500.0))

# %%
assert alice.id == 1
assert alice.owner == "Alice"
assert alice.balance == 1000.0

# %%
assert bob.id == 2
assert repo.get_by_id(2).owner == "Bob"

# %%
assert repo.get_by_id(99) is None

# %%
assert len(repo.get_all()) == 2

# %% [markdown]
#
# ### Schritt 3: Einzahlung
#
# Schreiben Sie eine Funktion `deposit(repo, account_id, amount)`:
# - Konto abfragen
# - Kontostand erhöhen
# - Konto aktualisieren

# %%

# %%
deposit(repo, alice.id, 200.0)
assert repo.get_by_id(alice.id).balance == 1200.0

# %%
deposit(repo, bob.id, 50.0)
assert repo.get_by_id(bob.id).balance == 550.0

# %% [markdown]
#
# ### Schritt 4: Abhebung
#
# Schreiben Sie eine Funktion `withdraw(repo, account_id, amount)`:
# - Konto abfragen
# - Prüfen, ob genug Geld vorhanden ist
# - Wenn ja: Kontostand verringern und aktualisieren
# - Wenn nein: `ValueError` auslösen

# %%

# %%
withdraw(repo, alice.id, 200.0)
assert repo.get_by_id(alice.id).balance == 1000.0

# %%
try:
    withdraw(repo, bob.id, 9999.0)
except ValueError as e:
    print(e)

# %%
assert repo.get_by_id(bob.id).balance == 550.0

# %% [markdown]
#
# ### Schritt 5: Überweisung
#
# Schreiben Sie eine Funktion `transfer(repo, from_id, to_id, amount)`:
# - Verwenden Sie `with repo.con:` für Transaktionssicherheit
# - Abhebung und Einzahlung als eine Transaktion
#
# *Hinweis:* Da `withdraw` und `deposit` intern `with self.con:` verwenden,
# müssen Sie hier die Operationen direkt auf dem Konto ausführen, damit alles
# in einer einzigen Transaktion abläuft.

# %%

# %%
transfer(repo, alice.id, bob.id, 300.0)
assert repo.get_by_id(alice.id).balance == 700.0
assert repo.get_by_id(bob.id).balance == 850.0

# %%
try:
    transfer(repo, alice.id, bob.id, 9999.0)
except ValueError as e:
    print(e)

# %%
assert repo.get_by_id(alice.id).balance == 700.0
assert repo.get_by_id(bob.id).balance == 850.0

# %%
