# import the sqlite module
import sqlite3
import pandas as pd

# Get and read of the excel table
Cadastro = pd.read_csv('DB/Cadastro.csv')
Compras = pd.read_csv('DB/Compras.csv')
Perdas = pd.read_csv('DB/Perdas.csv')
Vendas = pd.read_csv('DB/Vendas.csv')


# initialize a conection the databse or create a new on if it does not exist
connCadastro = sqlite3.connect('DB/silver_Cadastro.db')
connCompras = sqlite3.connect('DB/silver_Compras.db')
connPerdas = sqlite3.connect('DB/silver_Perdas.db')
connVendas = sqlite3.connect('DB/silver_Vendas.db')


# Set the dataframe with new table
Cadastro.to_sql("Cadastro", connCadastro, if_exists="replace", index=False)
Compras.to_sql("Compras", connCompras, if_exists="replace", index=False)
Perdas.to_sql("Perdas", connPerdas, if_exists="replace", index=False)
Vendas.to_sql("Vendas", connVendas, if_exists="replace", index=False)


# Initialize a method to create a cursor
pointerCadastro = connCadastro.cursor()
pointerCompras = connCompras.cursor()
pointerPerdas = connPerdas.cursor()
pointerVendas = connVendas.cursor()

# 4. Feche a conexão
#connCadastro.close()
#connCompras.close()
#connPerdas.close()
#connVendas.close()
