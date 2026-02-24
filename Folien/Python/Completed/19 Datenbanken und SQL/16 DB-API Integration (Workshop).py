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
# - Eine `BankSystem`-Klasse für die Geschäftslogik

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
# - `add(self, owner, balance) -> Account` - Konto einfügen, mit generierter ID zurückgeben
# - `get_by_id(self, account_id) -> Account | None` - Konto abfragen
# - `get_all(self) -> list[Account]` - Alle Konten abfragen
# - `update(self, account)` - Konto aktualisieren

# %% [markdown]
#
# *Hinweise:*
# - Verwenden Sie `with self.con:` für Transaktionssicherheit bei schreibenden Operationen
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

    def add(self, owner: str, balance: float = 0.0) -> Account:
        with self.con:
            cursor = self.con.execute(
                "INSERT INTO accounts(owner, balance) VALUES (?, ?)",
                (owner, balance),
            )
        return Account(cursor.lastrowid, owner, balance)

    def get_by_id(self, account_id: int) -> Account | None:
        row = self.con.execute(
            "SELECT * FROM accounts WHERE id = ?", (account_id,)
        ).fetchone()
        if row is None:
            return None
        return Account(*row)

    def get_all(self) -> list[Account]:
        rows = self.con.execute("SELECT * FROM accounts")
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
alice = repo.add("Alice", 1000.0)
bob = repo.add("Bob", 500.0)

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
# ### Schritt 3: `BankSystem` mit Einzahlung und Abhebung
#
# Implementieren Sie eine `BankSystem`-Klasse mit:
# - `__init__(self, repo)` - Repository speichern
# - `deposit(self, account_id, amount)` - Konto abfragen, Kontostand erhöhen,
#   aktualisieren
# - `withdraw(self, account_id, amount)` - Konto abfragen, prüfen ob genug Geld
#   vorhanden ist, Kontostand verringern und aktualisieren; `ValueError` auslösen
#   wenn nicht genug Geld vorhanden ist

# %%
class BankSystem:
    def __init__(self, repo: AccountRepository):
        self.repo = repo

    def deposit(self, account_id: int, amount: float):
        account = self.repo.get_by_id(account_id)
        account.balance += amount
        self.repo.update(account)

    def withdraw(self, account_id: int, amount: float):
        account = self.repo.get_by_id(account_id)
        if account.balance < amount:
            raise ValueError(
                f"Insufficient balance: {account.balance} < {amount}"
            )
        account.balance -= amount
        self.repo.update(account)

# %%
bank = BankSystem(repo)

# %%
bank.deposit(alice.id, 200.0)
assert repo.get_by_id(alice.id).balance == 1200.0

# %%
bank.deposit(bob.id, 50.0)
assert repo.get_by_id(bob.id).balance == 550.0

# %%
bank.withdraw(alice.id, 200.0)
assert repo.get_by_id(alice.id).balance == 1000.0

# %%
try:
    bank.withdraw(bob.id, 9999.0)
except ValueError as e:
    print(e)

# %%
assert repo.get_by_id(bob.id).balance == 550.0


# %% [markdown]
#
# ### Schritt 4: Überweisung
#
# Erweitern Sie die `BankSystem`-Klasse um eine Methode
# `transfer(self, from_id, to_id, amount)`:
# - Abhebung vom Quellkonto und Einzahlung auf das Zielkonto

# %%
class BankSystem:
    def __init__(self, repo: AccountRepository):
        self.repo = repo

    def deposit(self, account_id: int, amount: float):
        account = self.repo.get_by_id(account_id)
        account.balance += amount
        self.repo.update(account)

    def withdraw(self, account_id: int, amount: float):
        account = self.repo.get_by_id(account_id)
        if account.balance < amount:
            raise ValueError(
                f"Insufficient balance: {account.balance} < {amount}"
            )
        account.balance -= amount
        self.repo.update(account)

    def transfer(self, from_id: int, to_id: int, amount: float):
        self.withdraw(from_id, amount)
        self.deposit(to_id, amount)

# %%
bank = BankSystem(repo)

# %%
bank.transfer(alice.id, bob.id, 300.0)
assert repo.get_by_id(alice.id).balance == 700.0
assert repo.get_by_id(bob.id).balance == 850.0

# %%
try:
    bank.transfer(alice.id, bob.id, 9999.0)
except ValueError as e:
    print(e)

# %%
assert repo.get_by_id(alice.id).balance == 700.0
assert repo.get_by_id(bob.id).balance == 850.0

# %% [markdown]
#
# ### Diskussion: Transaktionssicherheit
#
# Unsere `transfer`-Methode ruft `withdraw` und `deposit` nacheinander auf.
# Jede dieser Methoden führt ein eigenes `UPDATE` in einer eigenen Transaktion durch.
#
# **Problem:** Wenn das Programm zwischen den beiden Aufrufen abstürzt, ist das
# Geld vom ersten Konto abgebucht, aber nicht auf dem zweiten Konto angekommen.
#
# In einer echten Anwendung muss eine Überweisung **atomar** sein — entweder
# beide Änderungen werden durchgeführt oder keine.

# %% [markdown]
#
# ### Lösung: Atomare Überweisung im Repository
#
# - `transfer`-Methode im Repository: beide Updates in einer Transaktion
# - `BankSystem` validiert und delegiert an das Repository

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

    def add(self, owner: str, balance: float = 0.0) -> Account:
        with self.con:
            cursor = self.con.execute(
                "INSERT INTO accounts(owner, balance) VALUES (?, ?)",
                (owner, balance),
            )
        return Account(cursor.lastrowid, owner, balance)

    def get_by_id(self, account_id: int) -> Account | None:
        row = self.con.execute(
            "SELECT * FROM accounts WHERE id = ?", (account_id,)
        ).fetchone()
        if row is None:
            return None
        return Account(*row)

    def get_all(self) -> list[Account]:
        rows = self.con.execute("SELECT * FROM accounts")
        return [Account(*row) for row in rows]

    def update(self, account: Account):
        with self.con:
            self.con.execute(
                "UPDATE accounts SET owner = ?, balance = ? WHERE id = ?",
                (account.owner, account.balance, account.id),
            )

    def transfer(self, from_id: int, to_id: int, amount: float):
        with self.con:
            self.con.execute(
                "UPDATE accounts SET balance = balance - ? WHERE id = ?",
                (amount, from_id),
            )
            self.con.execute(
                "UPDATE accounts SET balance = balance + ? WHERE id = ?",
                (amount, to_id),
            )

# %%
class BankSystem:
    def __init__(self, repo: AccountRepository):
        self.repo = repo

    def deposit(self, account_id: int, amount: float):
        account = self.repo.get_by_id(account_id)
        account.balance += amount
        self.repo.update(account)

    def withdraw(self, account_id: int, amount: float):
        account = self.repo.get_by_id(account_id)
        if account.balance < amount:
            raise ValueError(
                f"Insufficient balance: {account.balance} < {amount}"
            )
        account.balance -= amount
        self.repo.update(account)

    def transfer(self, from_id: int, to_id: int, amount: float):
        from_account = self.repo.get_by_id(from_id)
        if from_account.balance < amount:
            raise ValueError(
                f"Insufficient balance: {from_account.balance} < {amount}"
            )
        self.repo.transfer(from_id, to_id, amount)

# %%
con2 = sqlite3.connect(":memory:")
repo2 = AccountRepository(con2)
repo2.create_table()
alice2 = repo2.add("Alice", 1000.0)
bob2 = repo2.add("Bob", 500.0)
bank2 = BankSystem(repo2)

# %%
bank2.transfer(alice2.id, bob2.id, 300.0)
assert repo2.get_by_id(alice2.id).balance == 700.0
assert repo2.get_by_id(bob2.id).balance == 800.0

# %%
try:
    bank2.transfer(alice2.id, bob2.id, 9999.0)
except ValueError as e:
    print(e)

# %%
assert repo2.get_by_id(alice2.id).balance == 700.0
assert repo2.get_by_id(bob2.id).balance == 800.0
