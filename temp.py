from fastapi.testclient import TestClient
from app import api, Prediction
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),              # logs to console
        logging.FileHandler("pytest_logs.log")  # logs to file
    ]
)
logger = logging.getLogger(__name__)

client = TestClient(api)

test_body_valid = {
        "shipping_cost": 277.112640,
        "lead_time_days": 24,
        "defect_rate": 0.037831,
        "base_cost": 1489.444050,
        "tariff_rate": 0.000,
        "year": 2025,
        "country_origin": "India",
        "hs_code": "722490"
    }

def test_predict_cost(mocker):
    mocker.patch("app.predict", return_value=1700.00)
    response = client.post("/predict_cost", json=test_body_valid)
    assert response.status_code == 200
    assert response.json() == Prediction(predicted_cost=1700.0).model_dump()

def test_missing_field():
    invalid_payload = test_body_valid.copy()
    del invalid_payload["shipping_cost"]
    response = client.post("/predict_cost", json=invalid_payload)
    assert response.status_code == 422

def test_negative_shipping_cost():
    invalid_payload = test_body_valid.copy()
    invalid_payload["shipping_cost"] = -10.0
    response = client.post("/predict_cost", json=invalid_payload)
    assert response.status_code == 422

def test_negative_tariff_rate():
    invalid_payload = test_body_valid.copy()
    invalid_payload["tariff_rate"] = -0.01
    response = client.post("/predict_cost", json=invalid_payload)
    assert response.status_code == 422

def test_invalid_datatype_for_floats():
    payload = test_body_valid.copy()
    payload["shipping_cost"] = 'test'
    response = client.post("/predict_cost", json=payload)
    assert response.status_code == 422

def test_invalid_datatype_for_floats_v2():
    print("Starting test_invalid_datatype_for_floats_v2")
    payload = test_body_valid.copy()
    payload["shipping_cost"] = 'test'
    response = client.post("/predict_cost", json=payload)
    assert response.status_code == 422

def test_invalid_datatype_for_floats_v3():
    logger.info("Starting test_invalid_datatype_for_floats")
    payload = test_body_valid.copy()
    payload["shipping_cost"] = 'test'
    response = client.post("/predict_cost", json=payload)
    assert response.status_code == 422
    logger.info("test_invalid_datatype_for_floats correctly returned 422")