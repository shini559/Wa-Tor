from fish import Fish


class Shark(Fish): 
    def _init_(self, x: int, y: int):
        super()._init_(x, y)
        self.reproduction_timer: int = 0