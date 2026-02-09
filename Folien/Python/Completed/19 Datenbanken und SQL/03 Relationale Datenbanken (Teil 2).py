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
# ## Probleme ohne Primärschlüssel
#
# Im letzten Workshop konnten wir (möglicherweise) zwei identische Zeilen in
# eine Tabelle einfügen. Welche Probleme verursacht das?
#
# | name       | address    |
# |------------|------------|
# | John Smith | 123 Elm St |
# | Jane Doe   | 456 Oak St |
# | John Smith | 123 Elm St |

# %% [markdown]
#
# <ul>
#   <li class="fragment">Welchen "John Smith" wollen wir aktualisieren, wenn er
#     umzieht?</li>
#   <li class="fragment">Wie können wir nur eine der doppelten Zeilen
#     löschen?</li>
#   <li class="fragment">Wie würden wir einen bestimmten Kunden in einer
#     Bestellungstabelle referenzieren?</li>
#   <li class="fragment">Wir brauchen eine Möglichkeit, jede Zeile eindeutig
#     zu identifizieren!</li>
# </ul>

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
#    <li class="fragment">Es ist umständlich, mehrere Spalten zu verwenden, um einen Kunden in anderen
#       Tabellen zu referenzieren</li>
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
#     zusätzliche Spalte <tt>id</tt> eingeführt, die einen eindeutigen
#     Bezeichner für jeden Kunden darstellt.</li>
#   <li>Die <tt>id</tt> kann dann als Primärschlüssel verwendet werden.</li>
# </ul>

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
