# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Daten einfügen (INSERT)</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

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
# ## Einfügen von Zeilen
#
# - Der Befehl `INSERT INTO` wird verwendet, um Daten in eine Tabelle
#   einzufügen.
# - Er benötigt die Namen der Spalten und die Werte, die eingefügt werden
#   sollen.
#   - Textwerte müssen in einfache Anführungszeichen gesetzt werden.
# - Wenn Spalten nicht angegeben werden:
#   - Für `AUTOINCREMENT` Spalten wird der Wert automatisch generiert
#   - Andernfalls wird `NULL` eingefügt
#   - Ist eine Spalte als `NOT NULL` definiert, schlägt das Einfügen fehl


# %% [markdown]
#
# ```sql
# INSERT INTO customers (name, address) VALUES ('John Smith', '123 Elm St');
# ```

# %% [markdown]
#
# ```sql
# -- Error: NOT NULL constraint failed: customers.address
# INSERT INTO customers (address) VALUES ('456 Oak St');
# -- OK
# INSERT INTO customers (name) VALUES ('Jane Doe');
# ```

# %% [markdown]
#
# ## Workshop: Daten einfügen
#
# - Fügen Sie mit SQL-Befehlen die gleichen Daten wie in den vorherigen
#   Workshops in die Tabellen ein.
# - Achten Sie darauf, die `NOT NULL`-Bedingungen zu beachten.

# %% [markdown]
#
# Tabelle `customers`:
#
# | id | name         | address      |
# |----|--------------|--------------|
# |  1 | John Smith   | 123 Elm St   |
# |  2 | Jane Doe     | 456 Oak St   |
# |  3 | John Smith   | 789 Maple St |
#
# Tabelle `products`:
#
# | id     | product_name | price | description                                |
# |--------|--------------|-------|--------------------------------------------|
# |   2341 | Tomatensuppe | 1.99  | Unsere fantastische Tomatensuppe in Dosen. |
# | 939504 | Tomatensuppe | 2.49  | Premium-Tomatensuppe in Glasflaschen.      |
# |    346 | Kichererbsen | 0.59  | In Wasser einweichen und genießen...       |
#
# Tabelle `orders`:
#
# | id | customer_id | product_id | quantity |
# |----|-------------|------------|----------|
# |  1 |           1 |       2341 |        2 |
# |  2 |           2 |     939504 |        1 |
# |  3 |           1 |        346 |        3 |
# |  4 |           1 |       2341 |        2 |
