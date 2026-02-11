# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Daten abfragen (SELECT)</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# ## `SELECT` Abfragen
#
# - Mit `SELECT` Abfragen kann man Daten aus einer oder mehreren Tabellen in
#   einer Datenbank abrufen
# - Man kann angeben, welche Spalten abgerufen werden sollen, sowie Bedingungen
#   für die Filterung der Ergebnisse angeben
# - Das Ergebnis der Abfrage ist eine Tabelle mit den angeforderten Daten


# %% [markdown]
#
# ### Alle Daten aus einer Tabelle abrufen
#
# - `SELECT *` gibt alle Spalten zurück
# - `FROM customers` gibt an, aus welcher Tabelle die Daten kommen

# %% [markdown]
#
# ```sql
# SELECT * FROM customers;
# ```

# %% [markdown]
#
# ### Bestimmte Spalten auswählen
#
# - Man kann auch nur bestimmte Spalten auswählen:

# %% [markdown]
#
# ```sql
# SELECT name, address FROM customers;
# ```

# %% [markdown]
#
# ### Spalten-Aliase
#
# - Wir können Spalten mit `AS` einen Alias geben:

# %% [markdown]
# ```sql
# SELECT id, name, address FROM customers;
# ```

# %% [markdown]
# ```sql
# SELECT id AS customer_id, name AS customer_name, address AS customer_address
#   FROM customers;
# ```

# %% [markdown]
#
# ### Die `WHERE`-Klausel
#
# - Die `WHERE`-Klausel wird verwendet, um die Ergebnisse einer
#   `SELECT`-Anweisung zu filtern
# - Man kann Vergleichsoperatoren (z.B.  `=`, `<`, `>`) und logische Operatoren
#   (z.B. `AND`, `OR`, `NOT`) verwenden, um die Bedingungen zu spezifizieren

# %% [markdown]
#
# ```sql
# SELECT * FROM orders WHERE quantity >= 2;
# ```

# %% [markdown]
#
# ### Daten aus mehreren Tabellen verbinden
#
# - Wenn wir Daten aus mehreren Tabellen brauchen, können wir sie verbinden
# - Dazu geben wir in der `WHERE`-Klausel an, welche Spalten übereinstimmen
#   sollen
# - Wenn Spaltennamen in mehreren Tabellen vorkommen, verwenden wir
#   `tabellenname.spaltenname`

# %% [markdown]
#
# ```sql
# SELECT * FROM customers, orders WHERE customers.id = orders.customer_id;
# ```


# %% [markdown]
#
# ### `JOIN`: Tabellen explizit verbinden
#
# - Statt Tabellen mit Komma und `WHERE` zu verbinden, kann man die
#   `JOIN`-Klausel verwenden
# - `JOIN` macht deutlich, welche Tabellen verbunden werden und wie
# - Die Bedingung für die Verbindung wird mit `ON` angegeben
# - `JOIN` ist die empfohlene Schreibweise

# %% [markdown]
# ```sql
# SELECT customers.id AS customer_id, orders.id AS order_id
#   FROM customers
#   JOIN orders ON customers.id = orders.customer_id;
# ```


# %% [markdown]
#
# ### Drei Tabellen verbinden
#
# - Man kann auch mehr als zwei Tabellen verbinden
# - Hier verbinden wir Kunden, Bestellungen und Produkte:

# %% [markdown]
#
# ```sql
# SELECT name, address, product_name, quantity, price
#   FROM customers, orders, products
#   WHERE customers.id = orders.customer_id
#   AND products.id = orders.product_id;
# ```

# %% [markdown]
#
# ### Dasselbe mit `JOIN`
#
# - Die gleiche Abfrage mit der empfohlenen `JOIN`-Syntax:

# %% [markdown]
#
# ```sql
# SELECT name, address, product_name, quantity, price
#   FROM customers
#   JOIN orders ON customers.id = orders.customer_id
#   JOIN products ON products.id = orders.product_id;
# ```

# %% [markdown]
#
# ## Workshop: Einfache SQL-Abfragen
#
# Erstellen Sie SQL-Abfragen, die folgende Ergebnisse zurückgeben:
#
# 1. Alle Kunden mit ihren Bestellungen (Name, Adresse, Produktname, Menge)
# 2. Alle Bestellungen von 'John Smith' (Name, Produktname, Menge)
# 3. Alle Produkte, die der Kunde mit der ID 2 bestellt hat (Produktname, Preis)
#
# *Hinweis:*
# - Verwenden Sie `JOIN` oder die `WHERE`-Klausel zum Verbinden von Tabellen
# - Verwenden Sie `WHERE` zum Filtern
