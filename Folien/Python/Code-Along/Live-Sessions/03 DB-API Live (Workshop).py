# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>DB-API Live (Workshop)</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# ## Workshop: Bibliotheks-Datenbank
#
# Sie wollen Daten für eine kleine Bibliothek in einer SQLite-Datenbank
# speichern. Jeder Autor wird durch folgende Daten beschrieben:
#
# - Autor-ID
# - Name
# - Herkunftsland
#
# Jedes Buch wird repräsentiert durch:
#
# - Buch-ID
# - Titel
# - Erscheinungsjahr
# - Autor-ID (Fremdschlüssel)

# %% [markdown]
#
# Schreiben Sie folgende Funktionen:
#
# - `create_library_db(con)`, die die Tabellen erzeugt
# - `add_author(con, id_, name, country)`, die einen Autor einfügt
# - `add_book(con, id_, title, year, author_id)`, die ein Buch einfügt
# - `add_books(con, books)`, die mehrere Bücher einfügt
# - `get_book_info(con, book_id)`, die die Daten eines Buchs zurückgibt
#   (falls Sie SQL-Joins kennen, geben Sie den Autornamen statt der ID zurück)
# - `find_old_books(con, year)`, die die Titel aller Bücher zurückgibt,
#   die vor dem angegebenen Jahr erschienen sind
# - `print_books_by_author(con, author_name)`, die alle Bücher eines Autors
#   ausgibt (falls Sie SQL-Joins nicht kennen, können Sie die Autor-ID übergeben)

# %%
import sqlite3

# %%
con = sqlite3.connect(":memory:")

# %%

# %%
create_library_db(con)

# %%

# %%
add_author(con, 1, "George Orwell", "UK")
add_author(con, 2, "Gabriel Garcia Marquez", "Colombia")
add_author(con, 3, "Haruki Murakami", "Japan")

# %%
assert con.execute("SELECT * FROM authors ORDER BY id").fetchall() == [
    (1, "George Orwell", "UK"),
    (2, "Gabriel Garcia Marquez", "Colombia"),
    (3, "Haruki Murakami", "Japan"),
]

# %%

# %%
add_book(con, 1, "1984", 1949, 1)

# %%
assert con.execute("SELECT * FROM books").fetchall() == [(1, "1984", 1949, 1)]

# %%
from typing import Sequence

# %%

# %%
BOOKS = [
    (2, "Animal Farm", 1945, 1),
    (3, "One Hundred Years of Solitude", 1967, 2),
    (4, "Norwegian Wood", 1987, 3),
    (5, "Kafka on the Shore", 2002, 3),
]

# %%
add_books(con, BOOKS)

# %%
assert con.execute("SELECT * FROM books ORDER BY id").fetchall() == [
    (1, "1984", 1949, 1),
    *BOOKS,
]

# %%

# %%
assert get_book_info(con, 1) == (1, "1984", "George Orwell", 1949)

# %%
assert get_book_info(con, 10) is None

# %%

# %%
assert find_old_books(con, 1950) == ["1984", "Animal Farm"]

# %%

# %%

# %% [markdown]
#
# Ausgabe:
# ```
# Norwegian Wood (1987): id = 4, author = Haruki Murakami
# Kafka on the Shore (2002): id = 5, author = Haruki Murakami
# ```

# %%
