import pandas as pd

from app.core.model_loader import load_model
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

        return {
            "prediction": prediction,
            "probability": probability,
        }