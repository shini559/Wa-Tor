from entity import Entity


class Fish (Entity): 
    def _init_(self, x: int, y: int):
        super()._init_(x, y)
        print(type())
        self.reproduction_timer: int = 0
