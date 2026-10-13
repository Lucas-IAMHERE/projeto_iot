# Pipeline de Dados IoT com Docker e PostgreSQL

Este projeto implementa um pipeline completo de dados focado no processamento de leituras de temperatura de dispositivos IoT. Utiliza Python para ingestão de dados, Docker e PostgreSQL para armazenamento, e Streamlit com Plotly para a visualização interativa dos dados.

## Tecnologias Utilizadas
* **Python 3:** Linguagem principal para processamento de dados e backend.
* **Docker:** Para isolamento e execução rápida do banco de dados relacional.
* **PostgreSQL:** Banco de dados para armazenamento estruturado das leituras e criação de Views analíticas.
* **Pandas & SQLAlchemy:** Limpeza, transformação e integração de dados (ETL).
* **Streamlit & Plotly:** Construção do dashboard web e geração de gráficos interativos.

## Estrutura do Projeto
* `/data`: Contém o ficheiro CSV original (`IOT-temp.csv`) extraído do Kaggle.
* `/src`: Códigos-fonte (`main.py` para ETL e `dashboard.py` para a interface).
* `/docs`: Documentação teórica do projeto.

## Visualizações do Dashboard

*(Insira aqui as capturas de ecrã do seu dashboard a funcionar)*

![Gráficos do Dashboard](coloque_o_nome_da_sua_imagem_aqui.png)

As visualizações incluem:
1. Média de temperatura por dispositivo.
2. Contagem de volume de leituras recebidas por hora.
3. Análise de temperaturas máximas e mínimas por dia.

## Como Executar o Projeto

**1. Levantar o banco de dados (Docker):**
No terminal, inicie o container PostgreSQL:
```bash
docker run --name postgres-iot -e POSTGRES_PASSWORD=admin -p 5432:5432 -d postgres