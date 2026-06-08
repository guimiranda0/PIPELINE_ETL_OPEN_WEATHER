import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

def extrair_dados_clima(cidade):
    url = "https://api.openweathermap.org/data/2.5/weather"
    
    # Conferindo se o Python vai passar o valor da variável cidade sem aspas na chave
    parametros = {
        "q": cidade,
        "appid": API_KEY,
        "units": "metric",
        "lang": "pt_br"
    }
    
    print(f"Buscando dados de clima para: {cidade}...")
    
    resposta = requests.get(url, params=parametros)
    
    if resposta.status_code == 200:
        return resposta.json()
    else:
        print(f"Erro na requisição código de status: {resposta.status_code}")
        return None