# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Phase 5: Berichte und Paketierung</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
#
# <div style="text-align:center;">Coding-Akademie München</div>
# <br/>


# %% [markdown]
#
# # Phase 5: Berichte und Paketierung

# %% [markdown]
#
# ## Ziel
#
# In dieser Phase implementieren Sie ein Berichtssystem mit austauschbaren
# Formaten (Text und CSV) über eine abstrakte Schnittstelle. Anschließend
# strukturieren Sie das gesamte Projekt als sauberes Python-Paket mit
# Unterpaketen.

# %% [markdown]
#
# ## So sieht das Ergebnis aus
#
# ```python
# from pyfinanz.reports import TextReportGenerator, CsvReportGenerator
#
# text_gen = TextReportGenerator()
# csv_gen = CsvReportGenerator()
#
# # Beide haben dieselbe Schnittstelle
# for gen in [text_gen, csv_gen]:
#     print(gen.generate_monthly_report(konto, "2026-03"))
#     print(gen.generate_category_report(konto))
#     print(gen.generate_budget_report(tracker, konto))
# ```
#
# Nach der Umstrukturierung:
#
# ```
# pyfinanz/
#   src/
#     pyfinanz/
#       __init__.py
#       models/
#         __init__.py
#         category.py
#         transaction.py
#       storage/
#         __init__.py
#         base.py
#         memory_store.py
#         sqlite_store.py
#         json_io.py
#       account.py
#       budget.py
#       reports.py
#   tests/
#   pyproject.toml
# ```

# %% [markdown]
#
# ## Vorbereitung
#
# **Aufgabe V1:** Üben Sie String-Formatierung mit f-Strings. Erstellen Sie
# eine Funktion, die eine Liste von Produkten (Name, Preis) als
# Tabelle ausgibt:
#
# ```python
# def format_table(products):
#     lines = []
#     for name, price in products:
#         lines.append(f"  {name:<20s} {price:>8.2f}")
#     return "\n".join(lines)
#
# # Ergebnis:
# #   Brot                    2.50
# #   Milch                   1.20
# ```
#
# `<20s` bedeutet: linksbündig, 20 Zeichen breit. `>8.2f` bedeutet:
# rechtsbündig, 8 Zeichen breit, 2 Nachkommastellen.
#
# > **Kursreferenz:** „F-Strings" (in Abschnitt 04 Strings)
#
# **Aufgabe V2:** Üben Sie die Arbeit mit dem `csv`-Modul. Schreiben Sie
# Daten in einen `StringIO`-Puffer und lesen Sie sie zurück:
#
# ```python
# import csv
# import io
#
# output = io.StringIO()
# writer = csv.writer(output)
# writer.writerow(["name", "preis"])
# writer.writerow(["Brot", "2.50"])
# text = output.getvalue()
# ```
#
# > **Kursreferenz:** „Das csv-Modul" (in Abschnitt 16 Dateien und
# > IO_Operationen)
#
# **Aufgabe V3:** Erstellen Sie eine abstrakte Klasse `Formatter` mit einer
# abstrakten Methode `format(data)` und zwei konkrete Unterklassen
# `TextFormatter` und `CsvFormatter`, die dieselben Daten unterschiedlich
# formatieren.
#
# > **Kursreferenz:** „Abstrakte Klassen" (in Abschnitt 11 Vererbung und
# > Polymorphie)
#
# **Aufgabe V4:** Erstellen Sie ein Mini-Paket mit einem Unterpaket, um
# Imports und Re-Exports zu üben:
#
# ```
# meinpaket/
#   __init__.py
#   werkzeuge/
#     __init__.py
#     rechner.py   # def addiere(a, b): return a + b
# ```
#
# Fügen Sie in `werkzeuge/__init__.py` einen Re-Export hinzu, damit
# `from meinpaket.werkzeuge import addiere` funktioniert.
#
# > **Kursreferenz:** „Module und Packages" und „Packages" (in Abschnitt 14
# > Module und Packages)

# %% [markdown]
#
# ## Aufgaben
#
# ### Schritt 1: Abstrakte Schnittstelle `ReportGenerator`
#
# Erstellen Sie `src/pyfinanz/reports.py` mit einer abstrakten Klasse
# `ReportGenerator`:
#
# - `generate_monthly_report(account, month)` — Monatsübersicht als String
# - `generate_category_report(account)` — Kategorie-Aufschlüsselung als
#   String
# - `generate_budget_report(tracker, account)` — Budget-Status als String
#
# Die Methoden geben Strings zurück — **keine Dateien schreiben**. Der
# Aufrufer entscheidet, was mit dem String passiert (anzeigen, speichern
# usw.).
#
# > **Kursreferenz:** „Abstrakte Klassen" (in Abschnitt 11 Vererbung und
# > Polymorphie)
#
# ### Schritt 2: `TextReportGenerator`
#
# Implementieren Sie `TextReportGenerator(ReportGenerator)`:
#
# **`generate_monthly_report`:**
# - Überschrift mit Monat und Trennlinie
# - Jede Transaktion: Datum, Beschreibung, Vorzeichen (+/-), Betrag,
#   Kategorie in eckigen Klammern
# - Zusammenfassung: Einnahmen, Ausgaben, Netto
#
# Verwenden Sie f-Strings mit Formatierung:
# ```python
# f"  {tx.date}  {tx.description:<20s} {sign}{tx.amount:>8.2f}  [{tx.category.value}]"
# ```
#
# **`generate_category_report`:**
# - Verwenden Sie `account.category_breakdown()`
# - Zeigen Sie jede Kategorie mit Betrag und Prozentanteil
# - Sortiert nach Betrag (absteigend) — `category_breakdown` liefert das
#   bereits
#
# **`generate_budget_report`:**
# - Verwenden Sie `tracker.check_budgets(account)`
# - Zeigen Sie für jedes Budget: Kategorie, Monat, Limit, Ausgaben,
#   Verbleibend, Fortschrittsbalken mit Prozent
# - Der Fortschrittsbalken kann mit `"=" * filled + " " * rest` erstellt
#   werden
#
# > **Kursreferenz:** „F-Strings" (in Abschnitt 04 Strings)
#
# ### Schritt 3: `CsvReportGenerator`
#
# Implementieren Sie `CsvReportGenerator(ReportGenerator)`:
#
# Verwenden Sie `csv.writer` mit `io.StringIO`:
#
# ```python
# import csv
# import io
#
# output = io.StringIO()
# writer = csv.writer(output)
# writer.writerow(["spalte1", "spalte2"])  # Header
# writer.writerow(["wert1", "wert2"])      # Daten
# return output.getvalue()
# ```
#
# **`generate_monthly_report`:**
# - Header: `date,description,amount,type,category`
# - Betrag als `signed_amount` (negativ für Ausgaben)
#
# **`generate_category_report`:**
# - Header: `category,total,percentage`
#
# **`generate_budget_report`:**
# - Header: `category,month,limit,spent,remaining,percentage`
#
# > **Kursreferenz:** „Das csv-Modul" (in Abschnitt 16 Dateien und
# > IO_Operationen)
#
# ### Schritt 4: Tests
#
# Testen Sie:
# - Text-Bericht enthält Überschrift und Transaktionsdaten
# - Text-Bericht enthält korrekte Summen
# - Kategorie-Bericht ist nach Betrag sortiert
# - Budget-Bericht enthält Fortschrittsbalken (`[`, `]`, `%`)
# - CSV-Bericht hat korrekte Header-Zeile
# - CSV-Bericht hat richtige Anzahl Datenzeilen
# - CSV-Bericht enthält negative Beträge für Ausgaben
#
# > **Kursreferenz:** „Pytest" (in Abschnitt 18 Unit-Tests und Test
# > Frameworks)
#
# ### Schritt 5: Paketierung
#
# Strukturieren Sie das Projekt mit Unterpaketen um:
#
# **`models/`-Unterpaket:**
# - `category.py` → `models/category.py`
# - `transaction.py` → `models/transaction.py`
#
# **`storage/`-Unterpaket:**
# - `FinanceStore` ABC → `storage/base.py`
# - `InMemoryStore` → `storage/memory_store.py`
# - `SqliteStore` → `storage/sqlite_store.py`
# - JSON-Funktionen → `storage/json_io.py`
#
# Dateien, die auf oberster Ebene bleiben:
# - `account.py`, `budget.py`, `reports.py`
#
# Fügen Sie Re-Exports in den `__init__.py`-Dateien hinzu:
#
# ```python
# # models/__init__.py
# from pyfinanz.models.category import Category, TransactionType
# from pyfinanz.models.transaction import Transaction
#
# # storage/__init__.py
# from pyfinanz.storage.base import FinanceStore
# from pyfinanz.storage.memory_store import InMemoryStore
# from pyfinanz.storage.sqlite_store import SqliteStore
# from pyfinanz.storage.json_io import save_account_to_json, load_account_from_json
# ```
#
# Aktualisieren Sie alle Imports in Quell- und Testdateien. Führen Sie nach
# jeder Änderung `uv run pytest` aus.
#
# > **Kursreferenz:** „Module und Packages" und „Packages" (in Abschnitt 14
# > Module und Packages), „Der uv Package Manager for Python" (in
# > Abschnitt 14)

# %% [markdown]
#
# ## Prüfe dein Ergebnis
#
# - [ ] `uv run pytest` läuft ohne Fehler
# - [ ] `TextReportGenerator` und `CsvReportGenerator` erben beide von
#       `ReportGenerator`
# - [ ] Text-Berichte sind menschenlesbar mit Formatierung
# - [ ] CSV-Berichte haben korrekte Header und Datenzeilen
# - [ ] Die Verzeichnisstruktur hat `models/` und `storage/` Unterpakete
# - [ ] Jede `__init__.py` enthält sinnvolle Re-Exports
# - [ ] `from pyfinanz.models import Transaction, Category` funktioniert
# - [ ] `from pyfinanz.storage import InMemoryStore, SqliteStore` funktioniert
# - [ ] Sie haben mindestens 55 Tests (insgesamt)

# %% [markdown]
# *Antwort:* 
