# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Einführung in SQL</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# - SQL steht für Structured Query Language (strukturierte Abfragesprache)
# - SQL ist eine Programmiersprache zur Verwaltung und Manipulation von Daten in
#   einer relationalen Datenbank
# - SQL wird verwendet, um Tabellen und Daten in einer Datenbank zu erstellen,
#   zu ändern und abzufragen

# %% [markdown]
#
# ## Erstellen von Tabellen
#
# - Erinnerung: In einer relationalen Datenbank werden Daten in Tabellen
#   organisiert
# - Jede Tabelle besteht aus Zeilen und Spalten, wobei jede Zeile einen
#   Datensatz und jede Spalte ein Attribut des Datensatzes darstellt
# - Um Daten in einer Datenbank zu speichern, müssen wir zunächst eine Tabelle
#   erstellen
# - Diesen Teil von SQL nennt man Data Definition Language (DDL)

# %% [markdown]
#
# Tabelle **Customers**:
# | id | name   | email              |
# |----|--------|--------------------|
# | 1  | Alice  | alice@example.com  |
# | 2  | Bob    | bob@example.com    |
# | 3  | Charlie| charlie@example.com|

# %% [markdown]
#
# ## Tabellen erstellen
#
# - Der Befehl `CREATE TABLE` wird verwendet, um eine neue Tabelle in einer
#   Datenbank zu erstellen.
# - Man muss den Tabellennamen sowie die Spalten und Datentypen für die Tabelle
#   angeben
#
# ```sql
# CREATE TABLE customers (
#   id INTEGER PRIMARY KEY,
#   name TEXT NOT NULL,
#   email TEXT NOT NULL UNIQUE
# );
# ```

# %% [markdown]
#
# ## Verwalten von Daten
#
# - Mit unseren Kundendaten wollen wir verschiedene Operationen durchführen:
#   - Neue Kunden hinzufügen
#   - Daten abfragen (z.B. alle Kunden anzeigen)
#   - Bestehende Kunden aktualisieren (z.B. E-Mail-Adresse ändern)
#   - Kunden löschen
# - Diese Operationen werden in SQL als Data Manipulation Language (DML)
#   bezeichnet

# %% [markdown]
#
# ## Abrufen von Werten
#
# - `SELECT`:
#   - Der SELECT-Befehl wird verwendet, um Daten aus einer oder mehreren
#     Tabellen in einer Datenbank abzurufen
#   - Man kann angeben, welche Spalten abgerufen werden sollen, sowie
#     Bedingungen für Filterung der Ergebnisse angeben

# %% [markdown]
#
# ## Einfügen von Zeilen
#
# - Der Befehl `INSERT INTO` wird verwendet, um Daten in eine Tabelle einzufügen.
# - Er benötigt die Namen der Spalten und die Werte, die eingefügt werden sollen:
#
#  ```sql
# INSERT INTO customers (name, email) VALUES ('Alice', 'alice@example.com');
# ```


# %% [markdown]
#
# - `FROM`:
#   - Die `FROM`-Klausel gibt an, aus welchen Tabellen Daten abgerufen werden
#     sollen.
#   - Man kann Daten aus mehreren Tabellen abrufen, indem man sie miteinander
#     verbindet

# %% [markdown]
#
# - `WHERE`:
# - Die `WHERE`-Klausel wird verwendet, um die Ergebnisse einer
#   `SELECT`-Anweisung zu filtern
# - Man kann Vergleichsoperatoren (z.B.  `=`, `<`, `>`) und logische Operatoren
#   (z.B. `AND`, `OR`, `NOT`) verwenden, um die Bedingungen zu spezifizieren
#
#  ```sql
# SELECT * FROM customers where age > 18;
# ```

# %% [markdown]
#
# - `GROUP BY`:
# - Die `GROUP BY`-Klausel wird verwendet, um die Ergebnisse einer
#   `SELECT`-Anweisung nach einer oder mehreren Spalten zu gruppieren
# - Man kann Aggregatfunktionen (z.B. `SUM`, `AVG`, `COUNT`) verwenden, um
#   Berechnungen mit den gruppierten Daten durchzuführen

# %% [markdown]
#
# - `ORDER BY`:
# - Die `ORDER BY`-Klausel wird verwendet, um die Ergebnisse einer
#   `SELECT`-Anweisung nach einer oder mehreren Spalten zu sortieren
# - Man kann angeben, ob die Daten in aufsteigender oder absteigender
#   Reihenfolge sortiert werden sollen (`ASC`, `DESC`)

# %% [markdown]
#
# - `LIMIT`:
# - Die `LIMIT`-Klausel wird verwendet, um die Anzahl der Ergebnisse , die von
#   einer `SELECT` Anweisung zurückgegeben werden, zu begrenzen

# %% [markdown]
#
# ## Löschen von Zeilen
#
# - Der Befehl `DELETE FROM` wird verwendet, um Zeilen aus einer Tabelle zu
#   löschen
# - Die zu löschenden Zeilen werden oft mit einer `WHERE`-Klausel angegeben,
#   ähnlich der des Befehls `SELECT FROM`
#
# ```sql
# DELETE FROM customers WHERE name = 'Charlie';
# ```

# %% [markdown]
#
# ## Ändern von Tabellen
#
# - Der Befehl `ALTER TABLE` wird verwendet, um die Struktur einer bestehenden
#   Tabelle zu ändern
# - Man kann Spalten in einer Tabelle hinzufügen, ändern oder löschen, sowie
#   Beschränkungen für die Daten in der Tabelle einführen oder löschen
#
# ```sql
# ALTER TABLE customers ADD COLUMN age INTEGER;
# ```

# %% [markdown]
#
# ## Tabellen löschen:
#
# - Der Befehl `DROP TABLE` wird verwendet, um eine bestehende Tabelle aus einer
#   Datenbank zu entfernen
# - Dieser Befehl löscht dauerhaft alle Daten in der Tabelle, daher sollte er
#   mit mit Vorsicht verwendet werden
#
# ```sql
# DROP TABLE customers;
# ```

# %% [markdown]
#
# ## Indizes
#
# - Indizes werden verwendet, um die Leistung von Abfragen auf großen Tabellen
#   zu verbessern.
# - Der Befehl `CREATE INDEX` wird verwendet, um einen neuen Index auf einer
#   oder mehreren Spalten in einer Tabelle zu erstellen
# - Man kann angeben, ob der Index eindeutig sein soll und ob er aufsteigend
#   oder absteigend sortiert werden soll

# %% [markdown]
# ```sqlite
# $ sqlite3 shop.db
#
# -- create a new table
# sqlite> CREATE TABLE customers (
#    ...> id INTEGER PRIMARY KEY,
#    ...> name TEXT NOT NULL,
#    ...> email TEXT NOT NULL UNIQUE
#    ...> );
#
# -- add some data to the table
# sqlite> INSERT INTO customers (name, email) VALUES ('Alice', 'alice@example.com');
# sqlite> INSERT INTO customers (name, email) VALUES ('Bob', 'bob@example.com');
# sqlite> INSERT INTO customers (name, email) VALUES ('Charlie', 'charlie@example.com');
#
# -- display the contents of the table
# sqlite> SELECT * FROM customers;
# 1|Alice|alice@example.com
# 2|Bob|bob@example.com
# 3|Charlie|charlie@example.com
#
# -- add a new column to the table
# sqlite> ALTER TABLE customers ADD COLUMN age INTEGER;
#
# -- update some data in the table
# sqlite> UPDATE customers SET age = 25 WHERE name = 'Alice';
#
# -- delete a row from the table
# sqlite> DELETE FROM customers WHERE name = 'Charlie';
#
# -- display the updated contents of the table
# sqlite> SELECT * FROM customers;
# 1|Alice|alice@example.com|25
# 2|Bob|bob@example.com|
#
# -- exit the SQLite3 shell
# sqlite> .exit
# ```
