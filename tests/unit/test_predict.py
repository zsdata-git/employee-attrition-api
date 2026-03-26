from fastapi.testclient import TestClient

from app.main import app
from app.services.prediction_service import PredictionService

client = TestClient(app)


def fake_predict(self, payload):
    return {
        "prediction": 0,
        "probability": 0.42,
    }


def test_predict_endpoint_returns_prediction(monkeypatch):
    monkeypatch.setattr(PredictionService, "predict", fake_predict)

    payload = {
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
        "frequence_deplacement": "Frequent",
    }

    response = client.post("/predict/", json=payload)

    assert response.status_code == 200
    data = response.json()
    assert data["prediction"] == 0
    assert data["probability"] == 0.42