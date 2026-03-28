from fastapi import APIRouter, HTTPException

from app.db.models import PredictionRecord
from app.db.session import SessionLocal
from app.schemas.prediction_history import PredictionHistoryItem
from app.schemas.prediction_input import PredictionInput
from app.schemas.prediction_output import PredictionOutput
from app.services.prediction_service import PredictionService

router = APIRouter(prefix="/predict", tags=["Prediction"])


@router.post("/", response_model=PredictionOutput, summary="Predict employee attrition")
def predict_attrition(payload: PredictionInput):
    try:
        prediction_service = PredictionService()
        return prediction_service.predict(payload)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")
    

@router.get("/predictions", response_model=list[PredictionHistoryItem])
def get_predictions():
    db = SessionLocal()
    try:
        records = db.query(PredictionRecord).order_by(PredictionRecord.id.desc()).all()
        return records
    finally:
        db.close()


@router.post("/by-id/{employee_id}", response_model=PredictionOutput, summary="Predict employee attrition by employee id")
def predict_attrition_by_id(employee_id: int):
    try:
        prediction_service = PredictionService()
        return prediction_service.predict_by_employee_id(employee_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction by id error: {str(e)}")