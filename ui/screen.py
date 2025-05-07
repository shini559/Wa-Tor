import itertools
import tkinter as tk
import os
from src.core.config import WIDTH, HEIGHT, NB_TUNA, NB_SHARK
from PIL import Image, ImageTk
from src.core.simulation import Simulation
from tkinter import messagebox

CELL_SIZE = 15

base_path = os.path.dirname(os.path.abspath(__file__))
assets_path = os.path.join(base_path, "assets")

def load_image(filename):
    path = os.path.join(assets_path, filename)
    return ImageTk.PhotoImage(Image.open(path).resize((CELL_SIZE, CELL_SIZE)))

class GridDisplay(Simulation):
    def __init__(self, planet):
        super().__init__(planet)
        self.planet = planet
        self.root = tk.Tk()
        #self.root.resizable(False, False)
        self.root.title("Wa-Tor")
        self.canvas = tk.Canvas(self.root, width=WIDTH * CELL_SIZE, height=HEIGHT * CELL_SIZE, bg="lightblue")
        self.canvas.pack()
        self.setup_controls()

        # Chargement des images dans un self.images
        self.images = {
            "water": load_image("sea.png"),
            "tuna": load_image("fish.png"),
            "shark": load_image("shark.png"),
        }

        self.update()

    def update(self):
        """
        Met à jour l'affichage de la grille
        """
        if not self.pause:
            if self.planet.should_stop():
                self.pause = True
                tuna_count, shark_count = self.planet.count_entities()
                message = "Simulation arrêtée:\n"
                if self.planet.is_grid_full():
                    message += "La grille est pleine!"
                if tuna_count == 0:
                    message += "Plus de thons!"
                
                tk.messagebox.showinfo("Fin de simulation", message)
                return

            self.planet.update()
            self.chronon += 1
            self.draw()
        self.root.after(200, self.update)

    def draw(self):
        self.canvas.delete("all")

        for i, j in itertools.product(range(HEIGHT), range(WIDTH)):
            x = j * CELL_SIZE
            y = i * CELL_SIZE

            entity = self.planet.grid[i][j]
            if entity is None or str(entity) not in ["F", "S"]:
                img = self.images["water"]
            elif str(entity) == "F":
                img = self.images["tuna"]
            else:
                img = self.images["shark"]
            self.canvas.create_image(x, y, anchor="nw", image=img)

        self.root.image_refs = self.images  # conserver les images en mémoire
        self.chronon_label.config(text = f"Chronon: {self.planet.chronon}")


    def restart_simulation(self):
        """Réinitialise la planète et redémarre la simulation"""
        self.canvas.delete("all")
        self.planet.initialize(NB_TUNA, NB_SHARK)
        self.chronon = 0
        self.planet.chronon = 1
        self.pause = False
        self.pause_button.config(text="Pause")
        self.draw()
        if not hasattr(self, '_update_scheduled'):
            self._update_scheduled = True
            self.update()
