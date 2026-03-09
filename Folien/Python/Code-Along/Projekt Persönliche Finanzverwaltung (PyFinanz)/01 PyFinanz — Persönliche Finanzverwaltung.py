# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>PyFinanz — Persönliche Finanzverwaltung</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
#
# <div style="text-align:center;">Coding-Akademie München</div>
# <br/>


# %% [markdown]
#
# # PyFinanz — Persönliche Finanzverwaltung

# %% [markdown]
#
# ## Was bauen wir?
#
# In diesem Projekt entwickeln Sie **PyFinanz**, eine persönliche
# Finanzverwaltung in Python. Die Anwendung ermöglicht es, Einnahmen und Ausgaben
# zu erfassen, nach Kategorien zu analysieren, Budgets zu setzen und
# Finanzberichte zu erstellen.
#
# Sie bauen das Projekt schrittweise in 5 Phasen auf — vom einfachen Datenmodell
# bis zur Berichterstellung und Datenbank-Anbindung.

# %% [markdown]
#
# ## Funktionen
#
# - Transaktionen (Einnahmen und Ausgaben) mit Kategorien und Tags erfassen
# - Kontostand, Gesamteinnahmen und Gesamtausgaben berechnen
# - Transaktionen filtern (nach Kategorie, Zeitraum, Typ, Tags)
# - Transaktionen durchsuchen (mit regulären Ausdrücken)
# - Monatsübersichten und Ausgaben nach Kategorien aufschlüsseln
# - Budgets pro Kategorie setzen und überwachen
# - Finanzberichte als Text und CSV generieren
# - Daten als JSON speichern und laden
# - Transaktionen in einer SQLite-Datenbank verwalten

# %% [markdown]
#
# ## Domänenmodell
#
# ```
# Category (Enum)
#   HOUSING, FOOD, TRANSPORT, ENTERTAINMENT, HEALTH,
#   EDUCATION, CLOTHING, SALARY, FREELANCE, INVESTMENT, OTHER
#
# TransactionType (Enum)
#   INCOME, EXPENSE
#
# Transaction (frozen dataclass)
#   - description: str
#   - amount: float           (immer positiv)
#   - transaction_type: TransactionType
#   - category: Category
#   - date: str               (ISO-Format: YYYY-MM-DD)
#   - tags: frozenset[str]
#   + is_expense: bool        (Property)
#   + is_income: bool         (Property)
#   + signed_amount: float    (Property, negativ für Ausgaben)
#
# Account
#   - name: str
#   - transactions: list[Transaction]
#   + balance: float          (Property)
#   + income_total: float     (Property)
#   + expense_total: float    (Property)
#   + filter_by_category(category) → list[Transaction]
#   + filter_by_type(type) → list[Transaction]
#   + filter_by_date_range(start, end) → list[Transaction]
#   + filter_by_month(month) → list[Transaction]
#   + search(query) → list[Transaction]
#   + monthly_summary() → dict
#   + category_breakdown() → dict
#   + top_expenses(n) → list[Transaction]
#
# Budget (frozen dataclass)
#   - category: Category
#   - monthly_limit: float
#   - month: str              ("YYYY-MM")
#   + remaining(account) → float
#   + is_exceeded(account) → bool
#   + usage_percentage(account) → float
#
# BudgetTracker
#   + set_budget(category, limit, month) → Budget
#   + check_budgets(account) → list[tuple[Budget, float]]
#   + exceeded_budgets(account) → list[Budget]
#
# ReportGenerator (ABC)
#   + generate_monthly_report(account, month) → str
#   + generate_category_report(account) → str
#   + generate_budget_report(tracker, account) → str
#   ├── TextReportGenerator
#   └── CsvReportGenerator
#
# FinanceStore (ABC)
#   + add_transaction(account_name, transaction)
#   + get_transactions(account_name) → list[Transaction]
#   + get_account_names() → list[str]
#   + delete_transaction(account_name, transaction)
#   ├── InMemoryStore
#   └── SqliteStore
# ```

# %% [markdown]
#
# ## Phasenübersicht
#
# | Phase | Thema | Neue Konzepte |
# |-------|-------|---------------|
# | 1 | Datenmodell mit TDD | Enums, frozen Dataclass, Regex, Properties, pytest |
# | 2 | Filterung und Analyse | Comprehensions, Dicts, Sets, Aggregation, Budgets |
# | 3 | JSON-Persistenz | Dateien, pathlib, JSON-Serialisierung |
# | 4 | Datenbank | SQLite, DB-API, abstrakte Klassen, Vererbung |
# | 5 | Berichte und Paketierung | ABC, Vererbung, String-Formatierung, Pakete |
#
# Jede Phase baut auf der vorherigen auf. Arbeiten Sie die Phasen der Reihe nach
# durch.

# %% [markdown]
#
# ## Projekt-Setup
#
# Erstellen Sie das Projekt mit `uv`:
#
# ```bash
# uv init --lib pyfinanz
# cd pyfinanz
# uv add --dev pytest
# ```
#
# Ihre Projektstruktur sollte so aussehen:
#
# ```
# pyfinanz/
#   src/
#     pyfinanz/
#       __init__.py
#   tests/
#   pyproject.toml
# ```
#
# Neue Dateien legen Sie in `src/pyfinanz/` an, Tests in `tests/`.
#
# Führen Sie Tests mit folgendem Befehl aus:
#
# ```bash
# uv run pytest
# ```
