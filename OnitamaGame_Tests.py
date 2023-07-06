import hypothesis
from Style import Style
from OnitamaGame import OnitamaGame
from Player import Player
from Pieces import Pieces
from OnitamaBoard import OnitamaBoard
from OnitamaStack import OnitamaStack


def test_other_player():
    a = OnitamaGame(5, Player('X'), Player('Y'))
    assert a.other_player(a.player1).player_id == 'Y'
    assert a.other_player(Player('garbage')) == None
    assert a.other_player(a.player2).player_id == 'X'
    assert a.other_player(Player('different garbage?')) == None


def test_get_token():
    a = OnitamaGame(5, Player('X'), Player('Y'))
    assert a.get_token(2, 2) == Pieces.EMPTY
    assert a.get_token(0, 2) == Pieces.G1
    assert a.get_token(99999999999, 9) == ' '
    a = OnitamaGame(7, Player('X'), Player('Y'))
    assert a.get_token(9999, 98) == ' '
    assert a.get_token(0, 6) == Pieces.M1


def test_is_legal_move():
    a = OnitamaGame(5, Player('X'), Player('Y'))
    a.whose_turn = a.player1
    assert not a.is_legal_move(0, 0, 0, 3)
    assert a.is_legal_move(0, 0, 2, 2)
    a.whose_turn = a.player2
    assert not a.is_legal_move(4, 0, 4, 4)
    assert not a.is_legal_move(0, 0, 4, 4)
    assert a.is_legal_move(4, 0, 2, 2)
    assert not a.is_legal_move(3, 3, 3, 2)

def test_move():
    a = OnitamaGame(5, Player('X'), Player('Y'))
    a.whose_turn = a.player1
    assert not a.move(0, 0, 4, 4, 'horse')
    assert a.move(0, 0, 1, 0, 'horse')
    assert not a.move(99, 99, 90, 00, 'crab')
    assert not a.move(0, 0, 90, 00, 'crab')
    a.whose_turn = a.player2
    assert a.move(4, 0, 3, 1, 'mantis')
    assert a.whose_turn == a.player1
    assert a.move(1, 0, 2, 0, 'horse')


def test_get_winner():
    a = OnitamaGame(5, Player('X'), Player('Y'))
    assert a.get_winner() == Pieces.EMPTY
    a._board.set_token(0, 2, Pieces.G2)
    assert a.get_winner().player_id == a.player2.player_id
    a = OnitamaGame(5, Player('X'), Player('Y'))
    a._board.set_token(4, 2, Pieces.G1)
    assert a.get_winner().player_id == a.player1.player_id


def test_undo():
    a = OnitamaGame(5, Player('X'), Player('Y'))
    a.onitama_stack.push(a.get_board(), a.get_styles())
    a.undo()
    assert a.onitama_stack._stack == []
    assert a.whose_turn.player_id == a.player2.player_id


if __name__ == '__main__':
    import pytest

    pytest.main(['OnitamaGame_Tests.py'])
