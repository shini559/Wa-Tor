from config import TUNA_REPRODUCTION_TIME
from fish import Fish

class Tuna(Fish):
    """
    class Tuna
    """
    def __init__(self, x: int, y: int):
        """

        :param x:
        :param y:
        :return:
        """
        super().__init__(x, y)
        self.reproduction_timer: int = TUNA_REPRODUCTION_TIME
