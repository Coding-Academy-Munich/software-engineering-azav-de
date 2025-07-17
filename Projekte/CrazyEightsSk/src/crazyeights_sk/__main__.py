from .player import Player
from .game import CrazyEightsGame


def main(player_names=None):
    if player_names is None:
        player_names = ["Jack", "Jill"]
    players = [Player(name) for name in player_names]
    game = CrazyEightsGame(players)
    print(game)

    for _ in range(7):  # Each player takes 7 turns
        for player in players:
            player.take_turn(game)

    print("Game over!")
    print(game)


if __name__ == "__main__":
    main()
