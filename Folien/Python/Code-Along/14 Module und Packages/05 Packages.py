# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Packages</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# Packages (Pakete) erlauben es uns, verwandte Module zu organisieren

# %% [markdown]
#
# ### Beispiel: `html` Paket
#
# - `html` enthält Module, die für die Verarbeitung von HTML Dokumenten benötigt
#   werden
# - `html.entities` enthält eine Liste von HTML Entities
# - `html.parser` enthält einen HTML-Parser
# - `html` selber enthält nur Funktionen `escape()` und `unescape()`

# %%
import html

# %%
html.escape("<a href='test'>Test</a>")

# %%
html.unescape("&lt;a href=&#x27;test&#x27;&gt;Test&lt;/a&gt;")

# %%
import html.entities

# %%
html.entities.entitydefs["Psi"]

# %%
html.entities.html5["Psi;"]

# %%
from html.parser import HTMLParser


# %%
class PrintingHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start tag:", tag)
        for attr in attrs:
            print("     attr:", attr)

    def handle_endtag(self, tag):
        print("End tag:  ", tag)

    def handle_data(self, data):
        print("Data:     ", data)


# %%
parser = PrintingHTMLParser()

# %%
parser.feed('<div class="my-class"><a href="test">Test</a></div>')


# %% [markdown]
#
#  ### Struktur von Packages
#
# - Packages sind Ordner im Dateisystem
# - Sie können Module und andere Packages enthalten
# - Um zu kennzeichnen, dass ein Ordner ein Package ist, enthält er typischerweise eine
#   `__init__.py` Datei
# - Die `__init__.py` Datei kann leer sein (und ist oft leer)

# %%
from dirtree import dir_tree

# %%

# %% [markdown]
#
# ### Struktur des `greetings` Packages
#
# - Dateien für Module:
#   - [`formal.py`](greetings/formal.py)
#   - [`informal.py`](greetings/informal.py)
#   - [`generic.py`](greetings/generic.py)
# - Ordner für Sub-Packages:
#   - `intl` mit Datei [`generic.py`](greetings/intl/generic.py)

# %% [markdown]
#
# ## Namen von Packages
#
# - Namenskomponenten werden durch Punkte getrennt
#   - z.B. `<package>.<sub-package>.<sub-sub-package>.<module>`
# - Namenskonventionen:
#   - Namen sollten mit einem Kleinbuchstaben beginnen
#   - Namen sollten keine Unterstriche enthalten

# %% [markdown]
#
# ### Namen des `greetings` Packages
#
# - Dateien für Module:
#   - [`greetings.formal`](greetings/formal.py)
#   - [`greetings.generic`](greetings/generic.py)
#   - [`greetings.informal`](greetings/informal.py)
# - Ordner für Sub-Packages:
#   - `intl` mit Modul [`greetings.intl.generic`](greetings/intl/generic.py)

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %% [markdown]
#
#  ### Finden von Packages
#
#  - Python sucht in `sys.path` nach dem Package-Verzeichnis.
#  - Dieser kann durch die Environment-Variable `PYTHONPATH` oder direkt von
#    Python aus beeinflusst werden.
#  - In den meisten Fällen ist es besser, keine komplizierten Operationen an
#    `sys.path` vorzunehmen.

# %%
import sys

# %%

# %% [markdown]
#
#  ### Das `import` statement
#
#  `import a.b.c`:
#
#  - `a` und `b` müssen Packages (Verzeichnisse) sein
#  - `c` kann ein Modul oder ein Package sein
#
#  `from a.b.c import d`
#  - `a` und `b` müssen Packages sein
#  - `c` kann ein Modul oder ein Package sein
#  - `d` kann ein Modul, ein Package oder ein Name (d.h. eine Variable, eine Funktion,
#    eine Klasse, usw.) sein

# %% [markdown]
#
#  ### Referenzen innerhalb eines Packages
#
#  - `from . import a` importiert `a` aus dem aktuellen Package
#  - `from .. import a` importiert `a` aus dem übergeordneten Package
#  - `from .foo import a` importiert `a` aus dem "Geschwistermodul" `foo`

# %%
# %pycat greetings/generic.py

# %%
# %pycat greetings/intl/generic.py

# %% [markdown]
#
# ## Workshop: Persönlicher Finanz-Tracker
#
# ### Übersicht
#
# In diesem Workshop werden Sie einen einfachen persönlichen Finanz-Tracker
# entwickeln. Dieses Programm hilft den Benutzern, ihre persönlichen Finanzen,
# zu verfolgen und zu analysieren.
#
# Wir wollen das Programm in mehrere Pakete und Module einteilen.


# %% [markdown]
#
# ### Problem- und Funktionsdomäne
#
# Der persönliche Finanz-Tracker besteht aus zwei Hauptkomponenten: Ausgabenverfolgung
# und Einkommensverfolgung. Zusätzlich wird er Funktionen für das Generieren von
# Finanzberichten und das Erstellen von Budgets haben.
#
# **Schlüsselfunktionalitäten:**
#
# 1. **Ausgaben verfolgen:** Einzelne Ausgaben aufzeichnen und kategorisieren.
# 2. **Einkommen verfolgen:** Verschiedene Einkommensquellen aufzeichnen und
#    kategorisieren.
# 3. **Berichte generieren:** Zusammenfassungen von Finanzaktivitäten erstellen.
# 4. **Budgetanalyse:** Überprüfen ob Ausgaben in einem Budget liegen

# %% [markdown]
#
# ### Paket- und Modulstruktur
#
# Ihr Programm wird in zwei Hauptpakete unterteilt: `finance` und `analytics`. Jedes
# Paket enthält spezifische Module, die mit ihren Funktionalitäten verbunden sind.
#
# 1. **Paket: `finance`**
#    - **Modul: `expenses`**
#      - Klassen und Funktionen zum Hinzufügen, Kategorisieren und Zusammenfassen von Ausgaben.
#    - **Modul: `income`**
#      - Klassen und Funktionen zum Aufzeichnen und Kategorisieren von Einkommensquellen.

# %% [markdown]
#
# 2. **Paket: `analytics`** (ein Unter-Paket innerhalb von `finance`)
#    - **Modul: `reporting`**
#      - Funktionen zum Erstellen von Finanzberichten basierend auf Einkommen und
#        Ausgaben.
#    - **Modul: `budget`**
#      - Klassen und Funktionen zum Erstellen und Analysieren von Budgets.

# %% [markdown]
#
# ### Spezifikationen der Klassen und Funktionen
#
# - `expenses`:
#   - Klasse `Expense` with attributes `amount` and `category`
#   - Funktion `summarize_expenses(expenses: list[Expense]) -> dict[str, float]`
#     - Fasst Ausgaben nach Kategorien zusammen und berechnet die Gesamtsumme pro Kategorie.
#   - Funktion `total_expenses(expenses: list[Expense]) -> float`
#     - Berechnet die Gesamtausgaben.

# %% [markdown]
#
# - `income`:
#   - Klasse `Income` with attributes `amount` and `source`
#   - Funktion `summarize_incomes(incomes: list[Income]) -> dict[str, float]`
#     - Fasst Einkommen nach Quellen zusammen und berechnet die Gesamtsumme pro Quelle.
#   - Funktion `total_income(incomes: list[Income]) -> float`
#     - Berechnet das Gesamteinkommen.

# %% [markdown]
#
# - `analytics.reporting`:
#   - Funktion `print_financial_report(incomes: list[Income], expenses:
#     list[Expense]) -> None`
#     - Druckt folgende Informationen aus:
#       - Einnahmen pro Quelle
#       - Ausgaben pro Kategorie
#       - Gesamteinnahmen und -ausgaben.
#       - Überschuss oder Defizit.

# %% [markdown]
#
# - `analytics.budget`:
#   - Klasse `Budget` mit Attribut `limit`
#     - Methode `can_afford(expenses: list[Expense]) -> bool`
#       - Überprüft, ob die Gesamtausgaben innerhalb des Budgets liegen.

# %% [markdown]
#
# Fügen Sie ein Modul `main` hinzu, die die Funktionalität des Programms testet,
# indem Sie Listen von Einnahmen und Ausgaben, sowie ein Budget erstellt,
# überprüft ob die Ausgaben im Budget liegen und einen Finanzbericht generiert.

# %% [markdown]
#
# ### Paketreferenzen und Abhängigkeiten
#
# Dabei benötigen Sie folgende Abhängigkeiten zwischen Modulen:
#
# - `analytics.budget` muss auf `expenses` zugreifen, um die Daten für die
#   Budgetanalyse zu erhalten.
# - `analytics.reporting` muss auf `income` und `expenses` zugreifen, um die
#   Finanzberichte zu erstellen.
# - `main` muss auf alle Module (`income`, `expenses`, `analytics.budget`,
#   `analytics.reporting`) zugreifen.
#
# *Hinweis:* Die Abhängigkeiten zwischen den Modulen dienen dazu, die
# verschiedenen Import-Möglichkeiten zu demonstrieren. Sie sind nicht unbedingt
# das beste Beispiel för die Organisation von Funktionalität in Python.

# %% [markdown]
#
# ### Ausführen des Programms
#
# Im dem Verzeichnis, in dem sich das `finance` Paket befindet, können Sie das
# Programm mit dem Befehl `python -m finance.main` ausführen:

# %%
# # !python -m finance.main

# %%
# import finance.main

# %%
# finance.main.main()
