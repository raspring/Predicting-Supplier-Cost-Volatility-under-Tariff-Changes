import random
from locust import HttpUser, constant_pacing, task

class PredictionUser(HttpUser):
    host = "http://localhost:8000"
    wait_time = constant_pacing(1)
    @task
    def predict_cost_test(self):
        self.client.post(
            "/predict_cost",
            json = { "shipping_cost": 277.112640, 
                "lead_time_days": 24, 
                "defect_rate": 0.037831, 
                "base_cost": 1000.0 + random.random() * 4000.0, 
                "tariff_rate": 0.000, 
                "year": 2025, 
                "country_origin": 
                "India", 
                "hs_code": "722490" }
        )
