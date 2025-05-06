from typing import Tuple


class Position:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def get_position(self) -> Tuple[int, int]:
        """

        :return: Tuple[x : row, y : col]
        """
        return self.x, self.y

    def set_position(self, x: int, y: int) -> None:
        """

        :param x: row
        :param y: col
        :return: None
        """
        self.x = x
        self.y = y