import pandas as pd

from app.db.session import SessionLocal
from app.db.models import EmployeeRecord


def load_data():
    df = pd.read_csv("data/clean_employee_attrition.csv")

    db = SessionLocal()

    try:
        for _, row in df.iterrows():
            employee = EmployeeRecord(
                age=row["age"],
                genre=row["genre"],
                revenu_mensuel=row["revenu_mensuel"],
                statut_marital=row["statut_marital"],
                departement=row["departement"],
                poste=row["poste"],
                nombre_experiences_precedentes=row["nombre_experiences_precedentes"],
                annees_dans_l_entreprise=row["annees_dans_l_entreprise"],
                annees_dans_le_poste_actuel=row["annees_dans_le_poste_actuel"],
                satisfaction_employee_environnement=row["satisfaction_employee_environnement"],
                satisfaction_employee_nature_travail=row["satisfaction_employee_nature_travail"],
                satisfaction_employee_equipe=row["satisfaction_employee_equipe"],
                satisfaction_employee_equilibre_pro_perso=row["satisfaction_employee_equilibre_pro_perso"],
                note_evaluation_actuelle=row["note_evaluation_actuelle"],
                augmentation_salaire_precedente_pct=row["augmentation_salaire_precedente_pct"],
                heures_supplementaires=row["heures_supplementaires"],
                a_quitte_l_entreprise=row["a_quitte_l_entreprise"],
                distance_domicile_travail=row["distance_domicile_travail"],
                niveau_education=row["niveau_education"],
                domaine_etude=row["domaine_etude"],
                frequence_deplacement=row["frequence_deplacement"],
                annees_depuis_la_derniere_promotion=row["annees_depuis_la_derniere_promotion"],
                annes_sous_responsable_actuel=row["annes_sous_responsable_actuel"],
                a_suivi_formation=row["a_suivi_formation"],
                annee_experience_avant_entreprise=row["annee_experience_avant_entreprise"],
                mobilite_interne=row["mobilite_interne"],
                evolution_note=row["evolution_note"],
                utilisation_pee=row["utilisation_pee"],
            )

            db.add(employee)

        db.commit()
        print("Dataset loaded successfully.")

    except Exception as e:
        db.rollback()
        print("Error:", e)

    finally:
        db.close()


if __name__ == "__main__":
    load_data()