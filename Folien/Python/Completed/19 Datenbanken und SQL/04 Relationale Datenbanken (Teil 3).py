# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Relationale Datenbanken (Teil 3)</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# ## Fremdschlüssel und Beziehungen
#
# - Wir brauchen oft Beziehungen zwischen Tabellen, um Daten zu verknüpfen
#   - Beispiel: Bestellung benötigt Kunden- und Produktinformationen
# - Wie können wir eindeutig eine Zeile in einer anderen Tabelle referenzieren?
# - Wir merken uns den Primärschlüssel!
# - Dazu fügen wir eine Spalte in der Tabelle hinzu, die den Primärschlüssel der
#   anderen Tabelle referenziert
# - Das nennen wir einen Fremdschlüssel

# %% [markdown]
#
# Table **Orders**:
#
# | order_id | customer_id | item_id | quantity |
# |----------|-------------|---------|----------|
# |        1 |           1 |    2341 |        2 |
# |        2 |           2 |  939504 |        1 |
# |        3 |           1 |     346 |        3 |
# |        4 |           1 |    2341 |        2 |
#
# - `order_id` ist der Primärschlüssel
# - `customer_id` ist ein Fremdschlüssel, der auf die Tabelle **Kunden** verweist
# - `item_id` ist ein Fremdschlüssel, der auf die Tabelle **Produkte** verweist

