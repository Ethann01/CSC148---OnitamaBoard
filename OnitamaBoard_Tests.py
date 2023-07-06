from Style import Style
import hypothesis
from OnitamaBoard import OnitamaBoard
from Player import Player
from Pieces import Pieces

def test_construct_styles():
    a = OnitamaBoard(5, Player('X'), Player('Y'))

    assert len(a.styles) == 5
    assert len(a.styles[1].get_moves()) == 3
    assert a.styles[3].owner == 'Y'
    a.construct_styles()
    assert len(a.styles) == 10

def test_exchange_style():
    a = OnitamaBoard(5, Player('X'), Player('Y'))

    assert not a.exchange_style(Style([(0,1)], 'bruh', Pieces.EMPTY))
    assert a.exchange_style(a.styles[4])
    assert a.exchange_style(a.styles[0])

def test_valid_coordinate():
    a = OnitamaBoard(5, Player('X'), Player('Y'))
    assert not a.valid_coordinate(99,99)
    assert a.valid_coordinate(1,1)
    a = OnitamaBoard(7, Player('X'), Player('Y'))
    assert a.valid_coordinate(6,6)
    assert a.valid_coordinate(0,0)

def test_get_token():
    a = OnitamaBoard(5, Player('X'), Player('Y'))
    assert a.get_token(0,0) == Pieces.M1
    assert a.get_token(2,2) == Pieces.EMPTY
    a.set_token(2,2, Pieces.G1)
    assert a.get_token(2,2) == Pieces.G1

def test_set_token():
    a = OnitamaBoard(5, Player('X'), Player('Y'))
    a.set_token(2,1, Pieces.M2)
    assert a.get_token(2,1) == Pieces.M2
    a.set_token(2,1, Pieces.M1)
    assert a.get_token(2,1) == Pieces.M1
    a.set_token(0,4, Pieces.G2)
    assert a.get_token(0,4) == Pieces.G2
    a.set_token(4,4, Pieces.M1)
    assert a.get_token(4,4) == 'x'

if __name__ == '__main__':
    import pytest
    pytest.main(['OnitamaBoard_Tests.py'])
