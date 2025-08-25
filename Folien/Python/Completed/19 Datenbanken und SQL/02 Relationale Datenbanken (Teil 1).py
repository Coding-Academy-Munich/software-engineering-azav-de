# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Relationale Datenbanken (Teil 1)</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# ## Relationale Datenbanken:
#
# <img src="img/relational-db-01.png"
#      style="width:100%;margin:auto" alt="Relationale Datenbank"></img>

# %% [markdown]
#
# # Relationale Datenbanken
#
# - Speichert Daten in Tabellen mit vordefinierten Beziehungen
#   - Tabellen bestehen aus Zeilen und Spalten
#   - Jede Tabelle hat einen Primärschlüssel, der jede Zeile eindeutig identifiziert
#   - Beziehungen zwischen Tabellen werden über Fremdschlüssel hergestellt
# - Verwendet in der Regel SQL als Abfragesprache

# %% [markdown]
#
# ## Tabellen und Zeilen
#
# - Daten werden in Tabellen organisiert
# - Jede Tabelle hat eine feste Struktur:
#   - Einen Namen
#   - Benannte Spalten mit vorgegebenen Datentypen
# - Jede Zeile in einer Tabelle stellt einen einzelnen Datensatz dar
# - Zeilen werden durch einen eindeutigen Bezeichner oder Primärschlüssel
#   identifiziert

# %% [markdown]
#
# ## Beispiel: Datenbank für ein Online-Lebensmittelgeschäft
#
# - Gespeicherte Daten:
#   - Speisen und Getränke
#   - Kunden
#   - Bestellungen
#   - Rechnungen
#   - ...

# %% [markdown]
#
# Tabelle **Kunden**:
#
# | customer_id | name         | address      |
# |-------------|--------------|--------------|
# |           1 | John Smith   | 123 Elm St   |
# |           2 | Jane Doe     | 456 Oak St   |
#
# Tabelle **Produkte**:
#
# | item_id | item_name    | price | description                                |
# |---------|--------------|-------|--------------------------------------------|
# |    2341 | Tomatensuppe | 1.99  | Unsere fantastische Tomatensuppe in Dosen. |
# |     346 | Kichererbsen | 0.59  | In Wasser einweichen und genießen...       |

# %% [markdown]
#
# ## Spalten und Datentypen
#
# - Spalten stellen die Attribute oder Eigenschaften eines jeden Datensatzes
#   dar.
# - Jede Spalte hat einen bestimmten Datentyp, z. B. String, Integer oder Datum
#   - Datentypen sind weniger flexibel als in Python
#   - Sie helfen, die Konsistenz und Genauigkeit der Daten zu
#     gewährleisten.

# %% [markdown]
#
# ## Das SQLite-Datenbanksystem
#
# - [SQLite](https://www.sqlite.org/) ist eine leichtgewichtige, dateibasierte
#   relationale Datenbank
#   - Streng genommen: ein Datenbanksystem (DBMS)
# - Sie ist in C geschrieben und benötigt keine separate Serverinstallation
#   - SQLite kann in Anwendungen eingebettet werden
# - SQLite ist ideal für kleine bis mittelgroße Anwendungen und
#   Entwicklungsumgebungen

# %% [markdown]
#
# ## Ausführen von SQLite
#
# - SQLite kann über die Kommandozeile oder in Python-Skripten verwendet werden
# - Um die SQLite-Shell zu starten, geben Sie `sqlite3` in der Kommandozeile ein
# - Um eine Datenbank zu erstellen oder zu öffnen, geben Sie den Namen der Datenbankdatei an
# - Beispiel:
# ```bash
# sqlite3 shop.db
# ```

# %% [markdown]
#
# ## DB-Browser für SQLite
#
# - Der DB-Browser für SQLite ist eine grafische Benutzeroberfläche zur
#   Verwaltung von SQLite-Datenbanken
# - Er ermöglicht das Erstellen, Bearbeiten und Abfragen von Datenbanken
# - Das ist oft einfacher als die Verwendung der Kommandozeile
#
# [DB-Browser für SQLite](https://sqlitebrowser.org/)

# %% [markdown]
#
# ## Beispiel: Erstellen einer Datenbank in DB-Browser für SQLite
#
# 1. Öffnen Sie DB-Browser für SQLite
# 2. Klicken Sie auf "Neue Datenbank"
# 3. Wählen Sie einen Speicherort aus und geben Sie `shop.sqlite` als Dateinamen
#    ein
# 4. Klicken Sie auf OK
#    - Es öffnet sich ein Fenster zum Erstellen einer Tabelle
# 5. Erstellen Sie eine Tabelle:
#    - Geben Sie den Tabellennamen `customers` ein
#    - Fügen Sie Felder hinzu:
#      - `id` (INTEGER)
#      - `name` (TEXT)
#      - `address` (TEXT)
# 6. Klicken Sie auf "OK" und dann auf "Änderungen schreiben"

# %% [markdown]
#
# ## Einfügen von Daten in eine Tabelle
#
# - Gehen Sie zum Reiter "Daten durchsuchen"
# - Klicken Sie auf das Icon zum Einfügen einer neuen Zeile
# - Geben Sie Werte für die Felder ein
#   - Sie können das direkt in der Tabelle tun
#   - Es empfiehlt sich, die Breite der Spalten anpassen, um mehr Platz zu haben
#   - Sie können Änderungen auch im Fenster "Datenbankzelle bearbeiten"
#     vornehmen
#   - Danach müssen Sie auf "Übernehmen" klicken, um die Änderungen in die
#     Tabelle zu übernehmen
# - Klicken Sie auf "Änderungen schreiben", um die Daten zu speichern


# %% [markdown]
#
# ## Workshop: Erstellen der Produkt-Tabelle
#
# Erstellen Sie die Tabelle `products` mit den folgenden Feldern:
# - `id` (`INTEGER`)
# - `product_name` (`TEXT`)
# - `price` (`REAL`)

# %% [markdown]
#
# Fügen Sie einige Produkte hinzu:
# - `id`: 2341, `product_name`: "Tomatensuppe", `price`: 1.99, `description`: "Leckere Tomatensuppe"
# - `id`: 346, `product_name`: "Kichererbsen", `price`: 0.59, `description`: "Gesunde Kichererbsen"

# %% [markdown]
#
# - Was passiert, wenn Sie versuchen, zwei Zeilen mit den gleichen Werten für
#   alle Felder einzufügen?
