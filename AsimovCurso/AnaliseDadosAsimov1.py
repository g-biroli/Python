
#COMEÇO DAS ANÁLISES DE DADOS COM PYTHON
#Crriação da variável com o endereço da base de dados (csv)
caminho_dados = r"C:\Users\gabri\OneDrive\Belgeler\GitHub\Python\Dados\2025_Viagem.csv"

#Importação do Panda para o projeto
import pandas as pd
import os


# Verifica se o arquivo existe e carrega os dados
# Criação de um If else para ver se encontramos o arquivo da base de dados no computador
if os.path.exists(caminho_dados):
    df_viagens = pd.read_csv(caminho_dados, encoding="Windows-1252", sep=";")
    print("Arquivo carregado com sucesso!")
    print(df_viagens)
    df_viagens["Identificador do processo de viagem"]

