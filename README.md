# Wa-Tor
```
# Architecture du projet
Wa-Tor/
│
├── README.md              # Explication du projet, comment l'utiliser, etc.
├── requirements.txt       # Dépendances éventuelles
├── main.py                # Script principal pour démarrer la simulation
├── makefile.py            # Script application(exemple : make run pour executer l'application)
│
├── src/                   # Code source
│   ├── __init__.py
│   │
│   ├── core/              # Comportements et règles de la simulation
│   │   ├── __init__.py
│   │   ├── position.py    # Classe Position (x, y)
│   │   ├── planet.py      # Classe Planete (grille, toroïdalité, gestion globale)
│   │   ├── simulation.py  # Classe Simulation (deroulement de la simulation)
│   │   ├── fish.py        # Classe Fish (class abstract)
│   │   ├── tuna.py        # Classe Tuna (Thon) héritant de Fish
│   │   ├── shark.py       # Classe Shark (Requin) héritant de Fish
│   │   └── config.py      # Paramètres globaux (taille, temps de reproduction, etc.)
│
└── tests/                 # Tests unitaires
    ├── __init__.py
    ├── test_position.py   # Test class Position
    └── ...
```

# Developement

## pour installer l'environement

``` bash
make prepare
```

## pour installer les dependence
``` bash
make install
```

## pour executer 
``` bash
make run
```

## analyse la qualité du code
``` bash
make fix
make analyse
```
