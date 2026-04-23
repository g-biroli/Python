#%%
import sqlite3
import pandas as pd

# 1. Conecta no banco
conn = sqlite3.connect('web.db')
df_data = pd.read_csv('bd_data.csv')
df_data
df_data.index.name = 'id_index'
# %%
#Visualização do Dataframe
df_data
# %%
# Importando o dataframe para o banco de dados
df_data.to_sql('data', conn, index_label='id_index', if_exists='replace')
# %%

