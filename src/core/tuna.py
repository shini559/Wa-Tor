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
        super()._init_(x, y)
        self.reproduction_timer: int = 0
