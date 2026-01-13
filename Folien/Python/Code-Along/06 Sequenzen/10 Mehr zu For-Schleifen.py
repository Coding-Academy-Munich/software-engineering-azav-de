# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Mehr zu For-Schleifen</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# ## Zuweisung an mehrere Variablen
#
# Wir haben schon gesehen, dass man an mehrere Variablen gleichzeitig zuweisen kann:

# %%

# %% [markdown]
#
# Das ist auch in `for`-Schleifen möglich:

# %%
values = [(1, "one"), (2, "two"), (3, "three")]

# %%

# %%

# %% [markdown]
#
# ## Mini-Workshop: Anzahl und Gesamtpreis
#
# In der folgenden Liste haben wir Name, Stückzahl und Preis pro Stück für eine Liste
# von Einkäufen gespeichert. Schreiben Sie eine Funktion
# `anzahl_und_gesamtpreis(artikel: list[tuple[int, float]]) -> tuple[int, float]`,
# die die Gesamtzahl der gekauften Artikel und den Gesamtpreis berechnet:
#
# ```python
# >>> anzahl_und_gesamtpreis([(3, 2.0), (5, 1.0)])
# (8, 11.0)
# ```

# %%

# %%
artikel = [(3, 2.0), (5, 1.0)]

# %%
