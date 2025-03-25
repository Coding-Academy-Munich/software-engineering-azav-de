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
from tempfile import TemporaryDirectory

# %%
my_path = Path()
print("relative path:", my_path)
print("absolute path:", my_path.absolute())
my_path

# %%
my_file = my_path / "README.md"
print("Name:         ", my_file.name)
print("Parent:       ", my_file.parent.absolute())
print("Suffix:       ", my_file.suffix)
print("Change suffix:", my_file.with_suffix(".txt"))
print("Exists?       ", my_file.exists())

# %%
tmp_dir = TemporaryDirectory(ignore_cleanup_errors=True)
tmp_dir

# %%
tmp_dir_path = Path(tmp_dir.name)
print(tmp_dir_path.absolute())
print(tmp_dir_path.exists())

# %%
my_dir = tmp_dir_path / "subdir1/subdir2" / "subdir3"
my_dir.mkdir(parents=True, exist_ok=False)
my_dir.exists()

# %%
my_file = my_dir / "test.txt"
with my_file.open("w", encoding="utf-8") as file:
    file.write("Hello, world")
print("Exists?", my_file.exists(), "(should be True)")
print(list(my_dir.glob("*")))
my_file.unlink()
print("Exists?", my_file.exists(), "(should be False)")
print(list(my_dir.glob("*")))
my_file.unlink(missing_ok=True)

# %%
if my_dir.exists():
    my_dir.rmdir()
print("Exists?", my_dir.exists(), "(should be False)")

# %%
tmp_dir.cleanup()

# %%
tmp_dir_path.exists()
