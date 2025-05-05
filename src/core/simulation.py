import random
import time
from typing import List

from src.core.config import TIK
from src.core.entity.fish import Fish
from src.core.entity.planet import Planet
from src.core.entity.shark import Shark
from src.core.entity.tuna import Tuna


class Simulation:
    def __init__(self, planet: Planet):
        self.planet = planet

    def start(self):
        self.planet.init()

    def reset(self):
        self.planet.init()

    def etape(self, tik: int):
        fishs: List[Fish] = self.planet.ecosystem

        print(self.planet)

        for fish in fishs:
            fish.get_voisins(self.planet)

            print(f"fish de type {type(fish)} age {fish.age} ({fish.position}) a comme voisin {fish.voisins_entity} move disp {fish.move_dispo}")

            if fish.is_naissance:
                fish.naissance(self.planet)

            if isinstance(fish, Shark):
                fish: Shark
                tuna_repas = fish.meat([tuna for tuna in fish.voisins_entity if isinstance(tuna, Tuna)])
                if tuna_repas:
                    self.planet.ecosystem.remove(tuna_repas)
            else:
                pass

            fish.move()

            fish.set_age(fish.age + 1)

        self.planet.update()
        print('TIK', tik)
    def pause(self):
        pass

if __name__ == "__main__":
    simulation = Simulation(Planet())
    simulation.start()
    tik_count = 1
    while True:
        simulation.etape(tik_count)
        tik_count += 1
        time.sleep(TIK)