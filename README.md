# Wa-Tor
```
# Architecture du projet
Wa-Tor/
│
├── README.md              # Explication du projet, comment l'utiliser, etc.
├── requirements.txt       # Dépendances éventuelles
├── main.py                # Script principal pour démarrer la simulation
├── makefile.py            # Commandes utiles (ex: make run)
│
├── src/                   # Code source
│   ├── __init__.py
│   │
│   ├── core/              # Logique et comportements de la simulation
│   │   ├── __init__.py
│   │   ├── planet.py      # Classe Planète (grille, toroïdalité)
│   │   ├── simulation.py  # Classe Simulation (déroulement de la simulation)
│   │   ├── fish.py        # Classe abstraite Fish
│   │   ├── tuna.py        # Classe Tuna (thon)
│   │   ├── shark.py       # Classe Shark (requin)
│   │   └── config.py      # Paramètres globaux
│   │
│   └── ui/                # Interface graphique
│       ├── __init__.py
│       ├── screen.py      # Interface Tkinter (affichage, boutons)
│       └── assets/        # Images utilisées par l'interface
│           ├── __init__.py
│           ├── fish.png
│           ├── sea.png
│           └── shark.png
│
└── tests/                 # Tests unitaires
    ├── __init__.py
    ├── test_position.py
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
