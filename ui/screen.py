import itertools
import tkinter as tk
import os
from src.core.config import WIDTH, HEIGHT, NB_TUNA, NB_SHARK
from PIL import Image, ImageTk
from src.core.simulation import Simulation


CELL_SIZE = 20

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
        self.root.resizable(False, False)
        self.root.title("Wa-Tor")
        self.canvas = tk.Canvas(self.root, width=WIDTH * CELL_SIZE, height=HEIGHT * CELL_SIZE, bg="lightblue")
        self.canvas.pack()
        self.setup_controls()

        self.tuna_count_label = tk.Label(self.root, text="Tuna: 0", font=("Arial", 12))
        self.tuna_count_label.pack()

        self.shark_count_label = tk.Label(self.root, text="Shark: 0", font=("Arial", 12))
        self.shark_count_label.pack()


        # Chargement des images dans un self.images
        self.images = {
            "water": load_image("sea.png"),
            "tuna": load_image("fish.png"),
            "shark": load_image("shark.png"),
        }

        self.update()


    def update(self):
        """
        update the grid display
        """
        if not self.pause:
            self.planet.update()
            self.chronon += 1
            self.chronon_label.config(text = f"Chronon: {self.chronon_label}")
            self.draw()
        self.root.after(200, self.update)




    def draw(self):
        self.canvas.delete("all")

        nb_tuna, nb_shark = self.planet.count_fish()

        self.tuna_count_label.config(text=f"Tuna: {nb_tuna}")
        self.shark_count_label.config(text=f"Shark: {nb_shark}")

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





