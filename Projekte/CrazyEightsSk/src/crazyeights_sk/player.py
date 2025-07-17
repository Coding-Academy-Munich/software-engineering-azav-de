from enum import Enum, auto
import random
from .deck import SUITS, Card, Deck


class TurnAction(Enum):
    PLAYED_CARD = auto()
    DREW_CARD = auto()
    FAILED_DRAW = auto()


class Player:
    def __init__(self, name: str):
        self.name = name
        self.hand: list[Card] = []

    def __repr__(self) -> str:
        return f"Player({self.name!r})"

    def __str__(self) -> str:
        return f"{self.name} ({', '.join(str(c) for c in self.hand)})"

    def draw_n_cards(self, deck: "Deck", n: int) -> None:
        for _ in range(n):
            self.draw_card(deck)

    def draw_card(self, deck: "Deck") -> Card | None:
        card = deck.draw_card()
        if card:
            self.hand.append(card)
        return card

    def take_turn(self, game) -> TurnAction:
        self.notify_turn(game.top_discard)

        if self.try_to_play_card(game):
            return TurnAction.PLAYED_CARD

        drawn_card = self.draw_card(game.deck)
        if drawn_card:
            self.notify_card_drawn(drawn_card)
            return TurnAction.DREW_CARD
        else:
            self.notify_failed_draw()
            return TurnAction.FAILED_DRAW

    def try_to_play_card(self, game) -> bool:
        card_to_play = self.pick_card_to_play(game)
        if card_to_play:
            self.play_card(game, card_to_play)
            return True
        return False

    def pick_card_to_play(self, game) -> Card | None:
        playable_cards = self.get_playable_cards(game)
        if playable_cards:
            return playable_cards[0]
        return None

    def get_playable_cards(self, game) -> list[Card]:
        top_discard = game.top_discard
        return [card for card in self.hand if card.matches(top_discard)]

    def play_card(self, game, card: Card) -> None:
        self.hand.remove(card)
        game.discard(card)
        self.notify_card_played(card)
        if card.rank == "8":
            card.suit = self.pick_suit()
            self.notify_suit_picked(card.suit)

    def pick_suit(self) -> str:
        return random.choice(SUITS)

    def has_won(self) -> bool:
        return not self.hand

    def notify_turn(self, top_discard: Card) -> None:
        print(f"\n{self.name}'s turn. Top discard: {top_discard}")

    def notify_card_drawn(self, card: Card) -> None:
        print(f"{self.name} drew a card: {card}")

    def notify_failed_draw(self) -> None:
        print(f"{self.name} failed to draw a card.")

    def notify_card_played(self, card: Card) -> None:
        print(f"{self.name} played a card: {card}")

    def notify_suit_picked(self, suit: str) -> None:
        print(f"{self.name} picked a new suit: {suit}")