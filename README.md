# ☁️ Cloud Weather ETL Pipeline

Este é um pipeline de dados dinâmico e resiliente que realiza o processo de ETL (Extract, Transform, Load) para dados meteorológicos de qualquer cidade do mundo, integrando APIs externas e a nuvem da **Amazon Web Services (AWS)**.

## 🛠️ Arquitetura do Projeto

O pipeline foi desenhado seguindo as melhores práticas de Engenharia de Dados moderna:

1. **Extração (API):** Consome dados em tempo real da API OpenWeather.
2. **Camada Raw (Data Lake no S3):** Armazena os dados brutos estruturados em arquivos `.json` diretamente em um Bucket do **Amazon S3** (pasta `raw/`).
3. **Transformação (Pandas):** Lê o arquivo da nuvem, processa, limpa e padroniza as métricas principais utilizando Python e Pandas.
4. **Camada Processed (Data Lake no S3):** Salva o relatório analítico final em formato `.csv` de volta ao S3 (pasta `processed/`), pronto para consumo de ferramentas de BI.

## 🚀 Tecnologias Utilizadas

* **Python 3.12+**
* **uv** (Gerenciador de pacotes e ambientes virtuais ultrarrápido)
* **Pandas** (Manipulação e tratamento de dados)
* **Boto3** (SDK oficial da AWS para Python)
* **Amazon S3** (Armazenamento de objetos em nuvem)
* **OpenWeather API** (Fonte de dados)

## 🔧 Como Executar o Projeto

1. Clone o repositório:
   ```bash
   git clone [https://github.com/seu-usuario/pipeline-etl-cloud.git](https://github.com/seu-usuario/pipeline-etl-cloud.git)

2. Instale as dependências usando o `uv`:
  `uv sync`

3. Crie um arquivo .env na raiz do projeto seguindo o modelo:

  `OPENWEATHER_API_KEY=seu_token_aqui
  AWS_ACCESS_KEY_ID=sua_chave_aqui
  AWS_SECRET_ACCESS_KEY=seu_segredo_aqui
  AWS_BUCKET_NAME=nome_do_seu_bucket`

4. Execute o pipeline:
   `uv run main.py`

