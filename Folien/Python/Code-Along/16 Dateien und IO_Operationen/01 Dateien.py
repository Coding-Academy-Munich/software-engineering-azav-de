# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Dateien</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# # Dateien
#
# Bislang gehen am Ende der Programmausführung alle Daten, die wir berechnet
# haben, verloren.
#
# Die einfachste Variante, Daten zu persistieren ist sie in einer Datei zu speichern.
#
# Bitte überprüfen Sie vor der Ausführung von Code in diesem Notebook, dass Ihr
# aktuelles Arbeitsverzeichnis keine wichtigen Daten enthält!


# %%
import os

# %%
os.getcwd()

# %% [markdown]
#
#  - Mit `open()` kann eine Datei zum Lesen oder Schreiben geöffnet werden.
#  - Der `mode` Parameter gibt an, ob die Datei zum Lesen oder Schreiben geöffnet
#    wird:
#    - `r`: Lesen
#    - `w`: Schreiben. Der Inhalt der Datei wird gelöscht
#    - `a`: Schreiben. Die neuen Daten werden ans Ende der Datei geschrieben.
#    - `x`: Schreiben. Die Datei darf nicht existieren.
#    - `r+`: Lesen und Schreiben.
#  - Wird ans Ende von `mode` der Buchstabe `b` angehängt, so wird die Datei als
#    Binärdatei behandelt.


# %%
file = open("my-data-file.txt", "w")
file.write("The first line.\n")
file.write("The second line.\n")
file.close()

# %%
file = open("my-data-file.txt", "r")
contents = file.read()
file.close()
print(contents)

# %% [markdown]
#
#  - Dateien müssen immer mit `close()` geschlossen werden, auch wenn der
#    Programmteil, in dem die Datei verwendet wird, eine Exception auslöst.
#  - Das könnte mit `try ... finally` erfolgen.
#  - Python bietet dafür ein eleganteres Konstrukt:

# %%
with open("my-data-file.txt", "r") as file:
    contents = file.read()
print(contents)

# %% [markdown]
#
# ## Mode-Werte zum Schreiben

# %%
with open("my-data-file.txt", mode="w") as file:
    file.write("Another line.\n")
    file.write("Yet another line.\n")

# %%
with open("my-data-file.txt", mode="r") as file:
    contents = file.read()
print(contents)

# %%
with open("my-data-file.txt", mode="a") as file:
    file.write("Let's try this again.\n")
    file.write("Until we succeed.\n")

# %%
with open("my-data-file.txt", "r") as file:
    contents = file.readlines()
print(contents)

# %%
# with open("my-data-file.txt", mode="x") as file:
#     file.write("Let's try this again.\n")
#     file.write("Until we succeed.\n")

# %% [markdown]
# ## Mini-Workshop: Lesen und Schreiben in Dateien
#
# Schreiben Sie eine Funktion
# `write_text_to_file(text: str, file_name: str)-> None`,
# die den String `text` in die Datei `file_name` schreibt, sofern
# diese *nicht* existiert und eine Exception vom Typ `FileExistsError` wirft,
# falls die Datei existiert.
#
# *Hinweis:*  Beachten Sie die möglichen Werte für das `mode` Argument von
# `open()`.

# %%

# %% [markdown]
#
# Testen Sie die Funktion, indem Sie zweimal hintereinander versuchen den
# Text `Python 3.11` in die Datei `my-private-file.txt` zu schreiben.

# %%


# %%

# %% [markdown]
#
# Schreiben Sie eine Funktion `annotate_file(file_name: str) -> None`, die
# - den Inhalt der Datei `file_name` gefolgt von dem Text `(annotated version)`
#   auf dem Bildschirm ausgibt, falls sie existiert
# - den Text `No file found, we will bill the time we spent searching.` ausgibt
#   falls sie nicht existiert
# - in beiden Fällen den Text `Our invoice will be sent by mail.` ausgibt.

# %%

# %%

# %%
