import joblib

from app.core.config import settings
from app.models.threshold_classifier import ThresholdClassifier  # important pour joblib


def load_model():
    model = joblib.load(settings.MODEL_PATH)
    return model