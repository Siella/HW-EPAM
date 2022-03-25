"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"

Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"

    [[-, -, o],
     [-, o, o],
     [x, x, x]]

     Return value should be "x wins!"

"""
from itertools import chain
from typing import List

import numpy as np


class TicTacBoard:
    def __init__(self, board: List[List]):
        self.board = np.array(board)
        self._flatten_board = list(chain(*board))
        self.outcome = self.get_winner()

    @property
    def rows(self) -> List[List]:
        """Returns board rows."""
        return [list(self.board[i, :]) for i in range(3)]

    @property
    def columns(self) -> List[List]:
        """Returns board columns."""
        return [list(self.board[:, i]) for i in range(3)]

    @property
    def diagonals(self) -> List[List]:
        """Returns board diagonal and inverse one."""
        return [list(np.diag(self.board))] + \
            [list(np.diag(self.board[:, ::-1]))]

    def get_winner(self):
        """
        Possible outcomes: x wins, o wins, a draw, unfinished.
        """
        positions = self.rows + self.columns + self.diagonals
        is_winner = {'x': False, 'o': False}
        if ['x'] * 3 in positions:
            is_winner['x'] = True
        if ['o'] * 3 in positions:
            is_winner['o'] = True
        if any(is_winner.values()):
            return [key for key, val in is_winner.items()
                    if val is True][0] + ' wins!'
        if '-' not in self._flatten_board:
            return 'draw!'
        return 'unfinished!'


def tic_tac_toe_checker(board: List[List]) -> str:
    """Checks whether there is a winner. Returns an outcome."""
    tic_tac_board = TicTacBoard(board)
    return tic_tac_board.outcome


if __name__ == '__main__':
    board = [['o', 'x', 'o'],
             ['o', 'x', 'o'],
             ['x', 'o', 'x']]
    print(tic_tac_toe_checker(board))
