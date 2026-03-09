# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Phase 2: Filterung, Analyse und Budgets</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
#
# <div style="text-align:center;">Coding-Akademie München</div>
# <br/>


# %% [markdown]
#
# # Phase 2: Filterung, Analyse und Budgets

# %% [markdown]
#
# ## Ziel
#
# In dieser Phase erweitern Sie das `Account` um erweiterte Filter-, Such- und
# Analysefunktionen und implementieren ein Budgetsystem.

# %% [markdown]
#
# ## So sieht das Ergebnis aus
#
# ```python
# # Datumsfilter
# maerz = konto.filter_by_month("2026-03")
# zeitraum = konto.filter_by_date_range("2026-03-01", "2026-03-15")
#
# # Regex-Suche
# ergebnisse = konto.search("Miet")  # findet "Miete"
#
# # Monatsübersicht
# konto.monthly_summary()
# # {"2026-03": {"income": 3500.0, "expenses": 970.0, "net": 2530.0}}
#
# # Ausgaben nach Kategorie
# konto.category_breakdown()
# # {Category.HOUSING: 800.0, Category.FOOD: 120.0, ...}
#
# # Top-Ausgaben
# konto.top_expenses(3)  # Die 3 größten Ausgaben
#
# # Budgets
# from pyfinanz.budget import Budget, BudgetTracker
# tracker = BudgetTracker()
# tracker.set_budget(Category.FOOD, 200.0, "2026-03")
# tracker.set_budget(Category.HOUSING, 700.0, "2026-03")
# ueberschritten = tracker.exceeded_budgets(konto)  # [Budget(HOUSING, ...)]
# ```

# %% [markdown]
#
# ## Vorbereitung
#
# **Aufgabe V1:** Gegeben ist eine Liste von Strings mit Datumsangaben:
# `["2026-03-01", "2026-03-15", "2026-04-01", "2026-03-28"]`. Filtern Sie
# die Liste so, dass nur Daten übrig bleiben, die mit `"2026-03"` beginnen.
# Nutzen Sie String-Slicing (`date[:7]`) und eine List Comprehension.
#
# > **Kursreferenz:** „Komprehensionen: Elegantere Iteration" (in Abschnitt 12
# > Fortgeschrittene Kontrollstrukturen)
#
# **Aufgabe V2:** Erstellen Sie ein Dictionary, das Monatsnamen auf Summen
# abbildet. Gegeben ist eine Liste von Tupeln:
# `[("2026-03", 100), ("2026-04", 50), ("2026-03", 200)]`. Erstellen Sie
# daraus `{"2026-03": 300, "2026-04": 50}`.
#
# > **Kursreferenz:** „Dictionaries" (in Abschnitt 07 Weitere Datenstrukturen
# > und Reguläre Ausdrücke)
#
# **Aufgabe V3:** Sortieren Sie eine Liste von Dictionaries nach einem
# bestimmten Schlüssel. Gegeben: `[{"name": "B", "wert": 30}, {"name": "A", "wert": 50}]`.
# Sortieren Sie nach `"wert"` absteigend. Verwenden Sie `sorted()` mit
# `key=lambda x: x["wert"]` und `reverse=True`.
#
# > **Kursreferenz:** „Operationen auf Listen" (in Abschnitt 06 Sequenzen)

# %% [markdown]
#
# ## Aufgaben
#
# ### Schritt 1: Erweiterte Filter im `Account`
#
# Erweitern Sie Ihr `Account` um diese Methoden:
#
# - `filter_by_date_range(start, end)` — Transaktionen innerhalb eines
#   Zeitraums. Da ISO-Daten lexikographisch sortierbar sind, reicht ein
#   einfacher String-Vergleich: `start <= tx.date <= end`
# - `filter_by_month(month)` — Transaktionen eines bestimmten Monats
#   (`"YYYY-MM"`). Verwenden Sie `tx.date[:7]`
# - `search(query)` — Regex-Suche auf Beschreibungen (Groß-/Kleinschreibung
#   ignorieren)
# - `filter_by_tags(tags)` — Transaktionen, die mindestens einen der
#   übergebenen Tags haben
#
# > **Kursreferenz:** „Reguläre Ausdrücke" (in Abschnitt 07), „Mengen"
# > (in Abschnitt 07), „Komprehensionen: Elegantere Iteration" (in Abschnitt 12)
#
# ### Schritt 2: Aggregation
#
# Erweitern Sie `Account` um Analysemethoden:
#
# - `monthly_summary()` — Dictionary, das Monate auf
#   `{"income": ..., "expenses": ..., "net": ...}` abbildet
# - `category_breakdown()` — Dictionary, das Kategorien auf Gesamtausgaben
#   abbildet. Nur Ausgaben zählen. Sortiert nach Betrag (größte zuerst).
# - `top_expenses(n=5)` — Die n größten Ausgaben als sortierte Liste
#
# > **Kursreferenz:** „Dictionaries" und „Iteration über Dictionaries"
# > (in Abschnitt 07)
#
# ### Schritt 3: `Budget` und `BudgetTracker`
#
# Erstellen Sie eine neue Datei `src/pyfinanz/budget.py`:
#
# - `Budget` (frozen Dataclass): `category`, `monthly_limit`, `month`
#   - Validierung: `monthly_limit` muss positiv sein
#   - `spent(account)` — berechnet die Ausgaben in dieser Kategorie für den
#     Monat
#   - `remaining(account)` — Limit minus Ausgaben
#   - `is_exceeded(account)` — True wenn Ausgaben > Limit
#   - `usage_percentage(account)` — Ausgaben / Limit * 100
#
# - `BudgetTracker`: Verwaltet eine Liste von Budgets
#   - `set_budget(category, limit, month)` — erstellt oder ersetzt ein Budget
#   - `check_budgets(account)` — gibt alle Budgets mit Nutzungsprozent zurück
#   - `exceeded_budgets(account)` — gibt nur überschrittene Budgets zurück
#
# > **Kursreferenz:** „Dataclasses" (in Abschnitt 09 Objektmodell und Magic
# > Methods), „Klassen" und „Methoden" (in Abschnitt 08)
#
# ### Schritt 4: Tests
#
# Erstellen Sie `tests/budget_test.py` und erweitern Sie `tests/account_test.py`.
#
# Verwenden Sie Fixtures mit mehreren Transaktionen über verschiedene Monate.
#
# Testen Sie:
# - Datumsfilter mit Grenzwerten
# - Regex-Suche (Groß-/Kleinschreibung, Teilübereinstimmung)
# - `monthly_summary` mit bekannten Daten
# - `category_breakdown` (nur Ausgaben, richtige Summen)
# - Budget: unter Limit, genau am Limit, über Limit
# - `usage_percentage` Berechnung
#
# > **Kursreferenz:** „Pytest" (in Abschnitt 18 Unit-Tests und Test Frameworks)

# %% [markdown]
#
# ## Prüfe dein Ergebnis
#
# - [ ] `uv run pytest` läuft ohne Fehler
# - [ ] `filter_by_month("2026-03")` gibt nur Transaktionen vom März zurück
# - [ ] `filter_by_date_range("2026-03-01", "2026-03-10")` filtert korrekt
# - [ ] `search("miet")` findet "Miete" (Groß-/Kleinschreibung ignoriert)
# - [ ] `monthly_summary()` berechnet Einnahmen, Ausgaben und Netto korrekt
# - [ ] `category_breakdown()` enthält nur Ausgaben, sortiert nach Betrag
# - [ ] `top_expenses(3)` gibt die 3 größten Ausgaben zurück
# - [ ] Ein Budget von 700 € bei 800 € Ausgaben hat `is_exceeded == True`
# - [ ] `usage_percentage` berechnet korrekt (z.B. 800/700*100 ≈ 114%)
# - [ ] Sie haben mindestens 30 Tests (insgesamt)

# %% [markdown]
# *Antwort:* 
# ## Hinweise
#
# ### Zu Schritt 1: Erweiterte Filter
#
# ISO-Daten als Strings können direkt verglichen werden, weil die
# lexikographische Ordnung der zeitlichen Ordnung entspricht:
#
# ```python
# def filter_by_date_range(self, start: str, end: str) -> list[Transaction]:
#     return [tx for tx in self._transactions if start <= tx.date <= end]
# ```
#
# Für `filter_by_month`: Schneiden Sie die ersten 7 Zeichen ab (`"YYYY-MM"`):
#
# ```python
# def filter_by_month(self, month: str) -> list[Transaction]:
#     return [tx for tx in self._transactions if tx.date[:7] == month]
# ```
#
# Für `filter_by_tags`: Die Mengenoperation `&` (Schnittmenge) prüft, ob es
# gemeinsame Elemente gibt. Ein nicht-leeres Ergebnis ist truthy:
#
# ```python
# def filter_by_tags(self, tags: set[str]) -> list[Transaction]:
#     return [tx for tx in self._transactions if tx.tags & tags]
# ```
#
# ### Zu Schritt 2: Aggregation
#
# Für `monthly_summary`: Iterieren Sie über alle Transaktionen und gruppieren
# Sie nach `tx.date[:7]`:
#
# ```python
# def monthly_summary(self) -> dict[str, dict[str, float]]:
#     result = {}
#     for tx in self._transactions:
#         month = tx.date[:7]
#         if month not in result:
#             result[month] = {"income": 0.0, "expenses": 0.0, "net": 0.0}
#         if tx.is_income:
#             result[month]["income"] += tx.amount
#         else:
#             result[month]["expenses"] += tx.amount
#         result[month]["net"] += tx.signed_amount
#     return result
# ```
#
# Für `category_breakdown`: Verwenden Sie `sorted()` mit `key=lambda` und
# `reverse=True`, um nach Betrag absteigend zu sortieren.
#
# Für `top_expenses`: Filtern Sie zuerst nur Ausgaben, sortieren Sie dann nach
# `amount` absteigend, und nehmen Sie die ersten `n`.
#
# ### Zu Schritt 3: Budget
#
# `Budget.spent` nutzt die bereits implementierten Filtermethoden des Accounts:
#
# ```python
# def spent(self, account: Account) -> float:
#     txs = account.filter_by_month(self.month)
#     return sum(
#         tx.amount for tx in txs
#         if tx.is_expense and tx.category == self.category
#     )
# ```
#
# `BudgetTracker.set_budget` ersetzt ein bestehendes Budget für dieselbe
# Kategorie und denselben Monat. Filtern Sie zuerst das alte Budget heraus:
#
# ```python
# self._budgets = [
#     b for b in self._budgets
#     if not (b.category == category and b.month == month)
# ]
# ```
