# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Arbeiten mit Jupyter Notebooks</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# # Arbeiten mit Jupyter Notebooks
# ## Interaktives Rechnen für Software-Engineering

# %% [markdown]
#
# ## I. Was sind Jupyter Notebooks?
#
# **Definition und Zweck:**
# - Interaktive Dokumente, die Code, Text und Visualisierungen kombinieren
# - Benannt nach Julia, Python und R (früh unterstützte Sprachen)
# - Ideal für:
#   - Explorative Datenanalyse
#   - Lehren und Lernen
#   - Dokumentation mit Live-Code
#   - Prototyping und Experimentieren

# %% [markdown]
#
# ## II. Jupyter Notebooks in VS Code
#
# **Hauptfunktionen:**
# - Integrierte Entwicklungsumgebung
# - IntelliSense-Code-Vervollständigung
# - Debug-Funktionen
# - Git-Integration
# - Erweiterungsökosystem
# - Variablen-Explorer
# - Anpassbare Benutzeroberfläche

# %% [markdown]
#
# ## III. Zelltypen und Modi
#
# **Hauptzelltypen:**
# - Code-Zellen: Führen Programmcode aus
# - Markdown-Zellen: Formatieren Text mit Markdown
#
# **Interaktionsmodi:**
# - Befehlsmodus: Zellnavigation und -manipulation (kein Rahmen)
# - Bearbeitungsmodus: Bearbeiten des Zelleninhalts (Rahmen um Zelle)
# - Klicken Sie innerhalb/außerhalb der Zelle oder drücken Sie `Eingabe`/`Esc`,
#   um die Modi zu wechseln

# %%
# This is a code cell
print("Hello, Jupyter!")

# %%
# This is another code cell
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(f"Number: {num}, Square: {num**2}")

# %% [markdown]
#
# ## IV. Arbeiten mit Code-Zellen
#
# **Probieren Sie es aus:** Führen Sie die folgende Zelle aus, indem Sie darauf klicken und `Umschalt+Eingabe` drücken

# %%
# Dies ist eine Code-Zelle
print("Hallo, Jupyter!")

# %%
# Dies ist eine weitere Code-Zelle
zahlen = [1, 2, 3, 4, 5]
for zahl in zahlen:
    print(f"Zahl: {zahl}, Quadrat: {zahl**2}")

# %% [markdown]
#
# ### Arbeiten mit Code-Zellen
#
# **Ausführung**:
# - `Umschalt+Eingabe`: Zelle ausführen und zur nächsten Zelle gehen
# - `Strg+Eingabe`: Zelle ausführen und in derselben Zelle bleiben
# - `Alt+Eingabe`: Zelle ausführen und neue Zelle darunter einfügen
# - Ausführen-Schaltfläche in der Symbolleiste
# - Das Ergebnis des letzten Ausdrucks wird unterhalb der Zelle gedruckt

# %%
print("Text printed to the console")

# %%
17 + 4

# %%
x = 10

# %%
x

# %%
1
2
3

# %% [markdown]
#
# **Code-Organisation**:
# - Code-Zellen auf eine einzelne Aufgabe fokussieren
# - Komplexe Operationen in mehrere Zellen aufteilen
# - Variablen verwenden, um Daten zwischen Zellen zu übertragen
# - Bedenken Sie, dass die Ausführungsreihenfolge wichtig ist, nicht die Zellenreihenfolge im Dokument

# %%
# Vielleicht nicht die beste Art, Dinge zu organisieren:
print("Ausführung einer komplexen Operation...")
print("Ausführung einer anderen, nicht verwandten Operation...")

# %%
# Bessere Organisation: separate Zellen für separate Aufgaben
print("Ausführung einer komplexen Operation...")

# %% [markdown]
# print("Ausführung einer anderen, nicht verwandten Operation...")

# %%
x = 10

# %%
x = 20

# %% [markdown]
#
# **Ausführungsstatus**:
# - Zellen können in beliebiger Reihenfolge ausgeführt werden
# - Zellennummern `[1]`, `[2]` usw. zeigen die Ausführungsreihenfolge an
# - `Kernel > Neu starten & Alle ausführen` für sequenzielle Ausführung
# - Spinner in der unteren linken Zellenecke zeigt an, dass sie gerade ausgeführt wird
#   - (In Jupyter-Notebooks ist dies ein `[*]` neben der Zellennummer)

# %%
import time
# time.sleep(5)

# %%
# Define a variable
my_variable = 42
print(f"Initial value: {my_variable}")

# %%
# Use the variable in another cell
print(f"The value is still: {my_variable}")

# %%
# Modify the variable
my_variable += 10

# %%
print(f"New value: {my_variable}")

# %% [markdown]
#
# ## V. Variablenzustand und Speicher
#
# **Variablen bleiben zwischen Zellen erhalten:**

# %%
# Eine Variable definieren
meine_variable = 42
print(f"Anfangswert: {meine_variable}")

# %%
# Die Variable in einer anderen Zelle verwenden
print(f"Der Wert ist immer noch: {meine_variable}")

# %%
# Variable ändern
meine_variable += 10

# %%
print(f"Neuer Wert: {meine_variable}")

# %% [markdown]
#
# ## VI. Arbeiten mit Markdown-Zellen
#
# **Beispiele für Markdown-Formatierung:**

# %% [markdown]
# # Überschrift 1
# ## Überschrift 2
# ### Überschrift 3
#
# * Aufzählungspunkt 1
# * Aufzählungspunkt 2
#   * Verschachtelter Punkt
#
# 1. Nummerierte Liste
# 2. Zweiter Punkt

# %% [markdown]
#
# **Fetter Text** und *kursiver Text*
#
# `Inline-Code` und Codeblöcke:
# ```python
# def hallo():
#     return "Hallo, Welt!"
# ```
#
# [Link zu Google](https://google.com)
#
# Mathematische Gleichungen: $E = mc^2$

# %% [markdown]
#
# ## VII. Wichtige Tastaturkürzel
#
# **Befehlsmodus** (Drücken Sie `Esc`, um einzutreten):
# - `A`: Zelle darüber einfügen
# - `B`: Zelle darunter einfügen
# - `D,D`: Zelle löschen (D zweimal drücken)
# - `Y`: In Code-Zelle umwandeln
# - `M`: In Markdown-Zelle umwandeln
# - `Umschalt+Eingabe`: Zelle ausführen und zur nächsten gehen
# - `Strg+Eingabe`: Zelle ausführen und bleiben
# - `Pfeil auf/ab`: Zwischen Zellen navigieren

# %% [markdown]
#
# ## VIII. Interaktive Übung: Probieren Sie es selbst
#
# **Aufgaben:**
# 1. Erstellen Sie eine neue Code-Zelle unten (drücken Sie `B` im Befehlsmodus)
# 2. Schreiben Sie Code, der eine Funktion erstellt, um die Fakultät einer Zahl zu berechnen
#    ```python
#    def factorial(n):
#        if n <= 0:
#            return 1
#        else:
#            return n * factorial(n-1)
#    ```
# 3. Führen Sie die Zelle aus
# 4. Erstellen Sie eine weitere Zelle, um Ihre Funktion mit verschiedenen Eingaben zu testen
#    ```python
#    factorial(5)
#    ```
# 5. Führen Sie die Testzelle aus
# 6. Experimentieren Sie mit verschiedenen Eingaben, um zu sehen, wie sich die Funktion verhält
# 7. Erstellen Sie eine Markdown-Zelle, um Notizen oder Erklärungen zu schreiben
