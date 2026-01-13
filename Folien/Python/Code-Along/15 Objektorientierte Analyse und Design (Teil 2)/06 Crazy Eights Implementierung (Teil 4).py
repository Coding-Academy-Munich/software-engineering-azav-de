# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Crazy Eights Implementierung (Teil 4)</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
# <img src="img/cards-18.png" width="100%">

# %% [markdown]
#
# ### Ausführen eines Spiels
#
# <div style="float:left;margin:auto;padding:80px 0;width:60%">
# <ul>
#   <li class="fragment">Wer ist der Informationsexperte?</li>
#   <li class="fragment"><code>Game</code></li>
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
#   - Methode `play()`
#   - Hilfsmethoden:
#     - `play_all_rounds()`
#     - `print_result()`
