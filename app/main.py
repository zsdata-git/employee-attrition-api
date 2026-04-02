import pandas as pd
from fastapi import FastAPI

from app.api.routes.prediction import router as prediction_router
from app.core.config import settings
from app.db.base import Base
from app.db.models import EmployeeRecord
from app.db.session import SessionLocal, engine


def seed_employees_if_needed():
    print("🌱 Checking if seeding is needed...")

    if not settings.DATABASE_URL.startswith("sqlite"):
        print("❌ Not SQLite → seeding skipped")
        return
    print("📦 SQLite detected → seeding enabled")

    db = SessionLocal()

    try:
        existing_count = db.query(EmployeeRecord).count()
        print(f"📊 Existing employees in DB: {existing_count}")

        if existing_count > 0:
            print("✅ Data already exists → skipping seeding")
            return

        print("📂 Loading CSV...")
        df = pd.read_csv("data/clean_employee_attrition.csv", encoding="utf-8")
        print(f"✅ CSV loaded: {len(df)} rows")

        employees = []
        print("🔄 Creating Employee objects...")
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
            employees.append(employee)

        print(f"📥 Inserting {len(employees)} employees into DB...")
        db.add_all(employees)
        db.commit()
        print("🎉 SQLite employees table seeded successfully.")

    except Exception as e:
        print(f"❌ Error during seeding: {e}")
        db.rollback()
        raise

    finally:
        db.close()
        print("🔒 DB session closed")

app = FastAPI(
    title=settings.APP_NAME,
    description="API de prédiction du risque d'attrition des employés",
    version=settings.APP_VERSION,
)

print("🚀 Starting application...")
print(f"📦 Database URL: {settings.DATABASE_URL}")

Base.metadata.create_all(bind=engine)
print("✅ Database tables created")

seed_employees_if_needed()

@app.get("/")
def root():
    print("📡 Root endpoint called")
    return {"message": f"{settings.APP_NAME} is running"}


@app.get("/health")
def health_check():
    print("💚 Health check called")
    return {"status": "ok", "environment": settings.APP_ENV}


app.include_router(prediction_router)
print("🔗 Prediction router loaded")