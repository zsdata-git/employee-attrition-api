# Employee Attrition API

## Présentation du projet
Ce projet a pour objectif de déployer en production un modèle de machine learning capable de prédire la probabilité d’attrition d’un employé.

Le modèle a été entraîné au préalable dans un projet distinct. Ce dépôt correspond à la partie industrialisation et mise en production du modèle, avec une architecture de projet propre, une API, une gestion des dépendances, des tests, une base de données et une documentation.

## Objectifs
- exposer le modèle via une API FastAPI ;
- rendre l’inférence fiable, testable et documentée ;
- intégrer une base de données PostgreSQL ;
- mettre en place des tests unitaires et fonctionnels ;
- préparer un pipeline CI/CD ;
- documenter le projet et son utilisation.

## Stack technique
- Python
- FastAPI
- Pydantic
- SQLAlchemy
- PostgreSQL
- scikit-learn
- joblib
- pytest
- pytest-cov
- Git / GitHub

## Structure du projet
```text
employee-attrition-api/
├── app/                  # code source principal de l'application
│   ├── api/              # routes et endpoints API
│   ├── core/             # configuration centrale de l’application
│   ├── db/               # connexion et logique base de données
│   ├── models/           # modèles SQLAlchemy
│   ├── schemas/          # schémas Pydantic
│   ├── services/         # logique métier
│   └── main.py           # point d’entrée FastAPI
├── artifacts/
│   └── model/            # artefacts du modèle ML sauvegardé
├── tests/
│   ├── unit/             # tests unitaires
│   └── functional/       # tests fonctionnels
├── docs/                 # documentation du projet
├── notebooks/            # notebooks éventuels d’exploration
├── scripts/              # scripts utilitaires
├── .github/workflows/    # pipelines CI/CD
├── .gitignore
├── pyproject.toml
├── requirements.txt
├── uv.lock
└── README.md
```

## Installation du projet 

1. Cloner le dépôt
``` bash
git clone <url-du-repository>
cd employee-attrition-api
```

2. Créer et activer l'environnement virtuel 
``` bash
uv venv
.venv\Scripts\activate
```

3. Installer les dépendances 
``` bash 
uv sync
```

## Lancer l'application 

``` bash 
uv run uvicorn app.main:app --reload
```

puis ouvrir dans l'explorateur : 

http://127.0.0.1:8000
http://127.0.0.1:8000/docs

## Tests 
Les tests seront ajoutés dans le dossier `tests/` et exécutés avec `pytest`.

Exemple : 
``` Bash 
uv run pytest
```

## Gestion de version 
Le projet utilise Git avec : 
- une branche principale `main`;
- des branches dédiées par fonctionnalité;
- des commits explicites;
- des tags pour la gestion des versions. 

## Etat d'avancement 
Ce dépôt correspond à la phase d'initialisation et de structuration du projet de déploiement du modèle. 
Les prochaines étapes incluront : 
- le développement de l'API de prédiction; 
- l'intégration de la base PostgreSQL;
- les tests;
- la documentation; 
- la CI/CD;
- le déploiement. 

## Auteur 
projet réalisé par Hayette. 