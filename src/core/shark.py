from src.core.fish import Fish
from src.core.planet import Planet


class Shark(Fish):
    """
    class Shark
    """
    def __init__(self, x: int, y: int):
        """

        :param x:
        :param y:
        """
        super().__init__(x, y)
        self.reproduction_timer: int = 0

    def __str__(self):
        return "S"  # S pour Shark

