# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Klassenmethoden und Factories</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# ## Klassenmethoden und Factories
#
# Eine Factory ist eine Funktion (oder Klasse), die zur Konstruktion von
# Objekten verwendet werden kann. Python bietet mit Klassenmethoden ein
# mächtiges Konstrukt für die Implementierung von Factories an.
#
# Klassenmethoden sind Methoden, die typischerweise auf einer Klasse (und nicht
# einem Objekt) aufgerufen werden. Im Gegensatz zu statischen Methoden (die
# keine Information über die Klasse, auf der sie aufgerufen werden bekommen)
# bekommen Klassenmethoden das Klassenobjekt, auf dem sie aufgerufen werden, als
# argument. Dieses Klassenobjekt kann verwendet werden um Operationen
# auszuführen, die von der Klasse abhängen, z.B. das Erstellen von
# Objektinstanzen.

# %%
from dataclasses import dataclass

# %%
@dataclass
class Color:
    r: float = 0.0
    g: float = 0.0
    b: float = 0.0
    color_table = {
        "white": (1.0, 1.0, 1.0),
        "red": (1.0, 0.0, 0.0),
        "green": (0.0, 1.0, 0.0),
        "blue": (0.0, 0.0, 1.0),
    }

    @classmethod
    def from_string(cls, color):
        return cls(*cls.color_table.get(color, (0.0, 0.0, 0.0)))

    @classmethod
    def from_unsigned(cls, r, g, b):
        return cls(r / 255, g / 255, b / 255)


# %%
Color(0.5, 0.5, 0.5)

# %%
Color.from_string("red")

# %%
Color.from_unsigned(255, 0, 0)

# %% [markdown]
#
# Falls die Konstruktor-Argumente einer Subklasse mit der Oberklasse kompatibel
# sind, können die Klassenmethoden der Oberklasse direkt als Factories für die
# Unterklassen verwendet werden.

# %%
@dataclass
class AlphaColor(Color):
    alpha: float = 1.0


# %%
AlphaColor(0.5, 0.5, 0.5)

# %%
AlphaColor.from_string("red")

# %%
AlphaColor.from_unsigned(255, 0, 0)

# %% [markdown]
#
# ## Attribute von Klassen
#
# Die meisten Attribute werden auf der Instanz-Ebene definiert, d.h.,
# jedes Objekt hat seine eigenen Werte für die Attribute. Manchmal ist es
# aber sinnvoll Attribute auch auf der Klassenebene zu definieren:

# %%
class CountedAdder:
    # Attribut der Klasse, wird von allen Instanzen geteilt
    num_counters = 0

    def __init__(self, value):
        CountedAdder.num_counters += 1
        # Instanzvariable (-attribut): Jede Instanz hat eigene Werte dafür
        self.value = value

    def describe(self):
        print(
            f"One of {CountedAdder.num_counters} adders. "
            f"This one adds {self.value} to its argument."
        )

    def add(self, n):
        return self.value + n


# %%
print(CountedAdder.num_counters)
a1 = CountedAdder(10)
print(CountedAdder.num_counters)
a2 = CountedAdder(20)
print(CountedAdder.num_counters)

# %%
print(a1.add(1))
print(a2.add(2))

# %%
a1.describe()
a2.describe()

# %%
print(CountedAdder.num_counters)
print(a1.num_counters)
print(a2.num_counters)

# %%
print(CountedAdder.add)
print(a1.add)
print(a2.add)


# %% [markdown]
# ### Vererbung


# %%
class LoggingAdder(CountedAdder):
    def add(self, n):
        print(f"Adding {self.value} to {n}")
        return self.value + n


# %%
a3 = LoggingAdder(30)
print(a3.add(3))
print(a3.num_counters)

# %%
a1.describe()
a2.describe()
a3.describe()

# %%
# Method Resolution Order:
LoggingAdder.mro()

# %%
print(CountedAdder.add)
print(a1.add)
print(a2.add)
print(LoggingAdder.add)
print(a3.add)

# %%
print(CountedAdder.add)
print(a1.add.__func__)
print(a2.add.__func__)
print(LoggingAdder.add)
print(a3.add.__func__)

# %%
a1.__dict__["value"] = 15

# %%
a1.add(0)

# %%
LoggingAdder.__dict__
