import random
from typing import Tuple, List

from src.core.config import TUNA_REPRODUCTION_TIME


class Fish:
    """
    class Fish
    """
    def __init__(self, x: int, y: int):
        """

        :param x:
        :param y:
        :return:
        """
        self.x: int = x
        self.y: int = y

        self.last_x: int = x
        self.last_y: int = y

        self.age = 0
        self.reproduction_timer: int = TUNA_REPRODUCTION_TIME

        self.__alive: bool = True

        self.move_dispo: List[Tuple[int, int]] = []

    def move(self) -> None:
        """

        :param pos:
        :return:
        """
        x, y = self.move_dispo[random.randint(0, len(self.move_dispo) - 1)]

        self.last_x = self.x
        self.last_y = self.y

        self.x = x
        self.y = y

        self.move_dispo.clear()

    @property
    def last_move(self) -> tuple[int,int]:
        """
        return the last position
        :return: tuple[x,y]
        """
        return self.last_x, self.last_y

    def is_alive(self) -> bool:
        return self.__alive

