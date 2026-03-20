from fastapi import APIRouter

from app.schemas.prediction_input import PredictionInput
from app.schemas.prediction_output import PredictionOutput
from app.services.prediction_service import PredictionService

router = APIRouter(prefix="/predict", tags=["Prediction"])

prediction_service = PredictionService()


@router.post("/", response_model=PredictionOutput)
def predict_attrition(payload: PredictionInput):
    result = prediction_service.predict(payload)
    return result