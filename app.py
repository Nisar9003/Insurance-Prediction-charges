from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Annotated, Literal
import pickle
import pandas as pd

# Load model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

app = FastAPI()

# Enable CORS for public access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic Model
class UserInput(BaseModel):
    age: Annotated[int, Field(description="Age", examples=[30])]
    gender: Annotated[float, Field(description="0 = Male, 1 = Female", examples=[0.0])]
    bmi: Annotated[float, Field(description="BMI value", examples=[25.0])]
    children: Annotated[float, Field(description="Number of children", examples=[2.0])]
    smoker: Annotated[float, Field(description="0 = No, 1 = Yes", examples=[1.0])]
    region: Annotated[float, Field(description="0-3 region encoded", examples=[2.0])]


# API Endpoint (CLASS KE BAHAR)
@app.post("/predict")
def predict(input: UserInput):

    input_data = pd.DataFrame([input.model_dump()])
    prediction = model.predict(input_data)[0]

    return {"predicted_charges": float(prediction)}
