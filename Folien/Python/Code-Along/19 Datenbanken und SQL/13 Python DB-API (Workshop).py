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

# %%
create_employee_db(con)

# %%

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

# %%
create_employee(con, 1, "Geraldine E. Stegner", 1, 40)

# %%
assert con.execute("SELECT * FROM employees").fetchall() == [
    (1, "Geraldine E. Stegner", 1, 40)
]

# %%

# %%

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

# %%

# %%
assert get_employee_data(con, 1) == (1, "Geraldine E. Stegner", "Marketing", 40)

# %%
assert get_employee_data(con, 10) is None

# %%

# %%
assert get_part_time_employees(con) == [3, 5]

# %%

# %%

# %% [markdown]
#
# Ausgabe:
# ```
# Geraldine E. Stegner: id = 1, dep = Marketing, hours = 40
# Bobby A. Skaggs: id = 4, dep = Marketing, hours = 38
# ```

# %%
