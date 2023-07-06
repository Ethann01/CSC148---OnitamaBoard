class Turn:
    """
    Contains the information required for a turn. This includes
    the initial position as well as the destination of the piece,
    the name of the style being used and the player who's about
    to have their turn.

    === Attributes ===
    row_o: row of the starting position
    col_o: column of the starting position
    row_d: row of the destination
    col_d: column of the destination
    style_name: name of the style that will be used in the turn
    player: the player who is having their turn

    === Representation Invariants ===
    row_o is on the board.
    col_o is on the board.

    """
    row_o: int
    col_o: int
    row_d: int
    col_d: int
    style_name: str
    player: str

    # TODO: Add method type annotations
    def __init__(self, row_o: int, col_o: int, row_d: int, col_d: int, style_name: str, player: str) -> None:
        """
        Initializes the information necessary for a turn for other classes to make use of.
        """
        self.row_o = row_o
        self.col_o = col_o
        self.row_d = row_d
        self.col_d = col_d
        self.style_name = style_name
        self.player = player
