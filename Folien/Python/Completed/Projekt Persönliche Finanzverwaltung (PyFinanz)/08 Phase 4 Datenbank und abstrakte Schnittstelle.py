# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Phase 4: Datenbank und abstrakte Schnittstelle</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
#
# <div style="text-align:center;">Coding-Akademie München</div>
# <br/>


# %% [markdown]
#
# # Phase 4: Datenbank und abstrakte Schnittstelle

# %% [markdown]
#
# ## Ziel
#
# In dieser Phase implementieren Sie einen SQLite-basierten Speicher für
# Transaktionen und erstellen eine gemeinsame abstrakte Schnittstelle
# (`FinanceStore`), die verschiedene Backends vereint.

# %% [markdown]
#
# ## So sieht das Ergebnis aus
#
# ```python
# from pyfinanz.storage import InMemoryStore, SqliteStore
#
# # Beide Stores haben dieselbe Schnittstelle
# memory_store = InMemoryStore()
# sqlite_store = SqliteStore(":memory:")
#
# for store in [memory_store, sqlite_store]:
#     store.add_transaction("Girokonto", gehalt)
#     store.add_transaction("Girokonto", miete)
#     txs = store.get_transactions("Girokonto")
#     namen = store.get_account_names()  # ["Girokonto"]
# ```

# %% [markdown]
#
# ## Vorbereitung
#
# **Aufgabe V1:** Erstellen Sie eine SQLite-Datenbank im Speicher mit einer
# Tabelle `personen` (name TEXT, alter_ INTEGER). Fügen Sie einige Zeilen ein
# und lesen Sie sie mit `SELECT` wieder aus.
#
# > **Kursreferenz:** „Python DB-API (Teil 1)" und „Python DB-API (Teil 2)"
# > (in Abschnitt 19 Datenbanken und SQL)
#
# **Aufgabe V2:** Erstellen Sie eine abstrakte Klasse `Speicher` mit einer
# abstrakten Methode `speichern(daten)` und zwei konkrete Unterklassen
# `DateiSpeicher` und `ListSpeicher`, die die Methode unterschiedlich
# implementieren.
#
# > **Kursreferenz:** „Abstrakte Klassen" (in Abschnitt 11 Vererbung und
# > Polymorphie)

# %% [markdown]
#
# ## Aufgaben
#
# ### Schritt 1: Abstrakte Schnittstelle `FinanceStore`
#
# Erweitern Sie `storage.py` um eine abstrakte Basisklasse `FinanceStore`:
#
# - `add_transaction(account_name, transaction)` — Transaktion hinzufügen
# - `get_transactions(account_name)` — alle Transaktionen eines Kontos
# - `get_account_names()` — alle Kontonamen
# - `delete_transaction(account_name, transaction)` — Transaktion entfernen
# - `clear_account(account_name)` — alle Daten eines Kontos löschen
#
# > **Kursreferenz:** „Abstrakte Klassen" und „Vererbung" (in Abschnitt 11
# > Vererbung und Polymorphie)
#
# ### Schritt 2: `InMemoryStore`
#
# Implementieren Sie `InMemoryStore(FinanceStore)`, der Transaktionen in einem
# Dictionary `{kontoname: [transaktionen]}` speichert.
#
# - `get_transactions` gibt eine leere Liste zurück, wenn das Konto nicht
#   existiert
# - `delete_transaction` wirft `ValueError` wenn die Transaktion nicht
#   gefunden wird
#
# ### Schritt 3: Datenbankschema und `SqliteStore`
#
# Entwerfen und implementieren Sie `SqliteStore(FinanceStore)` mit drei
# Tabellen:
#
# - `accounts` — id, name (UNIQUE)
# - `transactions` — id, account_id (FK), description, amount,
#   transaction_type, category, date
# - `transaction_tags` — transaction_id (FK), tag, zusammengesetzter PK
#
# Implementieren Sie:
# - `_create_tables()` — Tabellen anlegen (`CREATE TABLE IF NOT EXISTS`)
# - `_get_or_create_account(name)` — Account-ID zurückgeben, ggf. anlegen
# - Alle Methoden von `FinanceStore`
#
# Beachten Sie: Das System unterstützt **mehrere Konten** — jede Transaktion
# gehört zu einem bestimmten Konto.
#
# > **Kursreferenz:** „Tabellen erstellen (CREATE TABLE)" und „Daten einfügen
# > (INSERT)" (in Abschnitt 19 Datenbanken und SQL), „Python DB-API (Teil 1)"
# > und „Python DB-API (Teil 2)"
#
# ### Schritt 4: Tests
#
# Verwenden Sie eine parametrisierte Fixture für beide Backends:
#
# ```python
# @pytest.fixture(params=["memory", "sqlite"])
# def store(request):
#     if request.param == "memory":
#         return InMemoryStore()
#     return SqliteStore(":memory:")
# ```
#
# Testen Sie:
# - Hinzufügen und Abrufen (Round-Trip)
# - Tags bleiben erhalten
# - Mehrere Konten (Transaktionen sind getrennt)
# - Löschen einzelner Transaktionen
# - Konto leeren
# - Nicht existierende Konten geben leere Liste zurück
#
# > **Kursreferenz:** „Pytest" (in Abschnitt 18 Unit-Tests und Test Frameworks)

# %% [markdown]
#
# ## Prüfe dein Ergebnis
#
# - [ ] `uv run pytest` läuft ohne Fehler
# - [ ] Alle Store-Tests laufen mit beiden Backends (memory, sqlite)
# - [ ] Transaktionen mit Tags überleben den Round-Trip durch die Datenbank
# - [ ] Mehrere Konten sind voneinander getrennt
# - [ ] `delete_transaction` entfernt genau eine Transaktion
# - [ ] `clear_account` entfernt Konto und alle Transaktionen
# - [ ] `InMemoryStore` und `SqliteStore` erben beide von `FinanceStore`
# - [ ] Sie haben mindestens 45 Tests (insgesamt)

# %% [markdown]
# *Antwort:* 
# ## Hinweise
#
# ### Zu Schritt 2: `InMemoryStore`
#
# Verwenden Sie ein Dictionary mit Listen als Werte:
#
# ```python
# class InMemoryStore(FinanceStore):
#     def __init__(self):
#         self._data: dict[str, list[Transaction]] = {}
#
#     def add_transaction(self, account_name, transaction):
#         if account_name not in self._data:
#             self._data[account_name] = []
#         self._data[account_name].append(transaction)
#
#     def get_transactions(self, account_name):
#         return list(self._data.get(account_name, []))
# ```
#
# Für `delete_transaction` verwenden Sie `list.remove()`:
#
# ```python
# txs = self._data.get(account_name, [])
# try:
#     txs.remove(transaction)
# except ValueError:
#     raise ValueError("Transaction not found.")
# ```
#
# ### Zu Schritt 3: `SqliteStore`
#
# Die Hilfsmethode `_get_or_create_account` sucht zuerst nach dem Konto und
# erstellt es nur, wenn es nicht existiert:
#
# ```python
# def _get_or_create_account(self, name: str) -> int:
#     cursor = self.connection.cursor()
#     cursor.execute("SELECT id FROM accounts WHERE name = ?", (name,))
#     row = cursor.fetchone()
#     if row is not None:
#         return row[0]
#     cursor.execute("INSERT INTO accounts (name) VALUES (?)", (name,))
#     self.connection.commit()
#     return cursor.lastrowid
# ```
#
# Beim Laden von Transaktionen müssen Sie für jede Transaktion auch die Tags
# aus der `transaction_tags`-Tabelle laden.
#
# Beim Löschen einer Transaktion: Suchen Sie zuerst die Transaktion anhand aller
# Felder (description, amount, type, category, date), löschen Sie dann zuerst
# die Tags und dann die Transaktion selbst.
#
# ### Zu Schritt 4: Parametrisierte Fixtures
#
# Da `SqliteStore(":memory:")` eine In-Memory-Datenbank verwendet, brauchen
# Sie kein `tmp_path` für die Datenbank-Tests. Die parametrisierte Fixture
# läuft jeden Test automatisch mit beiden Backends.
