# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Unveränderliche Dataclasses</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# - Es ist möglich "unveränderliche" Dataclasses zu definieren
# - Diese definieren automatisch eine `__hash__()` Methode
# - Damit können sie z.B. als Schlüssel in einem `dict` verwendet werden

# %%
from dataclasses import dataclass, field


# %%
@dataclass(frozen=True)
class FrozenPoint:
    x: float = field(default=0.0)
    y: float = field(default=0.0)


# %%
fp = FrozenPoint()
fp

# %%
# fp.x = 1.0

# %% [markdown]
#
# ## Arbeiten mit unveränderlichen Dataclasses
#
# - Statt dem Ändern eines Attributs wird ein neues Objekt erzeugt
# - Das `dataclasses` Modul stellt dafür die Funktion `replace()` zur Verfügung

# %%
from dataclasses import replace

# %%
fp

# %%
replace(fp, x=1.0)

# %%
fp

# %%
fp2 = replace(fp, x=1.0, y=2.0)
fp2


# %% [markdown]
#
# ## Workshop: Unveränderliche Dataclasses
#
# - Definieren Sie eine Dataclass `Name` mit folgenden Attributen
#   - `first_name: str`
#   - `last_name: str`
# - Erzeugen Sie eine Instanz `name` mit den Werten "Max" und "Mustermann"
# - Was passiert, wenn Sie `name` als Key in einem `dict` verwenden?
# - Modifizieren Sie die Klasse `Name` so, dass ihre Instanzen als Key in einem
#   `dict` verwendet werden können

# %%
from dataclasses import dataclass


# %%
@dataclass
class Name:
    first_name: str
    last_name: str


# %%
name = Name("Max", "Mustermann")

# %%
# d = {name: "Mr. Doe"}


# %%
@dataclass(frozen=True)
class Name:
    first_name: str
    last_name: str


# %%
name = Name("Max", "Mustermann")  # noqa

# %%
d = {name: "Mr. Doe"}

# %%
d[name]
