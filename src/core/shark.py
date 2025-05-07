from src.core.fish import Fish
from src.core.config import SHARK_REPRODUCTION_TIME, SHARK_ENERGY, SHARK_ENERGY_GAIN


class Shark(Fish):
    """
    class Shark
    """

    def __init__(self, x: int, y: int):
        """
        :param x: position x
        :param y: position y
        """
        super().__init__(x, y)
        self.reproduction_timer: int = SHARK_REPRODUCTION_TIME
        self.energy: int = SHARK_ENERGY

    def get_available_moves_with_food(self, width: int, height: int):
        """
        Cherche les positions adjacentes où il y a des thons
        """
        food_positions = []
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_x = (self.x + dx) % width
            new_y = (self.y + dy) % height
            entity = self.grid[new_y][new_x]
            if entity is not None and str(entity) == "F":
                food_positions.append((new_x, new_y))
        return food_positions

    def move(self, width: int, height: int) -> bool:
        """
        Déplace le requin et gère son énergie
        """
        # Réduire l'énergie
        self.energy -= 1

        # Vérifier si le requin meurt de faim
        if self.energy <= 0:
            self.grid[self.y][self.x] = None
            return True

        # Chercher de la nourriture
        food_positions = self.get_available_moves_with_food(width, height)
        if food_positions:
            # Manger un thon
            new_x, new_y = food_positions[0]
            self.last_x, self.last_y = self.x, self.y
            self.grid[self.y][self.x] = None
            self.x, self.y = new_x, new_y
            self.grid[new_y][new_x] = self
            self.energy += SHARK_ENERGY_GAIN

            # Gérer la reproduction
            self.age += 1
            self.try_reproduce()
            return True

        # Si pas de nourriture, mouvement normal
        return super().move(width, height)

    def reset_reproduction_timer(self):
        """
        Réinitialise le timer de reproduction
        """
        self.reproduction_timer = SHARK_REPRODUCTION_TIME

    def __str__(self):
        return "S"  # S pour Shark