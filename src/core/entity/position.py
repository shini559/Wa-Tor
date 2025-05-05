from typing import Tuple


class Position:
    def __init__(self, x:int, y:int):
        """

        :param x: row
        :param y: col
        """
        self.x = x
        self.y = y

    def set_position(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def get_position(self) -> Tuple[int, int]:
        return self.x, self.y

    def __repr__(self):
        return f"[{self.x} : {self.y}]"