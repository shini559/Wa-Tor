import itertools
import tkinter as tk
import os
from src.core.config import WIDTH, HEIGHT, NB_TUNA, NB_SHARK
from PIL import Image, ImageTk
from src.core.planet import Planet
from src.core.simulation import Simulation
from src.core.history import History



CELL_SIZE = 13

base_path = os.path.dirname(os.path.abspath(__file__))
assets_path = os.path.join(base_path, "assets")

def load_image(filename):
    path = os.path.join(assets_path, filename)
    return ImageTk.PhotoImage(Image.open(path).resize((CELL_SIZE, CELL_SIZE)))

class GridDisplay:
    def __init__(self):
        self.planet = Planet()
        self.simulation = Simulation(self.planet)

        self.root = tk.Tk()
        # self.root.resizable(False, False)
        self.root.title("Wa-Tor")
        self.canvas = tk.Canvas(self.root, width=WIDTH * CELL_SIZE, height=HEIGHT * CELL_SIZE, bg="lightblue")
        self.canvas.pack()
        self.setup_controls()

        self.tuna_count_label = tk.Label(self.root, text="Tuna: 0", font=("Arial", 12))
        self.tuna_count_label.pack()

        self.shark_count_label = tk.Label(self.root, text="Shark: 0", font=("Arial", 12))
        self.shark_count_label.pack()

        self.first_update = True
        self.status_label = tk.Label(self.root, text="Simulation en cours", font=("Arial", 12))
        self.status_label.pack()

        self.pause = False


        # Chargement des images dans un self.images
        self.images = {
            "water": load_image("sea.png"),
            "tuna": load_image("fish.png"),
            "shark": load_image("shark.png"),
        }

        self.update()

        self.history = History()


    def update(self):
        """
        Met à jour l'affichage de la grille et vérifie les conditions d'arrêt
        """
        if not self.pause:
            if self.first_update:
                self.first_update = False
                self.chronon_label.config(text=f"Chronon: {self.simulation.chronon}")
                self.simulation.cycle()
                self.draw()
            else:
                # Vérifier les conditions d'arrêt
                nb_tuna, nb_shark = self.planet.count_fish()
                total_creatures = nb_tuna + nb_shark
                total_cells = WIDTH * HEIGHT

                # Condition 1 : Plus aucune créature vivante
                if total_creatures == 0:
                    raison = "Plus aucune créature vivante"
                    self.status_label.config(text=f"Simulation terminée : {raison}", fg="red")
                    self.history.log(self.planet.chronon, raison, nb_tuna, nb_shark)
                    self.pause = True
                    return

                # Condition 2 : Grille pleine
                if total_creatures == total_cells:
                    raison = "La grille est pleine"
                    self.status_label.config(text=f"Simulation terminée : {raison}", fg="red")
                    self.history.log(self.planet.chronon, raison, nb_tuna, nb_shark)
                    self.pause = True
                    return

            self.chronon_label.config(text = f"Chronon: {self.simulation.chronon}")
            self.simulation.cycle()
            self.draw()
        self.root.after(200, self.update)


    def _extracted_from_update_13(self, arg0):
        print(arg0)
        self.pause = True
        return




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



    def setup_controls(self):
        """Configuration des controles communs"""
        self.chronon_label = tk.Label(self.root, text="Chronon: 1")
        self.chronon_label.pack(pady=10)

        self.pause_button = tk.Button(self.root, text="Pause", command=self.toggle_pause)
        self.pause = False
        self.pause_button.pack(pady=10)

        btn_frame = tk.Frame(self.root)  # conteneur pour les boutons
        btn_frame.pack(pady=10)

        stop_btn = tk.Button(btn_frame, text="Arrêter", command=self.stop_simulation, bg="red", fg="black")
        stop_btn.pack(side="left", padx=10, pady=5)

        restart_btn = tk.Button(btn_frame, text="Relancer", command=self.restart_simulation, bg="green", fg="black")
        restart_btn.pack(side="left", padx=10, pady=5)

    def toggle_pause(self):
        """
        Toggle the pause state of the simulation.
        """
        self.pause = not self.pause
        new_label = "Play" if self.pause else "Pause"
        self.pause_button.config(text=new_label)


    def restart_simulation(self):
        """Réinitialise la planète et redessine"""
        self.canvas.delete("all")
        self.simulation.restart()
        if hasattr(self, 'draw'):
            self.draw()


    def stop_simulation(self):
        """Ferme la fenêtre et enregistre l'arrêt manuel"""
        nb_tuna, nb_shark = self.planet.count_fish()
        self.history.log(
            self.planet.chronon, 
            "Arrêt manuel par l'utilisateur",
            nb_tuna,
            nb_shark
        )
        self.root.destroy()

    def run(self):
        """Lance la simulation"""
        if hasattr(self, 'draw'):
            self.draw()

        self.simulation.start()
        self.root.mainloop()