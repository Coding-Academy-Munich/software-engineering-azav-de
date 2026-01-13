# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Initialisierung von Dataclasses</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %%

# %%

# %%


# %% [markdown]
#
# Es ist möglich, komplexere Initialisierungen vorzunehmen:
#
# - Die `__post_init__()` Methode kann Code zur Initialisierung von Objekten
#   enthalten, der nach der generierten `__init__()` Methode ausgeführt wird.

# %%
from dataclasses import dataclass, field, InitVar


# %%

# %%
@dataclass
class Point3D:
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0

    def move(self, dx=0.0, dy=0.0, dz=0.0):
        self.x += dx
        self.y += dy
        self.z += dz


# %%
class DependentInit:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.point = Point3D(x, y, z)

    def __repr__(self):
        return f"DependentInit({self.point})"

# %%

# %%


# %% [markdown]
#
# - Der Typ `InitVar[T]` deklariert, dass ein Klassen-Attribut als Argument an
#   `__post_init__()` übergeben und nicht als Instanz-Attribut verwendet wird.
# - Das Keyword-Argument `init=False` für `field()` bewirkt, dass ein Attribut
#   nicht in der generierten `__init__()` Methode initialisiert wird.

# %%
@dataclass
class DependentInit:
    x: InitVar[float] = 0.0
    y: InitVar[float] = 0.0
    z: InitVar[float] = 0.0
    point: Point3D = field(init=False)

    def __post_init__(self, x, y, z):
        self.point = Point3D(x, y, z)

# %%

# %%

# %%

# %%

# %%
