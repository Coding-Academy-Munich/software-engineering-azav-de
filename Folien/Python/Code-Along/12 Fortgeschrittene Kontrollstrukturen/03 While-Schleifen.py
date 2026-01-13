# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>While-Schleifen</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
#  # While-Schleifen
#
#  Manchmal wollen wir einen Teil eines Programms immer wieder ausführen:
#
#  - Zahlenraten bis die richtige Zahl gefunden wurde
#  - Physik-Simulation bis das Ergebnis genau genug ist
#  - Verarbeitung von Benutzereingaben in interaktiven Programmen
#
#  Wenn wir die Anzahl der Wiederholungen nicht von vornherein wissen,
#  verwenden wir dafür in der Regel eine While-Schleife.

# %%

# %%

# %%

# %%

# %%


# %% [markdown]
#
# - Die bisherigen Beispiele hätten wir auch mit einer `for`-Schleife
#   implementieren können.
# - Das wäre die elegantere Lösung gewesen.
# - Wenn wir aber nicht wissen, wie oft wir die Schleife durchlaufen wollen, ist
#   eine `while`-Schleife die bessere Wahl.

# %%
from random import random

# %%
def führe_ein_experiment_aus(versuch_nr):
    """Führt ein Experiment aus
    Gibt True zurück wenn das Experiment erfolgreich war, andernfalls False.
    """
    print(f"Versuch Nr. {versuch_nr} gestartet...", end="")

    if random() > 0.8:
        print("Erfolg!")
        return True
    else:
        print("Fehlschlag.")
        return False

# %%


# %% [markdown]
#
#  ## Beenden von Schleifen
#
# Manchmal ist es leichter, die Abbruchbedingung einer Schleife im Rumpf zu
# bestimmen, statt am Anfang. Mit der Anweisung `break` kann man eine
# Schleife vorzeitig beenden:

# %%

# %% [markdown]
#
# Hier ist ein realistischeres Beispiel:

# %%

# %%

# %% [markdown]
# ## Ratespiele
#
# Die folgenden einfachen "Spiele" erlauben dem Spieler unbegrenzt viele
# Eingaben. Daher ist es sinnvoll, sie mit einer While-Schleife zu
# implementieren.
#
# ### Raten eines Wortes
#
# Implementieren Sie eine Funktion `rate_wort(lösung)`, die den Benutzer so
# lange nach einem Wort fragt, bis das eingegebene Wort der Lösung entspricht.

# %%

# %%

# %% [markdown]
#
# ## Zahlenraten
#
# - Schreiben Sie eine Funktion `rate_zahl()`, die eine Zufallszahl zwischen 1
#   und 100 erzeugt und den Benutzer solange raten lässt, bis er die Zahl
#   erraten hat.
# - Nach jedem Versuch soll dem Benutzer angezeigt werden, ob die geratene Zahl
#   zu groß oder zu klein war.
# - Hinweis: Verwenden Sie die Funktion `random.randint(min, max)` aus dem Modul
#   `random`.

# %%
import random

# %%

# %%

# %% [markdown]
#
# - Fügen Sie Ihrer Funktion eine Begrenzung der Rate-Versuche hinzu. Wenn der
#   Benutzer die Zahl in weniger als 6 Versuchen errät, soll die Meldung `Gut
#   geraten!` ausgegeben werden, ansonsten `Schlecht geraten!`.

# %%

# %%

# %%

# %% [markdown]
#
# - Erweitern Sie die Funktion, so dass der Benutzer entscheiden kann, ob er
#   erneut spielen möchte.

# %%

# %%

# %%
