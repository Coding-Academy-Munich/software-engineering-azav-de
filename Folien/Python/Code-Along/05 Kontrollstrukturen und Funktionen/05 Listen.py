# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Listen</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# ## Listen
#
# - Wir können mittlerweile Programme schreiben, die viele Arten von
#   Berechnungen ausführen, aber wir haben noch keine Möglichkeit, mehrere
#   Objekte zusammenzufassen.
# - Wenn wir beispielsweise eine Einkaufsliste erstellen wollen, müssen wir
#   uns im Moment mit folgender Lösung behelfen:

# %%
produkt_1 = "Haferflocken"
produkt_2 = "Kaffeebohnen"
produkt_3 = "Orangenmarmelade"

# %% [markdown]
#
# Diese Vorgehensweise hat viele Probleme:
#
# - Wir müssen genau wissen, wie viele Produkte wir kaufen wollen
# - Es gibt keine Möglichkeit Operationen auf allen Produkten auszuführen,
#   z.B. alle Produkte auszudrucken
# - Python weiß nicht, dass die Produkte zusammengehören
# - ...

# %% [markdown]
#
# ## Die Lösung: Listen

# %%

# %% [markdown]
# Der Typ von Listen ist `list`.

# %%

# %% [markdown]
# ## Erzeugen von Listen
#
# - Listen werden erzeugt, indem man ihre Elemente in eckige Klammern
#   einschließt.
# - Die Elemente einer Liste können beliebige Python-Werte sein.
# - Eine Liste kann Elemente mit verschiedenen Typen enthalten.

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
# Die Elemente einer Liste müssen keine Literale sein, man kann auch Werte von
# Variablen in einer Liste speichern:

# %%
produkt_1 = "Haferflocken"
produkt_2 = "Kaffeebohnen"
produkt_3 = "Orangenmarmelade"

# %%

# %% [markdown]
#
# Nachdem eine Liste erzeugt ist hat sie keine Verbindung zu den Variablen, die
# in ihrer Konstruktion verwendet wurden:

# %%

# %% [markdown]
# ## Zugriff auf Listenelemente

# %%
numbers = [2, 4, 6, 8]

# %%

# %%

# %%

# %% [markdown]
#
# ## Andere Möglichkeiten, Listen zu erzeugen
#
# Mit dem Additionsoperator `+` können Listen konkateniert werden:

# %%

# %% [markdown]
#
# Durch den Multiplikationsoperator `*` können die Elemente einer Liste
# wiederholt werden:

# %%

# %%

# %%

# %% [markdown]
# Mit der Funktion `list()` können manche andere Datentypen in Listen umgewandelt
# werden.
#
# Im Moment kennen wir nur Listen und Strings als mögliche Argumenttypen:

# %%

# %%


# %% [markdown]
#
# ## Mini-Workshop: Farben (Teil 1)
#
# - Definieren Sie eine Variable `grundfarben`, die eine Liste mit den Strings
#   `"Rot"`, `"Grün"` und `"Blau"` enthält.
# - Definieren Sie eine Variable `mischfarben`, die eine Liste mit den Strings
#   `"Cyan"`, `"Gelb"` und `"Magenta"` enthält.

# %%

# %%


# %% [markdown]
#
# Erzeugen Sie eine Liste `farben`, die die Elemente von `grundfarben` gefolgt von
# den Elementen von `mischfarben` enthält.

# %%


# %% [markdown]
#
# Erzeugen Sie eine Liste, die 15-mal die Zahl `1` enthält.

# %%


# %% [markdown]
#
# Erzeugen Sie die Liste `["r", "g", "b"]` aus dem String `"rgb"`.

# %%

