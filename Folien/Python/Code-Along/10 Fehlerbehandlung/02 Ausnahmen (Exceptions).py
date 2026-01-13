# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Ausnahmen (Exceptions)</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# ## Ausnahmen (Exceptions)
#
# - Das Auslösen einer Ausnahme unterbricht die Ausführung des Programms
# - Es wird die Kette von Funktionsaufrufen so weit abgebrochen, bis eine
#   Behandlung der Ausnahme erfolgt

# %%

# %%


# %%

# %% [markdown]
#
# - Nicht behandelte Ausnahmen brechen die Programmausführung ab:

# %%

# %%

# %%

# %% [markdown]
# ## Fehlerklassen
#
# In Python gibt es viele vordefinierte Fehlerklassen, mit denen verschiedene
# Fehlerarten signalisiert werden können:
# - `Exception`: Basisklasse aller behandelbaren Exceptions
# - `ArithmeticError`: Basisklasse aller Fehler bei Rechenoperationen:
#   - `OverflowError`: Überlauf bei einer Rechenoperation
#   - `ZeroDivisionError`: Division durch 0
# - `LookupError`: Basisklasse wenn ein ungültiger Index/Key für eine Datenstruktur
#   verwendet wurde
#   - `IndexError`: Index außerhalb des gültigen Bereichs
#   - `KeyError`: Key nicht in einem Dictionary vorhanden
# - `AssertionError`: Fehlerklasse, die von `assert` verwendet wird
# - `EOFError`: Fehler wenn `input()` unerwartet das Ende einer Datei erreicht
# - ...
#
# Die Liste der in der Standardbibliothek definierten Fehlerklassen ist
# [hier](https://docs.python.org/3/library/exceptions.html).

# %% [markdown]
#
# ## Workshop: Bank Account
#
# Definieren Sie eine Klasse `BankAccount` mit einem Attribut `balance: float`
# und Methoden `deposit(amount: float)` und `withdraw(amount: float)`.
#
# *Hinweis: Für eine realistischere Implementierung sollte `decimal.Decimal`
# statt `float` verwendet werden.*
#
# Die Klasse soll in folgenden Fällen eine Exception vom Typ `ValueError`
# auslösen:
#
# - Wenn ein neuer `BankAccount` mit negativer `balance` angelegt werden soll.
# - Wenn `deposit` mit einem negativen Wert aufgerufen wird.
# - Wenn `withdraw` mit einem negativen Wert aufgerufen wird oder durch das
#   Abheben des Betrags die `balance` des Kontos negativ werden würde.

# %%

# %%

# %% [markdown]
#
# Testen Sie die Funktionalität der Klasse sowohl für erfolgreiche
# Transaktionen, als auch für Transaktionen, die Exceptions auslösen.

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

