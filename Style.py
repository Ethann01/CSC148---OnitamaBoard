from __future__ import annotations
from typing import List, Tuple, Union
from Pieces import Pieces


class Style:
    """
    Holds the information of a style card, including the name, owner and possible moves.
    It can get this information for styles and can compare it to other styles.

    === Attributes ===
    name: name of the style
    owner: owner of the style

    === Private Attributes ===
    _moves: the moves the piece can make relative to its starting position
    """
    _moves: List[Tuple(int, int)]
    name: str
    owner: str

    # TODO: Add method type annotations
    def __init__(self, pairs: List[Tuple(int, int)], name: str, owner: str=Pieces.EMPTY) -> None:
        """
        Initializes the information for a style, which are the style name, its moves and its owner.
        """
        self.name = name
        self._moves = pairs.copy()
        self.owner = owner

    # TODO: Add method type annotations
    def get_moves(self) -> List[Tuple(int, int)]:
        """
        Returns a deep copy of the list of moves.
        """
        return self._moves.copy()

    # TODO: Add method type annotations
    def __eq__(self, other: Style) -> bool:
        """
        Returns true iff the class's style name matches a given style name.
        """
        return self.name == other.name and self.owner == other.owner

    # TODO: Add method type annotations
    def __copy__(self) -> Style:
        """
        Returns a copy of the class's style.
        """
        return Style(self._moves.copy(), self.name, self.owner)
