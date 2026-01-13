# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Crazy Eights Starter Kit</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# - Drei Projekte für Crazy Eights:
#   - `CrazyEightsSk`: Starter Kit
#   - `CrazyEightsSimple`: Einfache Implementierung
#   - `CrazyEights`: Vollständige Implementierung

# %% [markdown]
#
# ## Aufbau der Projekte
#
# - `src`: Quellcode
#   - `src/crazyeights{_sk,_simple}`: Package für die Implementierung
# - `tests`: Tests
# - `pyproject.toml`: Festlegen/Konfigurieren des Build-Systems (setuptools)
# - `pytest.ini`: Konfiguration für `pytest`
# - `tox.ini`: Automatisierung der Tests für verschiedene Python-Versionen
# - `.bumpversion.cfg`: Inkrementieren der Versionsnummer mit `bumpversion`
# - `.gitignore`: Dateien, die nicht in Git aufgenommen werden sollen

# %% [markdown]
#
# ### Installieren für die Entwicklung
#
# ```bash
# > cd CrazyEightsSimple
# > python -m venv .venv
# > source .venv/bin/activate  # Linux/Mac
# > .venv\Scripts\activate  # Windows PowerShell
# > python -m pip install pip --upgrade
# > pip install -e . --group dev
# ```

# %% [markdown]
#
# ### Verwenden des installierten Pakets (1)
#
# Das Wheel enthält ein ausführbares Skript, das das Package verwendet:
#
# ```bash
# > crazy-eights-simple
# Computer 1's turn. Top of discard pile: 5♦
# Computer 1's hand: J♥, 3♣, A♣, 6♦, 7♣, 2♠, A♦
# Playable cards: 6♦, A♦
# Computer 1 plays A♦
# ...
# ```
#
# ```bash
# > crazy-eights-simple --help
# Usage: crazy-eights-simple [OPTIONS]
# ...
# ```

# %% [markdown]
#
# ### Verwenden des installierten Pakets (2)
#
# ```python
# >>> from crazyeights_simple import Card, Deck, Player
# >>> deck = Deck()
# >>> player = Player("Alice")
# >>> player.draw_n_cards(deck, 7)
# >>> player
# Player('Alice')
# >>> player.hand[0]
# Card('♥', '5')
# ```


# %% [markdown]
#
# ### Ausführen der Tests mit Pytest
#
# ```bash
# > cd CrazyEightsSimple
# > python -m pytest
# ```
#
# oder
#
# ```bash
# > cd CrazyEightsSimple
# > pytest
# ```

# %% [markdown]
#
# ### Ausführen der Tests mit Tox
#
# ```bash
# > cd CrazyEightsSimple
# > python -m tox
# ```
#
# oder
#
# ```bash
# > cd CrazyEightsSimple
# > tox
# ```

# %% [markdown]
#
# ### Inkrementieren der Versionsnummer
#
# ```bash
# > cd CrazyEightsSimple
# > crazyeights-simple --version
# crazyeights-simple, version 0.0.1
# > python -m bumpversion patch
# > crazyeights-simple --version
# crazyeights-simple, version 0.0.2
# ```

# %% [markdown]
#
# ### Erstellen eines installierbaren Wheels
#
# ```bash
# > cd CrazyEightsSimple
# > python -m build
# ```
#
# Das Wheel wird in `dist` abgelegt:
#
# ```bash
# > ls dist
# crazyeights_simple-0.0.1-py3-none-any.whl
# ```

# %% [markdown]
#
# ### Installation des Wheels
#
# ```bash
# > cd CrazyEightsSimple
# > python -m pip install dist/crazyeights_simple-0.0.1-py3-none-any.whl
# ```
#
# Das Package ist jetzt installiert:
#
# ```bash
# > python -m pip list | grep crazy  # Linux/Mac
# crazyeights-simple 0.0.1
# ```
#
# ```powershell
# > python -m pip list | Select-String crazy  # Windows PowerShell
# crazyeights-simple 0.0.1
# ```
