import pickle
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Literal
import uvicorn
from fastapi.encoders import jsonable_encoder

# Cargar el modelo
with open("best_RFC.pickle", "rb") as f:
   model = pickle.load(f)

# Cargar las columnas esperadas por el modelo
with open("categories_ohe.pickle", "rb") as f:
    ohe_tr = pickle.load(f)

# Crear la app
app = FastAPI(title="API de Predicción de Potabilidad del Agua")

# Definir el modelo de entrada con Pydantic
class WaterData(BaseModel):
    ph: float
    Hardness: float
    Solids: float
    Chloramines: float
    Sulfate: float
    Conductivity: float
    Organic_carbon: float
    Trihalomethanes: float
    Turbidity: float

# Función para procesar y predecir
def predict_water_potability(input_data: dict):
    df = pd.DataFrame.from_dict([input_data])
    df_ohe = pd.get_dummies(df).reindex(columns=ohe_tr, fill_value=0)
    prediction = model.predict(df_ohe)
    return int(prediction[0])

# Endpoint de predicción
@app.get("/")
def read_root():
    return {"mensaje": "Bienvenido a la API de potabilidad"}


@app.post("/prediccion")
def predict(data: WaterData):
    input_dict = data.dict()
    resultado = predict_water_potability(input_dict)
    return {
        "potability_prediction": resultado,
        "meaning": "Potable" if resultado == 1 else "No potable"
    }

# Si ejecutás directamente el archivo
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
