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

c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS products (product_id, product_name, price)')
conn.commit()
# %%
c.execute('DROP TABLE products')
#%%
c.execute('DROP TABLE data')
conn.commit()

# %%
c.execute('DROP TABLE data2')
conn.commit()

#%%
c.execute('CREATE TABLE IF NOT EXISTS products ([product_id] INTEGER PRIMARY KEY, [product_name] TEXT, [price] INTEGER)')

# %%
c.execute(''' INSERT INTO products (product_id, product_name, price)
          VALUES
          (1, 'Computer', 800),
          (2, 'Printer', 200),
          (3, 'Tablet', 300)
''')
# %%
conn.commit()

# %%
df_data2 = df_data.iloc[::-2]
df_data2.to_sql('data2', conn, if_exists='append')
# %%

#SELECT
c.execute("SELECT * FROM data")
c.fetchone()
c.fetchall()
df = pd.DataFrame(c.fetchall())
# %%
df = pd.DataFrame(c.fetchall())

# %%
c.execute("SELECT * FROM data WHERE A > 200")
df = pd.DataFrame(c.fetchall())
df
# %%
c.execute("SELECT * FROM data WHERE A > 200 and B > 250")
df = pd.DataFrame(c.fetchall())
df
# %%
query = "SELECT * FROM data"
df = pd.read_sql(query, conn, index_col='id_index')
df
# %%
# 1. Executa a alteração
c.execute("UPDATE data SET A=333 WHERE id_index='1'")
# 2. Salva permanentemente (FUNDAMENTAL)
conn.commit()
# 3. Atualiza a sua variável df lendo o banco de novo
df = pd.read_sql("SELECT * FROM data", conn, index_col='id_index')
# 4. Agora sim, visualize
df
# %%
c.execute("DELETE FROM data WHERE Unnamed:0=2")
conn.commit()
# %%
