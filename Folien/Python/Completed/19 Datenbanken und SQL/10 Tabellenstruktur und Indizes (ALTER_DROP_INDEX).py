# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Tabellenstruktur und Indizes (ALTER/DROP/INDEX)</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# ## Tabellen nachträglich ändern (ALTER TABLE)
#
# - Der Befehl `ALTER TABLE` ändert die Struktur einer bestehenden Tabelle
# - SQLite unterstützt nur vier Operationen:
#   - `RENAME TABLE` — Tabelle umbenennen
#   - `RENAME COLUMN` — Spalte umbenennen
#   - `ADD COLUMN` — Spalte hinzufügen
#   - `DROP COLUMN` — Spalte entfernen
# - **Nicht möglich** in SQLite: Spaltentyp ändern, Constraints nachträglich
#   hinzufügen oder entfernen

# %% [markdown]
#
# ## Spalte hinzufügen (ADD COLUMN)
#
# - `ADD COLUMN` fügt eine neue Spalte zu einer bestehenden Tabelle hinzu
# - Alle bestehenden Zeilen erhalten `NULL` in der neuen Spalte
# - Optional kann ein Standardwert mit `DEFAULT` angegeben werden

# %% [markdown]
#
# ```sql
# ALTER TABLE customers ADD COLUMN email TEXT;
# SELECT * FROM customers;
# ```


# %% [markdown]
#
# ## Standardwerte und NOT NULL
#
# - Eine neue Spalte kann einen `DEFAULT`-Wert haben
# - Wenn der Standardwert angegeben wird, erhalten bestehende Zeilen diesen Wert
#   statt `NULL`
# - Wenn eine neue Spalte `NOT NULL` sein soll, **muss** ein `DEFAULT` angegeben
#   werden
# - Ohne `DEFAULT` würde SQLite einen Fehler ausgeben, da bestehende Zeilen `NULL`
#   hätten

# %% [markdown]
#
# ```sql
# ALTER TABLE products ADD COLUMN in_stock INTEGER NOT NULL DEFAULT 1;
# SELECT * FROM products;
# ```


# %% [markdown]
#
# ## Tabellen und Spalten umbenennen
#
# - `RENAME TO` ändert den Tabellennamen
# - `RENAME COLUMN` ändert den Namen einer Spalte
# - Die Daten in der Tabelle werden dabei nicht verändert

# %% [markdown]
#
# ```sql
# ALTER TABLE customers RENAME TO clients;
# ALTER TABLE clients RENAME COLUMN name TO full_name;
# SELECT * FROM clients;
# ```


# %% [markdown]
#
# ## Spalte entfernen (DROP COLUMN)
#
# - `DROP COLUMN` entfernt eine Spalte und alle ihre Daten
# - Dieser Vorgang kann **nicht rückgängig** gemacht werden
# - **Einschränkungen:** Man kann keine Spalten entfernen, die Teil eines
#   Primärschlüssels, eines Index oder eines Fremdschlüssels sind

# %% [markdown]
#
# ```sql
# ALTER TABLE customers DROP COLUMN email;
# ```


# %% [markdown]
#
# ## Tabellen löschen (DROP TABLE)
#
# - `DROP TABLE` löscht eine Tabelle und **alle ihre Daten** dauerhaft
# - Es gibt **kein Rückgängigmachen** — die Daten sind unwiderruflich verloren
# - `IF EXISTS` verhindert einen Fehler, wenn die Tabelle nicht existiert
# - **Vorsicht** bei Tabellen, auf die andere Tabellen per Fremdschlüssel
#   verweisen — die verweisenden Tabellen können danach inkonsistent sein

# %% [markdown]
#
# ```sql
# DROP TABLE IF EXISTS test_table;
# ```


# %% [markdown]
#
# ## Was sind Indizes?
#
# - Ein Index ist wie das Stichwortverzeichnis in einem Buch — er hilft, Daten
#   schneller zu finden
# - Ohne Index muss die Datenbank jede Zeile einzeln durchsuchen (langsam bei
#   großen Tabellen)
# - Mit einem Index kann die Datenbank direkt zu den passenden Zeilen springen
# - Primärschlüssel haben automatisch einen Index

# %% [markdown]
#
# ## Index erstellen (CREATE INDEX)
#
# - `CREATE INDEX` erstellt einen Index auf einer oder mehreren Spalten
# - `IF NOT EXISTS` verhindert einen Fehler, wenn der Index schon existiert
# - Konvention für den Namen: `idx_tabellenname_spaltenname`

# %% [markdown]
#
# ```sql
# CREATE INDEX IF NOT EXISTS idx_customer_name ON customers(name);
# ```


# %% [markdown]
#
# ## Wann Indizes verwenden?
#
# - Verwenden Sie Indizes auf Spalten, die Sie häufig suchen oder filtern
#   (`WHERE`, `JOIN`)
# - Indizes beschleunigen das **Lesen**, verlangsamen aber das **Schreiben**
#   (`INSERT`, `UPDATE`, `DELETE`)
# - Erstellen Sie **nicht** auf jeder Spalte einen Index — nur dort, wo es hilft
# - Kleine Tabellen (wenige hundert Zeilen) brauchen normalerweise keine
#   zusätzlichen Indizes

# %% [markdown]
#
# ## Eindeutiger Index (UNIQUE INDEX)
#
# - Ein `UNIQUE`-Index stellt sicher, dass keine zwei Zeilen den gleichen Wert
#   in dieser Spalte haben
# - Der Versuch, einen doppelten Wert einzufügen, führt zu einem Fehler
# - **Ausnahme:** `NULL`-Werte gelten als unterschiedlich — mehrere `NULL`s sind
#   erlaubt
# - Nützlich für Spalten wie E-Mail-Adressen oder Benutzernamen

# %% [markdown]
#
# ```sql
# CREATE UNIQUE INDEX idx_customer_email ON customers(email);
# ```


# %% [markdown]
#
# ## Zusammengesetzte Indizes und Indizes löschen
#
# - Ein zusammengesetzter Index umfasst mehrere Spalten
# - Nützlich, wenn häufig nach einer Kombination von Spalten gesucht wird
# - `DROP INDEX` entfernt einen Index (die Daten in der Tabelle bleiben
#   unverändert)

# %% [markdown]
#
# ```sql
# CREATE INDEX idx_orders_cust_prod ON orders(customer_id, product_id);
# DROP INDEX IF EXISTS idx_orders_cust_prod;
# ```


# %% [markdown]
#
# ## Vorhandene Indizes anzeigen
#
# - `PRAGMA index_list(tabellenname)` zeigt alle Indizes einer Tabelle
# - `PRAGMA index_info(indexname)` zeigt, welche Spalten ein Index umfasst
# - In DB Browser: Indizes sind auch im Reiter "Datenbankstruktur" sichtbar

# %% [markdown]
#
# ```sql
# PRAGMA index_list(customers);
# ```


# %% [markdown]
#
# ## Workshop: Tabellenstruktur ändern und Indizes verwenden
#
# 1. Fügen Sie der `customers`-Tabelle eine neue Spalte `email` (TEXT) hinzu.
#    Überprüfen Sie das Ergebnis mit `SELECT`
# 2. Fügen Sie der `products`-Tabelle eine Spalte `in_stock` (INTEGER, NOT NULL,
#    DEFAULT 1) hinzu. Überprüfen Sie, dass der Standardwert bei allen bestehenden
#    Produkten gesetzt wurde
# 3. Benennen Sie die Spalte `address` in der `customers`-Tabelle in
#    `street_address` um
# 4. Erstellen Sie einen UNIQUE-Index auf `customers(email)`. Setzen Sie
#    verschiedene E-Mail-Adressen für einige Kunden. Versuchen Sie dann, zwei
#    Kunden die gleiche E-Mail-Adresse zu geben — beobachten Sie den Fehler
# 5. Erstellen Sie einen zusammengesetzten Index auf
#    `orders(customer_id, product_id)`. Überprüfen Sie mit
#    `PRAGMA index_list(orders)`, ob der Index existiert
# 6. Erstellen Sie eine neue Tabelle `test_table` und löschen Sie sie dann mit
#    `DROP TABLE IF EXISTS`

# %% [markdown]
#
# ### Lösung / Solution
#
# **1. Spalte email hinzufügen / Add email column:**
#
# ```sql
# ALTER TABLE customers ADD COLUMN email TEXT;
# SELECT * FROM customers;
# ```

# %% [markdown]
#
# **2. Spalte in_stock mit Standardwert / Add in_stock column with default:**
#
# ```sql
# ALTER TABLE products ADD COLUMN in_stock INTEGER NOT NULL DEFAULT 1;
# SELECT * FROM products;
# ```

# %% [markdown]
#
# **3. Spalte umbenennen / Rename column:**
#
# ```sql
# ALTER TABLE customers RENAME COLUMN address TO street_address;
# SELECT * FROM customers;
# ```

# %% [markdown]
#
# **4. UNIQUE-Index und Fehler testen / UNIQUE index and error test:**
#
# ```sql
# CREATE UNIQUE INDEX idx_customer_email ON customers(email);
# UPDATE customers SET email = 'john@example.com' WHERE id = 1;
# UPDATE customers SET email = 'jane@example.com' WHERE id = 2;
# -- This causes an error (duplicate email):
# -- UPDATE customers SET email = 'john@example.com' WHERE id = 3;
# ```

# %% [markdown]
#
# **5. Zusammengesetzter Index / Composite index:**
#
# ```sql
# CREATE INDEX idx_orders_cust_prod ON orders(customer_id, product_id);
# PRAGMA index_list(orders);
# ```

# %% [markdown]
#
# **6. Tabelle erstellen und löschen / Create and drop table:**
#
# ```sql
# CREATE TABLE test_table (id INTEGER PRIMARY KEY, data TEXT);
# DROP TABLE IF EXISTS test_table;
# -- Verify it's gone (no error because of IF EXISTS):
# DROP TABLE IF EXISTS test_table;
# ```
