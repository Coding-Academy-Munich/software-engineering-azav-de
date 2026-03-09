# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Phase 3: JSON-Persistenz</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
#
# <div style="text-align:center;">Coding-Akademie München</div>
# <br/>


# %% [markdown]
#
# # Phase 3: JSON-Persistenz

# %% [markdown]
#
# ## Ziel
#
# In dieser Phase lernen Sie, Kontodaten als JSON-Dateien zu speichern und zu
# laden. Sie implementieren Funktionen für den JSON-Export und -Import.

# %% [markdown]
#
# ## So sieht das Ergebnis aus
#
# ```python
# from pathlib import Path
# from pyfinanz.storage import save_account_to_json, load_account_from_json
#
# # Konto in JSON speichern
# save_account_to_json(konto, Path("girokonto.json"))
#
# # Später wieder laden
# geladenes_konto = load_account_from_json(Path("girokonto.json"))
#
# # Die JSON-Datei sieht so aus:
# # {
# #   "name": "Girokonto",
# #   "transactions": [
# #     {
# #       "description": "Gehalt",
# #       "amount": 3000.0,
# #       "transaction_type": "Income",
# #       "category": "Salary",
# #       "date": "2026-03-01",
# #       "tags": []
# #     },
# #     ...
# #   ]
# # }
# ```

# %% [markdown]
#
# ## Vorbereitung
#
# **Aufgabe V1:** Schreiben Sie ein Dictionary in eine JSON-Datei und lesen Sie
# es wieder zurück. Verwenden Sie `json.dump()` und `json.load()` mit
# `open()`.
#
# > **Kursreferenz:** „JSON" (in Abschnitt 16 Dateien und IO_Operationen)
#
# **Aufgabe V2:** Erstellen Sie ein verschachteltes Dictionary mit einer Liste
# von Dictionaries darin (ähnlich der JSON-Struktur einer Transaktion).
# Konvertieren Sie es zu JSON und zurück. Prüfen Sie, dass alle Daten erhalten
# bleiben.
#
# > **Kursreferenz:** „JSON mit eigenen Objekten" (in Abschnitt 16)

# %% [markdown]
#
# ## Aufgaben
#
# ### Schritt 1: JSON-Serialisierung
#
# Erstellen Sie eine neue Datei `src/pyfinanz/storage.py`. Implementieren Sie
# zwei Funktionen:
#
# - `save_account_to_json(account, path)` — speichert ein Account-Objekt als
#   JSON-Datei. Die Struktur:
#   ```json
#   {
#     "name": "Kontoname",
#     "transactions": [
#       {
#         "description": "...",
#         "amount": 100.0,
#         "transaction_type": "Income",
#         "category": "Salary",
#         "date": "2026-03-01",
#         "tags": ["tag1", "tag2"]
#       }
#     ]
#   }
#   ```
#   Enum-Werte werden als Strings gespeichert (`.value`), frozensets als
#   sortierte Listen.
#
# - `load_account_from_json(path)` — lädt ein Account-Objekt aus einer
#   JSON-Datei. Strings werden zurück in Enums konvertiert, Listen in
#   frozensets.
#
# > **Kursreferenz:** „JSON" und „JSON mit eigenen Objekten" (in Abschnitt 16
# > Dateien und IO_Operationen), „Dateien" und „Pathlib" (in Abschnitt 16)
#
# ### Schritt 2: Fehlerbehandlung
#
# Stellen Sie sicher, dass:
# - `FileNotFoundError` geworfen wird, wenn die Datei nicht existiert
#   (Python macht das automatisch bei `open()`)
# - `json.JSONDecodeError` geworfen wird bei ungültigem JSON (automatisch
#   durch `json.load()`)
#
# Sie müssen diese Fehler nicht selbst fangen — lassen Sie sie aufsteigen.
# Das ist bewusste Designentscheidung: Der Aufrufer entscheidet, wie er damit
# umgeht.
#
# > **Kursreferenz:** „Fehlerbehandlung" und „Propagation von Exceptions"
# > (in Abschnitt 10 Fehlerbehandlung)
#
# ### Schritt 3: Tests
#
# Erstellen Sie `tests/storage_test.py`. Verwenden Sie `tmp_path` für
# Dateisystem-Tests.
#
# Testen Sie:
# - Round-Trip: Speichern und Laden ergibt gleiche Daten
# - Alle Felder bleiben erhalten (Tags, Enum-Werte, Beträge)
# - Ungültige JSON-Datei wirft `json.JSONDecodeError`
# - Nicht existierende Datei wirft `FileNotFoundError`
#
# > **Kursreferenz:** „Pytest" (in Abschnitt 18 Unit-Tests und Test Frameworks)

# %% [markdown]
#
# ## Prüfe dein Ergebnis
#
# - [ ] `uv run pytest` läuft ohne Fehler
# - [ ] Ein Konto mit Transaktionen kann gespeichert und geladen werden
# - [ ] Alle Felder bleiben erhalten (Beschreibung, Betrag, Typ, Kategorie,
#       Datum, Tags)
# - [ ] Tags (frozenset) werden korrekt als Liste gespeichert und als
#       frozenset zurückgeladen
# - [ ] Die JSON-Datei ist menschenlesbar (eingerückt)
# - [ ] Sie haben mindestens 35 Tests (insgesamt)

# %% [markdown]
# *Antwort:* 
