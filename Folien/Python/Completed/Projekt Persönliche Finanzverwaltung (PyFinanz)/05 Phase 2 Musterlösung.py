# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Phase 2: Musterlösung</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
#
# <div style="text-align:center;">Coding-Akademie München</div>
# <br/>


# %% [markdown]
#
# # Phase 2: Musterlösung

# %% [markdown]
#
# ## Erweiterte `account.py`

# %% [markdown]
#
# ```python
# from __future__ import annotations
#
# import re
# from collections import defaultdict
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
#
#     def filter_by_date_range(self, start: str, end: str) -> list[Transaction]:
#         return [tx for tx in self._transactions if start <= tx.date <= end]
#
#     def filter_by_month(self, month: str) -> list[Transaction]:
#         return [tx for tx in self._transactions if tx.date[:7] == month]
#
#     def search(self, query: str) -> list[Transaction]:
#         pattern = re.compile(query, re.IGNORECASE)
#         return [tx for tx in self._transactions if pattern.search(tx.description)]
#
#     def filter_by_tags(self, tags: set[str]) -> list[Transaction]:
#         return [tx for tx in self._transactions if tx.tags & tags]
#
#     def monthly_summary(self) -> dict[str, dict[str, float]]:
#         result: dict[str, dict[str, float]] = {}
#         for tx in self._transactions:
#             month = tx.date[:7]
#             if month not in result:
#                 result[month] = {"income": 0.0, "expenses": 0.0, "net": 0.0}
#             if tx.is_income:
#                 result[month]["income"] += tx.amount
#             else:
#                 result[month]["expenses"] += tx.amount
#             result[month]["net"] += tx.signed_amount
#         return result
#
#     def category_breakdown(self) -> dict[Category, float]:
#         totals: dict[Category, float] = defaultdict(float)
#         for tx in self._transactions:
#             if tx.is_expense:
#                 totals[tx.category] += tx.amount
#         return dict(sorted(totals.items(), key=lambda item: item[1], reverse=True))
#
#     def top_expenses(self, n: int = 5) -> list[Transaction]:
#         expenses = [tx for tx in self._transactions if tx.is_expense]
#         expenses.sort(key=lambda tx: tx.amount, reverse=True)
#         return expenses[:n]
# ```

# %% [markdown]
#
# ## `budget.py`

# %% [markdown]
#
# ```python
# from __future__ import annotations
#
# from dataclasses import dataclass
#
# from pyfinanz.account import Account
# from pyfinanz.category import Category
#
#
# @dataclass(frozen=True)
# class Budget:
#     category: Category
#     monthly_limit: float
#     month: str
#
#     def __post_init__(self) -> None:
#         if self.monthly_limit <= 0:
#             raise ValueError("Monthly limit must be positive.")
#
#     def spent(self, account: Account) -> float:
#         txs = account.filter_by_month(self.month)
#         return sum(
#             tx.amount for tx in txs
#             if tx.is_expense and tx.category == self.category
#         )
#
#     def remaining(self, account: Account) -> float:
#         return self.monthly_limit - self.spent(account)
#
#     def is_exceeded(self, account: Account) -> bool:
#         return self.spent(account) > self.monthly_limit
#
#     def usage_percentage(self, account: Account) -> float:
#         return (self.spent(account) / self.monthly_limit) * 100.0
#
#
# class BudgetTracker:
#     def __init__(self) -> None:
#         self._budgets: list[Budget] = []
#
#     def set_budget(
#         self, category: Category, monthly_limit: float, month: str
#     ) -> Budget:
#         self._budgets = [
#             b for b in self._budgets
#             if not (b.category == category and b.month == month)
#         ]
#         budget = Budget(
#             category=category, monthly_limit=monthly_limit, month=month
#         )
#         self._budgets.append(budget)
#         return budget
#
#     def get_budget(self, category: Category, month: str) -> Budget | None:
#         for b in self._budgets:
#             if b.category == category and b.month == month:
#                 return b
#         return None
#
#     def check_budgets(self, account: Account) -> list[tuple[Budget, float]]:
#         return [(b, b.usage_percentage(account)) for b in self._budgets]
#
#     def exceeded_budgets(self, account: Account) -> list[Budget]:
#         return [b for b in self._budgets if b.is_exceeded(account)]
# ```
