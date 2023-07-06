from typing import List, Union
from OnitamaBoard import OnitamaBoard
from Player import Player
from Pieces import Pieces
from OnitamaStack import OnitamaStack
from Style import Style


class OnitamaGame:
    """
    An OnitamaGame class consisting of a game board, and keeping track of which player's
    turn it currently is and some statistics about the game (e.g. how many tokens each player
    has). It knows who the winner of the game is, and when the game is over.

    === Attributes ===
    size : the size of this onitama game.
    player1 : Player object representing player 1(Michael).
    player2 : Player object representing player 2(Ilir).
    whose_turn : Player whose turn it is.
    board_stack : A stack of Onitama boards that

    === Private Attributes ===

    _board:
        Onitama board object with information on player positions and board layout.

    === Representation Invariants ===
    - Size must be an odd number greater or equal to 5

    """
    size: int
    player1: Player
    player2: Player
    _board: OnitamaBoard
    whose_turn: Player
    onitama_stack: OnitamaStack

    def __init__(self, size: int = 5, player1: Union[Player, None] = None, player2: Union[Player, None] = None) -> None:
        """
        DO NOT MODIFY THIS!!!
        Constructs a game of Onitama with 2 players passed in as parameters
        Sets <whose_turn> to <player1>
        Sets the <self.size> of Onitama to the passed in <size> if valid.

        Precondition: The size must be odd and greater than or equal to 5.
        """
        self.size = size
        self.player1 = player1 if player1 is not None else Player(Pieces.G1)
        self.player2 = player2 if player2 is not None else Player(Pieces.G2)
        self.player1.set_onitama(self)
        self.player2.set_onitama(self)
        self._board = OnitamaBoard(self.size, self.player1, self.player2)
        self.whose_turn = self.player1
        self.onitama_stack = OnitamaStack()

    def other_player(self, player: Player) -> Union[Player, None]:
        """
        Given one <player>, returns the other player. If the given <player> is invalid,
        returns null.

        >>> a = OnitamaGame(5, Player('c'), Player('d'))
        >>> a.other_player(a.player1).player_id
        'd'
        >>> a = OnitamaGame(5, Player('c'), Player('d'))
        >>> a.other_player(a.player2).player_id
        'c'
        >>> a = OnitamaGame(5, Player('c'), Player('d'))
        >>> a.other_player(Player('b'))
        None
        """
        '''
        if player != self.player1 and\
            player != self.player2:
            return None
        if player == self.player1:
            return self.player2
        return self.player1
        '''
        if player == self.player1:
            return self.player2
        elif player == self.player2:
            return self.player1
        else:
            if player != self.player1 or player != self.player2:
                return None

    def get_token(self, row: int, col: int) -> str:
        """
        Returns the player token that is in the given position, or the empty
        character if no player token is there or if the position provided is invalid.

        >>> a = OnitamaGame(5, Player('c'), Player('d'))
        >>> a.get_token(3, 3)
        ' '
        >>> a = OnitamaGame(5, Player('c'), Player('d'))
        >>> a.get_token(4, 2)
        'Y'
        >>> a = OnitamaGame(5, Player('c'), Player('d'))
        >>> a.get_token(0, 0)
        'x'
        """
        return self._board.get_token(row, col)

    def is_legal_move(self, row_o: int, col_o: int, row_d: int, col_d: int) -> bool:
        """
        Checks if a move with the given parameters would be legal based on the
        origin and destination coordinates.
        This method should specifically check for the following 3 conditions:
            1)  The movement is in the bounds of this game's board.
            2)  The correct piece is being moved based on the current player's turn.
            3)  The destination is valid.
                A player CANNOT move on top of their own piece.

        Precondition: <row_o> and <col_o> must be on the board.

        >>> a = OnitamaGame(5, Player('c'), Player('d'))
        >>> a.is_legal_move(0, 0, 1, 0)
        True
        >>> a.is_legal_move(0, 0, 0, 1)
        False
        >>> a.is_legal_move(0, 0, 4, 0)
        True
        """

        if not self._board.valid_coordinate(row_d, col_d):
            return False
        if self._board.get_token(row_o, col_o) == Pieces.EMPTY:
            return False
        if self._board.get_token(row_o, col_o) == Pieces.M1 or \
                self._board.get_token(row_o, col_o) == Pieces.G1:
            if self.whose_turn != self.player1:
                return False
            if self._board.get_token(row_d, col_d) == Pieces.M1 or \
                    self._board.get_token(row_d, col_d) == Pieces.G1:
                return False
        if self._board.get_token(row_o, col_o) == Pieces.M2 or \
                self._board.get_token(row_o, col_o) == Pieces.G2:
            if self.whose_turn != self.player2:
                return False
            if self._board.get_token(row_d, col_d) == Pieces.M2 or \
                    self._board.get_token(row_d, col_d) == Pieces.G2:
                return False
        return True

    def move(self, row_o: int, col_o: int, row_d: int, col_d: int, style_name: str) -> bool:
        """
        Attempts to make a move for player1 or player2 (depending on whose turn it is) from
        position <row_o>, <col_o> to position <row_d>, <col_d>.

        On a successful move, it stores the current (unmodified) state of the board and
        the list of styles to <self.onitama_stack> by calling the
        <self.onitama_stack.push(var1, var2)> method.

        After storing the move, it will make the valid move and modify the board and
        actually make the move.

        Returns true if the move was successfully made, false otherwise.

        Preconditon: <row_o> and <col_o> must be on the board.

        Postcondition: A valid move was made on the OnitamaBoard and the correct styles were exchanged.

        >>> a = OnitamaGame(5, Player('c'), Player('d'))
        >>> a.move(0, 0, 4, 0, 'horse')
        False
        >>> a.move(0, 0, 1, 0, 'horse')
        True
        >>> a.move(0, 0, 9999, 0, 'horse')
        False
        """

        if not self.is_legal_move(row_o, col_o, row_d, col_d):
            return False
        for style in self.get_styles():
            if style.name == style_name:
                currentstyle = style
        valid = False
        for pair in currentstyle.get_moves():
            if self.whose_turn == self.player1:
                if row_o - pair[0] == row_d and \
                        col_o - pair[1] == col_d:
                    valid = True
            if self.whose_turn == self.player2:
                if row_o + pair[0] == row_d and \
                        col_o + pair[1] == col_d:
                    valid = True
        if not valid:
            return False
        self.onitama_stack.push(self.get_board(), self.get_styles_deep_copy())
        self._board.exchange_style(currentstyle)
        self._board.set_token(row_d, col_d, self._board.get_token(row_o, col_o))
        self._board.set_token(row_o, col_o, Pieces.EMPTY)
        self.whose_turn = self.other_player(self.whose_turn)
        return True


    def get_winner(self) -> Union[Player, None]:
        """
        Returns the winner of the game if the game is over, or the board token for
        EMPTY if the game is not yet finished. As per Onitama's rules, the winner of
        the game is the player whose Grandmaster reaches the middle column on the
        opposite row from the start position, OR the player who captures the other
        player's Grandmaster.

        >>> a = OnitamaGame(5, Player('c'), Player('d'))
        >>> a.get_winner()
        ' '
        >>> a._board.set_token(4,2, Pieces.G1)
        >>> a.get_winner().player_id
        'c'
        >>> a = OnitamaGame(5, Player('c'), Player('d'))
        >>> a._board.set_token(4,2, Pieces.EMPTY)
        >>> a.get_winner().player_id
        'c'
        """

        board = self.get_board()
        if board[0][self.size // 2] == Pieces.G2:
            return self.player2
        if board[- 1][self.size // 2] == Pieces.G1:
            return self.player1
        g1check = False
        g2check = False
        for row in self.get_board():
            for square in row:
                if square == Pieces.G1:
                    g1check = True
                elif square == Pieces.G2:
                    g2check = True
        if g1check and g2check:
            return None
        if g1check and not g2check:
            return self.player1
        return self.player2

    def undo(self) -> None:
        """
        DO NOT MODIFY THIS!!!
        Undo's the Onitama game's state to the previous turn's state if possible.

        >>> a = OnitamaGame(5, Player('c'), Player('d'))
        >>> a.onitama_stack.push(a.get_board(), a.get_styles())
        >>> a.undo()
        >>> a.onitama_stack._stack
        []
        >>> a.undo()

        >>> a = OnitamaGame(5, Player('c'), Player('d'))
        >>> a.onitama_stack.push(a.get_board(), a.get_styles())
        >>> a.undo()
        >>> a.whose_turn.player_id
        'd'
        """
        if not self.onitama_stack.empty():
            # The pop call here returns a board and a list of styles that we use
            # to revert to the previous state of the game
            board, styles = self.onitama_stack.pop()
            self._board.set_board(board)
            self._board.styles = styles
            # Switch to the previous player's turn
            self.whose_turn = self.other_player(self.whose_turn)

    def get_styles(self) -> List[Style]:
        """
        Get the different styles of movement in Onitama, this is the direct reference
        to the styles list.
        """
        return self._board.styles

    def get_styles_deep_copy(self) -> List[Style]:
        """
        DO NOT MODIFY THIS!!!
        Get a DEEP COPY of the different styles of movement in Onitama.
        This makes a new List and has a different memory address than <self._board.styles>
        """
        return self._board.get_styles_deep_copy()

    def get_board(self) -> List[List[str]]:
        """
        DO NOT MODIFY THIS!!!
        Gets a deep copy of this OnitamaBoard.
        """
        return self._board.deep_copy()

    def set_board(self, size: int, board: List[List[str]]) -> None:
        """
        DO NOT MODIFY THIS!!!
        Construct a new OnitamaBoard with the given size and preset board.
        """
        self.size = size
        self._board = OnitamaBoard(
            self.size, self.player1, self.player2, board=board)

    def get_board_string(self) -> str:
        """
        Returns string representation of this board.
        """
        return str(self._board)

    def get_styles_string(self) -> str:
        """
        Returns string representation of all available styles.
        """
        empty_string = 'Fifth style: \n'
        p1_string = f'Player {self.player1.player_id} styles:\n'
        p2_string = f'Player {self.player2.player_id} styles:\n'
        for sty in self.get_styles():
            if sty.owner == self.player1.player_id:
                p1_string += str(sty) + '\n'
            elif sty.owner == self.player2.player_id:
                p2_string += str(sty) + '\n'
            else:
                empty_string += str(sty) + '\n'

        return p1_string + p2_string + empty_string
