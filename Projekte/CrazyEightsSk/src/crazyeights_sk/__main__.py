from .player import Player
from .game import CrazyEightsGame


def main(player_names=None):
    if player_names is None:
        player_names = ["Jack", "Jill"]
    players = [Player(name) for name in player_names]
    game = CrazyEightsGame(players)

    game.play()
    print()
    print(game)


if __name__ == "__main__":
    main()
