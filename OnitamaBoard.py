from Player import Player
from typing import List, Union
from Style import Style
from Pieces import Pieces


class EvenSizeError(Exception):
    pass


class OnitamaBoard:
    """
    An OnitamaBoard class consisting of a game board, and keeping track of player token information and styles.
    It can set and clear the board and check if potential plays are valid through coordinate checking.

    === Attributes ===
    size : A board's width and height.
    player1 : Player object representing player who will play the G1 and M1 pieces.
    player2 : Player object representing player who will play the G2 and M2 pieces.
    styles :  A list of all possible play styles including: dragon, crab, horse, mantis, rooster.

    === Private Attributes ===
    _board :
        A nested list representing a grid layout for the board.

    === Representation Invariants ===
    - Size is always an odd number greater or equal to 5.
    - player1 has G1 and M1 pieces.
    - player2 has G2 and M2 pieces.
    """
    size: int
    player1: Player
    player2: Player
    styles: List[Style]
    _board: List[List[str]]

    def __init__(self, size: int, player1: Player, player2: Player, board: Union[List[List[str]], None] = None) -> None:
        """
        Constructs an empty Onitama board. Places four monks and one grandmaster
        on opposite sides of the board. Creates five Styles and distributes them
        among the players.
        """
        if size % 2 == 0:
            raise EvenSizeError("Size must be an odd number.")
        self.size = size
        self.player1 = player1
        self.player2 = player2
        self.styles = []
        self.construct_styles()
        if board is not None:
            self._board = self.deep_copy()
        else:
            self._board = []
            for num in range(self.size):
                self._board.append([])
                for num1 in range(self.size):
                    self._board[num].append(Pieces.EMPTY)
        for num in range(self.size):
            self._board[0][num] = Pieces.M1
            self._board[self.size - 1][num] = Pieces.M2
        self._board[0][self.size // 2] = Pieces.G1
        self._board[self.size - 1]\
            [self.size // 2] = Pieces.G2

    def construct_styles(self) -> None:
        """
        Constructs the 5 movement styles of Onitama for this board. Normally,
        there are 16 movement styles and they are distributed randomly, however for
        this assignment, you are only required to use 5 of them (Dragon, Crab, Horse,
        Mantis, and Rooster).

        You can find the movement patterns for these styles under assets/{style}.png,
        where {style} is one of the five styles mentioned above. Additionally, you
        can also find the images in README.md.

        IMPORTANT: Additionally, we are going to distribute the styles at the start
        of the game in a static or consistent manner. Player 1 (G1) must get the Crab
        and Horse styles. Player 2 (G2) must get the Mantis and Rooster styles. Extra
        (EMPTY) must get the Dragon style.

        Please be sure to follow the distribution of styles as mentioned above as
        this is important for testing. Failure to follow this distribution of styles
        will result in the LOSS OF A LOT OF MARKS.

        >>> a = OnitamaBoard(5, Player('c'), Player('d'))
        >>> a.styles is not []
        True
        >>> a.styles[0].name == 'crab'
        True
        >>> a.construct_styles()
        >>> len(a.styles) == 10
        True
        """
        crab = Style([(0, 2), (-1, 0), (0, -2)], 'crab', Pieces.G1)
        horse = Style([(-1, 0), (1, 0), (0, -1)], 'horse', Pieces.G1)
        dragon = Style([(-1, -2), (-1, 2), (1, -1), (1, 1)], 'dragon', Pieces.EMPTY)
        mantis = Style([(-1, -1), (-1, 1), (1, 0)], 'mantis', Pieces.G2)
        rooster = Style([(0, -1), (0, 1), (1, -1), (-1, 1)], 'rooster', Pieces.G2)

        self.styles.append(crab)
        self.styles.append(horse)
        self.styles.append(dragon)
        self.styles.append(mantis)
        self.styles.append(rooster)

    def exchange_style(self, style: Style) -> bool:
        """
        Exchange the given <style> with the empty style (the style whose owner is
        EMPTY). Hint: Exchanging will involve swapping the owners of the styles.

        Precondition: <style> cannot be the empty style.

        >>> a = OnitamaBoard(5, Player('c'), Player('d'))
        >>> a.exchange_style(Style([(0,1)], 'something', Pieces.EMPTY))
        False
        >>> a.exchange_style(a.styles[0])
        True
        >>> a.exchange_style(a.styles[1])
        True
        """
        if style not in self.styles:
            return False
        for element in self.styles:
            if element.owner == Pieces.EMPTY:
                element.owner, style.owner = style.owner, element.owner
                return True
        return False

    def valid_coordinate(self, row: int, col: int) -> bool:
        """
        Returns true iff the provided coordinates are valid (exists on the board).

        >>> a = OnitamaBoard(5, Player('c'), Player('d'))
        >>> a.valid_coordinate(8,8)
        False
        >>> a.valid_coordinate(1,1)
        True
        >>> a.valid_coordinate(0,0)
        True
        """
        return row < self.size and col < self.size and \
    row >= 0 and col >= 0

    def get_token(self, row: int, col: int) -> str:
        """
        Returns the player token that is in the given <row> <col> position, or the empty
        character if no player token is there or if the position provided is invalid.

        >>> a = OnitamaBoard(5, Player('c'), Player('d'))
        >>> a.get_token(0,0)
        'x'
        >>> a.get_token(99,99)
        ' '
        >>> a.get_token(4,2)
        'Y'
        """
        if row > self.size or col > self.size:
            return Pieces.EMPTY
        return self._board[row][col]

    def set_token(self, row: int, col: int, token: str) -> None:
        """
        Sets the given position on the board to be the given player (or throne/empty)
        <token>.

        >>> a = OnitamaBoard(5, Player('c'), Player('d'))
        >>> a.set_token(0,0,Pieces.EMPTY)
        >>> a.get_token(0,0)
        ' '
        >>> a.set_token(2,2,Pieces.G1)
        >>> a.get_token(2,2)
        'X'
        >>> a.set_token(2,4,Pieces.G2)
        >>> a.get_token(2,4)
        'Y'
        """
        self._board[row][col] = token

    def get_styles_deep_copy(self) -> List[Style]:
        """
        DO NOT MODIFY THIS!!!
        Returns a deep copy of the styles of this board.
        """
        return [style.__copy__() for style in self.styles]

    def deep_copy(self) -> List[List[str]]:
        """
        DO NOT MODIFY THIS!!!
        Creates and returns a deep copy of this OnitamaBoard's
        current state.
        """
        return [row.copy() for row in self._board]

    def set_board(self, board: List[List[str]]) -> None:
        """
        DO NOT MODIFY THIS!!!
        Sets the current board's state to the state of the board which is passed in as a parameter.
        """
        self._board = [row.copy() for row in board]

    def __str__(self) -> str:
        """
        Returns a string representation of this game board.
        """
        s = '  '
        for col in range(self.size):
            s += str(col) + ' '

        s += '\n'

        s += ' +'
        for col in range(self.size):
            s += "-+"

        s += '\n'

        for row in range(self.size):
            s += str(row) + '|'
            for col in range(self.size):
                s += self._board[row][col] + '|'

            s += str(row) + '\n'

            s += ' +'
            for col in range(self.size):
                s += '-+'

            s += '\n'

        s += '  '
        for col in range(self.size):
            s += str(col) + ' '

        s += '\n'
        return s
