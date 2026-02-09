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
# ## Warum sind Primärschlüssel wichtig?
#
# - Primärschlüssel gewährleisten die Eindeutigkeit von Datensätzen in einer Tabelle
# - Sie ermöglichen die effiziente Identifizierung und den Zugriff auf Daten
# - Sie werden verwendet, um Beziehungen zwischen Tabellen herzustellen
#   - Spalten, die den Primärschlüssel einer anderen Tabelle referenzieren,
#     nennt man Fremdschlüssel

# %% [markdown]
#
# ## Beispiel: Bestellungen
#
# - Wie können wir eine Bestellung in unserer Datenbank speichern?
#   - Der Einfachheit halber nehmen wir an, dass eine Bestellung immer nur ein
#     Produkt enthält.
# - Naiv:
#   - Name des Kunden
#   - Name des Produkts
#   - Anzahl der bestellten Produkte

# %% [markdown]
#
# Tabelle `customers` für Kunden:
#
# | id | name         | address      |
# |----|--------------|--------------|
# |  1 | John Smith   | 123 Elm St   |
# |  2 | Jane Doe     | 456 Oak St   |
#
# Tabelle `products` für Produkte:
#
# | id   | name         | price | description                                |
# |------|--------------|-------|--------------------------------------------|
# | 2341 | Tomatensuppe | 1.99  | Unsere fantastische Tomatensuppe in Dosen. |
# | 346  | Kichererbsen | 0.59  | In Wasser einweichen und genießen...       |
#
# Tabelle `orders` für Bestellungen:
#
# | customer_name | product_name | quantity |
# |---------------|--------------|----------|
# | John Smith    | Tomatensuppe |        2 |
# | Jane Doe      | Tomatensuppe |        1 |
# | John Smith    | Kichererbsen |        3 |

# %% [markdown]
#
# ## Problem mit der naiven Lösung:
#
# - Kunden mit dem gleichen Namen können nicht unterschieden werden
# - Produkte mit dem gleichen Namen können nicht unterschieden werden
# - Bestellungen können nicht eindeutig zugeordnet werden

# %% [markdown]
#
# Tabelle `customers`:
#
# | id | name       | address      |
# |----|------------|--------------|
# |  1 | John Smith | 123 Elm St   |
# |  2 | Jane Doe   | 456 Oak St   |
# |  3 | John Smith | 789 Maple St |
#
# Tabelle `products`:
#
# | id     | product_name | price | description                                |
# |--------|--------------|-------|--------------------------------------------|
# | 2341   | Tomatensuppe | 1.99  | Unsere fantastische Tomatensuppe in Dosen. |
# | 939504 | Tomatensuppe | 2.49  | Premium-Tomatensuppe in Glasflaschen.      |
# | 346    | Kichererbsen | 0.59  | In Wasser einweichen und genießen...       |
#
# Tabelle `orders`:
#
# | customer_name | product_name | quantity |
# |---------------|--------------|----------|
# | John Smith    | Tomatensuppe |        2 |
# | Jane Doe      | Tomatensuppe |        1 |
# | John Smith    | Kichererbsen |        3 |
# | John Smith    | Tomatensuppe |        2 |

# %% [markdown]
#
# ## Lösung: Fremdschlüssel
#
# - Wir verwenden in der Bestellung nicht Kunden- und Produktnamen
# - Wir verwenden stattdessen die IDs
#   - Diese sind Primärschlüssel in den Tabellen `customers` und `products`
#   - Damit wissen wir, dass sie eindeutig sind
# - Spalten, die den Primärschlüssel einer anderen Tabelle referenzieren,
#   nennt man **Fremdschlüssel**
#   - `customer_id` und `product_id` sind Fremdschlüssel in `orders`
# - Wir geben jeder Bestellung eine eindeutige ID
#   - Diese wird Primärschlüssel in der Tabelle `orders`

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
# | order_id | customer_id | product_id | quantity |
# |----------|-------------|------------|----------|
# |        1 |           1 |       2341 |        2 |
# |        2 |           2 |     939504 |        1 |
# |        3 |           1 |        346 |        3 |
# |        4 |           1 |       2341 |        2 |
#
# - `order_id` ist der Primärschlüssel
# - `customer_id` ist ein Fremdschlüssel, der auf die Tabelle `customers` verweist
# - `product_id` ist ein Fremdschlüssel, der auf die Tabelle `products` verweist

# %% [markdown]
#
# ## Workshop: Fremdschlüssel
#
# - Modifizieren Sie die Tabelle `orders`, so dass die Fremdschlüssel korrekt
#   definiert sind.
#
# *Hinweis:*
# - Wenn Sie die Tabelle bearbeiten, gibt es einen Reiter `Fremdschlüssel`, in
#   dem Sie die Fremdschlüssel definieren können.
# - Geben Sie dazu Werte für folgende Spalten ein:
#   - `Spalten`: Die Spalte in der aktuellen Tabelle, die den Fremdschlüssel
#     enthält, z. B. `customer_id`
#   - `Referenz`: Die Spalte und Tabelle, auf die verwiesen wird, z.B.
#     `"customers"("id")`
