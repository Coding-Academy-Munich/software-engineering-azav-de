# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>GRASP: Informationsexperte</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
# <img src="img/cards-19.png" width="100%">

# %% [markdown]
#
# ## Wie läuft ein Spiel ab?
#
# - Spieler bekommen Karten
# - Einer der Spieler beginnt
# - Spieler legt eine Karte ab
# - Wenn er das nicht kann
#     - Zieht er eine Karte
#     - Legt diese wieder ab, falls möglich
# - Wenn er keine Karten mehr hat, hat er gewonnen
# - Ansonsten ist der nächste Spieler dran

# %% [markdown]
#
# ## Wer ist für das Verteilen der Karten zuständig?
#
# - Die Spieler?
#   - So funktioniert es in der wirklichen Welt
#   - Wie müsste dazu unser Domänenmodell aussehen?

# %% [markdown]
#
# <div style="float:left;margin:auto;padding:80px 0;width:55%">
# <ul>
# <li>Spieler kennen sich nicht gegenseitig</li>
# <li>Wir könnten eine Beziehung zwischen Spielern einführen</li>
# <li>Aber: wer verwaltet die?</li>
# </ul>
# </div>
# <img src="img/crazy-eights-dm.svg"
#      style="float:right;margin:auto;width:45%"/>

# %% [markdown]
#
# <div style="float:left;margin:auto;padding:80px 0;width:35%">
# <ul>
# <li><code>Game</code></li>
# <li><strike><code>Player</code></strike></li>
# <li><code>Deck</code></li>
# <li>Eine andere Klasse?</li>
# </ul>
# </div>
# <img src="img/crazy-eights-dm.svg"
#      style="float:right;margin:auto;width:60%"/>

# %% [markdown]
#
# ## Informationsexperte (Information Expert, GRASP)
#
# ### Frage
#
# An welche Klasse sollen wir eine Verantwortung delegieren?
#
# ### Antwort
#
# An die Klasse, die die **meisten Informationen** hat, um die Verantwortung zu
# erfüllen.
#
# Diese Klasse heißt **Informationsexperte** oder einfach **Experte**.

# %% [markdown]
#
# <div style="float:left;margin:auto;padding:80px 0;width:50%">
# <h2>Wer ist der Informationsexperte?</h2>
# <ul>
# <li><code>Game</code> kennt alle Spieler</li>
# <li><code>Game</code> kennt das <code>Deck</code></li>
# <li>Keine andere Klasse kennt alle Spieler und das Kartenspiel</li>
# </ul>
# <p>$\Rightarrow$ <code>Game</code> ist der Informationsexperte</p>
# </div>
# <div style="float:right;margin:auto;padding:80px 0;width:45%">
# <img src="img/crazy-eights-dm.svg"
#      style="float:right;margin:auto;width:100%"/>
# </div>

# %% [markdown]
#
# - Wie kann `Game` die Karten verteilen?
# - `Game` kann die benötigte Funktionalität selber implementieren
# - `Game` kann die Aufgabe an eine andere Klasse delegieren

# %% [markdown]
#
# ### Implementierung der ersten Variante
#
# `Game` implementiert die Funktionalität selber
#
# - Iteriere über alle Spieler
# - Ziehe 7 Karten aus dem Kartenspiel
# - Füge die Karten zur Hand des Spielers hinzu
# - Behandle den Fall, dass das Kartenspiel leer wird (optional)

# %% [markdown]
#
# <ul>
#   <li>Was ist zur Implementierung notwendig?
#     <ul>
#       <li class="fragment">Zugriff auf alle Spieler</li>
#       <li class="fragment">Zugriff auf das Kartenspiel</li>
#       <li class="fragment"><em>Ziehen einer Karte aus dem Kartenspiel</em></li>
#       <li class="fragment"><em>Hinzufügen einer Karte zur Hand eines
#         Spielers</em></li>
#     </ul>
#   </li>
#   <li class="fragment">Das sind zwei neue Verantwortungen</li>
# </ul>

# %% [markdown]
#
# ### Wer sind die Informationsexperten?
#
# <div style="float:left;margin:auto;padding:80px 0;width:60%">
# <ul>
# <li class="fragment">Ziehen einer Karte aus dem Kartenspiel</li>
#   <ul><li class="fragment"><code>Deck</code> kennt alle Karten</li></ul>
# <li class="fragment">Hinzufügen einer Karte zur Hand eines Spielers</li>
#   <ul><li class="fragment"><code>Player</code> kennt seine Hand</li></ul>
# <li class="fragment">Andere Klassen kennen diese Informationen nicht</li>
# <li class="fragment">$\Rightarrow$ <code>Deck</code> und <code>Player</code> sind die
#   Informationsexperten</li>
# </ul>
# </div>
# <div style="float:right;margin:auto;padding:80px 0;width:40%">
# <img src="img/crazy-eights-dm.svg"
#      style="float:right;margin:auto;width:100%"/>
# </div>

# %%
class CrazyEightsGame:  # noqa
    """Implementation of the Crazy 8 game that implements drawing the cards itself."""

    def __init__(self, players):
        self.deck = Deck()
        self.players = players
        self.deal_cards()

    def __repr__(self):
        return f"CrazyEightsGame({self.players!r})"

    def __str__(self):
        result = f"Crazy Eights with {len(self.players)} players:\n"
        for player in self.players:
            result += f"  {player}\n"
        return result

    def deal_cards(self):
        for player in self.players:
            for _ in range(7):
                card = self.deck.draw_card()
                if card:
                    player.take_card(card)
                else:
                    raise ValueError("Not enough cards in deck")


# %%
class Player:  # noqa
    def __init__(self, name: str):
        self.name = name
        self.hand = []

    def __repr__(self) -> str:
        return f"Player({self.name!r})"

    def __str__(self) -> str:
        return f"{self.name} ({', '.join(str(c) for c in self.hand)})"

    def take_card(self, card: "Card") -> None:
        self.hand.append(card)


# %%
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self) -> str:
        return f"Card({self.suit!r}, {self.rank!r})"

    def __str__(self) -> str:
        return f"{self.rank}{self.suit}"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Card):
            return NotImplemented
        return self.suit == other.suit and self.rank == other.rank


# %%
SUITS = ["♥", "♦", "♣", "♠"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

# %%
import random


# %%
class Deck:  # noqa
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in SUITS for rank in RANKS]
        random.shuffle(self.cards)

    def __repr__(self) -> str:
        return f"<Deck with {len(self.cards)} cards>"

    def __str__(self) -> str:
        return f"Deck with {len(self.cards)} cards" if self.cards else "Empty deck"

    def __len__(self) -> int:
        return len(self.cards)

    def __getitem__(self, index) -> Card:
        return self.cards[index]

    def draw_card(self) -> Card | None:
        return self.cards.pop() if self.cards else None


# %%
game = CrazyEightsGame([Player("Jack"), Player("Jill")])

# %%
print(game)


# %% [markdown]
#
# ### Implementierung der zweiten Variante
#
# `Game` delegiert die Aufgabe an eine andere Klasse
#
# - Iteriere über alle Spieler
# - Informiere den Spieler, dass er eine Karte ziehen soll
#   - Dazu braucht der Spieler Zugriff auf das Kartenspiel
#   - Wir übergeben eine Referenz auf das Kartenspiel an den Spieler


# %%
class CrazyEightsGame:  # noqa
    """Implementation of the Crazy 8 game that delegates drawing cards to the player."""

    def __init__(self, players):
        self.deck = Deck()
        self.players = players
        self.deal_cards()

    def __repr__(self):
        return f"CrazyEightsGame({self.players!r})"

    def __str__(self):
        result = f"Crazy Eights with {len(self.players)} players:\n"
        for player in self.players:
            result += f"  {player}\n"
        return result

    def deal_cards(self):
        for player in self.players:
            player.draw_n_cards(self.deck, 7)


# %%
from typing import Optional


# %%
class Player:  # noqa
    def __init__(self, name: str):
        self.name = name
        self.hand = []

    def __repr__(self) -> str:
        return f"Player({self.name!r})"

    def __str__(self) -> str:
        return f"{self.name} ({', '.join(str(c) for c in self.hand)})"

    def draw_n_cards(self, deck: "Deck", n: int) -> None:
        for _ in range(n):
            self.draw_card(deck)

    def draw_card(self, deck: "Deck") -> Optional["Card"]:
        card = deck.draw_card()
        if card:
            self.hand.append(card)
        return card


# %%
game = CrazyEightsGame([Player("Jack"), Player("Jill")])

# %%
print(game)

# %% [markdown]
#
# <h3>Vergleich der Varianten</h3>
# <h4>1. Variante</h4>
# <ul>
#   <li class="fragment">
#     <code>Player</code> ist von <code>Deck</code> unabhängig (geringere Kopplung)
#   </li>
#   <li class="fragment"><code>Game</code> hat mehr Verantwortungen</li>
#   <li class="fragment">
#     <code>Game</code> hat Verantwortungen mit unterschiedlichen Abstraktionsgraden:
#     <ul>
#       <li class="fragment">Orchestrierung des Spiels</li>
#       <li class="fragment">
#         Implementierung des Mechanismus zum Verteilen der Karten
#       </li>
#     </ul>
#   </li>
# </ul>


# %% [markdown]
#
# <h4>2. Variante</h4>
# <ul>
#   <li class="fragment"><code>Game</code> hat weniger Verantwortungen
#     <ul>
#       <li class="fragment">
#         Alle Verantwortungen haben den ähnlichen Abstraktionsgrad
#       </li>
#     </ul>
#   </li>
#   <li class="fragment"><code>Player</code> hat mehr Verantwortungen
#     <ul>
#       <li class="fragment">Höhere Kopplung</li>
#       <li class="fragment">
#         Mehr Flexibilität in der Implementierung der Verantwortungen
#       </li>
#     </ul>
#   </li>
# </ul>


# %% [markdown]
#
# - Sie können sich jetzt den Workshops versuchen
# - Falls Sie das Gefühl haben, dass Sie noch zu wenig Übung haben, können Sie
#   sich das nächste Video ansehen, in dem wir die restlichen Verantwortungen
#   des Crazy-Eights-Spiels implementieren werden

# %% [markdown]
#
# ## Workshop: Informationsexperte für Drei Gewinnt
#
# - Welche Verantwortungen gibt es im Drei-Gewinnt-Spiel?
# - Welche Klasse ist jeweils der Informationsexperte?
# - Implementieren Sie die Verantwortungen basierend auf Ihrer Analyse

# %% [markdown]
#
# ### Verantwortungen im Drei-Gewinnt-Spiel
#
# | Verantwortung                           | Informationsexperte |
# | --------------------------------------- | ------------------- |
# | Ausführen der Hauptschleife             | `Game`              |
# | Darstellen des Spielfelds               | `Board`             |
# | Bestimmen des nächsten Spielers         | `Game`              |
# | Bestimmen des zu markierenden Feldes    | `Player`            |
# | Markieren eines Feldes                  | `Board`             |
# | Überprüfen, ob ein Spieler gewonnen hat | `Game`              |

# %%
class Mark:
    EMPTY = " "
    X = "X"
    O = "O"


# %%
class Field:
    def __init__(self):
        self.mark = Mark.EMPTY

    def set_mark(self, mark):
        if self.mark == Mark.EMPTY:
            self.mark = mark
            return True
        return False

    def __str__(self):
        return self.mark


# %%
class Board:
    def __init__(self):
        self.fields = [[Field() for _ in range(3)] for _ in range(3)]

    def display(self):
        for row in self.fields:
            print("|".join(str(field) for field in row))
            print("-+-+-")

    def is_full(self):
        return all(field.mark != Mark.EMPTY for row in self.fields for field in row)

    def set_mark(self, row, col, mark):
        return self.fields[row][col].set_mark(mark)


# %%
class Player:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    def get_move(self):
        col, row = None, None
        while row is None:
            try:
                col, row = map(
                    int,
                    input(
                        f"{self.name}'s turn. Enter row and column "
                        "(0-2, separated by space): "
                    ).split(),
                )
            except ValueError:
                print("Invalid input, try again.")
                continue
            if not (0 <= row < 3 and 0 <= col < 3):
                print("Invalid input, try again.")
                row = None
        return col, row


# %%
class TicTacToeGame:
    def __init__(self, player1, player2):
        self.board = Board()
        self.players = [player1, player2]
        self.current_player_index = 0

    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index

    def current_player(self):
        return self.players[self.current_player_index]

    def play(self):
        while not self.board.is_full():
            self.board.display()
            player = self.current_player()
            col, row = player.get_move()
            if self.board.set_mark(row, col, player.mark):
                if self.check_winner(row, col, player.mark):
                    self.board.display()
                    print(f"Congratulations! {player.name} wins!")
                    return
                self.switch_player()
            else:
                print("Field is already occupied, try again.")
        print("It's a draw!")

    def check_winner(self, row, col, mark):
        # Check row, column, and diagonals for a win
        win_row = all(self.board.fields[row][c].mark == mark for c in range(3))
        win_col = all(self.board.fields[r][col].mark == mark for r in range(3))
        win_diag1 = all(self.board.fields[i][i].mark == mark for i in range(3))
        win_diag2 = all(self.board.fields[i][2 - i].mark == mark for i in range(3))
        return win_row or win_col or win_diag1 or win_diag2


# %%
ttt_player1 = Player("Jack", Mark.X)

# %%
ttt_player2 = Player("Jill", Mark.O)

# %%
ttt_game = TicTacToeGame(ttt_player1, ttt_player2)

# %%
# ttt_game.play()


# %% [markdown]
#
# ## Optionaler Workshop: Informationsexperte für Crazy Eights
#
# - Welche weiteren Verantwortungen gibt es im Crazy-Eights-Spiel?
# - Welche Klasse ist jeweils der Informationsexperte?
#
# (Wir werden diese Fragen in den nächsten Videos ausführlich besprechen.)
