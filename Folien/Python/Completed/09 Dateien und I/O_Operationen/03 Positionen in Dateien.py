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
# # Positionen in Dateien
#
#  - Mit den Methoden `tell()` und `seek()` kann die Position in der Datei
#    abgefragt oder verändert werden.

# %%
line = "0123456789A123456789B123456789C123456789\n"
text = line * 2

# %%
with open("my-data-file.txt", mode="w") as file:
    file.write(text)

# %%
with open("my-data-file.txt", mode="r") as file:
    contents = file.read()
print(contents)

# %%
with open("my-data-file.txt", "r+") as file:
    print(f"File position before reading: {file.tell()}")
    contents = file.read()
    print(f"File position after reading: {file.tell()}")
    file.write(line)
    print(f"File position after writing: {file.tell()}")
print(contents)

# %%
new_line = "!! Let's overwrite a part of the file !!"
len(new_line)

# %%
with open("my-data-file.txt", "r+") as file:
    print(f"File has {len(file.readlines())} lines.")
    file.seek(41)
    file.write(new_line)
    file.seek(0)
    print(file.read())
