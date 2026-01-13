# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Importieren von Modulen</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# - `import` Anweisung
# - `from`-`import` Anweisung
# - Umbenennen mit `as`

# %% [markdown]
#
# ### Importieren mit `from`-`import`
#
# - Statt das gesamte Modul zu importieren, können wir auch einzelne Funktionen
#   importieren
# - Syntax: `from <modulname> import <funktionsname>`
# - Damit ist nur die importierte Funktion verfügbar
# - Ihr Name kann direkt verwendet werden, ohne den Modulnamen voranzustellen

# %%
# import my_test_module

# %%

# %%

# %%

# %%

# %% [markdown]
#
# - Wenn wir mehrere Funktionen aus einem Modul importieren, können wir sie
#   mit Kommas trennen

# %%

# %%

# %%

# %%

# %% [markdown]
#
# ### Umbenennen mit `as`
#
# - Manchmal ist der Name eines Moduls zu lang oder nicht aussagekräftig
# - Dann können wir das Modul mit `as` umbenennen

# %%

# %%

# %%

# %% [markdown]
#
# - Wir können auch Funktionen umbenennen

# %%


# %%

# %% [markdown]
#
# ### Importieren aller Namen mit `*`
#
# - Wir können alle Namen eines Moduls mit `*` importieren
# - Syntax: `from <modulname> import *`
# - Damit werden (fast) alle im Modul definierten Namen importiert
#   - Ausnahme: Namen, die mit `_` beginnen
# - Der Name des Moduls wird nicht importiert
# - Außer zum interaktiven Experimentieren sollten wir dies vermeiden

# %%


# %%


# %%

# %% [markdown]
#
# ## Workshop: Importieren von Modulen
#
# - Importieren Sie das Modul `workshop_module`, das Sie im vorherigen Workshop
#   erstellt haben unter dem Namen `wm`
# - Rufen Sie die Funktionen `say_hello()` und `say_bye()` auf

# %%

# %%

# %%

# %% [markdown]
#
# - Importieren Sie die Funktion `say_hello()` aus dem Modul `workshop_module`.
# - Importieren Sie die Funktion `say_bye()` aus dem Modul `workshop_module` unter
#   dem Namen `goodbye`.
# - Rufen Sie die Funktionen auf.
# - Was passiert, wenn Sie `say_bye()` aufrufen?

# %%

# %%

# %%

# %%

# %%
