# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Einführung in SQL (Teil 3)</b>
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
# ### Die `FROM`-Klausel
#
# - Die `FROM`-Klausel gibt an, aus welchen Tabellen Daten abgerufen werden
#   sollen.
#   - Das kann eine Tabelle aus der Datenbank, oder das Ergebnis einer
#     `SELECT`-Abfrage sein.
# - Man kann Daten aus mehreren Tabellen abrufen, indem man sie miteinander
#   verbindet.

# %% [markdown]
# ```sql
# SELECT * FROM customers;
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
# ### Spalten-Aliase
#
# - Wenn Spalten in verschiedenen Tabellen den gleichen Namen haben, können wir
#   ihnen mit `AS` einen Alias geben:

# %% [markdown]
# ```sql
# SELECT customers.id, orders.id
#   FROM customers, orders
#   WHERE customers.id = orders.customer_id;
# ```

# %% [markdown]
# ```sql
# SELECT customers.id AS customer_id, orders.id AS order_id
#   FROM customers, orders
#   WHERE customer_id = orders.customer_id;
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
# ### Berechnete Spalten
#
# - Wir können auch Berechnungen in der `SELECT`-Klausel durchführen:

# %% [markdown]
#
# ```sql
# SELECT name, address, product_name, quantity, price, quantity * price AS total_price
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
# SELECT name, address, product_name, quantity, price, quantity * price AS total_price
#   FROM customers
#   JOIN orders ON customers.id = orders.customer_id
#   JOIN products ON products.id = orders.product_id;
# ```

# %% [markdown]
#
# ### Unterabfragen (Subqueries)
#
# - Man kann auch das Ergebnis einer `SELECT`-Abfrage als Tabelle verwenden
# - Solche verschachtelten Abfragen nennt man Unterabfragen (Subqueries)

# %% [markdown]
#
# ```sql
# SELECT name, total_price
#   FROM (SELECT customer_id, quantity * price AS total_price
#     FROM orders
#     JOIN products ON products.id = orders.product_id) AS subquery
#   JOIN customers ON customers.id = subquery.customer_id;
# ```


# %% [markdown]
#
# ### `DISTINCT`
#
# - Der `DISTINCT`-Operator wird verwendet, um doppelte Werte aus den Ergebnissen
#   einer `SELECT`-Anweisung zu entfernen

# %% [markdown]
#
# ```sql
# SELECT DISTINCT name, address
#   FROM customers, orders
#   WHERE customers.id = orders.customer_id;
# ```


# %% [markdown]
#
# ## Workshop: SQL-Abfragen
#
# - Fügen Sie zur `customers`-Tabelle einige neue Kunden hinzu
# - Fügen Sie zur `products`-Tabelle einige neue Produkte hinzu
# - Erstellen Sie SQL-Abfragen, die folgende Ergebnisse zurückgeben:
#   1. Die Namen und Adressen aller Kunden, die Bestellungen aufgegeben haben
#   2. Die Namen und Preise aller Produkte, die verkauft wurden
#   3. Den ID und den Gesamtpreis jeder Bestellung des Kunden mit der (Kunden-)ID 1
#
# *Hinweis:*
# - Sie können `JOIN` oder die `WHERE`-Klausel zum Verbinden von Tabellen
#   verwenden
# - Verwenden Sie `DISTINCT`, um doppelte Ergebnisse zu vermeiden

# %% [markdown]
#
# ```sql
# INSERT INTO customers (name, address) VALUES ('David Parker', '587 Oak St');
# INSERT INTO customers (name, address) VALUES ('Emma Wilson', '123 Maple Ave');
# INSERT INTO products (product_name, price) VALUES ('Widget', 19.99);
# INSERT INTO products (product_name, price) VALUES ('Gadget', 29.99);
# ```

# %% [markdown]
#
# ```sql
# SELECT DISTINCT name, address
#   FROM customers, orders
#   WHERE customers.id = orders.customer_id;
# -- Alternative
# SELECT DISTINCT name, address
#   FROM customers
#   WHERE id IN (SELECT customer_id FROM orders);
# ```

# %% [markdown]
#
# Die zweite Variante (Subquery) erlaubt es uns, Kunden zu finden, die nicht
# bestellt haben:

# %% [markdown]
#
# ```sql
# SELECT DISTINCT name, address
#   FROM customers
#   WHERE id NOT IN (SELECT customer_id FROM orders);
# ```


# %% [markdown]
#
# ```sql
# SELECT DISTINCT product_name, price
#   FROM products, orders
#   WHERE products.id = orders.product_id;
# -- Alternative
# SELECT DISTINCT product_name, price
#   FROM products
#   WHERE id IN (SELECT product_id FROM orders);
# ```

# %% [markdown]
#
# ```sql
# SELECT orders.id, quantity * price AS total_price
#   FROM orders, products
#   WHERE orders.product_id = products.id
#   AND orders.customer_id = 1;
# ```
