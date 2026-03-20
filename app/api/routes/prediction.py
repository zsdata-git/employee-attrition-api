from fastapi import APIRouter, HTTPException

from app.schemas.prediction_input import PredictionInput
from app.schemas.prediction_output import PredictionOutput
from app.services.prediction_service import PredictionService

router = APIRouter(prefix="/predict", tags=["Prediction"])

prediction_service = PredictionService()


@router.post("/", response_model=PredictionOutput, summary="Predict employee attrition")
def predict_attrition(payload: PredictionInput):
    try:
        return prediction_service.predict(payload)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")