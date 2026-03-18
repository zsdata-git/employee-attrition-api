from fastapi import FastAPI

from app.core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    description="API de prédiction du risque d'attrition des employés",
    version=settings.APP_VERSION,
)


@app.get("/")
def root():
    return {"message": f"{settings.APP_NAME} is running"}


@app.get("/health")
def health_check():
    return {"status": "ok", "environment": settings.APP_ENV}