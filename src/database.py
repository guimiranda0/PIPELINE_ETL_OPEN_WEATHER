import os 
import boto3
from dotenv import load_dotenv

#Vai ler as credencias no arquivo .env
load_dotenv()

BUCKET_NAME = os.getenv("AWS_BUCKET_NAME")

def obter_cliente_s3():
    return boto3.client(
        "s3",
        aws_access_key_id= os.getenv("AWS_ACESS_KEY"),
        aws_secret_access_key= os.getenv("AWS_SECRET_ACESS_KEY")       
    )

def enviar_para_s3(caminho_local, caminho_s3):
    """
        Função responsável por pegar um arquivo local e fazer o upload para o Bucket da AWS

        params: caminho_local -> caminho para o arquivo físico no meu computador
        params: caminho_s3 -> caminho para onde o arquivo vai na nuvem

    """
    
    try:
        s3 = obter_cliente_s3()

        print(f"[AWS S3] Enviando {caminho_local} para s3://{BUCKET_NAME}/{caminho_s3}...")

        #Comando da AWS que faz o upload do arquivo físico 
        s3.upload_file(caminho_local, BUCKET_NAME, caminho_s3)

        print("[AWS S3] Upload concluído com sucesso!")
        return True
    
    except Exception as e:

        print(f"[AWS S3] Erro ao realizar o upload dos arquivos para o S3: {e}")
        return False



