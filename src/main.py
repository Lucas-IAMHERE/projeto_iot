import pandas as pd
from sqlalchemy import create_engine, text

print("1. A ler o ficheiro CSV...")
# Lê o CSV da pasta data
df = pd.read_csv('data/IOT-temp.csv')

# Renomear as colunas para o padrão exigido pelo código do professor
df = df.rename(columns={
    'id': 'device_id', 
    'temp': 'temperature',
    'noted_date': 'data_hora'
})

# Converter a coluna de data para o formato correto e extrair dia e hora
df['data_hora'] = pd.to_datetime(df['data_hora'], format='mixed')
df['data_leitura'] = df['data_hora'].dt.date
df['hora_leitura'] = df['data_hora'].dt.hour

print("2. A ligar ao banco de dados PostgreSQL...")
# Conexão com o Docker (utilizando a senha 'admin' que configurou)
engine = create_engine('postgresql+psycopg2://postgres:admin@localhost:5432/postgres')

print("3. A enviar os dados para o banco (isto pode demorar alguns segundos)...")
# Envia a tabela para o banco de dados
df.to_sql('temperature_readings', engine, if_exists='replace', index=False)

print("4. A criar as Views SQL...")
with engine.connect() as conn:
    # View 1: Média de temperatura (Exemplo do professor)
    conn.execute(text("""
        DROP VIEW IF EXISTS avg_temp_por_dispositivo;
        CREATE VIEW avg_temp_por_dispositivo AS
        SELECT device_id, AVG(temperature) as avg_temp
        FROM temperature_readings
        GROUP BY device_id;
    """))

    # View 2: Leituras por hora do dia
    conn.execute(text("""
        DROP VIEW IF EXISTS leituras_por_hora;
        CREATE VIEW leituras_por_hora AS
        SELECT hora_leitura AS hora, COUNT(*) AS contagem
        FROM temperature_readings
        GROUP BY hora_leitura
        ORDER BY hora_leitura;
    """))

    # View 3: Temperaturas máximas e mínimas por dia
    conn.execute(text("""
        DROP VIEW IF EXISTS temp_max_min_por_dia;
        CREATE VIEW temp_max_min_por_dia AS
        SELECT data_leitura AS data, MAX(temperature) AS temp_max, MIN(temperature) AS temp_min
        FROM temperature_readings
        GROUP BY data_leitura
        ORDER BY data_leitura;
    """))
    conn.commit() # Grava as alterações no banco

print("Concluído! Base de dados alimentada com sucesso.")