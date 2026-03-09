# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Phase 1: Musterlösung</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
#
# <div style="text-align:center;">Coding-Akademie München</div>
# <br/>


# %% [markdown]
#
# # Phase 1: Musterlösung

# %% [markdown]
#
# ## `category.py`

# %% [markdown]
#
# ```python
# from __future__ import annotations
#
# from enum import Enum
#
#
# class Category(Enum):
#     HOUSING = "Housing"
#     FOOD = "Food"
#     TRANSPORT = "Transport"
#     ENTERTAINMENT = "Entertainment"
#     HEALTH = "Health"
#     EDUCATION = "Education"
#     CLOTHING = "Clothing"
#     SALARY = "Salary"
#     FREELANCE = "Freelance"
#     INVESTMENT = "Investment"
#     OTHER = "Other"
#
#
# class TransactionType(Enum):
#     INCOME = "Income"
#     EXPENSE = "Expense"
# ```

# %% [markdown]
#
# ## `transaction.py`
#
# Die frozen Dataclass validiert Beschreibung, Betrag und Datumsformat.
# Properties berechnen den vorzeichenbehafteten Betrag.

# %% [markdown]
#
# ```python
# from __future__ import annotations
#
# import re
# from dataclasses import dataclass
#
# from pyfinanz.category import Category, TransactionType
#
# _DATE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}$")
#
#
# @dataclass(frozen=True)
# class Transaction:
#     description: str
#     amount: float
#     transaction_type: TransactionType
#     category: Category
#     date: str
#     tags: frozenset[str] = frozenset()
#
#     def __post_init__(self) -> None:
#         stripped = self.description.strip()
#         if not stripped:
#             raise ValueError("Description must not be empty.")
#         if stripped != self.description:
#             object.__setattr__(self, "description", stripped)
#         if self.amount <= 0:
#             raise ValueError("Amount must be positive.")
#         if not _DATE_PATTERN.match(self.date):
#             raise ValueError(
#                 f"Date must be in ISO format (YYYY-MM-DD), got '{self.date}'."
#             )
#
#     @property
#     def is_expense(self) -> bool:
#         return self.transaction_type == TransactionType.EXPENSE
#
#     @property
#     def is_income(self) -> bool:
#         return self.transaction_type == TransactionType.INCOME
#
#     @property
#     def signed_amount(self) -> float:
#         return -self.amount if self.is_expense else self.amount
#
#     def __str__(self) -> str:
#         sign = "-" if self.is_expense else "+"
#         return (
#             f"{self.date}  {self.description:<20s} "
#             f"{sign}{self.amount:>8.2f}  [{self.category.value}]"
#         )
# ```

# %% [markdown]
#
# ## `account.py`
#
# Das Account speichert Transaktionen in einer internen Liste. Properties
# berechnen Summen mit Generator-Ausdrücken.

# %% [markdown]
#
# ```python
# from __future__ import annotations
#
# from pyfinanz.category import Category, TransactionType
# from pyfinanz.transaction import Transaction
#
#
# class Account:
#     def __init__(self, name: str) -> None:
#         self.name = name
#         self._transactions: list[Transaction] = []
#
#     def add_transaction(self, t: Transaction) -> None:
#         self._transactions.append(t)
#
#     @property
#     def transactions(self) -> list[Transaction]:
#         return list(self._transactions)
#
#     @property
#     def balance(self) -> float:
#         return sum(t.signed_amount for t in self._transactions)
#
#     @property
#     def income_total(self) -> float:
#         return sum(t.amount for t in self._transactions if t.is_income)
#
#     @property
#     def expense_total(self) -> float:
#         return sum(t.amount for t in self._transactions if t.is_expense)
#
#     def filter_by_category(self, category: Category) -> list[Transaction]:
#         return [t for t in self._transactions if t.category == category]
#
#     def filter_by_type(self, t: TransactionType) -> list[Transaction]:
#         return [tx for tx in self._transactions if tx.transaction_type == t]
# ```

# %% [markdown]
#
# ## Beispieltests

# %% [markdown]
#
# ```python
# import pytest
# from pyfinanz.account import Account
# from pyfinanz.category import Category, TransactionType
# from pyfinanz.transaction import Transaction
#
#
# def test_transaction_signed_amount_expense():
#     tx = Transaction("Rent", 800, TransactionType.EXPENSE,
#                      Category.HOUSING, "2026-03-01")
#     assert tx.signed_amount == -800.0
#
#
# def test_transaction_signed_amount_income():
#     tx = Transaction("Salary", 3000, TransactionType.INCOME,
#                      Category.SALARY, "2026-03-01")
#     assert tx.signed_amount == 3000.0
#
#
# def test_transaction_rejects_empty_description():
#     with pytest.raises(ValueError):
#         Transaction("", 100, TransactionType.EXPENSE,
#                     Category.OTHER, "2026-01-01")
#
#
# def test_transaction_rejects_bad_date():
#     with pytest.raises(ValueError):
#         Transaction("Test", 100, TransactionType.EXPENSE,
#                     Category.OTHER, "not-a-date")
#
#
# @pytest.fixture
# def account():
#     acc = Account("Main")
#     acc.add_transaction(
#         Transaction("Salary", 3000, TransactionType.INCOME,
#                     Category.SALARY, "2026-03-01"))
#     acc.add_transaction(
#         Transaction("Rent", 800, TransactionType.EXPENSE,
#                     Category.HOUSING, "2026-03-02"))
#     acc.add_transaction(
#         Transaction("Groceries", 120, TransactionType.EXPENSE,
#                     Category.FOOD, "2026-03-05"))
#     return acc
#
#
# def test_balance(account):
#     assert account.balance == pytest.approx(2080.0)
#
#
# def test_income_total(account):
#     assert account.income_total == pytest.approx(3000.0)
#
#
# def test_expense_total(account):
#     assert account.expense_total == pytest.approx(920.0)
#
#
# def test_filter_by_category(account):
#     food = account.filter_by_category(Category.FOOD)
#     assert len(food) == 1
#     assert food[0].description == "Groceries"
# ```
