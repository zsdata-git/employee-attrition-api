from fastapi import FastAPI

app = FastAPI(
    title="Employee Attrition API",
    description="API de prédiction du risque d'attrition des employés",
    version="0.1.0"
)


@app.get("/")
def root():
    return {"message": "Employee Attrition API is running"}


@app.get("/health")
def health_check():
    return {"status": "ok"}