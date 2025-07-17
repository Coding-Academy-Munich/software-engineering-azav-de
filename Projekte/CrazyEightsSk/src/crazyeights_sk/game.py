from .deck import Deck
from .player import Player


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