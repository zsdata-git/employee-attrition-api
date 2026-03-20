import pandas as pd

from app.core.model_loader import load_model
from app.schemas.prediction_input import PredictionInput


class PredictionService:
    def __init__(self):
        self.model = load_model()

    def predict(self, payload: PredictionInput) -> dict:
        input_dict = payload.model_dump()
        input_df = pd.DataFrame([input_dict])

        prediction = int(self.model.predict(input_df)[0])
        probability = float(self.model.predict_proba(input_df)[0, 1])

        return {
            "prediction": prediction,
            "probability": probability,
        }