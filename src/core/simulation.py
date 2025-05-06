from src.core.planet import Planet
import tkinter as tk
from src.core.config import NB_TUNA, NB_SHARK



class Simulation:
    """
    deroulement de la simulation
    """
    def __init__(self, planet: Planet):
        self.planet: Planet = planet
        self.root = None
        self.canvas = None
        self.chronon = 0
        self.pause = False

    def setup_controls(self):
        """:cvarConfiguration des controles communs"""
        self.chronon_label = tk.Label(self.root, text="Chronon: 1", bg="lightblue", fg="black")
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

    def run(self):
        """Lance la simulation"""
        if hasattr(self, 'draw'):
            self.draw()
        self.root.mainloop()

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
        self.planet.initialize(NB_TUNA, NB_SHARK)
        self.planet.chronon = 1
        if hasattr(self, 'draw'):
            self.draw()

    def _cycle(self):
        """
        deroulement du cycle de la simulation en cours
        :return:
        """
        pass

    def stop_simulation(self):
        """Ferme la fenêtre"""
        self.root.destroy()

