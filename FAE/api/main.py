import os
import sys

# Add the parent directory to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

from fastapi import FastAPI
from starlette.responses import JSONResponse

from predictor.predict import ModelPredictor
from api.models.models import Fire

app = FastAPI()

@app.get('/', status_code=200)
async def healthcheck():
    return 'FAE classifier is all ready to go!'

@app.post('/predict')
def extract_name(fire_features: Fire):
    predictor = ModelPredictor('C:/Users/rbernal/Documents/GitHub/Proyecto Final/ProyectoFinal/FAE/models/logistic_regression_output.pkl')
    X = [fire_features.SIZE,
         fire_features.FUEL_lpg,
         fire_features.FUEL_kerosene,
         fire_features.FUEL_thinner,
         fire_features.DISTANCE,
         fire_features.DESIBEL,
         fire_features.AIRFLOW,
         fire_features.FREQUENCY]
    prediction = predictor.predict([X])
    return JSONResponse(f"Resultado predicción: {prediction}")
