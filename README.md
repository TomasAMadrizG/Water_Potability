🧪 API de Predicción de Potabilidad del Agua
Esta aplicación utiliza un modelo de aprendizaje automático (RandomForestClassifier) para predecir si una muestra de agua es potable (segura para el consumo humano) o no potable, basado en 9 características químicas y físicas.
La API está construida con FastAPI y permite hacer predicciones a través de solicitudes HTTP.

📁 Estructura del proyecto
.
├── main.py                 # API con FastAPI
├── call_api.py             # Cliente para probar la API localmente
├── best_RFC.pkl            # Modelo entrenado
├── categories_ohe.pickle   # Columnas utilizadas en el modelo
├── requirements.txt        # Dependencias del proyecto
├── README.md               # Este archivo

🧠 Ejemplo de predicción
Desde /docs o vía código (ver call_api.py), podés enviar un JSON como:
{
  "ph": 7.0,
  "Hardness": 150.0,
  "Solids": 20000.0,
  "Chloramines": 7.5,
  "Sulfate": 300.0,
  "Conductivity": 450.0,
  "Organic_carbon": 10.0,
  "Trihalomethanes": 80.0,
  "Turbidity": 3.0
}
La respuesta será algo como:
{
  "potability_prediction": 1,
  "meaning": "Potable"
}
🧪 Evaluación del Modelo
Modelo: RandomForestClassifier
Validación cruzada: 6-fold CV
Métrica principal: AUC-ROC
AUC promedio: ~0.65 (moderada capacidad predictiva)

📌 Notas
El modelo fue entrenado con el dataset de Water Potability
Se utilizó one-hot encoding y tratamiento de valores nulos
La API está lista para ser desplegada en servicios como Render, Railway, Heroku o Docker

🧑‍💻 Autor
Desarrollado por Tomás Madriz

