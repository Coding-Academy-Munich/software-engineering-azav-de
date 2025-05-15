class Mark:
    EMPTY = " "
    X = "X"
    O = "O"


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


class Player:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    @staticmethod
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
