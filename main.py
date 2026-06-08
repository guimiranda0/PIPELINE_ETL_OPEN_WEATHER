import json
from src.extract import extrair_dados_clima
from src.transform import transformar_dados_clima
from src.database import enviar_para_s3

print("--- INICIANDO PIPELINE DE ETL EM CLOUD (AWS) ---")

cidade_escolhida = input("Digite o nome da cidade que deseja consultar o clima: ").strip()

if not cidade_escolhida:
    print("Erro você precisa digitar uma cidade")
    exit()

cidade_formatada = cidade_escolhida.lower().replace(" ", "_")

dados_previsao = extrair_dados_clima(cidade_escolhida)

if dados_previsao:
    caminho_arquivo_raw = f'data/raw/clima_{cidade_formatada}.json'
    caminho_s3_raw = f"raw/clima_{cidade_formatada}.json"

    with open (caminho_arquivo_raw, 'w', encoding="utf-8") as arquivo:
        json.dump(dados_previsao,arquivo,indent=4,ensure_ascii=False)

    print(f"[EXTRACT] Dados brutos salvos com sucesso!")

    enviar_para_s3(
        caminho_local= caminho_arquivo_raw,
        caminho_s3 = caminho_s3_raw
    )

    print("\n[TRANSFORM] Iniciando a transformação dos dados...")

    dados_filtrados = transformar_dados_clima(cidade_formatada)

    caminho_local_processed = f"data/processed/relatorio_clima_{cidade_formatada}.csv"
    caminho_s3_processed = f"processed/relatorio_clima_{cidade_formatada}.csv"

    #Para ajustar o nome do arquivo localmente antes de mandar para a nuvem
    import os
    if os.path.exists("data/processed/relatorio_clima.csv"):
        os.rename("data/processed/relatorio_clima.csv", caminho_local_processed)
    
    enviar_para_s3(
        caminho_local= caminho_local_processed,
        caminho_s3 = caminho_s3_processed
    )

    print("\n--- PIPELINE CONCLUÍDO COM SUCESSO EM PRODUÇÃO ---")

else:
    print("Falha no pipeline: Não foi possível extrair os dados da API.")

