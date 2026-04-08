---
title: Employee Attrition API
emoji: 📊
colorFrom: blue
colorTo: indigo
sdk: docker
app_port: 7860
pinned: false
---


# Employee Attrition API

## Présentation du projet

Ce projet a pour objectif de déployer une API de prédiction du risque d’attrition des employés à partir d’un modèle de machine learning déjà entraîné en amont.

L’API permet :
- de prédire le risque d’attrition à partir d’un payload JSON ;
- de prédire le risque d’attrition à partir de l’identifiant d’un employé stocké en base ;
- de conserver un historique des prédictions ;
- de consulter l’état de santé de l’application.

Le projet a été industrialisé avec une architecture claire, une validation des données, des tests automatisés, une base de données et un déploiement sur Hugging Face Spaces.

---

## Objectifs

- exposer le modèle via une API FastAPI ;
- rendre l’inférence fiable, testable et documentée ;
- intégrer une base de données pour stocker les employés et l’historique des prédictions ;
- mettre en place des tests unitaires et fonctionnels ;
- mesurer la couverture des tests avec `pytest-cov` ;
- permettre un déploiement local et sur Hugging Face.

---

## Fonctionnalités

- `GET /` : vérifier que l’API est en cours d’exécution ;
- `GET /health` : vérifier l’état de santé de l’application ;
- `POST /predict/` : lancer une prédiction à partir d’un JSON ;
- `GET /predict/predictions` : récupérer l’historique des prédictions ;
- `POST /predict/by-id/{employee_id}` : lancer une prédiction à partir d’un employé présent en base.

---

## Stack technique

- Python
- FastAPI
- Pydantic
- SQLAlchemy
- PostgreSQL
- SQLite
- scikit-learn
- joblib
- pytest
- pytest-cov
- Git / GitHub
- GitHub Actions
- Docker
- Hugging Face Spaces

---


## Architecture du projet

```text
employee-attrition-api/
├── app/
│   ├── api/
│   │   └── routes/
│   │       └── prediction.py              # endpoints API
│   ├── core/
│   │   ├── config.py                      # variables d’environnement et configuration
│   │   └── model_loader.py                # chargement du modèle ML
│   ├── db/
│   │   ├── base.py                        # base SQLAlchemy
│   │   ├── models.py                      # tables SQLAlchemy
│   │   └── session.py                     # connexion base de données
│   ├── models/
│   │   └── threshold_classifier.py        # logique liée au classifieur / seuil
│   ├── schemas/
│   │   ├── prediction_history.py          # schéma de l’historique des prédictions
│   │   ├── prediction_input.py            # schéma d’entrée
│   │   └── prediction_output.py           # schéma de sortie
│   ├── services/
│   │   └── prediction_service.py          # logique métier de prédiction
│   └── main.py                            # point d’entrée FastAPI
├── artifacts/
│   └── model/
│       └── attrition_threshold_model.joblib   # modèle sauvegardé
├── data/
│   └── clean_employee_attrition.csv       # dataset nettoyé
├── docs/
│   └── database_schema.md                 # schéma BDD
├── scripts/
│   ├── create_db.py                       # création des tables
│   └── load_dataset.py                    # chargement du dataset
├── tests/
│   ├── functional/
│   └── unit/
│       ├── test_health.py
│       ├── test_predict.py
│       └── test_prediction_service.py
├── .github/
│   └── workflows/
│       ├── ci.yml                         # pipeline CI
│       └── deploy.yml                     # déploiement Hugging Face
├── Dockerfile
├── pyproject.toml
├── requirements.txt
├── uv.lock
└── README.md
```
---

## Base de données 

Le projet utilise deux configurations selon le contexte :

### En local
+ base de données PostgreSQL
+ stockage des employés
+ stockage de l’historique des prédictions

### Sur Hugging Face Spaces
+ base de données SQLite
+ utilisée comme solution de fallback pour faciliter le déploiement
+ le dataset est automatiquement injecté au démarrage si nécessaire

-> Cette approche permet :
+ une base plus réaliste en local avec PostgreSQL ;
+ un déploiement plus simple et autonome sur Hugging Face avec SQLite.

---

## Modèle de Machine Learning & prédiction

#### Le modèle de machine learning est chargé depuis :

artifacts/model/attrition_threshold_model.joblib

#### Le service de prédiction :
+ transforme les données d’entrée en DataFrame ;
+ appelle predict() pour obtenir la classe prédite ;
+ appelle predict_proba() pour obtenir la probabilité associée ;
+ enregistre les résultats dans la table predictions.

---

## Documentation API 
La documentation interactive Swagger est disponible à l’adresse :

### En local :
http://127.0.0.1:8000/docs

### Sur Hugging Face : 
https://hayette-employee-attrition-api.hf.space/docs

---

## Exemples d'utilisation

### 1. Vérifier que l'API fonctionne 
``` bash
curl http://127.0.0.1:8000/health
```

-> réponse attendue : 
``` JSON
{
  "status": "ok",
  "environment": "development"
}
```

### 2. Prédiction via JSON 
``` bash
curl -X POST "http://127.0.0.1:8000/predict/" \
  -H "Content-Type: application/json" \
  -d '{
    "age": 35,
    "revenu_mensuel": 3200,
    "nombre_experiences_precedentes": 2,
    "annees_dans_l_entreprise": 5,
    "annees_dans_le_poste_actuel": 3,
    "satisfaction_employee_environnement": 3,
    "satisfaction_employee_nature_travail": 4,
    "satisfaction_employee_equipe": 4,
    "satisfaction_employee_equilibre_pro_perso": 3,
    "note_evaluation_actuelle": 3,
    "augmentation_salaire_precedente_pct": 10,
    "distance_domicile_travail": 12,
    "niveau_education": 3,
    "annees_depuis_la_derniere_promotion": 1,
    "annes_sous_responsable_actuel": 2,
    "annee_experience_avant_entreprise": 4,
    "evolution_note": 1,
    "utilisation_pee": 1,
    "mobilite_interne": 0,
    "a_suivi_formation": 1,
    "heures_supplementaires": 0,
    "genre": "M",
    "statut_marital": "Marié(e)",
    "departement": "Consulting",
    "poste": "Consultant",
    "domaine_etude": "Autre",
    "frequence_deplacement": "Frequent"
  }'
```

-> exemple de réponse:
```JSON
{
  "prediction": 0,
  "probability": 0.42
}
```

### 3. Prédiction par identifiant employé 
```bash
curl -X POST "http://127.0.0.1:8000/predict/by-id/5"
```

->exemple de réponse: 
```JSON
{
  "prediction": 1,
  "probability": 0.70
}
```
### 4. Historique des prédictions 
```bash
curl http://127.0.0.1:8000/predict/predictions
```
---

## Installation du projet 

1. Cloner le dépôt
``` bash
git clone https://github.com/zsdata-git/employee-attrition-api.git
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
---
## Lancer l'application en local

``` bash 
uv run uvicorn app.main:app --reload
```

puis ouvrir dans l'explorateur : 

http://127.0.0.1:8000
http://127.0.0.1:8000/docs

---
## Initialisation de la base locale 

Créer les tables : 
``` bash 
uv run python -m scripts.create_db
```

Charger le dataset :
``` bash 
uv run python -m scripts.load_dataset
```

---

## Tests 

### Lancer les tests
``` Bash 
uv run pytest
```

### Lancer la couverture 
``` Bash
uv run pytest --cov=app --cov-report=term-missing
```

Le projet contient :
+ des tests d’API (health, predict, predict/by-id) ;
+ des tests du service métier ;
+ des tests de cas d’erreur simples.

À ce stade du projet :
+ les tests unitaires et fonctionnels principaux sont en place ;
+ la couverture est mesurée avec pytest-cov ;
+ les cas les plus critiques sont couverts (health check, prédiction, erreurs de validation, prédiction par identifiant).

---

## Déploiement 
L’application est déployée sur Hugging Face Spaces avec Docker.

Le workflow de déploiement :
+ pousse le code vers le Space Hugging Face ;
+ démarre l’application dans un conteneur ;
+ utilise SQLite comme base embarquée ;
+ injecte automatiquement le dataset au démarrage si nécessaire.

---
## Maintenance et mises à jour
Pour faire évoluer le projet proprement :  
1. créer une nouvelle branche par fonctionnalité ;
2. développer et tester localement ;
3. lancer pytest et pytest-cov avant merge ;
4. merger dans main uniquement quand les tests passent ;
5. versionner les étapes importantes avec des tags Git.

---

## Auteur 
projet réalisé par Hayette. 