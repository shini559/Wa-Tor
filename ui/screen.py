import tkinter as tk
import os
from src.core.config import WIDTH, HEIGHT
from PIL import Image, ImageTk

CELL_SIZE = 30

base_path = os.path.dirname(os.path.abspath(__file__))
assets_path = os.path.join(base_path, "assets")

def load_image(filename):
    path = os.path.join(assets_path, filename)
    return ImageTk.PhotoImage(Image.open(path).resize((CELL_SIZE, CELL_SIZE)))

class GridDisplay():
    def __init__(self, planet):
        self.planet = planet
        self.root = tk.Tk()
        self.root.resizable(False, False)
        self.root.title("Wa-Tor")

        self.canvas = tk.Canvas(self.root, width=WIDTH * CELL_SIZE, height=HEIGHT * CELL_SIZE, bg="lightblue")
        self.canvas.pack()

        # Chargement des images dans self.images
        self.images = {
            "water": load_image("sea.png"),
            "tuna": load_image("fish.png"),
            "shark": load_image("shark.png"),
        }

    def draw(self):
        self.canvas.delete("all")

        for i in range(HEIGHT):
            for j in range(WIDTH):
                x = j * CELL_SIZE
                y = i * CELL_SIZE

                entity = self.planet.grid[i][j]
                if entity is None:
                    img = self.images["water"]
                elif str(entity) == "F":
                    img = self.images["tuna"]
                elif str(entity) == "S":
                    img = self.images["shark"]
                else:
                    img = self.images["water"]

                self.canvas.create_image(x, y, anchor="nw", image=img)

        self.root.image_refs = self.images  # conserver les images en mémoire

    def run(self):
        self.draw()
        self.root.mainloop()
