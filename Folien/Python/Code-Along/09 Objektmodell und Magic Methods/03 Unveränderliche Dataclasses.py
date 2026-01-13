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
@dataclass
class FrozenPoint:
    x: float = field(default=0.0)
    y: float = field(default=0.0)

# %%

# %%

# %% [markdown]
#
# ## Arbeiten mit unveränderlichen Dataclasses
#
# - Statt dem Ändern eines Attributs wird ein neues Objekt erzeugt
# - Das `dataclasses` Modul stellt dafür die Funktion `replace()` zur Verfügung

# %%

# %%

# %%

# %%

# %%


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

# %%

# %%

# %%


# %%

# %%

# %%

# %%
