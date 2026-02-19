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
def create_library_db(con: sqlite3.Connection):
    return con.executescript(
        """
        BEGIN;
        CREATE TABLE authors(id INTEGER PRIMARY KEY, name TEXT, country TEXT);
        CREATE TABLE books(id INTEGER PRIMARY KEY, title TEXT, year INTEGER, author_id INTEGER);
        COMMIT;
        """
    )


# %%
create_library_db(con)


# %%
def add_author(con: sqlite3.Connection, id_: int, name: str, country: str):
    con.execute("INSERT INTO authors VALUES (?, ?, ?)", (id_, name, country))
    con.commit()


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
def add_book(
    con: sqlite3.Connection, id_: int, title: str, year: int, author_id: int
):
    con.execute("INSERT INTO books VALUES (?, ?, ?, ?)", (id_, title, year, author_id))
    con.commit()


# %%
add_book(con, 1, "1984", 1949, 1)

# %%
assert con.execute("SELECT * FROM books").fetchall() == [(1, "1984", 1949, 1)]

# %%
from typing import Sequence


# %%
def add_books(con: sqlite3.Connection, books: Sequence):
    con.executemany("INSERT INTO books VALUES (?, ?, ?, ?)", books)
    con.commit()


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
def get_book_info(con: sqlite3.Connection, book_id: int):
    return con.execute(
        """
        SELECT b.id, b.title, a.name, b.year
        FROM books AS b
        JOIN authors AS a
        ON b.author_id = a.id
        WHERE b.id = ?
        """,
        (book_id,),
    ).fetchone()


# %%
assert get_book_info(con, 1) == (1, "1984", "George Orwell", 1949)

# %%
assert get_book_info(con, 10) is None


# %%
def get_book_info_no_join(con: sqlite3.Connection, book_id: int):
    return con.execute(
        """
        SELECT id, title, author_id, year
        FROM books
        WHERE id = ?
        """,
        (book_id,),
    ).fetchone()


# %%
assert get_book_info_no_join(con, 1) == (1, "1984", 1, 1949)

# %%
assert get_book_info_no_join(con, 10) is None


# %%
def find_old_books(con: sqlite3.Connection, year: int):
    return [
        title
        for (title,) in con.execute(
            "SELECT title FROM books WHERE year < ?", (year,)
        ).fetchall()
    ]


# %%
assert find_old_books(con, 1950) == ["1984", "Animal Farm"]


# %%
def print_books_by_author(con: sqlite3.Connection, author_name: str):
    books = con.execute(
        """
        SELECT b.id, b.title, a.name, b.year
        FROM books AS b
        JOIN authors AS a
        ON b.author_id = a.id
        WHERE a.name = ?
        """,
        (author_name,),
    )
    for id_, title, author, year in books:
        print(f"{title} ({year}): id = {id_}, author = {author}")


# %%
print_books_by_author(con, "Haruki Murakami")

# %% [markdown]
#
# Ausgabe:
# ```
# Norwegian Wood (1987): id = 4, author = Haruki Murakami
# Kafka on the Shore (2002): id = 5, author = Haruki Murakami
# ```

# %%
