# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>`while`-Schleifen</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# Benötigt user input!

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
zahl = 0

# %%
while zahl < 3:
    print(f"Versuch {zahl}")
    zahl += 1  #

# %%
import time

# %%
def starte_rakete(countdown):
    print("Willkommen zum Raketenstart-Simulator!")

    while countdown > 0:
        print(f"Rakete startet in {countdown} Sekunden...")
        time.sleep(1)
        countdown -= 1

    print("Start! 🚀")


# %%
starte_rakete(10)


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
versuch_nr = 1
while not führe_ein_experiment_aus(versuch_nr):
    versuch_nr += 1


# %% [markdown]
#
#  ## Beenden von Schleifen
#
# Manchmal ist es leichter, die Abbruchbedingung einer Schleife im Rumpf zu
# bestimmen, statt am Anfang. Mit der Anweisung `break` kann man eine
# Schleife vorzeitig beenden:

# %%
i = 1
while i < 10:
    print(i)
    if i % 3 == 0:
        break
    i += 1
print("Nach der Schleife:", i)


# %% [markdown]
#
# Hier ist ein realistischeres Beispiel:

# %%
def nerve_benutzer():
    while True:
        text = input("Gib hi ein! ")
        if text.lower() == "hi":
            break
        else:
            print("Du hast", text, "eingegeben.")


# %%
# nerve_benutzer()

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
def rate_wort(lösung):
    geratenes_wort = input("Bitte geben Sie ein Wort ein: ")
    while geratenes_wort != lösung:
        geratenes_wort = input("Bitte versuchen Sie es nochmal: ")
    print("Genau!")


# %%
# rate_wort("Haus")

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
def rate_zahl():
    """Lässt den Benutzer eine Zufallszahl zwischen 1 und 100 raten."""
    zufallszahl = random.randint(1, 100)
    print("Ich habe mir eine Zahl zwischen 1 und 100 ausgedacht.")

    while True:
        geraten = int(input("Bitte geben Sie eine Zahl ein: "))
        if geraten < zufallszahl:
            print("Zu klein!")
        elif geraten > zufallszahl:
            print("Zu groß!")
        else:
            print("Genau richtig!")
            break

# %%
# rate_zahl()

# %% [markdown]
#
# - Fügen Sie Ihrer Funktion eine Begrenzung der Rate-Versuche hinzu. Wenn der
#   Benutzer die Zahl in weniger als 6 Versuchen errät, soll die Meldung `Gut
#   geraten!` ausgegeben werden, ansonsten `Schlecht geraten!`.

# %%
import random

# %%
def rate_zahl():
    tries = 6
    solution = random.randint(1, 100)

    print("Willkommen zu dem Zahlenratespiel!")
    print("Ich habe mir eine Zahl zwischen 1 und 100 ausgedacht. Du hast 6 Versuche, um sie zu erraten.")

    while tries > 0:
        guess = int(input("Bitte Zahl eingeben: "))

        if guess < solution:
            print("Zu niedrig!")
        elif guess > solution:
            print("Zu hoch!")
        else:
            print("Gut geraten!")
            break

        tries -= 1

    if tries == 0 and guess != solution:
        print("Schlecht geraten! Die Zahl war.", solution)

# %%
# guess_number()

# %% [markdown]
#
# - Erweitern Sie die Funktion, so dass der Benutzer entscheiden kann, ob er
#   erneut spielen möchte.

# %%
import random


# %%
def rate_zahl():
    while True:
        tries = 6
        solution = random.randint(1, 100)

        print("Willkommen zu dem Zahlenratespiel!")
        print("Ich habe mir eine Zahl zwischen 1 und 100 ausgedacht. Du hast 6 Versuche, um sie zu erraten.")

        while tries > 0:
            guess = int(input("Bitte Zahl eingeben: "))

            if guess < solution:
                print("Zu niedrig!")
            elif guess > solution:
                print("Zu hoch!")
            else:
                print("Gut geraten!")
                break

            tries -= 1

        if tries == 0 and guess != solution:
            print("Schlecht geraten! Die Zahl war.", solution)

        play_again = input("Möchten Sie noch einmal spielen? (j/n): ")
        if play_again.lower() != "j":
            print("Auf Wiedersehen!")
            break

# %%
# rate_zahl()
