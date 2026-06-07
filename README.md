## Predicting Supplier Cost Volatility App

Uses a linear regression model to predict the total landed cost of shipments based on supply chain parameters including tariff rate.

### Running the app

```bash
pip install -r requirements.txt
uvicorn app:api --reload
```

- Web UI: http://localhost:8000/home — form-based interface with input validation
- Interactive API docs: http://localhost:8000/docs

### API

`POST /predict_cost` — returns a predicted landed cost.

Example request body:

```json
{
  "shipping_cost": 277.112640,
  "lead_time_days": 24,
  "defect_rate": 0.037831,
  "base_cost": 1489.444050,
  "tariff_rate": 0.000,
  "year": 2025,
  "country_origin": "India",
  "hs_code": "722490"
}
```

> Note: use straight quotes (`"`) not curly/smart quotes (`"`) when sending requests manually.

### Testing

```bash
pytest                  # unit tests
locust -f locustfile.py # load tests (app must be running)
```

### Requirements

Tested with Python 3.13.5. See `requirements.txt`.
