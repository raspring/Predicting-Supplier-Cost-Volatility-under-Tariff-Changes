from fastapi import FastAPI
import joblib
import numpy as np
from pydantic import BaseModel, PositiveFloat, NonNegativeFloat
import pandas as pd

ML_MODEL = joblib.load("./tariff_model.joblib")

# FastAPI.
api_title = "PredictingSupplierCostVolatilityApp"
api_description = """
PredictingSupplierCostVolatilityApp allows you to predict the total landed cost for shipments with various parameters including the tariff rate.
"""
api = FastAPI(title=api_title, description=api_description)

class CostFeatures(BaseModel):
    shipping_cost: PositiveFloat
    lead_time_days: int
    defect_rate: PositiveFloat
    base_cost: PositiveFloat
    tariff_rate: NonNegativeFloat
    year: int
    country_origin: str
    hs_code: str


class Prediction(BaseModel):
    predicted_cost: float

def predict(features: dict) -> float:
    """
    Generate prediction using the trained ML model.
    """

    X = pd.DataFrame([features])

    return float(ML_MODEL.predict(X)[0])


@api.post("/predict_cost", response_model=Prediction)
def predict_cost(data: CostFeatures) -> Prediction:
    """
    Predicts the landed cost of the shipment based on the input parameters.
    """
    #prediction = predict(data.dict())
    prediction = predict(data.model_dump())
    return Prediction(predicted_cost=prediction)
