from enum import StrEnum
from .deck import Deck
from .player import Player, TurnAction

class GameResult(StrEnum):
    CURRENT_PLAYER_WON = "Current player won."
    NO_PLAYABLE_CARDS = "No playable cards left."
    NOT_ENOUGH_PLAYERS = "Not enough players to start the game."

class CrazyEightsGame:
    def __init__(self, players):
        self.deck: Deck = Deck()
        self.players: list[Player] = players
        self.discard_pile = [self.deck.draw_card()]
        self.current_player_index: int = 0

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

    def discard(self, card):
        self.discard_pile.append(card)

    @property
    def top_discard(self):
        return self.discard_pile[-1]

    @property
    def current_player(self) -> Player:
        return self.players[self.current_player_index]

    def pick_next_player(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def play(self):
        result = self.play_all_rounds()
        self.print_result(result)

    def play_all_rounds(self) -> GameResult:
        if len(self.players) < 2:
            return GameResult.NOT_ENOUGH_PLAYERS

        while True:
            action_taken = self.current_player.take_turn(self)
            if action_taken == TurnAction.PLAYED_CARD:
                if self.current_player.has_won():
                    return GameResult.CURRENT_PLAYER_WON
            elif action_taken == TurnAction.FAILED_DRAW:
                return GameResult.NO_PLAYABLE_CARDS

            self.pick_next_player()

    def print_result(self, result: GameResult):
        if result == GameResult.CURRENT_PLAYER_WON:
            print(f"{self.current_player.name} has won the game!")
        elif result == GameResult.NO_PLAYABLE_CARDS:
            print("No playable cards left. The game ends.")
        elif result == GameResult.NOT_ENOUGH_PLAYERS:
            print("Not enough players to start the game.")
        else:
            print("Game ended with an unknown result.")
