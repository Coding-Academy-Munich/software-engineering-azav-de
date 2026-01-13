# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Einführung in SQL (Teil 4)</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# - `GROUP BY`:
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
# ## Workshop: SQL-Abfragen
#
# - Fügen Sie zur `customers`-Tabelle einige neue Kunden hinzu
# - Fügen Sie zur `products`-Tabelle einige neue Produkte hinzu
# - Erstellen Sie SQL-Abfragen, die folgende Ergebnisse zurückgeben:
#   1. Den Namen und Gesamtumsatz eines bestimmten Kunden
#   2. Die Namen und den Umsatz aller Kunden, die eine Bestellung aufgegeben
#      haben
#   3. Die Namen der drei Kunden mit dem höchsten Gesamtumsatz

# %% [markdown]
#
# ```sql
# SELECT name, SUM(quantity * price) AS total_sales
#   FROM customers, orders, products
#   WHERE customers.id = orders.customer_id
#   AND products.id = orders.product_id
#   AND customers.id = 1
#   GROUP BY name;
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
