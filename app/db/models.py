from datetime import datetime

from sqlalchemy import DateTime, Float, Integer, JSON, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class PredictionRecord(Base):
    __tablename__ = "predictions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    input_data: Mapped[dict] = mapped_column(JSON, nullable=False)
    prediction: Mapped[int] = mapped_column(Integer, nullable=False)
    probability: Mapped[float] = mapped_column(Float, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


class EmployeeRecord(Base):
    __tablename__ = "employees"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    age: Mapped[float] = mapped_column(Float)
    genre: Mapped[str] = mapped_column(String(50))
    revenu_mensuel: Mapped[float] = mapped_column(Float)
    statut_marital: Mapped[str] = mapped_column(String(50))
    departement: Mapped[str] = mapped_column(String(100))
    poste: Mapped[str] = mapped_column(String(100))
    nombre_experiences_precedentes: Mapped[float] = mapped_column(Float)
    annees_dans_l_entreprise: Mapped[float] = mapped_column(Float)
    annees_dans_le_poste_actuel: Mapped[float] = mapped_column(Float)
    satisfaction_employee_environnement: Mapped[float] = mapped_column(Float)
    satisfaction_employee_nature_travail: Mapped[float] = mapped_column(Float)
    satisfaction_employee_equipe: Mapped[float] = mapped_column(Float)
    satisfaction_employee_equilibre_pro_perso: Mapped[float] = mapped_column(Float)
    note_evaluation_actuelle: Mapped[float] = mapped_column(Float)
    augmentation_salaire_precedente_pct: Mapped[float] = mapped_column(Float)
    heures_supplementaires: Mapped[int] = mapped_column(Integer)
    a_quitte_l_entreprise: Mapped[int] = mapped_column(Integer)
    distance_domicile_travail: Mapped[float] = mapped_column(Float)
    niveau_education: Mapped[float] = mapped_column(Float)
    domaine_etude: Mapped[str] = mapped_column(String(100))
    frequence_deplacement: Mapped[str] = mapped_column(String(50))
    annees_depuis_la_derniere_promotion: Mapped[float] = mapped_column(Float)
    annes_sous_responsable_actuel: Mapped[float] = mapped_column(Float)
    a_suivi_formation: Mapped[int] = mapped_column(Integer)
    annee_experience_avant_entreprise: Mapped[float] = mapped_column(Float)
    mobilite_interne: Mapped[int] = mapped_column(Integer)
    evolution_note: Mapped[float] = mapped_column(Float)
    utilisation_pee: Mapped[int] = mapped_column(Integer)