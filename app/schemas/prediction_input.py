from pydantic import BaseModel, ConfigDict


class PredictionInput(BaseModel):
    # NUMERIC
    age: float
    revenu_mensuel: float
    nombre_experiences_precedentes: float
    annees_dans_l_entreprise: float
    annees_dans_le_poste_actuel: float
    satisfaction_employee_environnement: float
    satisfaction_employee_nature_travail: float
    satisfaction_employee_equipe: float
    satisfaction_employee_equilibre_pro_perso: float
    note_evaluation_actuelle: float
    augmentation_salaire_precedente_pct: float
    distance_domicile_travail: float
    niveau_education: float
    annees_depuis_la_derniere_promotion: float
    annes_sous_responsable_actuel: float
    annee_experience_avant_entreprise: float
    evolution_note: float

    # BINARY
    utilisation_pee: int
    mobilite_interne: int
    a_suivi_formation: int
    heures_supplementaires: int

    # CATEGORICAL
    genre: str
    statut_marital: str
    departement: str
    poste: str
    domaine_etude: str
    frequence_deplacement: str

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
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
        }
    )
