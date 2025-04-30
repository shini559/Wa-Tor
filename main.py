from src.core.planet import Planet
from ui.screen import GridDisplay
from src.core.config import NB_TUNA, NB_SHARK

# Création et initialisation de la planète
planet = Planet()
planet.initialize(NB_TUNA, NB_SHARK)

#planet.display()

app = GridDisplay(planet)
app.run()
