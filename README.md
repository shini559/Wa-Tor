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
│   │   ├── planet.py      # Classe Planete (grille, toroïdalité, gestion globale)
│   │   ├── entity.py      # Classe de base Entity (poisson, requin)
│   │   ├── fish.py        # Classe Fish (Poisson) héritant de Entity
│   │   ├── tona.py        # Classe Shark (Thon) héritant de Fish
│   │   ├── shark.py       # Classe Shark (Requin) héritant de Fish
│   │   └── config.py      # Paramètres globaux (taille, temps de reproduction, etc.)
│   │
│   ├── utils/             # Fonctions utilitaires (ex: calcul voisinage, affichage)
│   │   ├── __init__.py
│   │   └── visualizer.py  # (optionnel) Affichage texte ou graphique de la simulation
│
└── tests/                 # Tests unitaires
    ├── __init__.py
    ├── test_planet.py
    ├── test_fish.py
    ├── test_shark.py
    └── test_utils.py
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
