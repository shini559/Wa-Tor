from src.core.planet import Planet


class Simulation:
    """
    deroulement de la simulation
    """
    def __init__(self, planet: Planet):
        self.planet: Planet = planet


    def start(self):
        """
        comencer la simulation
        :return:
        """
        pass


    def pause(self):
        """
        maitre en pause la simulation
        :return:
        """
        pass


    def reset(self):
        """
        recomencer la simulation de zero
        :return:
        """
        pass


    def _cycle(self):
        """
        deroulement du cycle de la simulation en cour
        :return:
        """
        pass

