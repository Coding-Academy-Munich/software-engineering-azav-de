# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>CLI Apps mit Typer</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# ## Was ist eine CLI App?
#
# - Eine **Kommandozeilen-App (CLI App)** ist ein Programm, mit dem wir
#   interagieren, indem wir Befehle in ein Terminal eingeben.
# - `python my_script.py` ist ein CLI-Befehl.

# %% [markdown]
#
# ### Warum?
#
# - **Automatisierung:**
#   - CLIs sind einfach zu skripten und automatisieren.
# - **Effizienz:**
#   - Für viele Aufgaben schneller als das Klicken durch eine grafische
#   Benutzeroberfläche (GUI).
# - **Integration:**
#   - Sie sind die Bausteine größerer Entwicklungs- und Data-Science-Workflows.
#   - (Denken Sie an `git`, `python`, `pip`.)
# - **Entwicklungszeit:**
#   - Sie sind oft schneller zu schreiben und zu warten als GUIs.

# %% [markdown]
#
# ## Einführung in `typer`
#
# `typer` ist eine moderne Python-Bibliothek zum Erstellen von CLIs.
# - **Einfach & Intuitiv:**
#   - Sie schreiben normale Python-Funktionen,
#   - `typer` verwandelt sie in eine robuste CLI.
# - **Typenbasiert:**
#   - `typer` verwendet Standard-Python-Typannotationen (`str`, `int`, `bool`),
#   um Benutzereingaben zu verarbeiten, zu validieren und zu konvertieren.
# - **Automatische Hilfe:**
#   - `typer` generiert automatisch schöne, hilfreiche Dokumentation für Ihre
#     Benutzer.
#   - `your_app --help`.
# - **Weniger Fehler:**
#   - `typer` reduziert Boilerplate-Code und häufige Fehler.

# %% [markdown]
#
# ## Grundlegende Konzepte: Argumente vs. Optionen
#
# - **Argumente:**
#   - Erforderliche Eingaben, die in einer bestimmten Reihenfolge bereitgestellt
#     werden.
# - **Optionen:**
#   - Optionale Einstellungen, die das Verhalten des Programms ändern.

# %% [markdown]
#
# ### Argumente
#
# - Sie sind **erforderliche** Eingaben.
# - Sie sind **positionell** (die Reihenfolge ist wichtig).
# - "Substantive", mit denen Ihr Programm arbeitet.
# - *Beispiel:*
#   - `copy source.txt destination.txt`
#   - `source.txt` und `destination.txt` sind Argumente.

# %% [markdown]
#
# ### Optionen (oder Flags)
#
# - Sie sind typischerweise **optional** und fungieren als Einstellungen.
# - Sie werden durch einen Namen identifiziert, wie `--verbose` oder `-v`.
# - Sie ändern das Verhalten des Programms.
# - *Beispiel:* In `ls -l --all` sind `-l` und `--all` Optionen.

# %% [markdown]
#
# ## Die einfachste `typer` App: `typer.run()`
#
# - Für eine CLI mit einem einzigen Zweck ist `typer.run()` alles, was Sie
#   brauchen.
# - Es nimmt eine Funktion und verwandelt sie in eine CLI-Anwendung.


# %% [markdown]
#
# Lassen Sie uns eine einfache "Begrüßer"-App erstellen.
#
# ```python
# # greeter.py
# import typer
#
# def main(name: str):
#     """
#     A simple program that greets NAME.
#     """
#     print(f"Hello, {name}!")
#
# if __name__ == "__main__":
#     typer.run(main)
# ```


# %% [markdown]
#
# ### Wie führen wir das Programm aus?
#
# ```shell
# $ python greeter.py Alice
# Hello, Alice!
# ```

# %% [markdown]
#
# - `typer.run(main)` sagt `typer`, dass es unsere `main`-Funktion verwalten
#   soll.
# - Der Parameter `name` der Funktion wird automatisch zu einem
#   CLI-**Argument**.
# - `typer` verwendet den Typ-Hinweis (`str`), um zu wissen, dass das Argument
#   Text erwartet.

# %% [markdown]
#
# ## Defining Arguments & Options with `Annotated`
#
# - How do we give `typer` more details about a parameter, like a help message?
# - `typing.Annotated`.
# - Think of `Annotated` as a way to "decorate" or add extra information to a
#   type hint.

# %% [markdown]
#
# ### Defining a Detailed Argument
#
# You wrap the type hint with `Annotated` and add a `typer.Argument` inside it.
# ```python
# from typing import Annotated
# import typer
#
# def main(name: Annotated[str, typer.Argument(help="The name of the person to greet.")]):
#     print(f"Hello, {name}!")
#
# if __name__ == "__main__":
#     typer.run(main)
# ```
# Jetzt weiß `typer`, dass `name` ein **Argument** ist und zeigt den `help`-Text
# im Hilfemenü an.

# %% [markdown]
#
# ### Definieren einer Option
#
# - Das gleiche Muster, aber mit `typer.Option`.
# - Option, um die Anzahl der Wiederholungen zu steuern.

# %% [markdown]
#
# ```python
# from typing import Annotated
# import typer
#
# def main(
#     name: Annotated[str, typer.Argument(help="Who to greet.")],
#     repeat: Annotated[int, typer.Option(help="Number of times to repeat the greeting.")] = 1,
# ):
#     for i in range(repeat):
#         print(f"Hello, {name}!")
#
# if __name__ == "__main__":
#     typer.run(main)
# ```

# %% [markdown]
#
# ### Wie führen wir das Programm aus?
#
# ```fshell
# # Die Option wird durch ihren Namen identifiziert
# $ python greeter.py Bob --repeat 3
# Hello, Bob!
# Hello, Bob!
# Hello, Bob!
# ```

# %% [markdown]
#
# - `typer.Option` sagt `typer`, dass es sich um eine **Option** handelt.
#   - Da wir einen Standardwert (`= 1`) angegeben haben, ist sie optional.
# - `typer` konvertiert die Eingabe "3" automatisch nach `int`, weil wir einen
#   Typ-Hint angegeben haben.

# %% [markdown]
#
# ## Multi-Command Apps with `typer.Typer`
#
# - Was, wenn Ihre App mehrere Befehle benötigt?
#   - z.B.ein Taschenrechner mit `add` und `subtract`?
# - Sie verwenden ein `typer.Typer`-Objekt, um sie zu verwalten.

# %% [markdown]
#
# ### Das 3-Schritte-Muster
#
# 1. **Erstellen Sie eine App-Instanz:**
#    ```python
#    app = typer.Typer(help="A simple calculator app.")
#    ```

# %% [markdown]
#
# 2. **Definieren Sie Befehle mit einem Dekorator:**
#
# Verwenden Sie den `@app.command()`-Dekorator für jede Funktion, die ein Befehl
# sein soll.
#
#    ```python
#    @app.command()
#    def add(a: int, b: int):
#        """Add two numbers."""
#        print(f"The sum is: {a + b}")
#
#    @app.command()
#    def subtract(a: int, b: int):
#        """Subtract second number from the first."""
#        print(f"The result is: {a - b}")
#    ```

# %% [markdown]
#
# 3. **Führen Sie die `app()`-Funktion aus:**
#    ```python
#    if __name__ == "__main__":
#        app()
#    ```

# %% [markdown]
#
# ### Wie führen wir das Programm aus?
#
# ```shell
# $ python calculator.py add 5 3
# The sum is: 8
#
# $ python calculator.py subtract 10 4
# The result is: 6
# ```

# %% [markdown]
#
# ## Mehr zu Argumenten und Optionen
#
# `typer` bietet leistungsstarke Möglichkeiten, Argumente und Optionen zu
# definieren.

# %% [markdown]
#
# ### Optionen mit mehreren Werten
#
# Wenn Sie einen Parameter als `list` typisieren, können Sie ihn mehrmals
# angeben.
# ```python
# from typing import List
# import typer
# @app.command()
# def process_tags(tag: List[str] = typer.Option(None, "--tag", help="A tag to process.")):
#     if not tag:
#         print("No tags provided.")
#     else:
#         print(f"Processing tags: {tag}")
# ```
#
# Run with: `python my_app.py process-tags --tag important --tag urgent`

# %% [markdown]
#
# ## Automatische Hilfe
#
# - Einer der größten Vorteile von `typer` ist das kostenlose Hilfemenü.
# - Basierend auf Ihrem Code generiert es alles für Sie.
# - Wenn Sie `python calculator.py --help` auf unserer Taschenrechner-App
#   ausführen, würde es Folgendes produzieren:
#
# ```text
# Usage: calculator.py [OPTIONS] COMMAND [ARGS]...
#
#   A simple calculator app.
#
# Options:
#   --help  Show this message and exit.
#
# Commands:
#   add       Add two numbers.
#   subtract  Subtract second number from the first.
# ```


# %% [markdown]
#
# - `typer` erstellt sogar Hilfemenüs für jeden Unterbefehl!
# - Wenn Sie `python calculator.py add --help` ausführen, zeigt es die Argumente
#   speziell für den `add`-Befehl an.

# %% [markdown]
#
# ## Zusammenfassung & Wichtige Erkenntnisse
#
# - `typer` macht es einfach, leistungsstarke und benutzerfreundliche CLIs zu
#   erstellen.
# - Verwenden Sie `typer.run(my_func)` für Skripte mit einem einzigen Befehl.
# - Verwenden Sie `app = typer.Typer()` und `@app.command()` für Apps mit
#   mehreren Befehlen.
# - Funktionsparameter werden zu **Argumenten** (erforderlich, positionell) oder
#   **Optionen** (optional, benannt).
# - Verwenden Sie `typing.Annotated` oder die `typer.Argument()` /
#   `typer.Option()` Defaults, um sie zu konfigurieren.
# - `typer` verwendet Ihre Typannotationen (`str`, `bool`, `int`), um die
#   Benutzereingaben automatisch zu verarbeiten.
# - Sie erhalten fantastische, automatisch generierte **Hilfemeldungen**
#   kostenlos!

# %% [markdown]
#
# ## Workshop: Kommandozeilen Apps mit `typer`
#
# - Erstellen Sie eine CLI-App, die TODO-Listen verwaltet.
# - Implementieren Sie Befehle zum Hinzufügen, Entfernen und Auflisten von
#   Aufgaben und zum Markieren von Aufgaben als erledigt.
# - Speichern Sie die Aufgaben in einer Datei, um sie zwischen den Sitzungen
#   zu behalten.
