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
durchlauf = 0
while durchlauf < 3:
    print(f"Durchlauf {durchlauf}")
    durchlauf += 1  # <==


# %%
import random

# %%
def führe_ein_experiment_aus(versuch_nr):
    """Führt ein Experiment aus
    Gibt True zurück wenn das Experiment erfolgreich war, andernfalls False.
    """
    print(f"Versuch Nr. {versuch_nr} gestartet...", end="")

    if random.random() > 0.8:
        print("Erfolg!")
        return True
    else:
        print("Fehlschlag.")
        return False


# %%
versuch_nr = 0

while not führe_ein_experiment_aus(versuch_nr):
    versuch_nr += 1

print("Wir haben einen erfolgreichen Versuch ausgeführt.")

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


# %%
def annoy_user():
    while True:
        text = input("Say hi! ")
        if text.lower() == "hi":
            break
        else:
            print("You chose", text)


# %%
# annoy_user()

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
# ### Zahlenraten
#
# Implementieren Sie eine Funktion `rate_zahl(lösung)`, die den Benutzer so
# lange nach einer Zahl fragt, bis er die Lösung erraten hat. Nach jeder
# Eingabe soll dem Benutzer angezeigt werden, ob die eingegebene Zahl zu
# groß, zu klein oder richtig ist.

# %%
def rate_zahl(lösung):
    geratene_zahl = input("Bitte geben Sie eine Zahl ein: ")
    while int(geratene_zahl) != lösung:
        if int(geratene_zahl) < lösung:
            print(f"{geratene_zahl} ist zu klein.")
        else:
            print(f"{geratene_zahl} ist zu groß.")
        geratene_zahl = input("Bitte versuchen Sie es noch einmal: ")
    print("Sie haben gewonnen!")


# %%
# rate_zahl(23)

# %% [markdown]
#
# Wie müssen Sie Ihre Lösung modifizieren, damit der Spieler durch Eingabe
# einer leeren Zeichenkette das Spiel abbrechen kann?

# %%
def rate_zahl_1(lösung):
    geratene_zahl = input("Bitte geben Sie eine Zahl ein: ")
    while geratene_zahl and int(geratene_zahl) != lösung:
        if int(geratene_zahl) < lösung:
            print(f"{geratene_zahl} ist zu klein.")
        else:
            print(f"{geratene_zahl} ist zu groß.")
        geratene_zahl = input("Bitte versuchen Sie es noch einmal: ")
    if geratene_zahl:
        print("Sie haben gewonnen!")
    else:
        print("Aufgeben ist feige!")


# %%
# rate_zahl_1(23)

# %% [markdown]
# Lösung unter Zuhilfenahme der Funktion `klassifiziere_zahl`

# %%
def classify_number(guess, solution):
    if guess < solution:
        return False, "Your guess is too small! "
    elif guess > solution:
        return False, "Your guess is too large! "
    else:
        return True, "You won!"


# %%
def guess_number_2(solution):
    guess = input("Please enter a guess: ")
    is_success, hint = classify_number(int(guess), solution)
    while not is_success:
        guess = input(hint)
        is_success, hint = classify_number(int(guess), solution)
    print("You won!")

# %%
# rate_zahl_2(23)
