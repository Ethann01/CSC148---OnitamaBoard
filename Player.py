from __future__ import annotations
from Pieces import Pieces
from Style import Style
from typing import Dict, List, Tuple, Union
from Turn import Turn
from random import randint


class Player:
    """
    Gathers information on a specified player. Can find the locations
    of the specified player, can gather its styles, and can find the valid moves
    for the player.

    === Attributes ===
    player_id: a player or Pieces.EMPTY for the class to find information on

    """
    player_id: str

    # TODO: Add method type annotations
    def __init__(self, player_id: str) -> None:
        """
        Initializes the player id, so the class can
        distinguish between the two players as well
        as "EMPTY" things, things that no player own.
        """
        self.player_id = player_id

    # TODO: Add method type annotations
    def get_turn(self) -> Union[List[Turn], None]:
        """
        Returns turn information from a random style the player owns.
        """
        raise NotImplementedError

    # TODO: Add method type annotations
    def get_tokens(self) -> List[Tuple(int, int)]:
        """
        Returns a list of the locations of player_id pieces.
        """
        board = self.onitama.get_board()
        tokens = []
        for i, row in enumerate(board):
            for j, token in enumerate(row):
                if token.lower() == self.player_id.lower():
                    tokens.append((i, j))
        return tokens

    # TODO: Add method type annotations
    def get_styles(self) -> List[Style]:
        """
        Returns a list of the styles that the player
        represented by player_id owns.
        """
        styles = []
        for sty in self.onitama.get_styles():
            if sty.owner == self.player_id:
                styles.append(sty)
        return styles

    # TODO: Add method type annotations
    def get_valid_turns(self) -> Dict[str, List[Turn]]:
        """
        Returns a dictionary that contains the various style names along with
        the turn information for every valid move.
        """
        styles = self.get_styles()
        tokens = self.get_tokens()
        turns = {}
        for sty in styles:
            turns[sty.name] = []
            for row, col in tokens:
                for d_row, d_col in sty.get_moves():
                    # Flip move direction if player is X
                    if self.player_id == Pieces.G1:
                        d_row *= -1
                        d_col *= -1
                    # Check is_legal_move
                    if self.onitama.is_legal_move(row, col, row + d_row, col + d_col):
                        turns[sty.name].append(Turn(row, col, row + d_row,
                                                    col + d_col, sty.name, self.player_id))

        return turns

    # TODO: Add method type annotations
    def set_onitama(self, onitama) -> None:
        """
        Creates an OnitamaGame class object.
        """
        self.onitama = onitama


class PlayerRandom(Player):
    """
    For a given player this class gives turn information from a random style
    the player owns.

    === Attributes ===
    player_id: a player or Pieces.EMPTY for the class to find a turn for
    """

    # TODO: Add method type annotations
    def __init__(self, player_id: str) -> None:
        """
        Initializes the player id, so the class can
        distinguish between the two players as well
        as "EMPTY" things, things that no player own.
        """
        super().__init__(player_id)

    # TODO: Add method type annotations
    def get_turn(self) -> Union[List[Turn], None]:
        turns = []
        valid_turns = self.get_valid_turns()
        for style_name in valid_turns:
            turns.extend(valid_turns[style_name])

        # Return a random valid turn
        if len(turns) == 0:
            return None
        return turns[randint(0, len(turns) - 1)]
