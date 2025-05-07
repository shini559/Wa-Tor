from src.core.config import TUNA_REPRODUCTION_TIME
from src.core.fish import Fish

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


    def reset_reproduction_timer(self):
        """
        Réinitialise le timer de reproduction
        """
        self.reproduction_timer = TUNA_REPRODUCTION_TIME

    def __str__(self):
        return "F"  # F pour Fish (poisson)

