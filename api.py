from fastapi import FastAPI
import pandas as pd
from main import ChurnData
import joblib

app= FastAPI()

model= joblib.load('customer_churn_api.pkl')

@app.get('/')
def home():
    return {'message':'Customer Churn API Running'}

@app.get('/Welcome')
def get_name(name: str):
    return {'Welcome':f'{name}'}

@app.post('/predict')
def predict(data: ChurnData):
    input_data= pd.DataFrame([[
        data.tenure,
        data.MonthlyCharges,
        data.TotalCharges]], columns=[
            'tenure',
            'MonthlyCharges',
            'TotalCharges'])
    
    print(input_data)
    print(input_data.columns)
    pred= model.predict(input_data)
    if pred[0]==1:
        result= 'Customer Likely to Churn'
    else:
        result= 'Customer Likely to Stay'
    
    return {'Prediction': result}