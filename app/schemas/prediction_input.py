from pydantic import BaseModel


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

    # CATEGORICAL ORD
    frequence_deplacement: str