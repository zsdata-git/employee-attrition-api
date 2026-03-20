from pydantic import BaseModel


class PredictionOutput(BaseModel):
    prediction: int
    probability: float