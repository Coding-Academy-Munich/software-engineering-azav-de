# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Einführung in SQL (Teil 6)</b>
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
# ## Tabellen löschen:
#
# - Der Befehl `DROP TABLE` wird verwendet, um eine bestehende Tabelle aus einer
#   Datenbank zu entfernen
# - Dieser Befehl löscht dauerhaft alle Daten in der Tabelle, daher sollte er
#   mit mit Vorsicht verwendet werden
#
# ```sql
# DROP TABLE customers;
# ```

# %% [markdown]
#
# ## Indizes
#
# - Indizes werden verwendet, um die Leistung von Abfragen auf großen Tabellen
#   zu verbessern.
# - Der Befehl `CREATE INDEX` wird verwendet, um einen neuen Index auf einer
#   oder mehreren Spalten in einer Tabelle zu erstellen
# - Man kann angeben, ob der Index eindeutig sein soll und ob er aufsteigend
#   oder absteigend sortiert werden soll
