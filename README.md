# 🌊 Wa-Tor — Simulation de Monde Toroïdal

**Wa-Tor** est une simulation de vie marine inspirée du modèle écologique de l’univers toroïdal, dans lequel des thons (`Tuna`) et des requins (`Shark`) interagissent dans un environnement clos. Chaque entité suit un cycle de vie défini avec des comportements propres (déplacement, reproduction, prédation). L’objectif est de visualiser l’évolution d’un écosystème simple dans un monde sans bords (toroïdal).

---

## 📁 Architecture du projet

```

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
│      ├── __init__.py
│      ├── planet.py      # Classe Planète (grille, toroïdalité)
│      ├── simulation.py  # Classe Simulation (déroulement de la simulation)
│      ├── fish.py        # Classe abstraite Fish
│      ├── tuna.py        # Classe Tuna (thon)
│      ├── shark.py       # Classe Shark (requin)
│      └── config.py      # Paramètres globaux
│   
│──ui/                # Interface graphique
│   ├── __init__.py
│   ├── screen.py      # Interface Tkinter (affichage, boutons)
│   └── assets/        # Images utilisées par l'interface
│          ├── __init__.py
│          ├── fish.png
│          ├── sea.png
│          └── shark.png
│
└── tests/                 # Tests unitaires
    ├── __init__.py
    ├── test_position.py
    └── ...

```

---

## 🚀 Lancer la simulation

### 🧱 Préparer l’environnement (crée un environnement virtuel et le configure) :
```bash
make prepare
```

### 📦 Installer les dépendances :
```bash
make install
```

### ▶️ Exécuter la simulation :
```bash
make run
```

---

## 🧪 Qualité et analyse du code

### Formatter automatiquement le code :
```bash
make fix
```

### Analyser le code (linting / conventions) :
```bash
make analyse
```

---

## ✅ Fonctionnalités principales

- 🌍Monde toroïdal (les entités sortent d’un côté et réapparaissent de l’autre).
- 🐟Déplacement autonome des entités (avec priorités différentes selon l’espèce).
- 🦈Prédation : les requins chassent les thons s’ils sont à proximité.
- ⏱ Système de chronons pour gérer le temps dans la simulation.
- 🎨Interface graphique avec bouton Pause/Play et Relancer.
- 🐣Reproduction des entités après un certain nombre de chronons.
- ⚡️Gestion de l’énergie des requins (meurent s’ils ne mangent pas).
- 💾Export ou sauvegarde de l’état de la simulation.
- 📊Statistiques d’évolution (nombre de thons/requins par chronon).


---

## 💡 À venir (roadmap)

- 🧪Intégration de tests unitaires.

---

## 🤝 Contribution

Les contributions sont les bienvenues ! Tu peux :
- proposer des améliorations,
- signaler des bugs,
- ajouter de nouvelles fonctionnalités.


---

## 📜 Licence

Ce projet est open-source.