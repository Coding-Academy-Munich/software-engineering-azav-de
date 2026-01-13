# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Pathlib</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# ## Objektorientierter Umgang mit Dateien: Pathlib
#
# Das `pathlib`-Modul bietet mit der Klasse `Path` einen sehr eleganten
# objektorientierten Ansatz zum Umgang mit Dateien:

# %%

# %% [markdown]
#
# - `Path`-Objekte stellen Pfade zu Dateien und Verzeichnissen dar.
#   - Die Verzeichnisse und Dateien, die sie repräsentieren, müssen nicht
#     existieren.
#   - Es gibt aber Methoden, um zu prüfen, ob sie existieren, um sie zu
#     erzeugen, oder mit existierenden Verzeichnissen und Dateien zu arbeiten.
# - `Path`-Objekte sind plattformunabhängig.

# %%

# %%

# %% [markdown]
#
# - Bei der Umwandlung in Strings werden `Path`-Objekte in relative Pfade
#   umgewandelt.
# - Ohne Argumente wird der aktuelle Arbeitsordner verwendet.
# - Mit `absolute()` kann der absolute Pfad ermittelt werden.

# %%

# %% [markdown]
#
# - Der `Path`-Konstruktor kann auch mit Strings aufgerufen werden:
#   - `Path("test.txt")`
#     - Pfad zur Datei `test.txt` im aktuellen Arbeitsverzeichnis.
#   - `Path("my-dir/test.txt")`
#     - Pfad zur Datei `test.txt` im Unterverzeichnis `my-dir` des aktuellen
#       Arbeitsverzeichnisses.
#   - Es können auch absolute Pfade verwendet werden, die Syntax ist dann
#     plattformunabhängig:
#     - `Path("/home/user/test.txt")` (Linux)
#     - `Path("C:/Users/user/test.txt")` (Windows)
#     - `Path("C:\\Users\\user\\test.txt")` (Windows)

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %% [markdown]
#
# - `Path`-Objekte bieten viele nützliche Attribute und Methoden.
# - Einige davon beziehen sich auf auf den Pfad:
#   - `path / "my-dir"`: Erzeugt einen neuen Pfad, der `path` und `my-dir`
#     kombiniert.
#   - `name`: Name der Datei oder des Verzeichnisses
#   - `parent`: Verzeichnis, in dem sich die Datei oder das Verzeichnis befindet
#   - `suffix`: Dateiendung (z.B. `.txt`)
#   - `with_suffix()`: Erzeugt einen neuen Pfad mit einer anderen Dateiendung

# %%

# %%

# %%

# %%

# %%

# %%

# %% [markdown]
#
# - Manche Methoden beziehen sich auf das Dateisystem:
#   - `exists()`: Prüft, ob die Datei oder das Verzeichnis existiert
#   - `mkdir()`: Erzeugt ein Verzeichnis
#   - `open()`: Öffnet die Datei zum Lesen oder Schreiben
#   - `unlink()`: Löscht die Datei

# %%
my_file = Path("README.md")

# %%

# %% [markdown]
#
# - Wir wollen die Dateisystem-Operationen in einem temporären Verzeichnis
#   durchführen.
# - Das `tempfile`-Modul bietet dafür die Klasse `TemporaryDirectory`.
# - Diese Klasse erzeugt ein temporäres Verzeichnis, das beim Schließen des
#   Objekts gelöscht wird.

# %%

# %%

# %%

# %%

# %%

# %%

# %% [markdown]
#
# ### Erzeugen von Verzeichnissen

# %%

# %%

# %%

# %% [markdown]
#
# ### Erzeugen, Lesen und Schreiben von Dateien

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
# ### Löschen von Verzeichnissen und Dateien

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%
