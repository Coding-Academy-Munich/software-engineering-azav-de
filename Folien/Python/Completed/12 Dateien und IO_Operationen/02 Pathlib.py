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
from pathlib import Path

# %% [markdown]
#
# - `Path`-Objekte stellen Pfade zu Dateien und Verzeichnissen dar.
#   - Die Verzeichnisse und Dateien, die sie repräsentieren, müssen nicht
#     existieren.
#   - Es gibt aber Methoden, um zu prüfen, ob sie existieren, um sie zu
#     erzeugen, oder mit existierenden Verzeichnissen und Dateien zu arbeiten.
# - `Path`-Objekte sind plattformunabhängig.

# %%
my_path = Path()

# %%
my_path

# %% [markdown]
#
# - Bei der Umwandlung in Strings werden `Path`-Objekte in relative Pfade
#   umgewandelt.
# - Ohne Argumente wird der aktuelle Arbeitsordner verwendet.
# - Mit `absolute()` kann der absolute Pfad ermittelt werden.

# %%
print("relative path:", my_path)
print("absolute path:", my_path.absolute())

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
my_path = Path("test.txt")

# %%
my_path

# %%
my_path.absolute()

# %%
my_path = Path("my-dir/test.txt")

# %%
my_path.absolute()

# %%
my_path = Path("C:/Users/user/test.txt")

# %%
my_path.absolute()

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
my_file = my_path / "README.md"

# %%
my_file.name

# %%
my_file.parent.absolute()

# %%
my_file.suffix

# %%
my_file.with_suffix(".txt")

# %%
my_file

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
my_file.exists()

# %% [markdown]
#
# - Wir wollen die Dateisystem-Operationen in einem temporären Verzeichnis
#   durchführen.
# - Das `tempfile`-Modul bietet dafür die Klasse `TemporaryDirectory`.
# - Diese Klasse erzeugt ein temporäres Verzeichnis, das beim Schließen des
#   Objekts gelöscht wird.

# %%
from tempfile import TemporaryDirectory

# %%
tmp_dir = TemporaryDirectory(ignore_cleanup_errors=True)

# %%
tmp_dir

# %%
tmp_dir_path = Path(tmp_dir.name)

# %%
tmp_dir_path.absolute()

# %%
tmp_dir_path.exists()

# %% [markdown]
#
# ### Erzeugen von Verzeichnissen

# %%
my_dir = tmp_dir_path / "subdir1/subdir2" / "subdir3"

# %%
my_dir.mkdir(parents=True, exist_ok=False)

# %%
my_dir.exists()

# %% [markdown]
#
# ### Erzeugen, Lesen und Schreiben von Dateien

# %%
my_file = my_dir / "test.txt"

# %%
with my_file.open("w", encoding="utf-8") as file:
    file.write("Hello, world")

# %%
my_file.exists()

# %%
list(my_dir.glob("*"))

# %%
text = my_file.read_text(encoding="utf-8")

# %%
text

# %%
my_file.write_text("Some text...", encoding="utf-8")

# %%
my_file.read_text(encoding="utf-8")

# %% [markdown]
#
# ### Löschen von Verzeichnissen und Dateien

# %%
my_file.unlink()

# %%
my_file.exists()

# %%
list(my_dir.glob("*"))

# %%
my_file.unlink(missing_ok=True)

# %%
if my_dir.exists():
    my_dir.rmdir()

# %%
my_dir.exists()

# %%
tmp_dir.cleanup()

# %%
tmp_dir_path.exists()
