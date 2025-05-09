import csv
from pathlib import Path
from datetime import datetime
from src.core.config import (
    NB_TUNA, NB_SHARK,
    TUNA_REPRODUCTION_TIME, SHARK_REPRODUCTION_TIME,
    SHARK_ENERGY, SHARK_ENERGY_GAIN
)

class History:
    def __init__(self, file_path: str = "simulation_history.csv"):
        self.file_path = Path(file_path)
        self.headers = [
            "date", "heure",
            "NB_TUNA", "NB_SHARK",
            "TUNA_REPRODUCTION_TIME", "SHARK_REPRODUCTION_TIME",
            "SHARK_ENERGY", "SHARK_ENERGY_GAIN",
            "chronon_final",
            "nb_tuna_final",
            "nb_shark_final",
            "raison_arret"
        ]

        if not self.file_path.exists():
            self._write_header()

    def _write_header(self):
        with self.file_path.open("w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(self.headers)

    def log(self, chronon_final: int, raison="", nb_tuna_final=0, nb_shark_final=0):
        now = datetime.now()
        data = [
            now.strftime("%d-%m-%y"),
            now.strftime("%H:%M:%S"),
            NB_TUNA, NB_SHARK,
            TUNA_REPRODUCTION_TIME, SHARK_REPRODUCTION_TIME,
            SHARK_ENERGY, SHARK_ENERGY_GAIN,
            chronon_final,
            nb_tuna_final,
            nb_shark_final,
            raison
        ]
        with self.file_path.open("a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(data)