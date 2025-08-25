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
# ## Abrufen von Werten
#
# - `SELECT`:
#   - Der SELECT-Befehl wird verwendet, um Daten aus einer oder mehreren
#     Tabellen in einer Datenbank abzurufen
#   - Man kann angeben, welche Spalten abgerufen werden sollen, sowie
#     Bedingungen für Filterung der Ergebnisse angeben


# %% [markdown]
#
# ```sql
# SELECT * FROM customers;
# ```


# %% [markdown]
#
# - `FROM`:
#   - Die `FROM`-Klausel gibt an, aus welchen Tabellen Daten abgerufen werden
#     sollen.
#   - Man kann Daten aus mehreren Tabellen abrufen, indem man sie miteinander
#     verbindet

# %% [markdown]
# ```sql
# SELECT * FROM customers;
# ```

# %% [markdown]
#
# ```sql
# SELECT (name, address) FROM customers;
# ```

# %% [markdown]
# ```sql
# SELECT * FROM customers, orders;
# ```

# %% [markdown]
#
# - `WHERE`:
# - Die `WHERE`-Klausel wird verwendet, um die Ergebnisse einer
#   `SELECT`-Anweisung zu filtern
# - Man kann Vergleichsoperatoren (z.B.  `=`, `<`, `>`) und logische Operatoren
#   (z.B. `AND`, `OR`, `NOT`) verwenden, um die Bedingungen zu spezifizieren

# %% [markdown]
#
# ```sql
# SELECT * FROM customers where age > 18;
# ```

# %% [markdown]
#
# ```sql
# SELECT * FROM customers, orders WHERE customers.id = orders.customer_id;
# ```

# %% [markdown]
#
# ```sql
# SELECT (name, address, product_name, quantity)
#   FROM customers, orders, products
#   WHERE customers.id = orders.customer_id
#   AND products.id = orders.product_id;
# ```
