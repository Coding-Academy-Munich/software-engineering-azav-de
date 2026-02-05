# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Positionen in Dateien</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# ## Motivation
#
# - Bisher: Dateien sequentiell lesen oder schreiben
# - Problem: Was wenn wir nur einen Teil der Datei ändern wollen?
# - Lösung: Direkt zu bestimmten Positionen in der Datei springen

# %% [markdown]
#
# ## Die Methoden `tell()` und `seek()`
#
# - `tell()`: Gibt die aktuelle Position in der Datei zurück
# - `seek(position)`: Springt zu einer bestimmten Position
# - Position wird in **Bytes** gemessen (nicht Zeichen!)

# %% [markdown]
#
# ## Wichtig: Bytes vs. Zeichen
#
# - ASCII-Zeichen: 1 Byte pro Zeichen
# - UTF-8: 1-4 Bytes pro Zeichen
# - `seek()` arbeitet mit Bytes, nicht mit Zeichen!
# - Bei reinem ASCII ist das kein Problem

# %% [markdown]
#
# ## Beispiel: Testdaten erstellen
#
# - Wir erstellen eine Datei mit bekanntem Inhalt
# - Jede Zeile hat 41 Zeichen (inkl. Newline)

# %%
line = "0123456789A123456789B123456789C123456789\n"
text = line + line.lower()
print(text)

# %% [markdown]
#
# ## Datei schreiben und lesen

# %%

# %%

# %% [markdown]
#
# ## Position verfolgen mit `tell()`
#
# - Nach dem Öffnen: Position ist 0
# - Nach jedem Lesen/Schreiben: Position rückt vor
# - `tell()` zeigt immer die aktuelle Position

# %%
with open("my-data-file.txt", mode="w") as file:
    file.write(text)

# %%

# %%

# %% [markdown]
#
# ## Mit `seek()` springen
#
# - `seek(0)`: Zurück zum Anfang
# - `seek(n)`: Springe zu Byte n
# - Ermöglicht erneutes Lesen oder gezieltes Überschreiben

# %%
with open("my-data-file.txt", mode="w") as file:
    file.write(text)

# %%

# %% [markdown]
#
# ## Daten überschreiben
#
# - Mit `seek()` können wir zu einer Position springen
# - Dann mit `write()` überschreiben
# - **Wichtig**: Die neuen Daten überschreiben die alten!

# %%
new_text = "!!! OVERWRITTEN !!!"
len(new_text)

# %%
with open("my-data-file.txt", mode="w") as file:
    file.write(text)

# %%

# %% [markdown]
#
# ## Problem: Daten einfügen
#
# - `write()` überschreibt, fügt nicht ein!
# - Dateien sind wie ein Band, nicht wie eine Liste
# - Um Daten einzufügen, müssen wir den Rest verschieben

# %% [markdown]
#
# ## Vergleich: Listen vs. Dateien
#
# Listen können Elemente einfügen:

# %%

# %% [markdown]
#
# - Bei Dateien geht das **nicht** direkt!
# - Wir müssen den Rest der Datei manuell verschieben

# %% [markdown]
#
# ## Lösung: Daten in der Mitte einfügen
#
# Strategie:
# 1. Lesen bis zur Einfügeposition
# 2. Position merken mit `tell()`
# 3. Rest der Datei lesen und speichern
# 4. Zurück zur gemerkten Position mit `seek()`
# 5. Neue Daten schreiben
# 6. Gespeicherten Rest schreiben

# %%
with open("my-data-file.txt", mode="w") as file:
    file.write(text)

print("Before insertion:")
print("=" * 40)
with open("my-data-file.txt", mode="r") as file:
    print(file.read())
print("=" * 40)


# %%

# %%

# %% [markdown]
#
# ## Anwendungsfall: Datenblöcke fester Größe
#
# - Wenn alle Datensätze gleich groß sind:
#   - Können wir direkt zu einem bestimmten Datensatz springen
#   - Position = Index × Datensatzgröße
# - Beispiel: Highscore-Tabelle eines Spiels

# %% [markdown]
#
# ### Highscore-Datei erstellen
#
# - Jeder Eintrag: Name (10 Zeichen) + Punktzahl (6 Ziffern) + Newline
# - Feste Größe: 17 Bytes pro Eintrag

# %%
def format_record(name, score):
    return f"{name:10}{score:06d}\n"

RECORD_SIZE = 17  # 10 + 6 + 1

# %%
high_scores = [
    ("Alice", 950),
    ("Bob", 875),
    ("Carol", 820),
    ("David", 750),
    ("Eve", 700),
]

# %%

# %% [markdown]
#
# ### Bestimmten Rang direkt lesen
#
# - Wer ist auf Platz 3?
# - Position = (Rang - 1) × Datensatzgröße

# %%

# %% [markdown]
#
# ### Bestimmten Rang aktualisieren
#
# - Frank schlägt Carols Punktzahl und nimmt Platz 3 ein

# %%

# %%

# %% [markdown]
#
# ### Hinweis: Binärdaten für echte Anwendungen
#
# - Unser Beispiel verwendet Text (ASCII)
# - Problem: UTF-8-Zeichen haben unterschiedliche Byte-Längen
# - Lösung: Binärdaten mit Pythons `struct`-Modul
# - Beispiel: `struct.pack("10s i", name.encode(), score)`
# - Garantiert konsistente Datensatzgrößen

# %% [markdown]
#
# ## Zusammenfassung
#
# - `tell()`: Aktuelle Position abfragen
# - `seek(n)`: Zu Position n springen
# - Schreiben überschreibt, fügt nicht ein
# - Für Einfügen: Rest lesen, verschieben, schreiben
# - Besonders nützlich bei Daten fester Größe

# %% [markdown]
#
# ## Wann `tell()` und `seek()` verwenden?
#
# - **Ja**: Große Dateien, nur kleiner Teil zu ändern
# - **Ja**: Datenbanken mit festen Datensatzgrößen
# - **Nein**: Kleine Dateien (komplett neu schreiben ist einfacher)
# - **Nein**: Komplexe Textmanipulationen (besser im Speicher)
