# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Phase 5: Musterlösung</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
#
# <div style="text-align:center;">Coding-Akademie München</div>
# <br/>


# %% [markdown]
#
# # Phase 5: Musterlösung

# %% [markdown]
#
# ## `reports.py`

# %% [markdown]
#
# ```python
# from __future__ import annotations
#
# import csv
# import io
# from abc import ABC, abstractmethod
#
# from pyfinanz.account import Account
# from pyfinanz.budget import BudgetTracker
#
#
# class ReportGenerator(ABC):
#     @abstractmethod
#     def generate_monthly_report(self, account: Account, month: str) -> str: ...
#
#     @abstractmethod
#     def generate_category_report(self, account: Account) -> str: ...
#
#     @abstractmethod
#     def generate_budget_report(
#         self, tracker: BudgetTracker, account: Account
#     ) -> str: ...
#
#
# class TextReportGenerator(ReportGenerator):
#     def generate_monthly_report(self, account: Account, month: str) -> str:
#         txs = account.filter_by_month(month)
#         lines = [f"Monthly Report: {month}", "=" * 40]
#
#         income = sum(tx.amount for tx in txs if tx.is_income)
#         expenses = sum(tx.amount for tx in txs if tx.is_expense)
#
#         for tx in txs:
#             sign = "-" if tx.is_expense else "+"
#             lines.append(
#                 f"  {tx.date}  {tx.description:<20s} "
#                 f"{sign}{tx.amount:>8.2f}  [{tx.category.value}]"
#             )
#
#         lines.append("-" * 40)
#         lines.append(f"  Income:    {income:>10.2f}")
#         lines.append(f"  Expenses:  {expenses:>10.2f}")
#         lines.append(f"  Net:       {income - expenses:>10.2f}")
#         return "\n".join(lines)
#
#     def generate_category_report(self, account: Account) -> str:
#         breakdown = account.category_breakdown()
#         total = sum(breakdown.values())
#         lines = ["Category Report", "=" * 40]
#
#         for category, amount in breakdown.items():
#             pct = (amount / total * 100) if total > 0 else 0.0
#             lines.append(
#                 f"  {category.value:<20s} {amount:>10.2f}  ({pct:5.1f}%)"
#             )
#
#         lines.append("-" * 40)
#         lines.append(f"  {'Total':<20s} {total:>10.2f}")
#         return "\n".join(lines)
#
#     def generate_budget_report(
#         self, tracker: BudgetTracker, account: Account
#     ) -> str:
#         checks = tracker.check_budgets(account)
#         lines = ["Budget Report", "=" * 40]
#
#         for budget, pct in checks:
#             spent = budget.spent(account)
#             remaining = budget.remaining(account)
#             bar_length = 10
#             filled = min(int(pct / 100 * bar_length), bar_length)
#             bar = "=" * filled + " " * (bar_length - filled)
#             lines.append(
#                 f"  {budget.category.value:<15s} {budget.month}  "
#                 f"Limit: {budget.monthly_limit:>8.2f}  "
#                 f"Spent: {spent:>8.2f}  "
#                 f"Remaining: {remaining:>8.2f}  "
#                 f"[{bar}] {pct:.0f}%"
#             )
#
#         return "\n".join(lines)
#
#
# class CsvReportGenerator(ReportGenerator):
#     def generate_monthly_report(self, account: Account, month: str) -> str:
#         txs = account.filter_by_month(month)
#         output = io.StringIO()
#         writer = csv.writer(output)
#         writer.writerow(["date", "description", "amount", "type", "category"])
#         for tx in txs:
#             writer.writerow(
#                 [
#                     tx.date,
#                     tx.description,
#                     f"{tx.signed_amount:.2f}",
#                     tx.transaction_type.value,
#                     tx.category.value,
#                 ]
#             )
#         return output.getvalue()
#
#     def generate_category_report(self, account: Account) -> str:
#         breakdown = account.category_breakdown()
#         total = sum(breakdown.values())
#         output = io.StringIO()
#         writer = csv.writer(output)
#         writer.writerow(["category", "total", "percentage"])
#         for category, amount in breakdown.items():
#             pct = (amount / total * 100) if total > 0 else 0.0
#             writer.writerow([category.value, f"{amount:.2f}", f"{pct:.1f}"])
#         return output.getvalue()
#
#     def generate_budget_report(
#         self, tracker: BudgetTracker, account: Account
#     ) -> str:
#         checks = tracker.check_budgets(account)
#         output = io.StringIO()
#         writer = csv.writer(output)
#         writer.writerow(
#             ["category", "month", "limit", "spent", "remaining", "percentage"]
#         )
#         for budget, pct in checks:
#             spent = budget.spent(account)
#             remaining = budget.remaining(account)
#             writer.writerow(
#                 [
#                     budget.category.value,
#                     budget.month,
#                     f"{budget.monthly_limit:.2f}",
#                     f"{spent:.2f}",
#                     f"{remaining:.2f}",
#                     f"{pct:.1f}",
#                 ]
#             )
#         return output.getvalue()
# ```

# %% [markdown]
#
# ## Beispieltests

# %% [markdown]
#
# ```python
# import pytest
# from pyfinanz.account import Account
# from pyfinanz.budget import BudgetTracker
# from pyfinanz.category import Category, TransactionType
# from pyfinanz.reports import CsvReportGenerator, TextReportGenerator
# from pyfinanz.transaction import Transaction
#
#
# @pytest.fixture
# def account():
#     acc = Account("Main")
#     acc.add_transaction(
#         Transaction("Salary", 3000.0, TransactionType.INCOME,
#                     Category.SALARY, "2026-03-01")
#     )
#     acc.add_transaction(
#         Transaction("Rent", 800.0, TransactionType.EXPENSE,
#                     Category.HOUSING, "2026-03-02")
#     )
#     acc.add_transaction(
#         Transaction("Groceries", 120.0, TransactionType.EXPENSE,
#                     Category.FOOD, "2026-03-05")
#     )
#     return acc
#
#
# @pytest.fixture
# def tracker(account):
#     t = BudgetTracker()
#     t.set_budget(Category.FOOD, 200.0, "2026-03")
#     t.set_budget(Category.HOUSING, 1000.0, "2026-03")
#     return t
#
#
# class TestTextReportGenerator:
#     def setup_method(self):
#         self.gen = TextReportGenerator()
#
#     def test_monthly_report_header(self, account):
#         report = self.gen.generate_monthly_report(account, "2026-03")
#         assert "Monthly Report: 2026-03" in report
#
#     def test_monthly_report_contains_transactions(self, account):
#         report = self.gen.generate_monthly_report(account, "2026-03")
#         assert "Salary" in report
#         assert "Rent" in report
#
#     def test_monthly_report_totals(self, account):
#         report = self.gen.generate_monthly_report(account, "2026-03")
#         assert "3000.00" in report
#         assert "920.00" in report
#
#     def test_category_report_sorted(self, account):
#         report = self.gen.generate_category_report(account)
#         housing_pos = report.index("Housing")
#         food_pos = report.index("Food")
#         assert housing_pos < food_pos
#
#     def test_budget_report_has_bar(self, account, tracker):
#         report = self.gen.generate_budget_report(tracker, account)
#         assert "[" in report
#         assert "]" in report
#         assert "%" in report
#
#
# class TestCsvReportGenerator:
#     def setup_method(self):
#         self.gen = CsvReportGenerator()
#
#     def test_monthly_report_header_row(self, account):
#         report = self.gen.generate_monthly_report(account, "2026-03")
#         lines = report.strip().splitlines()
#         assert lines[0] == "date,description,amount,type,category"
#
#     def test_monthly_report_data_rows(self, account):
#         report = self.gen.generate_monthly_report(account, "2026-03")
#         lines = report.strip().splitlines()
#         assert len(lines) == 4  # header + 3 transactions
#
#     def test_monthly_report_expense_negative(self, account):
#         report = self.gen.generate_monthly_report(account, "2026-03")
#         assert "-800.00" in report
#
#     def test_category_report_header_row(self, account):
#         report = self.gen.generate_category_report(account)
#         lines = report.strip().splitlines()
#         assert lines[0] == "category,total,percentage"
#
#     def test_budget_report_header_row(self, account, tracker):
#         report = self.gen.generate_budget_report(tracker, account)
#         lines = report.strip().splitlines()
#         assert lines[0] == "category,month,limit,spent,remaining,percentage"
# ```

# %% [markdown]
#
# ## Paketstruktur nach Umstrukturierung

# %% [markdown]
#
# ```
# pyfinanz/
#   src/
#     pyfinanz/
#       __init__.py
#       models/
#         __init__.py        # Re-Exports: Category, TransactionType, Transaction
#         category.py
#         transaction.py
#       storage/
#         __init__.py        # Re-Exports: FinanceStore, InMemoryStore, SqliteStore, ...
#         base.py            # FinanceStore ABC
#         memory_store.py    # InMemoryStore
#         sqlite_store.py    # SqliteStore
#         json_io.py         # save_account_to_json, load_account_from_json
#       account.py
#       budget.py
#       reports.py
#   tests/
#     category_test.py
#     transaction_test.py
#     account_test.py
#     budget_test.py
#     storage_test.py
#     reports_test.py
#   pyproject.toml
# ```
