# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Tabellen erstellen (CREATE TABLE)</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# - SQL steht für Structured Query Language (strukturierte Abfragesprache)
# - SQL ist eine Programmiersprache zur Verwaltung und Manipulation von Daten in
#   einer relationalen Datenbank
# - SQL wird verwendet, um Tabellen und Daten in einer Datenbank zu erstellen,
#   zu ändern und abzufragen

# %% [markdown]
#
# ## Erstellen von Tabellen
#
# - Erinnerung: In einer relationalen Datenbank werden Daten in Tabellen
#   organisiert
# - Jede Tabelle besteht aus Zeilen und Spalten, wobei jede Zeile einen
#   Datensatz und jede Spalte ein Attribut des Datensatzes darstellt
# - Um Daten in einer Datenbank zu speichern, müssen wir zunächst eine Tabelle
#   erstellen
# - Diesen Teil von SQL nennt man Data Definition Language (DDL)

# %% [markdown]
#
# Tabelle `customers`:
#
# | id | name       | address      |
# |----|----------- |--------------|
# |  1 | John Smith | 123 Elm St   |
# |  2 | Jane Doe   | 456 Oak St   |
# |  3 | John Smith | 789 Maple St |

# %% [markdown]
#
# ## Tabellen erstellen
#
# - Der Befehl `CREATE TABLE` wird verwendet, um eine neue Tabelle in einer
#   Datenbank zu erstellen.
# - Man muss den Tabellennamen sowie die Spalten und Datentypen für die Tabelle
#   angeben

# %% [markdown]
#
# ```sql
# CREATE TABLE customers (
#   id INTEGER PRIMARY KEY AUTOINCREMENT,
#   name TEXT NOT NULL,
#   address TEXT
# );
# ```

# %% [markdown]
#
# Alternativ kann man Primär- und Fremdschlüssel auch nach den Spalten
# definieren
# - `PRIMARY KEY (id)`
# - `FOREIGN KEY (product_id) REFERENCES products(id)`
#
# Tabellen- und Spaltennamen _können_ in doppelte Anführungszeichen gesetzt
# werden.
#
# **Hinweis:** `AUTOINCREMENT` kann in SQLite nur in der Spaltendefinition
# verwendet werden: `id INTEGER PRIMARY KEY AUTOINCREMENT`

# %% [markdown]
#
# ```sql
# CREATE TABLE customers (
#   id INTEGER PRIMARY KEY AUTOINCREMENT,
#   name TEXT NOT NULL,
#   address TEXT
# );
# ```

# %% [markdown]
#
# ## Workshop: Erstellung von Tabellen mit SQL
#
# - Erstellen Sie mit dem DB Browser eine neue Datenbank `shop-sql.sqlite`
# - Erstellen Sie darin die `customers`, `products` und `orders` Tabellen aus
#   den letzten Workshops mit SQL-Befehlen
#
# *Hinweis:*
# - Verwenden Sie dazu den Tab `SQL ausführen` im DB Browser

# %% [markdown]
#
# ```sql
# CREATE TABLE customers (
#   id INTEGER PRIMARY KEY AUTOINCREMENT,
#   name TEXT NOT NULL,
#   address TEXT NOT NULL
# );
# ```

# %% [markdown]
#
# ```sql
# CREATE TABLE products (
#   id INTEGER PRIMARY KEY AUTOINCREMENT,
#   product_name TEXT NOT NULL,
#   price REAL NOT NULL,
#   description TEXT
# );
# ```

# %% [markdown]
#
# ```sql
# CREATE TABLE orders (
#   id INTEGER PRIMARY KEY AUTOINCREMENT,
#   customer_id INTEGER NOT NULL,
#   product_id INTEGER NOT NULL,
#   quantity INTEGER NOT NULL,
#   FOREIGN KEY (customer_id) REFERENCES customers(id),
#   FOREIGN KEY (product_id) REFERENCES products(id)
# );
# ```
