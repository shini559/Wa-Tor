import time

from src.core.display_interface import DisplayInterface
from src.core.entity.planet import Planet
from src.core.simulation import Simulation


class TerminalDisplay(DisplayInterface):
    def __init__(self):
        self.simulation: Simulation = Simulation(Planet())
        self.tik: int = 1

    def proccess(self):
        self.simulation.start()
        tik_count = 1
        while True:
            self.update()
            self.tik += 1
            time.sleep(self.tik)

    def start(self):
        self.simulation.start()

    def update(self):
        self.simulation.etape(self.tik)

    def pause(self):
        self.simulation.pause()

    def reset(self):
        self.simulation.reset()

