# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Berechnete Spalten und Unterabfragen</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# ### Berechnete Spalten
#
# - Wir können auch Berechnungen in der `SELECT`-Klausel durchführen:

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
# ### `DISTINCT`
#
# - Der `DISTINCT`-Operator wird verwendet, um doppelte Werte aus den Ergebnissen
#   einer `SELECT`-Anweisung zu entfernen

# %% [markdown]
#
# ```sql
# SELECT DISTINCT name, address
#   FROM customers
#   JOIN orders ON customers.id = orders.customer_id;
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
# ### Subqueries mit `IN` und `NOT IN`
#
# - Mit `IN` kann man prüfen, ob ein Wert in einer Liste von Werten enthalten ist
# - Die Liste kann auch das Ergebnis einer Unterabfrage sein

# %% [markdown]
#
# ```sql
# SELECT name, address
#   FROM customers
#   WHERE id IN (SELECT customer_id FROM orders);
# ```

# %% [markdown]
#
# - Mit `NOT IN` kann man Kunden finden, die keine Bestellungen aufgegeben haben:

# %% [markdown]
#
# ```sql
# SELECT name, address
#   FROM customers
#   WHERE id NOT IN (SELECT customer_id FROM orders);
# ```

# %% [markdown]
#
# ### `ORDER BY`
#
# - Die `ORDER BY`-Klausel wird verwendet, um die Ergebnisse einer
#   `SELECT`-Anweisung nach einer oder mehreren Spalten zu sortieren
# - Man kann angeben, ob die Daten in aufsteigender oder absteigender
#   Reihenfolge sortiert werden sollen (`ASC`, `DESC`)

# %% [markdown]
#
# ```sql
# SELECT name, address, product_name, quantity, price, quantity * price AS total_price
#   FROM customers, orders, products
#   WHERE customers.id = orders.customer_id
#   AND products.id = orders.product_id
#   ORDER BY total_price DESC;
# ```

# %% [markdown]
#
# ### `LIMIT`
#
# - Die `LIMIT`-Klausel wird verwendet, um die Anzahl der Ergebnisse, die von
#   einer `SELECT`-Anweisung zurückgegeben werden, zu begrenzen

# %% [markdown]
#
# ```sql
# SELECT name, address, product_name, quantity, price, quantity * price AS total_price
#   FROM customers, orders, products
#   WHERE customers.id = orders.customer_id
#   AND products.id = orders.product_id
#   ORDER BY total_price DESC
#   LIMIT 3;
# ```

# %% [markdown]
#
# ### `GROUP BY`
#
# - Die `GROUP BY`-Klausel wird verwendet, um die Ergebnisse einer
#   `SELECT`-Anweisung nach einer oder mehreren Spalten zu gruppieren
# - Man kann Aggregatfunktionen (z.B. `SUM`, `AVG`, `COUNT`) verwenden, um
#   Berechnungen mit den gruppierten Daten durchzuführen

# %% [markdown]
#
# ```sql
# SELECT name, SUM(quantity * price) AS total_price
#   FROM customers, orders, products
#   WHERE customers.id = orders.customer_id
#   AND products.id = orders.product_id
#   GROUP BY name;
# ```

# %% [markdown]
#
# ## Workshop: Fortgeschrittene SQL-Abfragen
#
# Erstellen Sie SQL-Abfragen, die folgende Ergebnisse zurückgeben:
#
# 1. Alle Bestellungen mit dem Gesamtpreis (`quantity * price`)
# 2. Die Namen aller Kunden, die Bestellungen aufgegeben haben (ohne Duplikate)
# 3. Alle Kunden, die **keine** Bestellung aufgegeben haben
# 4. Den Gesamtumsatz pro Kunde, absteigend nach Umsatz sortiert
# 5. Die drei Kunden mit dem höchsten Gesamtumsatz
#
# *Hinweis:*
# - Verwenden Sie `DISTINCT`, um Duplikate zu entfernen
# - Verwenden Sie `NOT IN` mit einer Unterabfrage für Aufgabe 3
# - Verwenden Sie `SUM()` mit `GROUP BY` für den Gesamtumsatz
# - Verwenden Sie `ORDER BY ... DESC` und `LIMIT` für die Top 3

# %% [markdown]
#
# ```sql
# SELECT name, product_name, quantity, price, quantity * price AS total_price
#   FROM customers
#   JOIN orders ON customers.id = orders.customer_id
#   JOIN products ON products.id = orders.product_id;
# ```

# %% [markdown]
#
# ```sql
# SELECT DISTINCT name
#   FROM customers
#   JOIN orders ON customers.id = orders.customer_id;
# ```

# %% [markdown]
#
# ```sql
# SELECT name, address
#   FROM customers
#   WHERE id NOT IN (SELECT customer_id FROM orders);
# ```

# %% [markdown]
#
# ```sql
# SELECT name, SUM(quantity * price) AS total_sales
#   FROM customers, orders, products
#   WHERE customers.id = orders.customer_id
#   AND products.id = orders.product_id
#   GROUP BY name
#   ORDER BY total_sales DESC;
# ```

# %% [markdown]
#
# ```sql
# SELECT name, SUM(quantity * price) AS total_sales
#   FROM customers, orders, products
#   WHERE customers.id = orders.customer_id
#   AND products.id = orders.product_id
#   GROUP BY name
#   ORDER BY total_sales DESC
#   LIMIT 3;
# ```
