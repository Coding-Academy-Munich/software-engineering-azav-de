# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Phase 1: Datenmodell mit TDD</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
#
# <div style="text-align:center;">Coding-Akademie München</div>
# <br/>


# %% [markdown]
#
# # Phase 1: Datenmodell mit TDD

# %% [markdown]
#
# ## Ziel
#
# In dieser Phase implementieren Sie die Grundbausteine der Finanzverwaltung:
#
# - Zwei Enums: `Category` (Ausgabenkategorien) und `TransactionType`
#   (Einnahme/Ausgabe)
# - Eine `Transaction`-Klasse (frozen Dataclass) mit Validierung
# - Eine `Account`-Klasse für die Verwaltung von Transaktionen
#
# Sie arbeiten dabei testgetrieben (TDD): Schreiben Sie **zuerst den Test**, dann
# die Implementierung.

# %% [markdown]
#
# ## So sieht das Ergebnis aus
#
# ```python
# from pyfinanz.category import Category, TransactionType
# from pyfinanz.transaction import Transaction
# from pyfinanz.account import Account
#
# # Transaktionen erstellen
# gehalt = Transaction("Gehalt", 3000, TransactionType.INCOME,
#                      Category.SALARY, "2026-03-01")
# miete = Transaction("Miete", 800, TransactionType.EXPENSE,
#                     Category.HOUSING, "2026-03-02")
# einkauf = Transaction("Einkauf", 120, TransactionType.EXPENSE,
#                       Category.FOOD, "2026-03-05",
#                       tags=frozenset({"wöchentlich"}))
#
# # Konto verwalten
# konto = Account("Girokonto")
# konto.add_transaction(gehalt)
# konto.add_transaction(miete)
# konto.add_transaction(einkauf)
#
# konto.balance       # 2080.0 (3000 - 800 - 120)
# konto.income_total  # 3000.0
# konto.expense_total # 920.0
#
# # Transaktionen filtern
# konto.filter_by_category(Category.FOOD)  # [einkauf]
# konto.filter_by_type(TransactionType.EXPENSE)  # [miete, einkauf]
# ```

# %% [markdown]
#
# ## Vorbereitung
#
# **Aufgabe V1:** Schreiben Sie eine Funktion `classify_amount`, die eine Zahl
# nimmt und `"income"` zurückgibt, wenn sie positiv ist, und `"expense"`, wenn
# sie negativ ist. Bei 0 soll `"neutral"` zurückgegeben werden.
#
# > **Kursreferenz:** „Funktionen" und „Kontrollstrukturen" (in Abschnitt 05
# > Kontrollstrukturen und Funktionen)
#
# **Aufgabe V2:** Schreiben Sie eine Funktion `validate_date`, die einen String
# nimmt und prüft, ob er dem Format `YYYY-MM-DD` entspricht. Verwenden Sie
# `re.match()` mit dem Muster `r"^\d{4}-\d{2}-\d{2}$"`. Geben Sie `True` oder
# `False` zurück.
#
# > **Kursreferenz:** „Reguläre Ausdrücke" (in Abschnitt 07 Weitere
# > Datenstrukturen und Reguläre Ausdrücke)
#
# **Aufgabe V3:** Schreiben Sie eine Funktion `format_amount`, die einen Betrag
# (float) und einen Typ (`"income"` oder `"expense"`) nimmt und einen
# formatierten String zurückgibt: `"+3000.00"` oder `"-800.00"`. Verwenden Sie
# f-Strings mit Formatangaben wie `f"{wert:>8.2f}"`.
#
# > **Kursreferenz:** „String-Interpolation" (in Abschnitt 05)
#
# **Aufgabe V4:** Schreiben Sie eine Funktion `total_amounts`, die eine Liste
# von Zahlen nimmt und die Summe der positiven und die Summe der negativen Zahlen
# getrennt zurückgibt. Verwenden Sie `sum()` mit einem Generator-Ausdruck.
#
# Beispiel: `total_amounts([3000, -800, -120, 500])` → `(3500, -920)`
#
# > **Kursreferenz:** „Listen" und „For-Schleifen" (in Abschnitt 05),
# > „Vordefinierte Funktionen" (in Abschnitt 04 Syntax und grundlegende
# > Datentypen)

# %% [markdown]
#
# ## Aufgaben
#
# ### Schritt 1: Projekt aufsetzen
#
# Erstellen Sie das Projekt wie in der Übersicht beschrieben. Erstellen Sie die
# leeren Dateien:
#
# - `src/pyfinanz/category.py`
# - `src/pyfinanz/transaction.py`
# - `src/pyfinanz/account.py`
# - `tests/transaction_test.py`
# - `tests/account_test.py`
#
# > **Kursreferenz:** „Der uv Package Manager" (in Abschnitt 14 Module und
# > Packages)
#
# ### Schritt 2: Enums
#
# Erstellen Sie in `category.py` zwei Enums:
#
# - `Category` mit 11 Werten: HOUSING, FOOD, TRANSPORT, ENTERTAINMENT, HEALTH,
#   EDUCATION, CLOTHING, SALARY, FREELANCE, INVESTMENT, OTHER. Jeder Wert hat
#   einen lesbaren String (z.B. `"Housing"`, `"Food"`).
# - `TransactionType` mit 2 Werten: INCOME und EXPENSE.
#
# > **Kursreferenz:** „Enumerationen" (in Abschnitt 15 Objektorientierte Analyse
# > und Design (Teil 2))
#
# ### Schritt 3: `Transaction`
#
# Erstellen Sie eine **frozen** Dataclass `Transaction` mit den Feldern:
# `description` (str), `amount` (float), `transaction_type` (TransactionType),
# `category` (Category), `date` (str), `tags` (frozenset[str], Standard: leer).
#
# Validierung in `__post_init__`:
# - `description` darf nicht leer sein (Whitespace entfernen und prüfen)
# - `amount` muss positiv sein (Beträge sind immer positiv, die Richtung
#   bestimmt der `transaction_type`)
# - `date` muss dem ISO-Format `YYYY-MM-DD` entsprechen (Regex prüfen)
#
# Properties:
# - `is_expense` — `True` wenn `transaction_type == EXPENSE`
# - `is_income` — `True` wenn `transaction_type == INCOME`
# - `signed_amount` — negativer Wert für Ausgaben, positiver für Einnahmen
#
# Optional: `__str__` für formatierte Ausgabe.
#
# > **Kursreferenz:** „Dataclasses" und „Unveränderliche Dataclasses" (in
# > Abschnitt 09 Objektmodell und Magic Methods), „Initialisierung von
# > Dataclasses", „Properties"
#
# ### Schritt 4: `Account`
#
# Erstellen Sie eine Klasse `Account` mit einem Namen und einer internen Liste
# von Transaktionen.
#
# Methoden und Properties:
# - `add_transaction(t)` — fügt eine Transaktion hinzu
# - `transactions` (Property) — gibt eine Kopie der Liste zurück
# - `balance` (Property) — Summe aller `signed_amount`-Werte
# - `income_total` (Property) — Summe aller Einnahmen
# - `expense_total` (Property) — Summe aller Ausgaben
# - `filter_by_category(category)` — Transaktionen einer Kategorie
# - `filter_by_type(t)` — Einnahmen oder Ausgaben
#
# > **Kursreferenz:** „Klassen" und „Methoden" (in Abschnitt 08 Klassen, Objekte
# > und Methoden), „Properties" (in Abschnitt 09)
#
# ### Schritt 5: Tests schreiben
#
# Schreiben Sie Tests für jede Klasse. Nutzen Sie TDD: Test **vor** der
# Implementierung.
#
# Testen Sie insbesondere:
# - Transaction-Validierung (leere Beschreibung, negativer Betrag, ungültiges
#   Datum)
# - `signed_amount` für Einnahmen und Ausgaben
# - Balance-Berechnung mit gemischten Transaktionen
# - Filterung nach Kategorie und Typ
# - Leeres Konto (Balance = 0)
#
# > **Kursreferenz:** „Pytest" und „Test-Driven-Development" (in Abschnitt 18
# > Unit-Tests und Test Frameworks)

# %% [markdown]
#
# ## Prüfe dein Ergebnis
#
# - [ ] `uv run pytest` läuft ohne Fehler
# - [ ] `Transaction("", 100, ...)` wirft `ValueError`
# - [ ] `Transaction("Test", -1, ...)` wirft `ValueError`
# - [ ] `Transaction("Test", 100, ..., date="2026-13-01")` wirft `ValueError`
#       (ungültiges Format)
# - [ ] Eine Ausgabe von 800 € hat `signed_amount == -800.0`
# - [ ] Eine Einnahme von 3000 € hat `signed_amount == 3000.0`
# - [ ] Ein Konto mit 3000 € Einnahmen und 920 € Ausgaben hat `balance == 2080.0`
# - [ ] `filter_by_category(Category.FOOD)` gibt nur Transaktionen der
#       Kategorie FOOD zurück
# - [ ] Sie haben mindestens 15 Tests

# %% [markdown]
# *Antwort:* 
