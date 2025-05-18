# 🧪 API de Predicción de Potabilidad del Agua

Esta aplicación utiliza un modelo de aprendizaje automático (`RandomForestClassifier`) para predecir si una muestra de agua es **potable** o **no potable**, basado en 9 características químicas y físicas.  
La API está construida con **FastAPI** y permite hacer predicciones mediante solicitudes HTTP.

---

## 📁 Estructura del proyecto
```bash
.
├── main.py # API con FastAPI
├── call_api.py # Cliente para probar la API localmente
├── best_RFC.pkl # Modelo entrenado
├── categories_ohe.pickle # Columnas utilizadas en el modelo
├── requirements.txt # Dependencias del proyecto
└── README.md # Este archivo
```

---

## ⚙️ Requisitos

- Python 3.8 o superior  
- pip  
- Entorno virtual (opcional)

---

## 🚀 Instalación y ejecución

```bash
git clone https://github.com/TomasAMadrizG/Water_Potability.git
cd tu-repo
pip install -r requirements.txt
uvicorn main:app --reload
```

Accede a la documentación interactiva en: [http://localhost:8000/docs](http://localhost:8000/docs)

#📥 Ejemplo de predicción
Podés enviar un JSON como este:
```bash
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
```
#📤 Respuesta esperada:
```bash
{
  "potability_prediction": 1,
   "meaning": "Potable"
}
```
# 📊 Evaluación del Modelo
### 🔍 Modelo: RandomForestClassifier

# 🔁 Validación cruzada: 6-fold CV

# 📈 Métrica: AUC-ROC

# ✅ AUC promedio: ~0.65 (capacidad predictiva moderada)

# 📝 Notas

Tratamiento: One-hot encoding, manejo de valores nulos.

