import json 
import pandas as pd

def transformar_dados_clima(cidade_formatada):
    caminho_leitura = f'data/raw/clima_{cidade_formatada}.json'

    with open(caminho_leitura, 'r', encoding="utf-8") as file:
        dados = json.load(file)

        cidade = dados["name"]
        temperatura = dados["main"]["temp"]
        umidade = dados["main"]["humidity"]
        condicao = dados["weather"][0]["description"]

    dados_limpos = {
        "Cidade": cidade,
        "Temperatura": temperatura,
        "Umidade": umidade,
        "Condicao" : condicao
    }

    df = pd.DataFrame([dados_limpos])

    caminho_salvamento = "data/processed/relatorio_clima.csv"

    df.to_csv(caminho_salvamento, index=False, encoding='utf-8')

    print(f"[TRANSFORM] Tabela criada e salva em CSV na pasta: {caminho_salvamento}")
    
    return dados_limpos
