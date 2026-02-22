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
@dataclass
class Account:
    id: int
    owner: str
    balance: float = 0.0

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
class AccountRepository:
    def __init__(self, connection: sqlite3.Connection):
        self.con = connection

    def create_table(self):
        with self.con:
            self.con.execute(
                """CREATE TABLE IF NOT EXISTS accounts(
                    id INTEGER PRIMARY KEY,
                    owner TEXT NOT NULL,
                    balance REAL DEFAULT 0.0
                )"""
            )

    def add(self, account: Account) -> Account:
        with self.con:
            cursor = self.con.execute(
                "INSERT INTO accounts(owner, balance) VALUES (?, ?)",
                (account.owner, account.balance),
            )
        return Account(cursor.lastrowid, account.owner, account.balance)

    def get_by_id(self, account_id: int) -> Account | None:
        row = self.con.execute(
            "SELECT * FROM accounts WHERE id = ?", (account_id,)
        ).fetchone()
        if row is None:
            return None
        return Account(*row)

    def get_all(self) -> list[Account]:
        rows = self.con.execute("SELECT * FROM accounts").fetchall()
        return [Account(*row) for row in rows]

    def update(self, account: Account):
        with self.con:
            self.con.execute(
                "UPDATE accounts SET owner = ?, balance = ? WHERE id = ?",
                (account.owner, account.balance, account.id),
            )


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
def deposit(repo: AccountRepository, account_id: int, amount: float):
    account = repo.get_by_id(account_id)
    account.balance += amount
    repo.update(account)

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
def withdraw(repo: AccountRepository, account_id: int, amount: float):
    account = repo.get_by_id(account_id)
    if account.balance < amount:
        raise ValueError(
            f"Insufficient balance: {account.balance} < {amount}"
        )
    account.balance -= amount
    repo.update(account)

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
def transfer(
    repo: AccountRepository, from_id: int, to_id: int, amount: float
):
    from_account = repo.get_by_id(from_id)
    to_account = repo.get_by_id(to_id)
    if from_account.balance < amount:
        raise ValueError(
            f"Insufficient balance: {from_account.balance} < {amount}"
        )
    from_account.balance -= amount
    to_account.balance += amount
    with repo.con:
        repo.con.execute(
            "UPDATE accounts SET balance = ? WHERE id = ?",
            (from_account.balance, from_account.id),
        )
        repo.con.execute(
            "UPDATE accounts SET balance = ? WHERE id = ?",
            (to_account.balance, to_account.id),
        )

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
