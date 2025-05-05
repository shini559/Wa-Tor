import random
from typing import List

from src.core.config import SHARK_REPRODUCTION_TIME
from src.core.entity.fish import Fish
from src.core.entity.position import Position
from src.core.entity.tuna import Tuna


class Shark(Fish):
    def __init__(self, pos: Position):
        super().__init__(pos)
        self._reproduction_timer = SHARK_REPRODUCTION_TIME

    def naissance(self, planet: "Planet"):
        planet.add(Shark(self.last_position))

    def meat(self, fishs: List[Tuna]) -> Tuna | None:
        """
        Choisis quel poisson va t'être mangé. Bon appétit !!!
        :param fishs: Liste des poissons qui peuvent être mangé
        :return: Le poisson qui s'est fait manger
        """
        if not fishs:
            return None

        fish: Tuna = fishs[random.randint(0, len(fishs) -1)]
        fish._alive = False
        print("MANGER !!!")
        return fish

    def set_age(self, age: int):
        self.age = age
        self.is_naissance = not (age % self._reproduction_timer == 0)

    def __repr__(self):
        return '🦈'

    def __str__(self):
        return '🦈'