from src.core.config import TUNA_REPRODUCTION_TIME
from src.core.entity.fish import Fish
from src.core.entity.position import Position


class Tuna(Fish):
    def __init__(self, pos: Position):
        super().__init__(pos)
        self._reproduction_timer = TUNA_REPRODUCTION_TIME

    def naissance(self, planet: "Planet"):
        planet.add(Tuna(self.last_position))
        self.is_naissance = False

    def set_age(self, age: int):
        self.age = age
        self.is_naissance = not (age % self._reproduction_timer == 0)

    def __repr__(self):
        return '🐟'

    def __str__(self):
        return '🐟'