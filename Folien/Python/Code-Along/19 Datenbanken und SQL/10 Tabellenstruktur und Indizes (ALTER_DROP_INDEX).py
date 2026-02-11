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
# ## Tabellen löschen
#
# - Der Befehl `DROP TABLE` wird verwendet, um eine bestehende Tabelle aus einer
#   Datenbank zu entfernen
# - Dieser Befehl löscht dauerhaft alle Daten in der Tabelle, daher sollte er
#   mit Vorsicht verwendet werden
#
# ```sql
# DROP TABLE customers;
# ```

# %% [markdown]
#
# ## Indizes
#
# - Indizes werden verwendet, um die Leistung von Abfragen auf großen Tabellen
#   zu verbessern
# - Der Befehl `CREATE INDEX` wird verwendet, um einen neuen Index auf einer
#   oder mehreren Spalten in einer Tabelle zu erstellen
# - Indizes beschleunigen das Suchen, verlangsamen aber das Einfügen und
#   Aktualisieren

# %% [markdown]
#
# ```sql
# CREATE INDEX idx_customer_name ON customers(name);
# ```

# %% [markdown]
#
# ### Eindeutiger Index
#
# - Mit `UNIQUE` kann man sicherstellen, dass alle Werte in der indizierten
#   Spalte eindeutig sind:

# %% [markdown]
#
# ```sql
# CREATE UNIQUE INDEX idx_product_name ON products(product_name);
# ```

# %% [markdown]
#
# ## Workshop: Tabellenstruktur ändern
#
# 1. Fügen Sie der `customers`-Tabelle eine neue Spalte `email` (TEXT) hinzu
# 2. Aktualisieren Sie einige Kunden mit E-Mail-Adressen
# 3. Erstellen Sie einen Index auf der Spalte `name` der `customers`-Tabelle
# 4. Erstellen Sie eine neue Tabelle `test_table` und löschen Sie sie dann wieder
#
# *Hinweis:*
# - Verwenden Sie `ALTER TABLE ... ADD COLUMN ...` zum Hinzufügen
# - Verwenden Sie `CREATE INDEX` zum Erstellen eines Index
# - Verwenden Sie `DROP TABLE` zum Löschen der Test-Tabelle
