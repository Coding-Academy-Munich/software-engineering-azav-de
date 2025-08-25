# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Einführung in SQL (Teil 5)</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# ## Löschen von Zeilen
#
# - Der Befehl `DELETE FROM` wird verwendet, um Zeilen aus einer Tabelle zu
#   löschen
# - Die zu löschenden Zeilen werden oft mit einer `WHERE`-Klausel angegeben,
#   ähnlich der des Befehls `SELECT FROM`
#
# ```sql
# DELETE FROM customers WHERE name = 'Charlie';
# ```
