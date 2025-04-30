from config import TUNA_REPRODUCTION_TIME


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

    def move(self, x: int, y: int):
        self.last_x = self.x
        self.last_y = self.y

        self.x = x
        self.y = y

    @property
    def last_move(self) -> tuple[int,int]:
        """
        return the last position
        :return: tuple[x,y]
        """
        return self.last_x, self.last_y
