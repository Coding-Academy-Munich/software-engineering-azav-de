# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Crazy Eights Implementierung (Teil 1)</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
# <img src="img/cards-18.png" width="100%">

# %% [markdown]
#
# ## Wie läuft ein Spiel ab?
#
# - Spieler bekommen Karten ✔
# - Einer der Spieler beginnt
# - Spieler führt seinen Zug aus
#   - Spieler legt eine Karte ab
#   - Wenn er das nicht kann
#       - Zieht er eine Karte
#       - Legt diese wieder ab, falls möglich
# - Wenn er keine Karten mehr hat, hat er gewonnen
# - Ansonsten ist der nächste Spieler dran

# %% [markdown]
#
# ### Auswahl des Startspielers
#
# <div style="float:left;margin:auto;padding:80px 0;width:60%">
# <ul>
#   <li class="fragment">Wer ist der Informationsexperte?</li>
#   <li class="fragment">Die <code>Game</code> Klasse</li>
#   <li class="fragment">
#     Wer ist verantwortlich für das Speichern des aktuellen Spielers?
#   </li>
#   <li class="fragment">Die <code>Game</code> Klasse</li>
# </ul>
# </div>
# <div style="float:right;margin:auto;padding:80px 0;width:40%">
# <img src="img/crazy-eights-dm.png"
#      style="float:right;margin:auto;width:100%"/>
# </div>

# %% [markdown]
#
# ### Implementierung
#
# - `Game` bekommt
#   - Attribut `current_player_index`
#   - Property `current_player`
#   - Methode `pick_next_player()`
