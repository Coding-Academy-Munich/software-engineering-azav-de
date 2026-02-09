# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Python DB-API (Workshop)</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# ## Mini-Workshop: Mitarbeiter-Datenbank
#
# Sie wollen Daten für die Mitarbeiter einer Firma in einer SQLite Datenbank
# speichern. Jeder Mitarbeiter wird dabei durch folgende Daten beschrieben:
#
# - Personalnummer
# - Name
# - Abteilungs-Nummer
# - Wochenarbeitszeit in Stunden
#
# Jede Abteilung wird repräsentiert durch folgende Daten:
#
# - Abteilungs-Nummer
# - Name der Abteilung

# %% [markdown]
#
# Schreiben Sie folgende Funktionen:
#
# - `create_employee_db(...)`, die die Tabellen erzeugt
# - `create_department(...)`, die eine neue Abteilung in die Datenbank einfügt.
# - `create_employee(...)`, die einen neuen Mitarbeiter in die Datenbank einfügt.
# - `create_employees(...)`, die mehrere neue Mitarbeiter in die Datenbank einfügt.
# - `get_employee_data(db, id)`, die die Daten für den Mitarbeiter mit
#    Personalnummer `id` zurückgibt. (Falls Sie SQL Joins kennen, können Sie statt
#    der Abteilungs-Nummer den Namen der Abteilung zurückgeben.)
# - `find_part_time_employees(...)`, die die Personalnummern alle Mitarbeiter
#    zurückgibt, die weniger als 30 Stunden pro Woche arbeiten.
# - `print_employees_in_department(con: sqlite3.Connection, name: str)`,
#    die die Daten aller Mitarbeiter in
#    der Abteilung mit Namen `name` ausdruckt. (Falls sie SQL-Joins nicht kennen,
#    können Sie auch die Abteilungs-Nummer an die Funktion übergeben.)

# %%
import sqlite3

# %%
con = sqlite3.connect(":memory:")


# %%
def create_employee_db(con: sqlite3.Connection):
    return con.executescript(
        """
        BEGIN;
        CREATE TABLE employees(id INTEGER, name TEXT, dep_id INTEGER, hours INTEGER);
        CREATE TABLE departments(id INTEGER, name TEXT);
        COMMIT;
        """
    )


# %%
create_employee_db(con)


# %%
def create_department(con: sqlite3.Connection, id_: int, name: str):
    con.execute("INSERT INTO departments VALUES (?, ?)", (id_, name))
    con.commit()


# %%
create_department(con, 1, "Marketing")
create_department(con, 2, "R&D")
create_department(con, 3, "Accounting")

# %%
assert con.execute("SELECT * FROM departments ORDER BY id").fetchall() == [
    (1, "Marketing"),
    (2, "R&D"),
    (3, "Accounting"),
]


# %%
def create_employee(
    con: sqlite3.Connection, id_: int, name: str, dep_id: int, hours: int
):
    con.execute("INSERT INTO employees VALUES (?, ?, ?, ?)", (id_, name, dep_id, hours))
    con.commit()


# %%
create_employee(con, 1, "Geraldine E. Stegner", 1, 40)

# %%
assert con.execute("SELECT * FROM employees").fetchall() == [
    (1, "Geraldine E. Stegner", 1, 40)
]

# %%
from typing import Sequence


# %%
def create_employees(con: sqlite3.Connection, data: Sequence):
    con.executemany("INSERT INTO employees VALUES (?, ?, ?, ?)", data)
    con.commit()


# %%
EMPLOYEES = [
    (2, "Tammy T. Selby", 2, 42),
    (3, "Pam Adams", 3, 24),
    (4, "Bobby A. Skaggs", 1, 38),
    (5, "Sandra A. Finley", 2, 26),
]

# %%
create_employees(con, EMPLOYEES)

# %%
assert con.execute("SELECT * FROM employees").fetchall() == [
    (1, "Geraldine E. Stegner", 1, 40),
    *EMPLOYEES,
]


# %%
def get_employee_data(con: sqlite3.Connection, id_: int):
    return con.execute(
        """
        SELECT e.id, e.name, d.name, e.hours
        FROM employees AS e
        JOIN departments AS d
        ON e.dep_id = d.id
        WHERE e.id = ?
        """,
        (id_,),
    ).fetchone()


# %%
assert get_employee_data(con, 1) == (1, "Geraldine E. Stegner", "Marketing", 40)

# %%
assert get_employee_data(con, 10) is None


# %%
def get_employee_data_no_join(con: sqlite3.Connection, id_: int):
    return con.execute(
        """
        SELECT id, name, dep_id, hours
        FROM employees AS e
        WHERE id = ?
        """,
        (id_,),
    ).fetchone()


# %%
assert get_employee_data_no_join(con, 1) == (1, "Geraldine E. Stegner", 1, 40)

# %%
assert get_employee_data_no_join(con, 10) is None


# %%
def get_part_time_employees(con: sqlite3.Connection):
    return [
        id_
        for (id_,) in con.execute(
            "SELECT id FROM employees WHERE hours < 30"
        ).fetchall()
    ]


# %%
assert get_part_time_employees(con) == [3, 5]


# %%
def print_employees_in_department(con: sqlite3.Connection, name: str):
    employees = con.execute(
        """
        SELECT e.id, e.name, d.name, e.hours
        FROM employees AS e
        JOIN departments AS d
        ON e.dep_id = d.id
        WHERE d.name = ?
        """,
        (name,),
    )
    for id_, name, dep, hours in employees:
        print(f"{name}: id = {id_}, dep = {dep}, hours = {hours}")


# %%
print_employees_in_department(con, "Marketing")

# %% [markdown]
#
# Ausgabe:
# ```
# Geraldine E. Stegner: id = 1, dep = Marketing, hours = 40
# Bobby A. Skaggs: id = 4, dep = Marketing, hours = 38
# ```

# %%
