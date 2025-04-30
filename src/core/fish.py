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

        self.age = 0
        self.reproduction_timer: int = TUNA_REPRODUCTION_TIME
