# Customer Churn Prediction API

## Objective
Predict customer churn using Machine Learning.

## Tech Stack
- FastAPI
- Scikit-learn
- Pandas
- Joblib

## Features Used
- tenure
- MonthlyCharges
- TotalCharges

## Run API

```bash
uvicorn app:app --reload
```

## Swagger UI

```text
http://127.0.0.1:8000/docs
```

## Sample Input

```json
{
  "tenure": 12,
  "MonthlyCharges": 75.5,
  "TotalCharges": 900.0
}
```