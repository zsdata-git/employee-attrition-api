import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    APP_ENV: str = os.getenv("APP_ENV", "development")
    APP_NAME: str = os.getenv("APP_NAME", "Employee Attrition API")
    APP_VERSION: str = os.getenv("APP_VERSION", "0.1.0")

    HOST: str = os.getenv("HOST", "127.0.0.1")
    PORT: int = int(os.getenv("PORT", "8000"))

    MODEL_PATH: str = os.getenv("MODEL_PATH", "artifacts/model/attrition_threshold_model.joblib")
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "sqlite:///./app.db",
    )

    HF_SPACE_REPO: str = os.getenv("HF_SPACE_REPO", "zsdata-git/employee-attrition-api")


settings = Settings()