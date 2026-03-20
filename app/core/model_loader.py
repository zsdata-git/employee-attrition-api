import joblib
import sys

from app.core.config import settings
from app.models.threshold_classifier import ThresholdClassifier


# Rend la classe accessible sous __main__.ThresholdClassifier
sys.modules["__main__"].ThresholdClassifier = ThresholdClassifier


def load_model():
    model = joblib.load(settings.MODEL_PATH)
    return model