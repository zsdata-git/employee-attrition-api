import pandas as pd

from app.core.model_loader import load_model
from app.db.models import EmployeeRecord, PredictionRecord
from app.db.session import SessionLocal
from app.schemas.prediction_input import PredictionInput


class PredictionService:
    def __init__(self, model=None):
        self.model = model

    def _get_model(self):
        if self.model is None:
            self.model = load_model()
        return self.model

    def predict(self, payload: PredictionInput) -> dict:
        model = self._get_model()
        input_dict = payload.model_dump()
        input_df = pd.DataFrame([input_dict])

        prediction = int(model.predict(input_df)[0])
        probability = float(model.predict_proba(input_df)[0, 1])

        db = SessionLocal() #ouvre une connexion à la base

        try:
            record = PredictionRecord(
                input_data=input_dict,
                prediction=prediction,
                probability=probability,
            ) #prepare une ligne à inserer dans la table predictions

            #enregistre vraiment cette ligne dans PostgreSQL : 
            db.add(record)
            db.commit() 

        except Exception:
            db.rollback()
            raise

        finally:
            db.close() #ferme proprement la connexion

          

        return {
            "prediction": prediction,
            "probability": probability,
        }
    

    def predict_by_employee_id(self, employee_id: int) -> dict:
        model = self._get_model()
        db = SessionLocal()

        try:
            employee = db.query(EmployeeRecord).filter(EmployeeRecord.id == employee_id).first()

            if employee is None:
                raise ValueError(f"Employee with id {employee_id} not found.")

            input_dict = {
                "age": employee.age,
                "genre": employee.genre,
                "revenu_mensuel": employee.revenu_mensuel,
                "statut_marital": employee.statut_marital,
                "departement": employee.departement,
                "poste": employee.poste,
                "nombre_experiences_precedentes": employee.nombre_experiences_precedentes,
                "annees_dans_l_entreprise": employee.annees_dans_l_entreprise,
                "annees_dans_le_poste_actuel": employee.annees_dans_le_poste_actuel,
                "satisfaction_employee_environnement": employee.satisfaction_employee_environnement,
                "satisfaction_employee_nature_travail": employee.satisfaction_employee_nature_travail,
                "satisfaction_employee_equipe": employee.satisfaction_employee_equipe,
                "satisfaction_employee_equilibre_pro_perso": employee.satisfaction_employee_equilibre_pro_perso,
                "note_evaluation_actuelle": employee.note_evaluation_actuelle,
                "augmentation_salaire_precedente_pct": employee.augmentation_salaire_precedente_pct,
                "heures_supplementaires": employee.heures_supplementaires,
                "distance_domicile_travail": employee.distance_domicile_travail,
                "niveau_education": employee.niveau_education,
                "domaine_etude": employee.domaine_etude,
                "frequence_deplacement": employee.frequence_deplacement,
                "annees_depuis_la_derniere_promotion": employee.annees_depuis_la_derniere_promotion,
                "annes_sous_responsable_actuel": employee.annes_sous_responsable_actuel,
                "a_suivi_formation": employee.a_suivi_formation,
                "annee_experience_avant_entreprise": employee.annee_experience_avant_entreprise,
                "mobilite_interne": employee.mobilite_interne,
                "evolution_note": employee.evolution_note,
                "utilisation_pee": employee.utilisation_pee,
            }

            input_df = pd.DataFrame([input_dict])

            prediction = int(model.predict(input_df)[0])
            probability = float(model.predict_proba(input_df)[0, 1])

            record = PredictionRecord(
                input_data=input_dict,
                prediction=prediction,
                probability=probability,
            )

            db.add(record)
            db.commit()

            return {
                "prediction": prediction,
                "probability": probability,
            }

        except Exception:
            db.rollback()
            raise

        finally:
            db.close()