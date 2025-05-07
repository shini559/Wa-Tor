from src.core.planet import Planet
import tkinter as tk
from src.core.config import NB_TUNA, NB_SHARK



class Simulation:
    """
    deroulement de la simulation
    """
    def __init__(self, planet: Planet):
        self.planet: Planet = planet

        self.chronon = 0

    def start(self):
        self.planet.initialize(NB_TUNA, NB_SHARK)
        self.planet.chronon = 1



    def restart(self):
        self.start()

    def cycle(self):
        """
        deroulement du cycle de la simulation en cours
        :return:
        """
        self.planet.update()
        self.chronon += 1

