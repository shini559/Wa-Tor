from .fish import Fish

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
