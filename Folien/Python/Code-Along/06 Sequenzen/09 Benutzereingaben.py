# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Benutzereingaben</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# # Benutzereingaben
#
# - Die Funktion `input()` erlaubt es dem Benutzer einen Text einzugeben.
# - Optional kann sie einen Eingabeprompt ausgeben.
# - Die Funktion gibt den vom Benutzer eingegebenen Text *als String* zurück.

# %%


# %%

# %%

# %% [markdown]
#
# ## Beispiel: Konvertierung von Temperaturen
#
# Wir wollen eine Anwendung schreiben, die den Benutzer nach einer Temperatur
# in Fahrenheit fragt und die entsprechende Temperatur in Grad Celsius
# zurückgibt.

# %%

# %%

# %%

# %% [markdown]
#
# Wir müssen den Rückgabewert von `input()` manuell in eine
# Zahl konvertieren, wenn wir damit rechnen wollen.

# %%

# %%


# %%


# %% [markdown]
#
#  Wir können eine Meldung ausgeben, wenn der Benutzer nichts eingibt (und die
#  Ausgabe etwas schöner gestalten):


# %%

# %%

# %% [markdown]
#
# Wir können in der `if`-Anweisung Truthiness ausnutzen:

# %%
def konvertiere_temperatur_3():
    fahrenheit = input("Bitte geben Sie die Temperatur in Fahrenheit ein: ")
    if fahrenheit != "":
        celsius = konvertiere_fahrenheit_nach_celsius(float(fahrenheit))
        print(f"{float(fahrenheit):.1f}F sind {celsius:.1f}°C")
    else:
        print("Bitte geben Sie eine gültige Temperatur ein.")

# %%


# %% [markdown]
#
# ## Mini-Workshop: Umrechnung in Meilen
#
# Schreiben Sie eine Funktion `konvertiere_km_nach_meilen(km)` die den Wert
# `km` von Kilometer in Meilen umrechnet (d.h. die den Wert in Meilen
# zurückgibt).
#
# *Hinweis:*
# - Ein Kilometer entspricht $0,621371$ Meilen

# %%

# %% [markdown]
# Testen Sie `konvertiere_km_nach_meilen(km)` für 1 und 5 km.

# %%

# %%

# %% [markdown]
#
# Schreiben Sie eine Funktion `meilen_app()`, die eine Länge in Kilometern einliest
# und die äquivalente Entfernung in Meilen ausgibt. Wenn die Eingabe ein leerer
# String ist, soll der String `Bitte geben Sie eine gültige Entfernung in km ein.`
# ausgegeben werden.
#
# *Hinweise*
# - Ein String kann mit `float()` in einen Float-Wert umgewandelt werden.
# - Verwenden Sie Truthiness in der Bedingung der `if`-Anweisung.

# %%


# %%


# %% [markdown]
#
# ## Mini-Workshop: Kino-Preis
#
# Das Python-Lichtspielhaus hat folgende Eintrittspreise:
#
# - Kleinkinder unter 2 Jahren sind frei.
# - Kinder von 2 bis 12 Jahren zahlen 2 Euro.
# - Teenager von 13 bis 17 Jahren zahlen 5 Euro.
# - Erwachsene zahlen 10 Euro.
# - Rentner (ab 65) zahlen 6 Euro.
#
# Schreiben Sie eine Funktion `kinopreis(alter)`, die den Preis in Abhängigkeit vom
# Alter berechnet und zurückgibt.


# %%


# %% [markdown]
# Testen Sie die Funktion `kinopreis()` für einige repräsentative Werte.

# %%

# %% [markdown]
#
# Schreiben Sie eine Funktion `drucke_kinopreis(alter)`,
# die einen Text der folgenden Art auf dem Bildschirm ausgibt:
#
# ```
# Sie sind 1 Jahr alt. Ihr Preis beträgt 0 Euro.
# Sie sind 15 Jahre alt. Ihr Preis beträgt 5 Euro.
# ```

# %%

# %% [markdown]
# Testen Sie `drucke_kinopreis()` für repräsentative Werte.

# %%

# %% [markdown]
#
# Schreiben Sie eine Funktion `kino_app()`, die ein Alter einliest und den
# Kinopreis für eine Person dieses Alters im gerade beschriebenen Format
# ausgibt. Zwei Beispielinteraktionen:
#
# ```
# Wie alt sind Sie? 37
# Sie sind 37 Jahre alt. Ihr Preis beträgt 10 Euro.
#
# Wie alt sind Sie? 12
# Sie sind 12 Jahre alt. Ihr Preis beträgt 2 Euro.
# ```

# %%

# %%

# %%

