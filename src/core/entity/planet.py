import random
from typing import List

from src.core.config import HEIGHT, WIDTH, NB_TUNA, NB_SHARK
from src.core.entity.fish import Fish
from src.core.entity.position import Position
from src.core.entity.shark import Shark
from src.core.entity.tuna import Tuna


class Planet:
    def __init__(self):
        self.ty: int = WIDTH # col
        self.tx: int = HEIGHT # row

        self.grid = self.clear()

        self.nb_tuna: int = NB_TUNA

        self.nb_shark: int = NB_SHARK

        self.ecosystem: List[Fish] = []


    def init(self) -> None:
        self.sort()

        self.update()


    def update(self) -> None:
        self.grid = self.clear()

        for fish in self.ecosystem:
            x, y = fish.position.get_position()

            self.grid[x][y] = fish


    def clear(self) -> List[List[None]]:
        return [[None for _ in range(self.ty)] for _ in range(self.tx)]


    def sort(self) -> None:
        positions = [(Position(x, y)) for x in range(self.tx) for y in range(self.ty)]
        random.shuffle(positions)

        positions = positions[:self.nb_tuna + self.nb_shark]

        tuna_positions = positions[:self.nb_tuna]
        [self.add(Tuna(p)) for p in tuna_positions]
        print('tuna_positions', tuna_positions)

        shark_positions = positions[self.nb_tuna:self.nb_tuna + self.nb_shark]
        [self.add(Shark(p)) for p in shark_positions]
        print('shark_positions', shark_positions)


    def add(self, fish: Fish):
        self.ecosystem.append(fish)


    def __str__(self) -> str:
        table_str: str = ""

        for row in self.grid:
            for cell in row:
                if cell is None:
                    table_str += "[~~]"
                else:
                    table_str += ('[' + str(cell)  + ']')
            table_str += '\n'
        return table_str


if __name__ == "__main__":
    planet = Planet()
    planet.init()
    print(planet)