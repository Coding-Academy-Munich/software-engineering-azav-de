# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Daten ändern und löschen (UPDATE/DELETE)</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# ## Aktualisieren von Daten
#
# - Der Befehl `UPDATE` wird verwendet, um bestehende Daten in einer Tabelle
#   zu ändern
# - Mit `SET` gibt man an, welche Spalten geändert werden sollen
# - Mit `WHERE` begrenzt man die Änderung auf bestimmte Zeilen
# - **Achtung:** Ohne `WHERE` werden alle Zeilen geändert!

# %% [markdown]
#
# ```sql
# UPDATE customers SET address = '789 Pine St' WHERE id = 1;
# ```

# %% [markdown]
#
# ### Mehrere Spalten aktualisieren
#
# - Man kann mehrere Spalten gleichzeitig aktualisieren:

# %% [markdown]
#
# ```sql
# UPDATE products SET price = 2.49, description = 'Neue Rezeptur' WHERE id = 2341;
# ```

# %% [markdown]
#
# ### Berechnete Werte
#
# - Man kann auch berechnete Werte verwenden:

# %% [markdown]
#
# ```sql
# UPDATE products SET price = price * 1.1;
# ```

# %% [markdown]
#
# ## Löschen von Zeilen
#
# - Der Befehl `DELETE FROM` wird verwendet, um Zeilen aus einer Tabelle zu
#   löschen
# - Die zu löschenden Zeilen werden oft mit einer `WHERE`-Klausel angegeben,
#   ähnlich der des Befehls `SELECT FROM`
# - **Achtung:** Ohne `WHERE` werden alle Zeilen gelöscht!

# %% [markdown]
#
# ```sql
# DELETE FROM customers WHERE name = 'Charlie';
# ```

# %% [markdown]
#
# ## Workshop: Daten aktualisieren und löschen
#
# Führen Sie die folgenden Aufgaben in DB Browser für SQLite aus:
#
# 1. Ändern Sie die Adresse des Kunden mit `id` 2 zu `'100 Main St'`
# 2. Erhöhen Sie den Preis aller Produkte um 10%
# 3. Fügen Sie einen neuen Kunden ein und löschen Sie ihn dann wieder
# 4. Überprüfen Sie nach jeder Änderung die Daten mit `SELECT`
#
# *Hinweis:*
# - Verwenden Sie `UPDATE ... SET ... WHERE ...` zum Aktualisieren
# - Verwenden Sie `DELETE FROM ... WHERE ...` zum Löschen
# - Vergessen Sie nicht, die Änderungen zu speichern

# %% [markdown]
#
# ```sql
# UPDATE customers SET address = '100 Main St' WHERE id = 2;
# SELECT * FROM customers;
# ```

# %% [markdown]
#
# ```sql
# UPDATE products SET price = price * 1.1;
# SELECT * FROM products;
# ```

# %% [markdown]
#
# ```sql
# INSERT INTO customers (name, address) VALUES ('Test User', 'Test St');
# SELECT * FROM customers;
# DELETE FROM customers WHERE name = 'Test User';
# SELECT * FROM customers;
# ```
