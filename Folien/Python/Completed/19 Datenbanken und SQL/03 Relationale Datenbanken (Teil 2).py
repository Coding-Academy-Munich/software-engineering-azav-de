# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Relationale Datenbanken (Teil 2)</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# ## Primärschlüssel
#
# - Primärschlüssel sind eindeutige Bezeichner für jede Zeile in einer Tabelle
# - Sie können aus einer oder mehreren Spalten bestehen
#   - Mehrere Spalten: zusammengesetzter Primärschlüssel
# - Die Werte der Spalte(n) des Primärschlüssels müssen eindeutig sein

# %% [markdown]
#
# Tabelle `customers` für Kunden mit Primärschlüssel `name`:
#
# | name         | address      |
# |--------------|--------------|
# | John Smith   | 123 Elm St   |
# | Jane Doe     | 456 Oak St   |
#
# <p class="fragment">Problem mit dem Primärschlüssel <tt>name</tt>:</p>
# <ul>
#   <li class="fragment">Was passiert, wenn wir einen zweiten Kunden mit dem
#     Namen "John Smith" hinzufügen wollen?</li>
#   <li class="fragment">Das ist nicht möglich, da der Primärschlüssel eindeutig
#     sein muss!</li>
# </ul>

# %% [markdown]
#
# Tabelle `customers` für Kunden mit zusammengesetztem Primärschlüssel `name`
# und `address`:
#
# | name         | address      |
# |--------------|--------------|
# | John Smith   | 123 Elm St   |
# | Jane Doe     | 456 Oak St   |
#
# <p class="fragment">
#   Problem mit dem zusammengesetzten Primärschlüssel:
# </p>
# <ul>
#   <li class="fragment">Theoretisch könnte es zwei Kunden mit dem Namen "John
#     Smith" geben, die an der gleichen Adresse wohnen</li>
#   <li class="fragment">Unwahrscheinlich, aber möglich</li>
#   <li class="fragment">Was ist, wenn ein Kunde umzieht?</li>
#     <ul>
#       <li class="fragment">Dann ändert sich der Primärschlüssel</li>
#       <li class="fragment">Das kann zu Problemen führen, wenn der Primärschlüssel in anderen Tabellen referenziert wird</li>
#     </ul>
# </ul>

# %% [markdown]
#
# Tabelle `customers` für Kunden mit synthetischem Primärschlüssel:
#
# | id | name         | address      |
# |----|--------------|--------------|
# |  1 | John Smith   | 123 Elm St   |
# |  2 | Jane Doe     | 456 Oak St   |
#
# <p class="fragment">
#   "Synthetischer" Primärschlüssel:
# </p>
# <ul class="fragment">
#   <li>Statt <tt>name</tt> und <tt>address</tt> als Primärschlüssel zu verwenden, wird eine
#     zusätzliche Spalte <tt>customer_id</tt> eingeführt, die einen eindeutigen
#     Bezeichner für jeden Kunden darstellt.</li>
#   <li>Der <tt>customer_id</tt> kann dann als Primärschlüssel verwendet werden.</li>
# </ul>

# %% [markdown]
#
# ## Warum sind Primärschlüssel wichtig?
#
# - Primärschlüssel gewährleisten die Eindeutigkeit von Datensätzen in einer Tabelle
# - Sie ermöglichen die effiziente Identifizierung und den Zugriff auf Daten
# - Sie werden verwendet, um Beziehungen zwischen Tabellen herzustellen
#   - Man nennt sie in diesem Kontext Fremdschlüssel

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
# | John Smith    | Tomato soup  |        2 |
# | Jane Doe      | Tomato soup  |        1 |
# | John Smith    | Chickpeas    |        3 |

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
# ## Lösung
#
# - Wir verwenden in der Bestellung nicht Kunden- und Produktnamen
# - Wir verwenden stattdessen die IDs
#   - Diese sind Primärschlüssel in den Tabellen `customers` und `products`
#   - Damit wissen wir, dass sie eindeutig sind
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

# %% [markdown]
#
# ## Workshop: Primärschlüssel
#
# - Wandeln Sie die folgenden Spalten in Primärschlüssel um:
#   - `customers`: `id`
#   - `products`: `id`
# - Was passiert dabei, wenn die Tabelle bereits zwei Zeilen mit dem gleichen
#   Primärschlüssel hat?
# - Wie können Sie das Problem beheben?
# - Was passiert, wenn Sie nach dem Einführen von Primärschlüsseln versuchen,
#   zwei Zeilen hinzuzufügen, die denselben Primärschlüssel haben?
#
# *Hinweis:*
# - Klicken Sie mit der rechten Maustaste auf eine Tabelle und wählen Sie
#   `Tabelle verändern` um sie zu bearbeiten
# - Die Checkbox `PK` markiert eine Spalte als Primärschlüssel

# %% [markdown]
#
# - Erstellen Sie eine Tabelle `orders` mit den folgenden Spalten:
#   - `id` (INTEGER, Primärschlüssel)
#   - `customer_id` (INTEGER)
#   - `product_id` (INTEGER)
#   - `quantity` (INTEGER)

# %% [markdown]
#
# - Fügen Sie die folgenden Bestellungen in die Tabelle `orders` ein:
#   - `id`: 1, `customer_id`: 1, `product_id`: 2341, `quantity`: 2
#   - `id`: 2, `customer_id`: 2, `product_id`: 939504, `quantity`: 1
#   - `id`: 3, `customer_id`: 1, `product_id`: 346, `quantity`: 3
#   - `id`: 4, `customer_id`: 1, `product_id`: 2341, `quantity`: 2
# - Was passiert, wenn Sie eine Bestellung einfügen, bei der der Wert von
#   `customer_id` nicht in der Tabelle `customers` vorhanden ist?
