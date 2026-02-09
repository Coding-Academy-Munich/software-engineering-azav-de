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
# ## Workshop: SQL-Abfragen
#
# - Fügen Sie zur `customers`-Tabelle einige neue Kunden hinzu
# - Fügen Sie zur `products`-Tabelle einige neue Produkte hinzu
# - Erstellen Sie SQL-Abfragen, die folgende Ergebnisse zurückgeben:
#   1. Den Namen und Gesamtumsatz eines bestimmten Kunden
#   2. Die Namen und den Umsatz aller Kunden, die eine Bestellung aufgegeben
#      haben, absteigend nach Umsatz sortiert
#   3. Die Namen der drei Kunden mit dem höchsten Gesamtumsatz
#
# *Hinweis:*
# - Verwenden Sie `SUM()` mit `GROUP BY` für den Gesamtumsatz
# - Verwenden Sie `ORDER BY ... DESC` zum Sortieren
# - Verwenden Sie `LIMIT` zur Begrenzung der Ergebnisse
