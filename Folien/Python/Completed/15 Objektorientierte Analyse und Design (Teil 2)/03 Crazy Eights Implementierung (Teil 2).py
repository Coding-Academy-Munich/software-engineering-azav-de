# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Crazy Eights Implementierung (Teil 2)</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
# <img src="img/cards-18.png" width="100%">

# %% [markdown]
#
# ### Ausführen eines Zuges
#
# <div style="float:left;margin:auto;padding:80px 0;width:60%">
# <ul>
#   <li class="fragment">Wer ist der Informationsexperte?</li>
#   <li class="fragment"><code>Game</code>, <code>Player</code> oder <code>Deck</code>
#     (oder <code>DiscardPile</code>)
#   </li>
#   <li class="fragment">
#     Hier liefert uns der Informationsexperte keine gute Antwort
#   </li>
#   <li class="fragment">
#     Wir überlegen, welche Lösung die höchste Kohäsion und niedrigste Kopplung
#     hat
#   </li>
#   <li class="fragment">
#     $\rightarrow$ <code>Player</code>
#   </li>
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
# - `TurnAction` Enumeration
# - `Player` bekommt
#   - Methode `take_turn(game) -> TurnAction`
#   - Hilfsmethoden:
#     - ...
# - `Game` bekommt
#   - Property `top_discard`
#   - Method `discard()`
# - `Card` bekommt
#   - Methode `matches(top_discard)`
# - Freistehende Funktion:
#   - `short_string(cards)`

# %% [markdown]
#
# #### Hilfsmethoden von `Player`
#
# - `notify_turn(top_discard)`
# - `try_to_play_card(game)`
# - `draw_and_play_card(game)`
# - `notify_card_drawn(card)`
# - `pick_card_to_play(top_discard)`
# - `get_playable_cards(top_discard)`
# - `draw_card(game)`
# - `play_card(card, game)`
# - `notify_card_played(card)`
# - `pick_suit()`
# - `notify_suit_picked(suit)`
