# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Phase 4: Musterlösung</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
#
# <div style="text-align:center;">Coding-Akademie München</div>
# <br/>


# %% [markdown]
#
# # Phase 4: Musterlösung

# %% [markdown]
#
# ## Vollständige `storage.py`
#
# Diese Datei enthält die abstrakte Schnittstelle `FinanceStore`, beide
# Implementierungen (`InMemoryStore` und `SqliteStore`) sowie die
# JSON-Funktionen aus Phase 3.

# %% [markdown]
#
# ```python
# from __future__ import annotations
#
# import json
# import sqlite3
# from abc import ABC, abstractmethod
# from pathlib import Path
#
# from pyfinanz.account import Account
# from pyfinanz.category import Category, TransactionType
# from pyfinanz.transaction import Transaction
#
#
# class FinanceStore(ABC):
#     @abstractmethod
#     def add_transaction(self, account_name: str, transaction: Transaction) -> None: ...
#
#     @abstractmethod
#     def get_transactions(self, account_name: str) -> list[Transaction]: ...
#
#     @abstractmethod
#     def get_account_names(self) -> list[str]: ...
#
#     @abstractmethod
#     def delete_transaction(
#         self, account_name: str, transaction: Transaction
#     ) -> None: ...
#
#     @abstractmethod
#     def clear_account(self, account_name: str) -> None: ...
#
#
# class InMemoryStore(FinanceStore):
#     def __init__(self) -> None:
#         self._data: dict[str, list[Transaction]] = {}
#
#     def add_transaction(self, account_name: str, transaction: Transaction) -> None:
#         if account_name not in self._data:
#             self._data[account_name] = []
#         self._data[account_name].append(transaction)
#
#     def get_transactions(self, account_name: str) -> list[Transaction]:
#         return list(self._data.get(account_name, []))
#
#     def get_account_names(self) -> list[str]:
#         return list(self._data.keys())
#
#     def delete_transaction(
#         self, account_name: str, transaction: Transaction
#     ) -> None:
#         txs = self._data.get(account_name, [])
#         try:
#             txs.remove(transaction)
#         except ValueError:
#             raise ValueError("Transaction not found.")
#
#     def clear_account(self, account_name: str) -> None:
#         self._data.pop(account_name, None)
#
#
# class SqliteStore(FinanceStore):
#     def __init__(self, db_path: str | Path) -> None:
#         self.connection = sqlite3.connect(str(db_path))
#         self._create_tables()
#
#     def _create_tables(self) -> None:
#         cursor = self.connection.cursor()
#         cursor.execute(
#             """CREATE TABLE IF NOT EXISTS accounts (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 name TEXT UNIQUE NOT NULL
#             )"""
#         )
#         cursor.execute(
#             """CREATE TABLE IF NOT EXISTS transactions (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 account_id INTEGER NOT NULL,
#                 description TEXT NOT NULL,
#                 amount REAL NOT NULL,
#                 transaction_type TEXT NOT NULL,
#                 category TEXT NOT NULL,
#                 date TEXT NOT NULL,
#                 FOREIGN KEY (account_id) REFERENCES accounts(id)
#             )"""
#         )
#         cursor.execute(
#             """CREATE TABLE IF NOT EXISTS transaction_tags (
#                 transaction_id INTEGER NOT NULL,
#                 tag TEXT NOT NULL,
#                 PRIMARY KEY (transaction_id, tag),
#                 FOREIGN KEY (transaction_id) REFERENCES transactions(id)
#             )"""
#         )
#         self.connection.commit()
#
#     def _get_or_create_account(self, name: str) -> int:
#         cursor = self.connection.cursor()
#         cursor.execute("SELECT id FROM accounts WHERE name = ?", (name,))
#         row = cursor.fetchone()
#         if row is not None:
#             return row[0]
#         cursor.execute("INSERT INTO accounts (name) VALUES (?)", (name,))
#         self.connection.commit()
#         return cursor.lastrowid
#
#     def add_transaction(self, account_name: str, transaction: Transaction) -> None:
#         account_id = self._get_or_create_account(account_name)
#         cursor = self.connection.cursor()
#         cursor.execute(
#             """INSERT INTO transactions
#                (account_id, description, amount, transaction_type, category, date)
#                VALUES (?, ?, ?, ?, ?, ?)""",
#             (
#                 account_id,
#                 transaction.description,
#                 transaction.amount,
#                 transaction.transaction_type.value,
#                 transaction.category.value,
#                 transaction.date,
#             ),
#         )
#         tx_id = cursor.lastrowid
#         for tag in transaction.tags:
#             cursor.execute(
#                 "INSERT INTO transaction_tags (transaction_id, tag) VALUES (?, ?)",
#                 (tx_id, tag),
#             )
#         self.connection.commit()
#
#     def get_transactions(self, account_name: str) -> list[Transaction]:
#         cursor = self.connection.cursor()
#         cursor.execute("SELECT id FROM accounts WHERE name = ?", (account_name,))
#         row = cursor.fetchone()
#         if row is None:
#             return []
#         account_id = row[0]
#
#         cursor.execute(
#             """SELECT id, description, amount, transaction_type, category, date
#                FROM transactions WHERE account_id = ?""",
#             (account_id,),
#         )
#         rows = cursor.fetchall()
#
#         transactions: list[Transaction] = []
#         for tx_row in rows:
#             tx_id, description, amount, tx_type, category, date = tx_row
#             cursor.execute(
#                 "SELECT tag FROM transaction_tags WHERE transaction_id = ?",
#                 (tx_id,),
#             )
#             tags = frozenset(tag_row[0] for tag_row in cursor.fetchall())
#             transactions.append(
#                 Transaction(
#                     description=description,
#                     amount=amount,
#                     transaction_type=TransactionType(tx_type),
#                     category=Category(category),
#                     date=date,
#                     tags=tags,
#                 )
#             )
#         return transactions
#
#     def get_account_names(self) -> list[str]:
#         cursor = self.connection.cursor()
#         cursor.execute("SELECT name FROM accounts")
#         return [row[0] for row in cursor.fetchall()]
#
#     def delete_transaction(
#         self, account_name: str, transaction: Transaction
#     ) -> None:
#         cursor = self.connection.cursor()
#         cursor.execute("SELECT id FROM accounts WHERE name = ?", (account_name,))
#         row = cursor.fetchone()
#         if row is None:
#             raise ValueError("Transaction not found.")
#         account_id = row[0]
#
#         cursor.execute(
#             """SELECT id FROM transactions
#                WHERE account_id = ? AND description = ? AND amount = ?
#                  AND transaction_type = ? AND category = ? AND date = ?""",
#             (
#                 account_id,
#                 transaction.description,
#                 transaction.amount,
#                 transaction.transaction_type.value,
#                 transaction.category.value,
#                 transaction.date,
#             ),
#         )
#         tx_row = cursor.fetchone()
#         if tx_row is None:
#             raise ValueError("Transaction not found.")
#         tx_id = tx_row[0]
#
#         cursor.execute(
#             "DELETE FROM transaction_tags WHERE transaction_id = ?", (tx_id,)
#         )
#         cursor.execute("DELETE FROM transactions WHERE id = ?", (tx_id,))
#         self.connection.commit()
#
#     def clear_account(self, account_name: str) -> None:
#         cursor = self.connection.cursor()
#         cursor.execute("SELECT id FROM accounts WHERE name = ?", (account_name,))
#         row = cursor.fetchone()
#         if row is None:
#             return
#         account_id = row[0]
#
#         cursor.execute(
#             "SELECT id FROM transactions WHERE account_id = ?", (account_id,)
#         )
#         tx_ids = [r[0] for r in cursor.fetchall()]
#         for tx_id in tx_ids:
#             cursor.execute(
#                 "DELETE FROM transaction_tags WHERE transaction_id = ?", (tx_id,)
#             )
#         cursor.execute(
#             "DELETE FROM transactions WHERE account_id = ?", (account_id,)
#         )
#         cursor.execute("DELETE FROM accounts WHERE id = ?", (account_id,))
#         self.connection.commit()
#
#
# def save_account_to_json(account: Account, path: Path) -> None:
#     data = {
#         "name": account.name,
#         "transactions": [
#             {
#                 "description": tx.description,
#                 "amount": tx.amount,
#                 "transaction_type": tx.transaction_type.value,
#                 "category": tx.category.value,
#                 "date": tx.date,
#                 "tags": sorted(tx.tags),
#             }
#             for tx in account.transactions
#         ],
#     }
#     path.write_text(json.dumps(data, indent=2), encoding="utf-8")
#
#
# def load_account_from_json(path: Path) -> Account:
#     data = json.loads(path.read_text(encoding="utf-8"))
#     account = Account(name=data["name"])
#     for tx_data in data["transactions"]:
#         account.add_transaction(
#             Transaction(
#                 description=tx_data["description"],
#                 amount=tx_data["amount"],
#                 transaction_type=TransactionType(tx_data["transaction_type"]),
#                 category=Category(tx_data["category"]),
#                 date=tx_data["date"],
#                 tags=frozenset(tx_data.get("tags", [])),
#             )
#         )
#     return account
# ```

# %% [markdown]
#
# ## Beispieltests mit parametrisierter Fixture

# %% [markdown]
#
# ```python
# import pytest
# from pyfinanz.category import Category, TransactionType
# from pyfinanz.storage import InMemoryStore, SqliteStore
# from pyfinanz.transaction import Transaction
#
#
# @pytest.fixture(params=["memory", "sqlite"])
# def store(request):
#     if request.param == "memory":
#         return InMemoryStore()
#     return SqliteStore(":memory:")
#
#
# @pytest.fixture
# def sample_tx():
#     return Transaction(
#         description="Groceries",
#         amount=45.50,
#         transaction_type=TransactionType.EXPENSE,
#         category=Category.FOOD,
#         date="2026-03-01",
#         tags=frozenset({"weekly", "essential"}),
#     )
#
#
# def test_add_and_get(store, sample_tx):
#     store.add_transaction("Main", sample_tx)
#     txs = store.get_transactions("Main")
#     assert len(txs) == 1
#     assert txs[0].description == "Groceries"
#     assert txs[0].amount == 45.50
#
#
# def test_tags_survive_round_trip(store, sample_tx):
#     store.add_transaction("Main", sample_tx)
#     txs = store.get_transactions("Main")
#     assert txs[0].tags == frozenset({"weekly", "essential"})
#
#
# def test_multiple_accounts_separated(store, sample_tx):
#     other = Transaction("Salary", 3000.0, TransactionType.INCOME,
#                         Category.SALARY, "2026-03-01")
#     store.add_transaction("Checking", sample_tx)
#     store.add_transaction("Savings", other)
#     assert len(store.get_transactions("Checking")) == 1
#     assert len(store.get_transactions("Savings")) == 1
#
#
# def test_delete_transaction(store, sample_tx):
#     other = Transaction("Salary", 3000.0, TransactionType.INCOME,
#                         Category.SALARY, "2026-03-01")
#     store.add_transaction("Main", sample_tx)
#     store.add_transaction("Main", other)
#     store.delete_transaction("Main", sample_tx)
#     txs = store.get_transactions("Main")
#     assert len(txs) == 1
#     assert txs[0].description == "Salary"
#
#
# def test_clear_account(store, sample_tx):
#     store.add_transaction("Main", sample_tx)
#     store.clear_account("Main")
#     assert store.get_transactions("Main") == []
#     assert "Main" not in store.get_account_names()
#
#
# def test_nonexistent_account_returns_empty(store):
#     assert store.get_transactions("Nonexistent") == []
# ```
