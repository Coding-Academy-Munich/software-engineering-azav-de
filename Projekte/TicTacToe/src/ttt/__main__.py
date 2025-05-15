import click

from ttt.tictactoegame import TicTacToeGame, Mark, Player


@click.command()
def main():
    player1 = Player("Player 1", Mark.X)
    player2 = Player("Player 2", Mark.O)
    game = TicTacToeGame(player1, player2)
    game.play()


if __name__ == "__main__":
    main()
