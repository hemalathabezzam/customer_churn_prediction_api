from pydantic import BaseModel

class ChurnData(BaseModel):
    tenure:int
    MonthlyCharges:float
    TotalCharges:float