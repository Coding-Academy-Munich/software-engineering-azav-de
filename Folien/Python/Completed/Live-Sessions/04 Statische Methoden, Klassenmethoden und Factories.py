# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Statische Methoden, Klassenmethoden und Factories</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# ## Die Klasse `Point`
#
# Wir verwenden wieder unsere `Point`-Klasse:

# %%
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"{type(self).__name__}(x={self.x}, y={self.y})"

    def distance_from_origin(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5


# %%
p = Point(3, 4)

# %%
p

# %%
p.distance_from_origin()

# %% [markdown]
#
# ## Punkte aus Polarkoordinaten erzeugen
#
# Was, wenn wir einen Punkt aus Polarkoordinaten $(r, \theta)$ erzeugen
# wollen?
#
# - $r$: Abstand vom Ursprung
# - $\theta$: Winkel zur x-Achse (im Bogenmaß)

# %%
import math

# %% [markdown]
#
# ### Lösung 1: Freie Funktion
#
# Wir können eine eigenständige Funktion schreiben:

# %%
def point_from_polar_coordinates(r, theta):
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    return Point(x, y)


# %%
polar_point = point_from_polar_coordinates(5, math.pi / 2)

# %%
polar_point

# %%
polar_point.distance_from_origin()

# %% [markdown]
#
# ### Probleme mit freien Funktionen
#
# - Die Funktion gehört nicht erkennbar zur Klasse `Point`
# - Benutzer müssen wissen, dass sie separat existiert
# - Bei vielen solcher Funktionen wird der Namensraum unübersichtlich
# - Besser: Die Funktion direkt an die Klasse binden

# %% [markdown]
#
# ## Statische Methoden
#
# - Eine Methode, die zur Klasse gehört, aber kein `self` oder `cls`
#   bekommt
# - Wird mit `@staticmethod` dekoriert
# - Aufruf auf der Klasse: `Point.from_polar_coordinates(...)`
# - Wie eine normale Funktion, aber innerhalb der Klasse organisiert

# %%
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"{type(self).__name__}(x={self.x}, y={self.y})"

    def distance_from_origin(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    @staticmethod
    def from_polar_coordinates(r, theta):
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        return Point(x, y)

    @staticmethod
    def from_cartesian_coordinates(x, y):
        return Point(x, y)


# %%
Point.from_polar_coordinates(5, math.pi / 2)

# %%
Point.from_cartesian_coordinates(3, 4)

# %% [markdown]
#
# Das funktioniert gut! Aber was passiert bei Unterklassen?

# %% [markdown]
#
# ## Das Problem mit Vererbung
#
# Definieren wir eine Unterklasse `ColorPoint`:

# %%
class ColorPoint(Point):
    def __init__(self, x, y, color="black"):
        super().__init__(x, y)
        self.color = color

    def __repr__(self):
        return (
            f"{type(self).__name__}"
            f"(x={self.x}, y={self.y}, color='{self.color}')"
        )


# %%
ColorPoint(3, 4, "red")

# %% [markdown]
#
# Was liefern die statischen Methoden?

# %%
cp = ColorPoint.from_polar_coordinates(5, math.pi / 2)

# %%
# cp

# %%
type(cp)

# %% [markdown]
#
# ### Warum geht das schief?
#
# - Statische Methoden wissen nicht, auf welcher Klasse sie aufgerufen
#   werden
# - `Point(x, y)` ist fest einprogrammiert
# - `ColorPoint.from_polar_coordinates(...)` erzeugt trotzdem einen
#   `Point`
# - Wir brauchen eine Methode, die die tatsächliche Klasse kennt

# %% [markdown]
#
# ## Klassenmethoden
#
# - Wie eine statische Methode, aber bekommt `cls` als ersten Parameter
# - `cls` ist die Klasse, auf der die Methode aufgerufen wurde
# - Wir verwenden `cls(...)` statt den Klassennamen fest einzuprogrammieren
# - So erzeugt die Factory automatisch den richtigen Typ

# %%
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"{type(self).__name__}(x={self.x}, y={self.y})"

    def distance_from_origin(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    @classmethod
    def from_polar_coordinates(cls, r, theta):
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        return cls(x, y)

    @classmethod
    def from_cartesian_coordinates(cls, x, y):
        return cls(x, y)


# %%
Point.from_polar_coordinates(5, math.pi / 2)

# %%
Point.from_cartesian_coordinates(3, 4)

# %% [markdown]
#
# Für `Point` selbst verhält sich das genauso wie vorher. Aber jetzt mit
# `ColorPoint`:

# %% [markdown]
#
# ## Der Vorteil: Unterklassen funktionieren

# %%
class ColorPoint(Point):
    def __init__(self, x, y, color="black"):
        super().__init__(x, y)
        self.color = color

    def __repr__(self):
        return (
            f"{type(self).__name__}"
            f"(x={self.x}, y={self.y}, color='{self.color}')"
        )


# %%
cp = ColorPoint.from_polar_coordinates(5, math.pi / 2)

# %%
# cp

# %%
type(cp)

# %%
ColorPoint.from_cartesian_coordinates(3, 4)

# %% [markdown]
#
# ## Zusätzliche Argumente weiterleiten
#
# `ColorPoint` hat einen zusätzlichen Parameter `color`. Mit `*args` und
# `**kwargs` können wir zusätzliche Argumente an den Konstruktor der
# Unterklasse weiterleiten:
#
# - `*args`: Beliebig viele positionale Argumente
# - `**kwargs`: Beliebig viele benannte Argumente

# %%
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"{type(self).__name__}(x={self.x}, y={self.y})"

    def distance_from_origin(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    @classmethod
    def from_polar_coordinates(cls, r, theta, *args, **kwargs):
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        return cls(x, y, *args, **kwargs)

    @classmethod
    def from_cartesian_coordinates(cls, x, y, *args, **kwargs):
        return cls(x, y, *args, **kwargs)


# %%
class ColorPoint(Point):
    def __init__(self, x, y, color="black"):
        super().__init__(x, y)
        self.color = color

    def __repr__(self):
        return (
            f"{type(self).__name__}"
            f"(x={self.x}, y={self.y}, color='{self.color}')"
        )


# %%
ColorPoint.from_cartesian_coordinates(3, 4, "red")

# %%
ColorPoint.from_cartesian_coordinates(3, 4, color="blue")

# %%
ColorPoint.from_polar_coordinates(5, math.pi / 2, color="green")

# %% [markdown]
#
# ## Zusammenfassung
#
# | | `@staticmethod` | `@classmethod` |
# |---|---|---|
# | Erster Parameter | keiner | `cls` (die Klasse) |
# | Kennt die Klasse? | Nein | Ja |
# | Gut für | Hilfsfunktionen | Factories |
# | Vererbung | Erzeugt immer die Basisklasse | Erzeugt die richtige Unterklasse |
#
# **Factory-Methoden** sind alternative Konstruktoren, die Objekte auf
# verschiedene Arten erzeugen (z.B. aus Polarkoordinaten, aus Strings,
# etc.)

# %% [markdown]
#
# ## Workshop: Fahrzeug-Factories
#
# Gegeben ist die folgende `Vehicle`-Klasse:

# %%
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __repr__(self):
        return f"{type(self).__name__}(make='{self.make}', model='{self.model}')"


# %%
Vehicle("Toyota", "Corolla")

# %% [markdown]
#
# Schreiben Sie eine statische Methode `from_string(s)`, die einen String
# der Form `"make:model"` parst und ein `Vehicle` erzeugt:
#
# ```python
# >>> Vehicle.from_string("Toyota:Corolla")
# Vehicle(make='Toyota', model='Corolla')
# ```

# %%
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __repr__(self):
        return f"{type(self).__name__}(make='{self.make}', model='{self.model}')"

    @staticmethod
    def from_string(s):
        make, model = s.split(":")
        return Vehicle(make, model)


# %%
v = Vehicle.from_string("Toyota:Corolla")
assert v.make == "Toyota"
assert v.model == "Corolla"
assert type(v) is Vehicle

# %%
v

# %% [markdown]
#
# Ändern Sie `from_string()` zu einer Klassenmethode. Definieren Sie dann
# eine Unterklasse `ElectricVehicle` mit einem zusätzlichen Attribut
# `range_km`:

# %%
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __repr__(self):
        return f"{type(self).__name__}(make='{self.make}', model='{self.model}')"

    @classmethod
    def from_string(cls, s):
        make, model = s.split(":")
        return cls(make, model)


# %%
class ElectricVehicle(Vehicle):
    def __init__(self, make, model, range_km=0):
        super().__init__(make, model)
        self.range_km = range_km

    def __repr__(self):
        return (
            f"{type(self).__name__}"
            f"(make='{self.make}', model='{self.model}'"
            f", range_km={self.range_km})"
        )


# %%
ev = ElectricVehicle.from_string("Tesla:Model3")
assert ev.make == "Tesla"
assert ev.model == "Model3"
assert type(ev) is ElectricVehicle

# %%
ev

# %% [markdown]
#
# Erweitern Sie `from_string()` mit `*args` und `**kwargs`, so dass
# zusätzliche Argumente an den Konstruktor der Unterklasse weitergeleitet
# werden:
#
# ```python
# >>> ElectricVehicle.from_string("Tesla:Model3", range_km=500)
# ElectricVehicle(make='Tesla', model='Model3', range_km=500)
# ```

# %%
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __repr__(self):
        return f"{type(self).__name__}(make='{self.make}', model='{self.model}')"

    @classmethod
    def from_string(cls, s, *args, **kwargs):
        make, model = s.split(":")
        return cls(make, model, *args, **kwargs)


# %%
class ElectricVehicle(Vehicle):
    def __init__(self, make, model, range_km=0):
        super().__init__(make, model)
        self.range_km = range_km

    def __repr__(self):
        return (
            f"{type(self).__name__}"
            f"(make='{self.make}', model='{self.model}'"
            f", range_km={self.range_km})"
        )


# %%
ev = ElectricVehicle.from_string("Tesla:Model3", range_km=500)
assert ev.make == "Tesla"
assert ev.model == "Model3"
assert ev.range_km == 500
assert type(ev) is ElectricVehicle

# %%
ev
