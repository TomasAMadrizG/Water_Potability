import requests

data = {
    'ph': 0,
    'Hardness': 204.890455,
    'Solids': 20791.318981,
    'Chloramines': 7.300212,
    'Sulfate': 368.516441,
    'Conductivity': 564.308654,
    'Organic_carbon': 10.379783,
    'Trihalomethanes': 86.990970,
    'Turbidity': 2.963135,
}

response = requests.post("http://127.0.0.1:8000/prediccion", json=data)
print(response.json())
