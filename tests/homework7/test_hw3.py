from homework7.hw3 import tic_tac_toe_checker


def test_x_wins():
    board = [['x', 'x', 'o'],
             ['o', 'x', 'o'],
             ['x', 'o', 'x']]
    assert tic_tac_toe_checker(board) == 'x wins!'


def test_o_wins():
    board = [['x', 'x', 'o'],
             ['o', 'o', 'o'],
             ['x', 'o', 'x']]
    assert tic_tac_toe_checker(board) == 'o wins!'


def test_draw():
    board = [['x', 'x', 'o'],
             ['o', 'o', 'x'],
             ['x', 'o', 'x']]
    assert tic_tac_toe_checker(board) == 'draw!'


def test_unfinished():
    board = [['-', '-', 'o'],
             ['-', 'x', 'o'],
             ['x', 'o', 'x']]
    assert tic_tac_toe_checker(board) == 'unfinished!'
