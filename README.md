Run successfully with python version 3.13.5 and the requirements located in this repository

This will use a linear regression to predict the total landed cost of various shipments based on paramters including the tariff rate.

fyi api is a bit finnicky on the input data types - I got hung up on plain text " vs hypertext " for like 30 min.  Here is example input to the model

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
