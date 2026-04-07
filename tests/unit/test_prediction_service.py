import numpy as np

from app.services.prediction_service import PredictionService
from app.schemas.prediction_input import PredictionInput


class FakeModel:
    def predict(self, df):
        return [1]

    def predict_proba(self, df):
        return np.array([[0.2, 0.8]])


def test_prediction_service_predict_returns_valid_output():
    service = PredictionService(model=FakeModel())

    payload = PredictionInput(
        age=35,
        revenu_mensuel=3200,
        nombre_experiences_precedentes=2,
        annees_dans_l_entreprise=5,
        annees_dans_le_poste_actuel=3,
        satisfaction_employee_environnement=3,
        satisfaction_employee_nature_travail=4,
        satisfaction_employee_equipe=4,
        satisfaction_employee_equilibre_pro_perso=3,
        note_evaluation_actuelle=3,
        augmentation_salaire_precedente_pct=10,
        distance_domicile_travail=12,
        niveau_education=3,
        annees_depuis_la_derniere_promotion=1,
        annes_sous_responsable_actuel=2,
        annee_experience_avant_entreprise=4,
        evolution_note=1,
        utilisation_pee=1,
        mobilite_interne=0,
        a_suivi_formation=1,
        heures_supplementaires=0,
        genre="M",
        statut_marital="Marié(e)",
        departement="Consulting",
        poste="Consultant",
        domaine_etude="Autre",
        frequence_deplacement="Frequent",
    )

    result = service.predict(payload)

    assert "prediction" in result
    assert "probability" in result
    assert result["prediction"] == 1
    assert result["probability"] == 0.8