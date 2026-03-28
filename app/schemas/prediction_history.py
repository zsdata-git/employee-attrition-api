from datetime import datetime

from pydantic import BaseModel


class PredictionHistoryItem(BaseModel):
    id: int
    prediction: int
    probability: float
    created_at: datetime