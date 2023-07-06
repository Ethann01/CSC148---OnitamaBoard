from typing import List
from Style import Style


class OnitamaStack:
    """
    A Stack ADT that stores versions of the game board
    along with versions of the style list. It can tell
    if the Stack is empty and it can also add and remove
    versions of the board and list.

    === Private Attributes ===
    _stack: The stack with the boards and styles.
    """
    _stack: List

    def __init__(self) -> None:
        self._stack = []

    def empty(self) -> bool:
        return self._stack == []

    def push(self, currentboard: List[List[str]], styles: List[Style]) -> None:
        self._stack.append([currentboard, styles])

    def pop(self):
        last = self._stack[-1]
        del self._stack[-1]
        return last
